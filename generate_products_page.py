import json
import os

with open("data/products-catalog.json", "r", encoding="utf-8") as f:
    catalog_obj = json.load(f)

json_embed = json.dumps(catalog_obj, indent=2, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>Product Catalogue | LEDONIX Architectural &amp; Luxury LED Lighting</title>
<meta content="Explore the comprehensive LEDONIX architectural lighting catalogue: COB Lights, Recessed Downlights, Strip & Rope Lights, Panels, Track & Magnetic Systems, Linear Profiles, Outdoor Luminaires, and LED Battens." name="description"/>
<meta content="#0b0d10" name="theme-color"/>
<link rel="icon" type="image/x-icon" href="favicon.ico"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Manrope:wght@500;600;700;800&display=swap" rel="stylesheet"/>

<style>
/* ========================================================
   LEDONIX LUXURY ARCHITECTURAL LIGHTING SHOWCASE STYLES
   Theme: Deep Architectural Dark (#0b0d10 / #12151a)
   Accents: LEDONIX Brand Red (#c9343b / #ed2939)
======================================================== */
:root {{
  --bg-main: #0b0d10;
  --bg-card: #12151a;
  --bg-card-alt: #161a22;
  --bg-stage: radial-gradient(circle at 50% 45%, rgba(201, 52, 59, 0.12) 0%, rgba(22, 27, 34, 0.95) 60%, #0d0f13 100%);
  --ink: #ffffff;
  --ink-muted: #95a1af;
  --ink-dim: #647080;
  --brand-red: #c9343b;
  --brand-red-glow: rgba(201, 52, 59, 0.35);
  --brand-red-subtle: rgba(201, 52, 59, 0.08);
  --line-glass: rgba(255, 255, 255, 0.08);
  --line-glass-active: rgba(201, 52, 59, 0.5);
  --line-divider: rgba(255, 255, 255, 0.06);
  --max-width: 1540px;
  --radius-lg: 24px;
  --radius-md: 16px;
  --radius-sm: 10px;
  --shadow-stage: 0 30px 80px rgba(0, 0, 0, 0.65);
  --shadow-glow: 0 0 25px rgba(201, 52, 59, 0.25);
}}

*, *::before, *::after {{
  box-sizing: border-box;
}}

html {{
  scroll-behavior: smooth;
  scroll-padding-top: 100px;
}}

body {{
  margin: 0;
  background-color: var(--bg-main);
  color: var(--ink);
  font-family: 'DM Sans', sans-serif;
  -webkit-font-smoothing: antialiased;
  line-height: 1.6;
  overflow-x: hidden;
}}

a {{
  color: inherit;
  text-decoration: none;
}}

img {{
  max-width: 100%;
  display: block;
}}

button, input, select, textarea {{
  font: inherit;
}}

.wrap {{
  width: min(var(--max-width), calc(100% - 48px));
  margin-inline: auto;
}}

/* Top Announcement */
.announcement {{
  background: #060709;
  color: #8c97a5;
  font-size: 12px;
  letter-spacing: 0.04em;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}}
.announcement .wrap {{
  min-height: 38px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
}}
.announcement strong {{
  color: #fff;
  font-weight: 700;
}}
.announcement a {{
  color: var(--brand-red);
  font-weight: 600;
}}

/* Navigation Bar */
.nav-shell {{
  position: sticky;
  top: 0;
  z-index: 90;
  background: rgba(11, 13, 16, 0.94);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--line-glass);
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
}}
nav {{
  height: 86px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 28px;
}}
.brand {{
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 6px 14px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--line-glass);
  border-radius: 14px;
  transition: all 0.25s ease;
}}
.brand:hover {{
  border-color: rgba(201, 52, 59, 0.4);
  background: rgba(201, 52, 59, 0.05);
}}
.brand-official-logo {{
  width: 138px;
  max-height: 46px;
  object-fit: contain;
}}
.nav-links {{
  display: flex;
  align-items: center;
  gap: 4px;
  border: 1px solid var(--line-glass);
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.03);
  padding: 5px;
}}
.nav-links a {{
  padding: 9px 16px;
  border-radius: 999px;
  font-size: 12.5px;
  font-weight: 700;
  color: #adb7c4;
  transition: all 0.2s ease;
}}
.nav-links a:hover,
.nav-links a.active {{
  color: #fff;
  background: rgba(255, 255, 255, 0.08);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.25);
}}
.nav-links a.active {{
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: #ffffff;
}}
.nav-cta, .btn {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 12px 24px;
  border-radius: 999px;
  background: var(--brand-red);
  color: #fff;
  font-size: 13px;
  font-weight: 700;
  border: 1px solid var(--brand-red);
  box-shadow: 0 6px 22px var(--brand-red-glow);
  transition: all 0.25s ease;
  cursor: pointer;
}}
.nav-cta:hover, .btn:hover {{
  background: #e5232e;
  border-color: #e5232e;
  transform: translateY(-2px);
  box-shadow: 0 10px 30px rgba(229, 35, 46, 0.45);
}}
.btn-outline {{
  background: transparent;
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: none;
}}
.btn-outline:hover {{
  background: rgba(255, 255, 255, 0.08);
  border-color: #fff;
  box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}}
.menu-toggle {{
  display: none;
  border: 1px solid var(--line-glass);
  background: rgba(255, 255, 255, 0.05);
  color: #fff;
  font-size: 22px;
  padding: 8px 12px;
  border-radius: 10px;
  cursor: pointer;
}}

/* Catalogue Page Header Section */
.catalogue-header {{
  padding: 54px 0 36px;
  border-bottom: 1px solid var(--line-divider);
  background: linear-gradient(180deg, rgba(201, 52, 59, 0.06) 0%, transparent 100%);
}}
.catalogue-header-row {{
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  gap: 36px;
  flex-wrap: wrap;
}}
.header-kicker {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  font-weight: 800;
  color: var(--brand-red);
  margin-bottom: 12px;
}}
.header-kicker::before {{
  content: '';
  width: 20px;
  height: 2px;
  background: var(--brand-red);
  border-radius: 2px;
}}
.catalogue-header h1 {{
  font: 800 clamp(34px, 4vw, 52px)/1.08 'Manrope', sans-serif;
  letter-spacing: -0.04em;
  color: #ffffff;
  margin: 0 0 14px;
}}
.catalogue-header p {{
  color: var(--ink-muted);
  font-size: 15px;
  line-height: 1.7;
  max-width: 600px;
  margin: 0;
}}
.header-search-wrap {{
  position: relative;
  min-width: 320px;
  max-width: 440px;
  flex: 1;
}}
.header-search-wrap input {{
  width: 100%;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--line-glass);
  border-radius: 999px;
  padding: 14px 22px 14px 46px;
  color: #fff;
  font-size: 13px;
  outline: none;
  transition: all 0.25s ease;
}}
.header-search-wrap input:focus {{
  border-color: var(--brand-red);
  background: rgba(255, 255, 255, 0.08);
  box-shadow: 0 0 20px var(--brand-red-glow);
}}
.header-search-wrap svg {{
  position: absolute;
  left: 18px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  stroke: var(--ink-dim);
  pointer-events: none;
}}

