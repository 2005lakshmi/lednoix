/**
 * Catalogue flipbook viewer — optimized for 150+ page catalogues.
 *
 * Key difference from the plain turn.js sample: pages are NOT built into
 * the DOM (and their images are NOT requested) until turn.js actually
 * needs them. We tell turn.js the total page count up front via the
 * `pages` option, then build + inject each page's markup only when the
 * 'missing' event asks for it. turn.js already evicts pages that scroll
 * out of its working range (see its `range()` function), so at any time
 * only a handful of pages (current + a few neighbours) exist in the DOM
 * and have had their <img> requested.
 *
 * Usage: just load this file after jquery.js + turn.js on a page with
 * a <div id="flipbook"></div>. Everything else is wired up from
 * data/pages.json (see DATA_URL below).
 */
(function () {
  "use strict";

  var DATA_URL = "data/pages.json";

  var $flip = null;
  var manifest = null;
  var pageAspect = 900 / 1260; // overwritten once manifest loads
  var builtPages = {}; // pageNumber -> true, once its DOM node exists
  var isSingle = false;
  var $root, $loading, $pageInput, $pageTotal, $viewport, $zoomWrap, $thumbRail, $railHandle;

  // --- Thumbnail rail state ---
  var RAIL_WIDTH = 120;
  var RAIL_BREAKPOINT = 860; // below this, the rail overlays instead of reserving space
  var railOpen = false;

  // --- Zoom/pan state ---
  var ZOOM_MIN = 1;
  var ZOOM_MAX = 3;
  var ZOOM_STEP = 0.6;
  var zoomLevel = 1;
  var panX = 0;
  var panY = 0;
  var isPanning = false;
  var panStart = null; // {x, y, panX, panY} at drag start

  function $(sel, ctx) {
    return (ctx || document).querySelector(sel);
  }

  function byPage(n) {
    return manifest.pages[n - 1];
  }

  // Build the DOM for one catalogue page. Only called the first time
  // turn.js actually needs that page, so this is where the lazy image
  // load happens.
  function buildPageElement(n) {
    var data = byPage(n);
    var div = document.createElement("div");
    div.className = "page" + (data.type === "cover" ? " hard" : "");
    div.setAttribute("data-page", n);

    var imgWrap = document.createElement("div");
    imgWrap.className = "page-img-wrap";

    var spinner = document.createElement("div");
    spinner.className = "page-spinner";
    imgWrap.appendChild(spinner);

    var img = document.createElement("img");
    img.alt = data.caption || "Page " + n;
    img.decoding = "async";
    img.loading = "eager"; // it's needed right now, no point deferring further
    img.addEventListener("load", function () {
      spinner.remove();
      imgWrap.classList.add("loaded");
    });
    img.addEventListener("error", function () {
      spinner.remove();
      imgWrap.classList.add("error");
      imgWrap.title = "Image failed to load";
    });
    img.src = data.img;
    imgWrap.appendChild(img);
    div.appendChild(imgWrap);

    if (data.caption) {
      var cap = document.createElement("small");
      cap.className = "page-caption";
      cap.textContent = data.caption;
      if (data.product_url) {
        var a = document.createElement("a");
        a.href = data.product_url;
        a.textContent = "View product →";
        a.className = "page-link";
        cap.appendChild(document.createElement("br"));
        cap.appendChild(a);
      }
      div.appendChild(cap);
    }

    var num = document.createElement("span");
    num.className = "page-num";
    num.textContent = n;
    div.appendChild(num);

    return div;
  }

  // turn.js 'missing' handler: it hands us the page numbers it wants
  // that don't exist in the DOM yet. We create + addPage exactly those.
  function onMissing(event, pages) {
    for (var i = 0; i < pages.length; i++) {
      var n = pages[i];
      if (builtPages[n]) continue;
      builtPages[n] = true;
      var el = buildPageElement(n);
      $flip.turn("addPage", el, n);
    }
  }

  function updateIndicator() {
    var page = $flip.turn("page");
    if (document.activeElement !== $pageInput) {
      $pageInput.value = page;
    }
    history.replaceState(null, "", "#page=" + page);
    updateActiveThumb(page);
  }

  // --- Thumbnail rail ---

  function buildThumbRail() {
    var total = manifest.total_pages || manifest.pages.length;
    var list = $thumbRail.querySelector(".thumb-list");
    var frag = document.createDocumentFragment();

    for (var n = 1; n <= total; n++) {
      var data = byPage(n);

      var item = document.createElement("button");
      item.type = "button";
      item.className = "thumb-item";
      item.setAttribute("data-page", n);
      item.setAttribute("aria-label", "Go to page " + n);

      var img = document.createElement("img");
      img.src = data.thumb || data.img;
      img.loading = "lazy"; // only fetched once scrolled near, same spirit as page lazy-loading
      img.decoding = "async";
      img.alt = "";
      item.appendChild(img);

      var label = document.createElement("span");
      label.className = "thumb-label";
      label.textContent = n;
      item.appendChild(label);

      item.addEventListener("click", function () {
        goToPage(this.getAttribute("data-page"));
      });

      frag.appendChild(item);
    }

    list.appendChild(frag);
  }

  function updateActiveThumb(page) {
    var prev = $thumbRail.querySelector(".thumb-item.active");
    if (prev) prev.classList.remove("active");
    var current = $thumbRail.querySelector('.thumb-item[data-page="' + page + '"]');
    if (current) {
      current.classList.add("active");
      current.scrollIntoView({ block: "nearest", behavior: "smooth" });
    }
  }

  function setRailOpen(open) {
    railOpen = open;
    $thumbRail.classList.toggle("closed", !open);
    $railHandle.classList.toggle("closed", !open);
    $railHandle.textContent = open ? "›" : "‹"; // › when open (click to close), ‹ when closed (click to open)
    fitSize();
  }

  function fitSize() {
    // Reserve room for the thumbnail rail only when it's open and the
    // viewport is wide enough to spare it; on narrow screens the rail
    // overlays on top instead so the book doesn't get squeezed.
    var railReserve = railOpen && window.innerWidth >= RAIL_BREAKPOINT ? RAIL_WIDTH + 16 : 0;
    var availW = window.innerWidth - 16 - railReserve;
    var availH = window.innerHeight - 16;

    var wantSingle = window.innerWidth < 760;
    isSingle = wantSingle;

    var ratioMultiplier = wantSingle ? 1 : 2; // double page shows 2 pages side by side
    var width, height;

    // fit by height first
    height = availH;
    width = height * pageAspect * ratioMultiplier;
    if (width > availW) {
      width = availW;
      height = width / (pageAspect * ratioMultiplier);
    }

    width = Math.floor(width);
    height = Math.floor(height);

    $viewport.style.width = width + "px";
    $viewport.style.height = height + "px";

    if ($flip) {
      var currentDisplay = $flip.turn("display");
      if (currentDisplay !== (wantSingle ? "single" : "double")) {
        $flip.turn("display", wantSingle ? "single" : "double");
      }
      $flip.turn("size", width, height);
    }
  }

  function goToPage(n) {
    n = parseInt(n, 10);
    var total = $flip.turn("pages");
    if (isNaN(n) || n < 1) n = 1;
    if (n > total) n = total;
    $flip.turn("page", n);
  }

  // --- Zoom/pan ---

  function clampPan() {
    if (zoomLevel <= 1) {
      panX = 0;
      panY = 0;
      return;
    }
    var maxX = ($viewport.offsetWidth * (zoomLevel - 1)) / 2;
    var maxY = ($viewport.offsetHeight * (zoomLevel - 1)) / 2;
    panX = Math.max(-maxX, Math.min(maxX, panX));
    panY = Math.max(-maxY, Math.min(maxY, panY));
  }

  function applyZoom(animated) {
    clampPan();
    $zoomWrap.style.transition = animated ? "transform 0.2s ease" : "none";
    $zoomWrap.style.transform = "translate(" + panX + "px, " + panY + "px) scale(" + zoomLevel + ")";
    var zoomed = zoomLevel > 1.001;
    $zoomWrap.classList.toggle("zoomed", zoomed);
    // Pages flip via click/drag on the same surface we pan with, so the two
    // gestures conflict — disable turn.js's own interaction while zoomed in,
    // and restore it once back at 1x.
    if ($flip) $flip.turn("disable", zoomed);
  }

  function setZoom(level, animated) {
    zoomLevel = Math.max(ZOOM_MIN, Math.min(ZOOM_MAX, level));
    applyZoom(animated !== false);
  }

  function wireZoom() {
    var stage = document.querySelector(".stage");

    stage.addEventListener("wheel", function (e) {
      // The thumbnail rail scrolls its own list with the wheel — leave
      // that alone and only hijack the wheel for zoom when it's actually
      // over the book.
      if (e.target.closest(".thumb-rail")) return;
      e.preventDefault();
      var delta = e.deltaY < 0 ? ZOOM_STEP / 2 : -ZOOM_STEP / 2;
      setZoom(zoomLevel + delta, false);
    }, { passive: false });

    function dragStart(x, y) {
      if (zoomLevel <= 1) return;
      isPanning = true;
      $zoomWrap.classList.add("panning");
      panStart = { x: x, y: y, panX: panX, panY: panY };
    }
    function dragMove(x, y) {
      if (!isPanning || !panStart) return;
      panX = panStart.panX + (x - panStart.x);
      panY = panStart.panY + (y - panStart.y);
      applyZoom(false);
    }
    function dragEnd() {
      isPanning = false;
      panStart = null;
      $zoomWrap.classList.remove("panning");
    }

    // turn.js binds its own mousedown/touchstart handler directly on
    // #flipbook in the bubble phase. #flipbook sits *inside* .stage, so a
    // bubble-phase listener on .stage always fires AFTER turn.js's handler
    // already grabbed the event — calling disable() ahead of time doesn't
    // stop that handler from having been wired up, so turn.js still starts
    // its own corner-fold/drag tracking at the same time we start panning,
    // and the two fight over the same mouse-move/mouse-up stream (hence the
    // "page thumbnail" peel visual, and movement that keeps going after
    // release until the next click resets turn.js's internal state).
    //
    // Fix: listen in the CAPTURE phase on an ancestor above #flipbook.
    // Capture runs top-down before bubble, so when zoomed we can
    // stopPropagation() and stop the event from ever reaching turn.js's
    // handler at all, instead of merely asking it to disable afterwards.
    stage.addEventListener("mousedown", function (e) {
      if (zoomLevel <= 1) return;
      e.stopPropagation();
      e.preventDefault();
      dragStart(e.clientX, e.clientY);
    }, true);
    document.addEventListener("mousemove", function (e) {
      if (!isPanning) return;
      e.stopPropagation();
      dragMove(e.clientX, e.clientY);
    }, true);
    document.addEventListener("mouseup", function (e) {
      if (!isPanning) return;
      e.stopPropagation();
      dragEnd();
    }, true);

    stage.addEventListener("touchstart", function (e) {
      if (zoomLevel <= 1 || e.touches.length !== 1) return;
      e.stopPropagation();
      dragStart(e.touches[0].clientX, e.touches[0].clientY);
    }, { capture: true, passive: true });
    stage.addEventListener("touchmove", function (e) {
      if (!isPanning || e.touches.length !== 1) return;
      e.stopPropagation();
      dragMove(e.touches[0].clientX, e.touches[0].clientY);
    }, { capture: true, passive: true });
    stage.addEventListener("touchend", function (e) {
      if (!isPanning) return;
      e.stopPropagation();
      dragEnd();
    }, true);

    document.addEventListener("keydown", function (e) {
      if (document.activeElement === $pageInput) return;
      if (e.key === "+" || e.key === "=") setZoom(zoomLevel + ZOOM_STEP, true);
      if (e.key === "-" || e.key === "_") setZoom(zoomLevel - ZOOM_STEP, true);
      if (e.key === "Escape" && zoomLevel > 1) setZoom(1, true);
    });
  }

  function initialPageFromUrl() {
    var hash = window.location.hash.match(/page=(\d+)/);
    if (hash) return parseInt(hash[1], 10);
    var query = window.location.search.match(/page=(\d+)/);
    if (query) return parseInt(query[1], 10);
    return 1;
  }

  function wireToolbar() {
    $pageInput.addEventListener("change", function () {
      goToPage($pageInput.value);
    });
    $pageInput.addEventListener("keydown", function (e) {
      if (e.key === "Enter") {
        goToPage($pageInput.value);
        $pageInput.blur();
      }
    });
    $railHandle.addEventListener("click", function () {
      setRailOpen(!railOpen);
    });

    document.querySelector(".btn-fullscreen").addEventListener("click", function () {
      if (!document.fullscreenElement) {
        $root.requestFullscreen && $root.requestFullscreen();
      } else {
        document.exitFullscreen && document.exitFullscreen();
      }
    });

    document.addEventListener("keydown", function (e) {
      if (document.activeElement === $pageInput) return;
      if (e.key === "ArrowRight") $flip.turn("next");
      if (e.key === "ArrowLeft") $flip.turn("previous");
    });

    var resizeTimer;
    window.addEventListener("resize", function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(fitSize, 120);
    });

    wireZoom();
  }

  function init() {
    $root = document.getElementById("catalogue-root");
    $loading = document.getElementById("loading");
    $pageInput = document.getElementById("page-input");
    $pageTotal = document.getElementById("page-total");
    $viewport = document.getElementById("flipbook");
    $zoomWrap = document.getElementById("zoom-wrap");
    $thumbRail = document.getElementById("thumb-rail");
    $railHandle = document.getElementById("rail-handle");

    fetch(DATA_URL)
      .then(function (res) {
        if (!res.ok) throw new Error("Could not load " + DATA_URL);
        return res.json();
      })
      .then(function (data) {
        manifest = data;
        pageAspect = (data.page_width || 900) / (data.page_height || 1260);
        document.title = data.title || document.title;
        document.documentElement.style.setProperty("--page-ratio", pageAspect);

        var total = manifest.total_pages || manifest.pages.length;
        $pageInput.max = total;
        $pageTotal.textContent = "/ " + total;
        buildThumbRail();

        var startPage = Math.min(Math.max(initialPageFromUrl(), 1), total);

        isSingle = window.innerWidth < 760;
        // Default the rail open on wide desktop screens (room to spare),
        // closed on anything narrower (would otherwise crowd the book).
        railOpen = window.innerWidth >= 1100;
        $thumbRail.classList.toggle("closed", !railOpen);
        $railHandle.classList.toggle("closed", !railOpen);
        $railHandle.textContent = railOpen ? "›" : "‹";

        $flip = jQuery($viewport);
        $flip.turn({
          width: 900,
          height: 600,
          pages: total,
          page: startPage,
          display: isSingle ? "single" : "double",
          acceleration: true,
          gradients: true,
          elevation: 50,
          duration: 700,
          cornerSize: 100,
          cornerSizeY: 0.5, // top half of the page flips forward/back from the top, bottom half from the bottom
          when: {
            missing: onMissing,
            turned: updateIndicator,
            turning: updateIndicator,
          },
        });

        fitSize();
        updateIndicator();
        wireToolbar();
        $loading.style.display = "none";
        $root.classList.add("ready");
      })
      .catch(function (err) {
        $loading.textContent =
          "Couldn't load the catalogue (" + err.message + "). Check that data/pages.json and the page images are reachable.";
        console.error(err);
      });
  }

  document.addEventListener("DOMContentLoaded", init);
})();
