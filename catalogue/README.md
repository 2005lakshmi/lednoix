# Catalogue Flipbook Viewer

A turn.js-based flipbook, rebuilt to handle 150+ pages without choking:
pages (and their images) only enter the DOM when turn.js actually needs
them — open the book and it requests ~3-4 images, not 150.

## Try it now (with placeholder data)

```
cd catalogue-viewer
python3 -m http.server 8080
```
Open http://localhost:8080 — it's currently loaded with 150 generated
placeholder pages so you can feel the real scale before your artwork
is ready.

## Swap in your real catalogue

1. Export your 150-page catalogue as a single PDF.
2. Run:
   ```
   python3 tools/pdf_to_pages.py --pdf /path/to/your-catalogue.pdf --title "Your Brand Catalogue"
   ```
   This renders each page as an optimized JPEG, builds thumbnails, and
   writes `data/pages.json`. It replaces the placeholder images.
3. (Optional) To attach a "View product →" link and a real caption to
   specific pages, make a CSV like:
   ```
   page,caption,product_url
   12,Downlight 18W Model LC-918,/products/downlight-18w
   13,Panel Light 36W Model LC-936,/products/panel-36w
   ```
   and re-run with `--captions-csv captions.csv`. Pages you don't list
   just get a plain page number — fine for pages that aren't tied to a
   single product (section dividers, etc).
4. Refresh the browser — no other changes needed.

You can also hand-edit `data/pages.json` directly if you'd rather set
captions/links per page without a CSV.

## Linking from a product page

Two ways to drop this into the site, from every product page:

**A) Link out to a specific page** (simplest, recommended):
```html
<a href="/catalogue/index.html#page=42">View in catalogue →</a>
```
The viewer reads `#page=N` on load and opens straight to that page. It
also keeps the URL hash updated as the visitor flips pages, so the page
is shareable/bookmarkable at any point.

**B) Embed inline via iframe:**
```html
<iframe src="/catalogue/index.html#page=42" style="width:100%;height:600px;border:0;"></iframe>
```

## Performance notes for 150+ pages

- **Lazy page loading**: `js/catalogue.js` initializes turn.js with just
  a page *count*, not page content. turn.js fires a `missing` event
  asking for the handful of pages it needs for the current view +
  immediate neighbours; only those get built and have their `<img src>`
  set. Pages that scroll out of range are dropped from the DOM again.
- **Image size**: keep page JPEGs in the 40-120 KB range (the PDF
  converter defaults to ~1100px wide, quality 80, which lands there).
  Going much above ~200 KB/page starts to feel sluggish on flips, even
  though only a few are loaded at once — each flip loads 1-2 new ones.
- **Responsive display**: single-page mode under ~760px width (mobile),
  two-page spread above it, resized to fit the viewport on load and on
  resize/orientation change.
- If your real catalogue has very image-heavy pages (large product
  photos), consider running the PDF through the converter at a lower
  `--dpi` (e.g. 120) or `--max-width` (e.g. 900) — screen viewing
  rarely needs more.

## Files

```
index.html            viewer shell + toolbar
css/style.css          styling
js/jquery.js, js/turn.js   vendored libraries (unmodified)
js/catalogue.js        lazy-loading logic, toolbar, deep-linking, responsive sizing
data/pages.json         manifest: page list, captions, product links
images/pages/           full-size page images
images/thumbs/          thumbnails (generated but not wired into the UI yet —
                         handy if you later want a thumbnail strip/grid view)
tools/generate_dummy_pages.py   regenerates the placeholder test data
tools/pdf_to_pages.py            converts your real PDF catalogue into the viewer's format
```