/* ========================================================
   MAIN SHOWCASE LAYOUT (Sidebar + Full Screen Content)
======================================================== */
.showcase-layout {{
  display: flex;
  gap: 48px;
  padding: 48px 0 90px;
  align-items: flex-start;
}}

/* Category Sidebar ("Our Product List") */
.showcase-sidebar {{
  flex: 0 0 320px;
  position: sticky;
  top: 110px;
  background: var(--bg-card);
  border: 1px solid var(--line-glass);
  border-radius: var(--radius-lg);
  padding: 28px 24px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
}}

/* Illuminated Pill Badge */
.sidebar-badge {{
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 8px 18px;
  border-radius: 999px;
  background: var(--brand-red-subtle);
  border: 1px solid rgba(201, 52, 59, 0.45);
  box-shadow: 0 0 20px rgba(201, 52, 59, 0.2), inset 0 0 10px rgba(201, 52, 59, 0.1);
  font: 800 11px/1 'Manrope', sans-serif;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #ffffff;
  margin-bottom: 22px;
}}
.pulse-dot {{
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--brand-red);
  box-shadow: 0 0 10px var(--brand-red), 0 0 4px #fff;
  animation: pulseGlow 2.2s infinite ease-in-out;
}}
@keyframes pulseGlow {{
  0%, 100% {{ transform: scale(1); opacity: 1; }}
  50% {{ transform: scale(1.35); opacity: 0.65; }}
}}

/* Category List Items */
.category-nav-list {{
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin: 0;
  padding: 0;
  list-style: none;
}}
.category-nav-item {{
  border-bottom: 1px solid var(--line-divider);
}}
.category-nav-item:last-child {{
  border-bottom: none;
}}
.category-nav-link {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 14px;
  border-radius: 12px;
  color: #adb7c4;
  font: 700 12.5px 'Manrope', sans-serif;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  transition: all 0.22s ease;
  cursor: pointer;
  position: relative;
}}
.category-nav-link .link-prefix {{
  margin-right: 10px;
  color: var(--ink-dim);
  transition: all 0.22s ease;
  font-weight: 800;
}}
.category-nav-link .link-label {{
  flex: 1;
}}
.category-nav-link .link-count {{
  font-size: 11px;
  font-weight: 800;
  color: var(--ink-dim);
  background: rgba(255, 255, 255, 0.05);
  padding: 2px 8px;
  border-radius: 999px;
  transition: all 0.2s ease;
}}

/* Hover & Active States */
.category-nav-link:hover {{
  color: #ffffff;
  background: rgba(255, 255, 255, 0.04);
  transform: translateX(3px);
}}
.category-nav-link:hover .link-prefix {{
  color: var(--brand-red);
  transform: translateX(2px);
}}

.category-nav-item.is-active .category-nav-link {{
  color: #ffffff;
  background: rgba(201, 52, 59, 0.14);
  border-left: 3px solid var(--brand-red);
  box-shadow: 0 4px 20px rgba(201, 52, 59, 0.15);
}}
.category-nav-item.is-active .link-prefix {{
  color: var(--brand-red);
  font-weight: 900;
}}
.category-nav-item.is-active .link-count {{
  background: var(--brand-red);
  color: #ffffff;
}}

/* Sidebar Help Box */
.sidebar-help-card {{
  margin-top: 24px;
  padding: 20px;
  border-radius: var(--radius-md);
  background: rgba(255, 255, 255, 0.02);
  border: 1px dashed rgba(255, 255, 255, 0.1);
}}
.sidebar-help-card h4 {{
  font: 700 13px 'Manrope', sans-serif;
  color: #fff;
  margin: 0 0 6px;
}}
.sidebar-help-card p {{
  font-size: 11.5px;
  color: var(--ink-dim);
  margin: 0 0 14px;
  line-height: 1.55;
}}
.sidebar-help-card a {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 11.5px;
  font-weight: 700;
  color: var(--brand-red);
}}
.sidebar-help-card a:hover {{
  text-decoration: underline;
}}

/* ========================================================
   CONTENT AREA & FULL SCREEN PRODUCT PRESENTATION
======================================================== */
.showcase-content {{
  flex: 1;
  min-width: 0;
}}

/* Category Header Banner */
.category-banner {{
  background: linear-gradient(135deg, rgba(201, 52, 59, 0.1) 0%, rgba(18, 21, 26, 0.95) 100%);
  border: 1px solid var(--line-glass);
  border-radius: var(--radius-lg);
  padding: 34px 40px;
  margin-bottom: 24px;
  position: relative;
  overflow: hidden;
}}
.category-banner::after {{
  content: '';
  position: absolute;
  top: -60px;
  right: -60px;
  width: 220px;
  height: 220px;
  background: radial-gradient(circle, var(--brand-red-glow) 0%, transparent 70%);
  filter: blur(25px);
  pointer-events: none;
}}
.banner-badge {{
  font: 800 10.5px/1 'Manrope', sans-serif;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--brand-red);
  margin-bottom: 10px;
}}
.category-banner h2 {{
  font: 800 clamp(26px, 3vw, 38px)/1.15 'Manrope', sans-serif;
  letter-spacing: -0.03em;
  color: #fff;
  margin: 0 0 10px;
}}
.category-banner p {{
  font-size: 14.5px;
  color: var(--ink-muted);
  line-height: 1.65;
  max-width: 780px;
  margin: 0;
}}

/* Top Quick-Jump Pill Bar (Jump to any fixture within category) */
.quick-jump-bar {{
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 20px;
  background: rgba(18, 21, 26, 0.85);
  backdrop-filter: blur(12px);
  border: 1px solid var(--line-glass);
  border-radius: 999px;
  margin-bottom: 34px;
  overflow-x: auto;
  scrollbar-width: thin;
}}
.quick-jump-label {{
  font: 800 11px/1 'Manrope', sans-serif;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--brand-red);
  white-space: nowrap;
}}
.quick-jump-pills {{
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: nowrap;
}}
.quick-jump-pill {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--line-glass);
  color: #adb7c4;
  font-size: 11.5px;
  font-weight: 700;
  white-space: nowrap;
  transition: all 0.2s ease;
  cursor: pointer;
}}
.quick-jump-pill:hover {{
  background: #ffffff;
  color: #0b0d10;
  border-color: #ffffff;
  transform: translateY(-1px);
}}

/* Full Screen-Width Product Showcase (1 Product per Section) */
.product-showcase-section {{
  background: var(--bg-card);
  border: 1px solid var(--line-glass);
  border-radius: var(--radius-lg);
  padding: 44px;
  margin-bottom: 44px;
  box-shadow: 0 25px 70px rgba(0, 0, 0, 0.6);
  display: grid;
  grid-template-columns: 1fr 1.15fr;
  gap: 52px;
  align-items: center;
  position: relative;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}}
.product-showcase-section:hover {{
  border-color: rgba(201, 52, 59, 0.3);
  box-shadow: 0 35px 90px rgba(0, 0, 0, 0.75), 0 0 30px rgba(201, 52, 59, 0.08);
}}

/* Visual Stage */
.visual-stage {{
  position: relative;
  background: var(--bg-stage);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 20px;
  min-height: 480px;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
  overflow: hidden;
  box-shadow: inset 0 0 60px rgba(0, 0, 0, 0.7);
}}

/* Pedestal Depth Oval Reflection */
.pedestal-floor {{
  position: absolute;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  width: 78%;
  height: 42px;
  border-radius: 50%;
  background: radial-gradient(ellipse at center, rgba(255, 255, 255, 0.12) 0%, rgba(201, 52, 59, 0.22) 40%, transparent 80%);
  filter: blur(8px);
  pointer-events: none;
}}

/* Product Image on Stage */
.stage-img {{
  max-height: 340px;
  max-width: 90%;
  width: auto;
  height: auto;
  object-fit: contain;
  filter: drop-shadow(0 25px 35px rgba(0, 0, 0, 0.85));
  transition: transform 0.45s cubic-bezier(0.2, 0.8, 0.2, 1);
  position: relative;
  z-index: 2;
}}
.visual-stage:hover .stage-img {{
  transform: scale(1.06) translateY(-4px);
}}

/* Model / Series Badge */
.stage-badge {{
  position: absolute;
  top: 18px;
  left: 18px;
  z-index: 3;
  background: rgba(11, 13, 16, 0.85);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 999px;
  padding: 6px 14px;
  font: 800 10.5px/1 'Manrope', sans-serif;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #ffffff;
}}

/* Enlarge View Lightbox Button */
.btn-enlarge {{
  position: absolute;
  bottom: 18px;
  right: 18px;
  z-index: 3;
  background: rgba(18, 21, 26, 0.9);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: #ffffff;
  border-radius: 999px;
  padding: 8px 16px;
  font: 700 11.5px 'Manrope', sans-serif;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s ease;
}}
.btn-enlarge:hover {{
  background: var(--brand-red);
  border-color: var(--brand-red);
  transform: scale(1.04);
  box-shadow: 0 4px 16px var(--brand-red-glow);
}}

/* Information Pane */
.info-pane {{
  display: flex;
  flex-direction: column;
}}
.info-category-tag {{
  font: 800 11px/1 'Manrope', sans-serif;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--brand-red);
  margin-bottom: 8px;
}}
.info-title {{
  font: 800 clamp(26px, 2.6vw, 36px)/1.12 'Manrope', sans-serif;
  letter-spacing: -0.035em;
  color: #ffffff;
  margin: 0 0 12px;
}}
.info-desc {{
  font-size: 14.5px;
  color: var(--ink-muted);
  line-height: 1.68;
  margin: 0 0 24px;
}}

/* 2-Column Key Specifications Grid */
.specs-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px 16px;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid var(--line-glass);
  border-radius: var(--radius-md);
  padding: 18px 20px;
  margin-bottom: 24px;
}}
.spec-item {{
  display: flex;
  flex-direction: column;
}}
.spec-key {{
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ink-dim);
  margin-bottom: 2px;
}}
.spec-val {{
  font-size: 12.5px;
  font-weight: 700;
  color: #ffffff;
}}

/* Bulleted Optical / Engineering Highlights */
.highlights-list {{
  margin: 0 0 28px;
  padding: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
}}
.highlights-list li {{
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: 13px;
  color: #adb7c4;
  line-height: 1.5;
}}
.highlights-list li::before {{
  content: '✓';
  color: var(--brand-red);
  font-weight: 900;
  font-size: 14px;
  line-height: 1.2;
}}

/* Action Buttons Row */
.action-buttons-row {{
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
}}
.btn-enquire-fixture {{
  background: var(--brand-red);
  color: #fff;
  border: 1px solid var(--brand-red);
  padding: 13px 24px;
  border-radius: 999px;
  font: 700 13px 'Manrope', sans-serif;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 6px 20px var(--brand-red-glow);
  transition: all 0.25s ease;
}}
.btn-enquire-fixture:hover {{
  background: #e5232e;
  border-color: #e5232e;
  transform: translateY(-2px);
  box-shadow: 0 10px 28px rgba(229, 35, 46, 0.4);
}}
.btn-catalogue-cutsheet {{
  background: rgba(255, 255, 255, 0.04);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 13px 22px;
  border-radius: 999px;
  font: 700 13px 'Manrope', sans-serif;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: all 0.25s ease;
}}
.btn-catalogue-cutsheet:hover {{
  background: rgba(255, 255, 255, 0.1);
  border-color: #ffffff;
  transform: translateY(-2px);
}}

/* Empty / No Results Box */
.no-results-box {{
  display: none;
  text-align: center;
  padding: 60px 20px;
  background: var(--bg-card);
  border: 1px dashed rgba(255, 255, 255, 0.15);
  border-radius: var(--radius-lg);
  margin-top: 20px;
}}
.no-results-box h3 {{
  font: 800 24px 'Manrope', sans-serif;
  margin: 0 0 10px;
  color: #fff;
}}
.no-results-box p {{
  color: var(--ink-muted);
  font-size: 14px;
  margin: 0 0 20px;
}}

/* ========================================================
   BOTTOM ENQUIRY / SPECIFICATION FORM
======================================================== */
.enquiry-section {{
  background: #06080a;
  border-top: 1px solid var(--line-glass);
  padding: 80px 0;
}}
.enquiry-grid {{
  display: grid;
  grid-template-columns: 1fr 1.15fr;
  gap: 56px;
  align-items: start;
}}
.enquiry-copy h2 {{
  font: 800 clamp(32px, 3.4vw, 46px)/1.12 'Manrope', sans-serif;
  letter-spacing: -0.04em;
  color: #fff;
  margin: 0 0 16px;
}}
.enquiry-copy p {{
  color: var(--ink-muted);
  font-size: 15px;
  line-height: 1.7;
  margin: 0 0 28px;
}}
.contact-meta-list {{
  display: flex;
  flex-direction: column;
  gap: 16px;
}}
.contact-meta-item {{
  display: flex;
  align-items: flex-start;
  gap: 14px;
  color: #adb7c4;
  font-size: 13.5px;
}}
.contact-meta-icon {{
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: rgba(201, 52, 59, 0.15);
  border: 1px solid rgba(201, 52, 59, 0.35);
  color: var(--brand-red);
  display: grid;
  place-items: center;
  font-size: 14px;
  flex-shrink: 0;
}}

.enquiry-form-card {{
  background: var(--bg-card);
  border: 1px solid var(--line-glass);
  border-radius: var(--radius-lg);
  padding: 36px;
  box-shadow: 0 30px 80px rgba(0, 0, 0, 0.5);
}}
.enquiry-form-card h3 {{
  font: 800 20px 'Manrope', sans-serif;
  margin: 0 0 6px;
  color: #fff;
}}
.enquiry-form-card p {{
  color: var(--ink-dim);
  font-size: 13px;
  margin: 0 0 22px;
}}
.form-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-bottom: 20px;
}}
.field {{
  display: flex;
  flex-direction: column;
  gap: 6px;
}}
.field.full {{
  grid-column: 1 / -1;
}}
.field label {{
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #adb7c4;
}}
.field input, .field select, .field textarea {{
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--line-glass);
  border-radius: 10px;
  padding: 12px 14px;
  color: #fff;
  font-size: 13px;
  outline: none;
  transition: all 0.2s ease;
}}
.field input:focus, .field select:focus, .field textarea:focus {{
  border-color: var(--brand-red);
  background: rgba(255, 255, 255, 0.07);
  box-shadow: 0 0 15px var(--brand-red-glow);
}}
.field select option {{
  background: #12151a;
  color: #fff;
}}
.field textarea {{
  min-height: 90px;
  resize: vertical;
}}

/* ========================================================
   LIGHTBOX ENLARGE MODAL
======================================================== */
.lightbox-backdrop {{
  position: fixed;
  inset: 0;
  z-index: 99999;
  background: rgba(4, 5, 7, 0.88);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  display: none;
  align-items: center;
  justify-content: center;
  padding: 24px;
}}
.lightbox-card {{
  background: var(--bg-card);
  border: 1px solid var(--line-glass);
  border-radius: var(--radius-lg);
  width: min(920px, 100%);
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
  padding: 40px;
  box-shadow: 0 35px 100px rgba(0, 0, 0, 0.85);
}}
.lightbox-close {{
  position: absolute;
  top: 18px;
  right: 18px;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  border: 1px solid rgba(255, 255, 255, 0.15);
  background: rgba(255, 255, 255, 0.05);
  color: #fff;
  font-size: 20px;
  cursor: pointer;
  display: grid;
  place-items: center;
  transition: all 0.2s ease;
}}
.lightbox-close:hover {{
  background: var(--brand-red);
  border-color: var(--brand-red);
}}
.lightbox-body-grid {{
  display: grid;
  grid-template-columns: 1fr 1.15fr;
  gap: 36px;
  align-items: center;
}}

/* Footer */
.footer {{
  background: #060709;
  color: #7b8694;
  padding: 60px 0 24px;
  border-top: 1px solid var(--line-divider);
}}
.footer-grid {{
  display: grid;
  grid-template-columns: 1.4fr 0.8fr 0.8fr 1fr;
  gap: 36px;
  padding-bottom: 40px;
}}
.footer .brand-official-logo {{
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--line-glass);
  border-radius: 10px;
  padding: 8px 12px;
  width: 140px;
  margin-bottom: 16px;
}}
.footer-about p {{
  font-size: 12.5px;
  line-height: 1.75;
  color: #7b8694;
  max-width: 320px;
}}
.footer h4 {{
  font: 700 13px 'Manrope', sans-serif;
  color: #fff;
  margin: 0 0 16px;
}}
.footer-links {{
  display: grid;
  gap: 10px;
}}
.footer-links a {{
  font-size: 12px;
  color: #8c97a5;
  transition: color 0.2s ease;
}}
.footer-links a:hover {{
  color: var(--brand-red);
}}
.footer-bottom {{
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  padding-top: 22px;
  display: flex;
  justify-content: space-between;
  gap: 20px;
  font-size: 11px;
  color: #55606e;
}}

/* ========================================================
   RESPONSIVE DESIGN (Tablets & Mobile)
======================================================== */
@media (max-width: 1160px) {{
  .showcase-layout {{
    flex-direction: column;
    gap: 36px;
  }}
  .showcase-sidebar {{
    position: sticky;
    top: 86px;
    z-index: 70;
    width: 100%;
    flex: none;
    padding: 16px;
    background: rgba(18, 21, 26, 0.95);
    backdrop-filter: blur(16px);
  }}
  .sidebar-badge {{
    margin-bottom: 12px;
  }}
  .category-nav-list {{
    flex-direction: row;
    overflow-x: auto;
    gap: 8px;
    padding-bottom: 4px;
    scrollbar-width: thin;
  }}
  .category-nav-item {{
    border-bottom: none;
    flex-shrink: 0;
  }}
  .category-nav-link {{
    padding: 8px 14px;
    white-space: nowrap;
    border: 1px solid var(--line-glass);
    border-radius: 999px;
  }}
  .sidebar-help-card {{
    display: none;
  }}
  .product-showcase-section {{
    grid-template-columns: 1fr;
    gap: 36px;
    padding: 32px;
  }}
}}

@media (max-width: 900px) {{
  .footer-grid {{
    grid-template-columns: 1fr 1fr;
  }}
  .enquiry-grid {{
    grid-template-columns: 1fr;
    gap: 36px;
  }}
  .lightbox-body-grid {{
    grid-template-columns: 1fr;
    gap: 24px;
  }}
}}

@media (max-width: 760px) {{
  .menu-toggle {{
    display: block;
  }}
  .nav-cta {{
    display: none;
  }}
  .nav-links {{
    display: none;
    position: absolute;
    top: 86px;
    left: 16px;
    right: 16px;
    background: #12151a;
    border: 1px solid var(--line-glass);
    border-radius: 18px;
    padding: 16px;
    flex-direction: column;
    box-shadow: 0 20px 60px rgba(0,0,0,0.7);
  }}
  .nav-links.open {{
    display: flex;
  }}
  .nav-links a {{
    width: 100%;
    text-align: left;
    padding: 12px 14px;
  }}
  .specs-grid {{
    grid-template-columns: 1fr;
  }}
  .form-grid {{
    grid-template-columns: 1fr;
  }}
  .product-showcase-section {{
    padding: 22px;
  }}
  .visual-stage {{
    min-height: 320px;
    padding: 24px;
  }}
  .stage-img {{
    max-height: 240px;
  }}
}}
</style>
</head>

<body>

<!-- Top Announcement Bar -->
<div class="announcement">
  <div class="wrap">
    <span><strong>LEDONIX</strong> &nbsp; Architectural lighting, built with purpose</span>
    <span>Manufacturing in Bengaluru · Since 2009 &nbsp; / &nbsp; <a href="tel:+919686331758">+91 96863 31758</a></span>
  </div>
</div>

<!-- Header Navigation -->
<div class="nav-shell">
  <div class="wrap">
    <nav aria-label="Main navigation">
      <a aria-label="LEDONIX home" class="brand" href="index.html#home">
        <img alt="LEDONIX logo" class="brand-official-logo" src="images/ledonix-logo.png"/>
      </a>
      <button aria-expanded="false" aria-label="Toggle navigation" class="menu-toggle" onclick="document.getElementById('navLinks').classList.toggle('open')">☰</button>
      <div class="nav-links" id="navLinks">
        <a class="active" href="products.html">Products</a>
        <a href="index.html#capabilities">Capabilities</a>
        <a href="index.html#applications">Applications</a>
        <a href="index.html#executed-installations">Projects</a>
        <a href="catalogue/lnx_catalogue.html" target="_blank" rel="noopener">Catalogue</a>
        <a href="index.html#contact">About &amp; Contact</a>
      </div>
      <a class="nav-cta" href="#enquiry">Discuss a project <span>↗</span></a>
    </nav>
  </div>
</div>

<main>
  <!-- Catalogue Header & Live Search -->
  <section class="catalogue-header">
    <div class="wrap">
      <div class="catalogue-header-row">
        <div>
          <div class="header-kicker">ARCHITECTURAL LIGHTING CATALOGUE · LUXURY SPECIFICATION</div>
          <h1>Precision Luminaires for Discerning Spaces.</h1>
          <p>Explore our engineered fixture families — from ultra-low glare pinholes to modular magnetic tracks and high-performance façade grazing optics.</p>
        </div>
        <div class="header-search-wrap">
          <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          <input id="catalogSearchInput" type="text" placeholder="Search fixtures by name, wattage, beam angle or CRI..." oninput="handleSearch(this.value)"/>
        </div>
      </div>
    </div>
  </section>

  <!-- Main Showcase Layout: Sidebar + Full Width Content -->
  <div class="wrap">
    <div class="showcase-layout">

      <!-- "Our Product List" Category Sidebar -->
      <aside class="showcase-sidebar" aria-label="Product Categories">
        <div class="sidebar-badge">
          <span class="pulse-dot"></span>
          <span>Our Product List</span>
        </div>

        <ul class="category-nav-list" id="categoryNavList">
          <!-- Populated dynamically -->
        </ul>

        <div class="sidebar-help-card">
          <h4>Looking for Flipbook View?</h4>
          <p>Browse our digital page-turn catalogue with complete engineering drawings and photometrics.</p>
          <a href="catalogue/lnx_catalogue.html" target="_blank" rel="noopener">
            Open Flipbook Cut Sheets ↗
          </a>
        </div>
      </aside>

      <!-- Full-Width Content Stage Area -->
      <section class="showcase-content">
        
        <!-- Category Banner -->
        <div class="category-banner" id="categoryBanner">
          <!-- Injected dynamically -->
        </div>

        <!-- Top Quick-Jump Pill Bar -->
        <div class="quick-jump-bar" id="quickJumpBar">
          <span class="quick-jump-label">Jump to:</span>
          <div class="quick-jump-pills" id="quickJumpPills">
            <!-- Injected dynamically -->
          </div>
        </div>

        <!-- Product Presentation Container (1 Product per Section) -->
        <div id="productsPresentationContainer">
          <!-- Injected dynamically -->
        </div>

        <!-- Empty Search Fallback -->
        <div class="no-results-box" id="noResultsBox">
          <h3>No matching fixtures in this category</h3>
          <p>We couldn't find any fixtures matching your search query in this category. Try searching for a different keyword like "COB", "9W", "Track", or "IP66".</p>
          <div id="crossCategoryMatches"></div>
          <div style="margin-top:16px;">
            <button class="btn" onclick="resetSearch()">View All Category Fixtures</button>
          </div>
        </div>

      </section>

    </div>
  </div>

  <!-- Integrated Project Quotation & Specification Form -->
  <section class="enquiry-section" id="enquiry">
    <div class="wrap">
      <div class="enquiry-grid">
        <div class="enquiry-copy">
          <div class="header-kicker">DIRECT FACTORY SPECIFICATION</div>
          <h2>Request Detailed Photometric &amp; Price Quotation.</h2>
          <p>Tell us about your project scale, required Kelvin temperatures, finishes, and quantities. Our Bengaluru engineering team responds with technical cut sheets and project-based pricing.</p>
          
          <div class="contact-meta-list">
            <div class="contact-meta-item">
              <div class="contact-meta-icon">📍</div>
              <div>
                <strong style="color:#fff; display:block;">LEDONIX Technologies Private Limited</strong>
                <span>Ground Floor, B11/2, Sundara Nagar, BEL Industrial Estate, Jalahalli, Bengaluru, Karnataka 560013</span>
              </div>
            </div>
            <div class="contact-meta-item">
              <div class="contact-meta-icon">📞</div>
              <div>
                <strong style="color:#fff; display:block;">Technical Consultation &amp; OEM</strong>
                <a href="tel:+919686331758" style="color:var(--brand-red); font-weight:700;">+91 96863 31758</a>
              </div>
            </div>
            <div class="contact-meta-item">
              <div class="contact-meta-icon">⏱</div>
              <div>
                <strong style="color:#fff; display:block;">Turnaround Time</strong>
                <span>Datasheets and quotations typically provided within 4 business hours.</span>
              </div>
            </div>
          </div>
        </div>

        <div class="enquiry-form-card">
          <h3>Fixture Enquiry Form</h3>
          <p>Select your luminaire and continue directly on WhatsApp or email for instant quotation.</p>

          <form id="enquiryForm" onsubmit="handleEnquirySubmit(event)">
            <div class="form-grid">
              <div class="field full">
                <label for="formFixture">Selected Fixture</label>
                <input id="formFixture" name="fixture" type="text" placeholder="e.g. ALLORA I — NEO COB SPOT LIGHT 9W" readonly style="background:rgba(201,52,59,0.08); border-color:rgba(201,52,59,0.4); color:#fff; font-weight:700;"/>
              </div>
              <div class="field">
                <label for="formName">Full Name *</label>
                <input id="formName" name="name" type="text" placeholder="Your name" required/>
              </div>
              <div class="field">
                <label for="formPhone">Phone / WhatsApp *</label>
                <input id="formPhone" name="phone" type="tel" placeholder="+91" required/>
              </div>
              <div class="field">
                <label for="formCompany">Company / Practice</label>
                <input id="formCompany" name="company" type="text" placeholder="Architect / Consultant / Contractor"/>
              </div>
              <div class="field">
                <label for="formScope">Project Scope</label>
                <select id="formScope" name="scope">
                  <option value="Luxury Residential">Luxury Residential</option>
                  <option value="Commercial Office">Commercial Office</option>
                  <option value="Hospitality &amp; Restaurant">Hospitality &amp; Restaurant</option>
                  <option value="Retail &amp; Showroom">Retail &amp; Showroom</option>
                  <option value="Façade &amp; Landscape">Façade &amp; Landscape</option>
                  <option value="OEM / Custom Manufacturing">OEM / Custom Manufacturing</option>
                </select>
              </div>
              <div class="field full">
                <label for="formNotes">Project Notes &amp; Quantities</label>
                <textarea id="formNotes" name="notes" placeholder="Please specify desired wattage, CCT (e.g. 3000K), quantity, and timeline..."></textarea>
              </div>
            </div>

            <div style="display:flex; gap:12px; align-items:center; flex-wrap:wrap;">
              <button class="btn" type="submit" style="padding:14px 28px;">
                Send Enquiry via WhatsApp ↗
              </button>
              <button type="button" class="btn btn-outline" onclick="copyEnquiryDetails()">
                Copy Details
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
</main>

<!-- Lightbox Modal for Enlarge View ⊕ -->
<div id="lightboxModal" class="lightbox-backdrop" onclick="if(event.target===this)closeLightbox()">
  <div class="lightbox-card" role="dialog" aria-modal="true" aria-label="Fixture Lightbox">
    <button class="lightbox-close" onclick="closeLightbox()" aria-label="Close modal">&times;</button>
    <div id="lightboxBody">
      <!-- Populated via JS -->
    </div>
  </div>
</div>

<!-- Footer -->
<footer class="footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-about">
        <a class="brand" href="index.html#home" style="display:inline-block; margin-bottom:12px;">
          <img alt="LEDONIX logo" class="brand-official-logo" src="images/ledonix-logo.png"/>
        </a>
        <p>LEDONIX Technologies Private Limited designs, manufactures and customizes LED lighting fixtures for residential, commercial and industrial applications — engineered in Bengaluru, delivered worldwide.</p>
      </div>
      <div>
        <h4>Architectural Ranges</h4>
        <div class="footer-links">
          <a href="#cob" onclick="switchCategory('cob')">COB Lights</a>
          <a href="#downlights" onclick="switchCategory('downlights')">Recessed Downlights</a>
          <a href="#track" onclick="switchCategory('track')">Track &amp; Magnetic</a>
          <a href="#linear" onclick="switchCategory('linear')">Linear &amp; Pendants</a>
          <a href="#outdoor" onclick="switchCategory('outdoor')">Outdoor &amp; Façade</a>
        </div>
      </div>
      <div>
        <h4>Navigation</h4>
        <div class="footer-links">
          <a href="index.html#home">Home</a>
          <a href="index.html#capabilities">Capabilities</a>
          <a href="index.html#applications">Applications</a>
          <a href="index.html#executed-installations">Projects</a>
          <a href="catalogue/lnx_catalogue.html" target="_blank" rel="noopener">Catalogue Cut Sheets</a>
          <a href="index.html#contact">Contact</a>
        </div>
      </div>
      <div>
        <h4>Get in Touch</h4>
        <div class="footer-links">
          <a href="tel:+919686331758">+91 96863 31758</a>
          <a href="index.html#contact">Bengaluru, Karnataka, India</a>
          <a href="#enquiry">Project &amp; OEM enquiries ↗</a>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="year">2026</span> LEDONIX Technologies Private Limited. All rights reserved.</span>
      <span>Designed for better light and better spaces.</span>
    </div>
  </div>
</footer>

<!-- JavaScript: Logic, Dynamic Rendering & Local file:/// Fallback Dataset -->
<script>
// Embedded Fallback Dataset ensuring 100% functionality on local file:/// viewing and HTTP
const CATALOG_DATA_FALLBACK = {json_embed};

(function(){{
  let catalog = CATALOG_DATA_FALLBACK;
  let activeCategoryId = "cob";
  let searchQuery = "";

  // Attempt to fetch from data/products-catalog.json if served over HTTP
  if (window.location.protocol === 'http:' || window.location.protocol === 'https:') {{
    fetch('data/products-catalog.json')
      .then(res => res.json())
      .then(data => {{
        if (data && data.categories) {{
          catalog = data;
          init();
        }}
      }})
      .catch(err => {{
        console.warn('Using embedded catalog fallback data', err);
        init();
      }});
  }} else {{
    init();
  }}

  function init() {{
    buildSidebar();
    syncFromHash();
    window.addEventListener('hashchange', syncFromHash);
    document.getElementById('year').textContent = new Date().getFullYear();
  }}

  const HASH_ALIASES = {{
    'cob': 'cob',
    'cobs': 'cob',
    'cob-lights': 'cob',
    'downlights': 'downlights',
    'downlight': 'downlights',
    'recessed-downlights': 'downlights',
    'strip': 'strip',
    'strip-lights': 'strip',
    'rope': 'strip',
    'neon': 'strip',
    'panel': 'panel',
    'panels': 'panel',
    'surface': 'panel',
    'track': 'track',
    'magnetic': 'track',
    'linear': 'linear',
    'pendant': 'linear',
    'pendants': 'linear',
    'outdoor': 'outdoor',
    'facade': 'outdoor',
    'wallwashers': 'outdoor',
    'floodlights': 'outdoor',
    'decorative': 'cob',
    'architectural': 'linear',
    'battens': 'battens',
    'fittings': 'battens',
    'industrial': 'battens'
  }};

  function syncFromHash() {{
    const raw = (window.location.hash || '').replace('#', '').toLowerCase();
    const targetId = HASH_ALIASES[raw] || raw;
    const found = catalog.categories.find(c => c.slug === targetId || c.id === targetId);
    if (found) {{
      activeCategoryId = found.id;
    }} else {{
      activeCategoryId = catalog.categories[0].id;
    }}
    updateActiveCategoryView();
  }}

  function buildSidebar() {{
    const navList = document.getElementById('categoryNavList');
    if (!navList) return;

    navList.innerHTML = catalog.categories.map(cat => {{
      const count = cat.products ? cat.products.length : 0;
      const cleanLabel = (cat.nav_title || '').replace(/^>\s*/, '').trim() || cat.name.toUpperCase();
      return `
        <li class="category-nav-item ${{cat.id === activeCategoryId ? 'is-active' : ''}}" id="nav-item-${{cat.id}}">
          <a class="category-nav-link" href="${{cat.hash}}" onclick="switchCategory('${{cat.id}}', event)">
            <span class="link-prefix">&gt;</span>
            <span class="link-label">${{cleanLabel}}</span>
            <span class="link-count">${{count}}</span>
          </a>
        </li>
      `;
    }}).join('');
  }}

  window.switchCategory = function(catId, event) {{
    if (event) event.preventDefault();
    activeCategoryId = catId;
    window.location.hash = '#' + catId;
    updateActiveCategoryView();
    // Scroll smoothly to the top of the content on mobile
    if (window.innerWidth <= 1160) {{
      document.querySelector('.showcase-content').scrollIntoView({{ behavior: 'smooth' }});
    }}
  }};

  function updateActiveCategoryView() {{
    // Update active nav link
    document.querySelectorAll('.category-nav-item').forEach(item => {{
      item.classList.remove('is-active');
    }});
    const activeItem = document.getElementById('nav-item-' + activeCategoryId);
    if (activeItem) activeItem.classList.add('is-active');

    const cat = catalog.categories.find(c => c.id === activeCategoryId) || catalog.categories[0];
    if (!cat) return;

    // Render Category Banner
    const banner = document.getElementById('categoryBanner');
    banner.innerHTML = `
      <div class="banner-badge">${{cat.badge}}</div>
      <h2>${{cat.name}}</h2>
      <p>${{cat.desc}}</p>
    `;

    renderProductShowcases(cat);
  }}

  function renderProductShowcases(cat) {{
    const container = document.getElementById('productsPresentationContainer');
    const quickBar = document.getElementById('quickJumpBar');
    const quickPills = document.getElementById('quickJumpPills');
    const noResults = document.getElementById('noResultsBox');

    let products = cat.products || [];

    // Filter by search query if any
    if (searchQuery) {{
      const q = searchQuery.toLowerCase();
      products = products.filter(p => {{
        const titleMatch = p.title.toLowerCase().includes(q);
        const codeMatch = p.code ? p.code.toLowerCase().includes(q) : false;
        const seriesMatch = p.series.toLowerCase().includes(q);
        const descMatch = p.desc.toLowerCase().includes(q);
        const specsMatch = Object.values(p.specs).some(val => val.toLowerCase().includes(q));
        return titleMatch || codeMatch || seriesMatch || descMatch || specsMatch;
      }});
    }}

    if (products.length === 0) {{
      container.innerHTML = '';
      quickBar.style.display = 'none';
      noResults.style.display = 'block';

      // Cross-category search suggestions
      const crossSec = document.getElementById('crossCategoryMatches');
      if (crossSec && searchQuery) {{
        const q = searchQuery.toLowerCase();
        const otherMatches = [];
        catalog.categories.forEach(c => {{
          if (c.id !== cat.id && c.products) {{
            const count = c.products.filter(p => {{
              return p.title.toLowerCase().includes(q) ||
                     (p.code && p.code.toLowerCase().includes(q)) ||
                     p.desc.toLowerCase().includes(q);
            }}).length;
            if (count > 0) {{
              otherMatches.push({{ cat: c, count: count }});
            }}
          }}
        }});

        if (otherMatches.length > 0) {{
          crossSec.innerHTML = '<p style="color:#adb7c4; font-size:13px; margin:18px 0 10px;">Found fixtures in other categories matching your search:</p>' +
            '<div style="display:flex; gap:10px; flex-wrap:wrap; justify-content:center;">' +
            otherMatches.map(m => `
              <button type="button" class="btn btn-outline" style="padding:6px 14px; font-size:12px; cursor:pointer;" onclick="switchCategory('${{m.cat.id}}')">
                ${{(m.cat.nav_title || m.cat.name).replace(/^>\\s*/, '')}} (${{m.count}} ${{m.count === 1 ? 'fixture' : 'fixtures'}}) &rarr;
              </button>
            `).join('') + '</div>';
        }} else {{
          crossSec.innerHTML = '';
        }}
      }} else if (crossSec) {{
        crossSec.innerHTML = '';
      }}
      return;
    }}

    noResults.style.display = 'none';
    quickBar.style.display = 'flex';

    // Render Quick Jump Pills
    quickPills.innerHTML = products.map((p, idx) => `
      <a class="quick-jump-pill" href="#fixture-${{p.id}}" onclick="smoothScrollTo('fixture-${{p.id}}', event)">
        <span>${{String(idx + 1).padStart(2, '0')}}</span>
        <span>${{p.title.split('—')[0].trim()}}</span>
      </a>
    `).join('');

    // Render Monumental Full Screen-Width Product Sections (1 per section)
    container.innerHTML = products.map(p => {{
      // Specs table
      const specRows = Object.entries(p.specs).map(([k, v]) => `
        <div class="spec-item">
          <span class="spec-key">${{k}}</span>
          <span class="spec-val">${{v}}</span>
        </div>
      `).join('');

      // Highlights
      const highlightItems = (p.highlights || []).map(h => `
        <li>${{h}}</li>
      `).join('');

      const catalogueLink = p.catalogue_page ? `catalogue/lnx_catalogue.html#page/${{p.catalogue_page}}` : 'catalogue/lnx_catalogue.html';

      return `
        <article class="product-showcase-section" id="fixture-${{p.id}}">
          <!-- Visual Stage (Left) -->
          <div class="visual-stage">
            <span class="stage-badge">${{p.badge}}</span>
            <div class="pedestal-floor"></div>
            <img class="stage-img" src="${{p.img}}" alt="${{p.title}}" loading="lazy"/>
            <button type="button" class="btn-enlarge" onclick="openLightbox('${{p.id}}')">
              <span>Enlarge View</span> <span>⊕</span>
            </button>
          </div>

          <!-- Information Pane (Right) -->
          <div class="info-pane">
            <div class="info-category-tag">${{p.category_tag}} · ${{p.series}}</div>
            <h2 class="info-title">${{p.title}}</h2>
            <p class="info-desc">${{p.desc}}</p>

            <div class="specs-grid">
              ${{specRows}}
            </div>

            <ul class="highlights-list">
              ${{highlightItems}}
            </ul>

            <div class="action-buttons-row">
              <button type="button" class="btn-enquire-fixture" onclick="selectFixtureForEnquiry('${{p.title.replace(/'/g, "\\\\'")}}', '${{p.code || ''}}')">
                <span>Enquire About This Fixture</span> <span>↗</span>
              </button>
              <a class="btn-catalogue-cutsheet" href="${{catalogueLink}}" target="_blank" rel="noopener">
                <span>View Catalogue Cut Sheet</span> <span>↗</span>
              </a>
            </div>
          </div>
        </article>
      `;
    }}).join('');
  }}

  window.handleSearch = function(val) {{
    searchQuery = val.trim();
    const cat = catalog.categories.find(c => c.id === activeCategoryId) || catalog.categories[0];
    renderProductShowcases(cat);
  }};

  window.resetSearch = function() {{
    const input = document.getElementById('catalogSearchInput');
    if (input) input.value = '';
    searchQuery = '';
    const cat = catalog.categories.find(c => c.id === activeCategoryId) || catalog.categories[0];
    renderProductShowcases(cat);
  }};

  window.smoothScrollTo = function(id, event) {{
    if (event) event.preventDefault();
    const el = document.getElementById(id);
    if (el) {{
      el.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }}
  }};

  // Pre-fill enquiry form and smooth scroll
  window.selectFixtureForEnquiry = function(title, code) {{
    const fixtureInput = document.getElementById('formFixture');
    if (fixtureInput) {{
      fixtureInput.value = title + (code ? ' [' + code + ']' : '');
    }}
    const enquirySec = document.getElementById('enquiry');
    if (enquirySec) {{
      enquirySec.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }}
    const nameInput = document.getElementById('formName');
    if (nameInput) {{
      setTimeout(() => nameInput.focus(), 600);
    }}
  }};

  window.handleEnquirySubmit = function(e) {{
    e.preventDefault();
    const form = document.getElementById('enquiryForm');
    const data = new FormData(form);
    const msg = [
      'LEDONIX Architectural Catalogue Enquiry',
      'Fixture: ' + (data.get('fixture') || 'General Portfolio Enquiry'),
      'Client: ' + data.get('name'),
      'Phone: ' + data.get('phone'),
      'Company: ' + (data.get('company') || 'N/A'),
      'Scope: ' + data.get('scope'),
      'Notes: ' + (data.get('notes') || 'Please share photometric cut sheets and quotation.')
    ].join('\\n');

    window.open('https://wa.me/919686331758?text=' + encodeURIComponent(msg), '_blank', 'noopener,noreferrer');
  }};

  window.copyEnquiryDetails = function() {{
    const form = document.getElementById('enquiryForm');
    const data = new FormData(form);
    const msg = [
      'LEDONIX Architectural Enquiry',
      'Fixture: ' + (data.get('fixture') || 'Not specified'),
      'Name: ' + (data.get('name') || 'Not specified'),
      'Phone: ' + (data.get('phone') || 'Not specified'),
      'Company: ' + (data.get('company') || 'N/A'),
      'Scope: ' + data.get('scope')
    ].join('\\n');

    navigator.clipboard.writeText(msg).then(() => {{
      alert('Enquiry specifications copied to clipboard!');
    }}).catch(() => {{
      alert('Unable to copy automatically. Please submit via WhatsApp.');
    }});
  }};

  // Lightbox Modal functions
  window.openLightbox = function(prodId) {{
    let found = null;
    for (const c of catalog.categories) {{
      found = (c.products || []).find(p => p.id === prodId);
      if (found) break;
    }}
    if (!found) return;

    const modal = document.getElementById('lightboxModal');
    const body = document.getElementById('lightboxBody');

    const specsList = Object.entries(found.specs).map(([k, v]) => `
      <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
        <td style="padding:8px 0; color:#8c97a5; font-size:12px; width:45%;">${{k}}</td>
        <td style="padding:8px 0; color:#fff; font-weight:700; font-size:12px;">${{v}}</td>
      </tr>
    `).join('');

    body.innerHTML = `
      <div class="lightbox-body-grid">
        <div style="background:radial-gradient(circle at center, rgba(201,52,59,0.18) 0%, rgba(20,24,30,0.98) 70%, #080a0c 100%); border-radius:18px; padding:36px; display:flex; align-items:center; justify-content:center; min-height:360px; border:1px solid rgba(255,255,255,0.08);">
          <img src="${{found.img}}" alt="${{found.title}}" style="max-height:300px; max-width:100%; object-fit:contain; filter:drop-shadow(0 20px 40px rgba(0,0,0,0.9));"/>
        </div>
        <div>
          <span style="font-size:10.5px; letter-spacing:0.18em; text-transform:uppercase; font-weight:800; color:var(--brand-red); display:block; margin-bottom:4px;">${{found.series}}</span>
          <h2 style="font:800 24px/1.2 'Manrope',sans-serif; margin:0 0 10px; color:#fff;">${{found.title}}</h2>
          <p style="font-size:13px; color:#adb7c4; line-height:1.6; margin:0 0 16px;">${{found.desc}}</p>
          
          <table style="width:100%; border-collapse:collapse; margin-bottom:20px;">
            <tbody>${{specsList}}</tbody>
          </table>

          <div style="display:flex; gap:10px; flex-wrap:wrap;">
            <button class="btn" style="padding:10px 20px; font-size:12px;" onclick="closeLightbox(); selectFixtureForEnquiry('${{found.title.replace(/'/g, "\\\\'")}}', '${{found.code || ''}}')">
              Enquire This Fixture ↗
            </button>
            <a class="btn btn-outline" style="padding:10px 18px; font-size:12px;" href="catalogue/lnx_catalogue.html" target="_blank" rel="noopener">
              Cut Sheet Flipbook ↗
            </a>
          </div>
        </div>
      </div>
    `;

    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }};

  window.closeLightbox = function() {{
    const modal = document.getElementById('lightboxModal');
    if (modal) modal.style.display = 'none';
    document.body.style.overflow = '';
  }};

  document.addEventListener('keydown', function(e) {{
    if (e.key === 'Escape') closeLightbox();
  }});

}})();
</script>
</body>
</html>
'''

# Write to root products.html
with open("products.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully written root products.html (Length:", len(html_content), ")")

# Write to LEDONIX WEBISITE files concept B
with open("LEDONIX WEBISITE files/ledonix webiste concept B/products.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully written concept B products.html")
