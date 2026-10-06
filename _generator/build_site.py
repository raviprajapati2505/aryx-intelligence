# -*- coding: utf-8 -*-
"""Generate the Aryx Intelligence static site."""
import json
import os
import re
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGIN = "https://aryxintelligence.com"
LOGO = "aryx_053931_grad_horizontal_white_bg.png"
VIDEO = "242043_medium.mp4"

CAPS = [
    ("ai-intelligence", "AI & Intelligence", "Enterprise AI, agents, governance", "ai"),
    ("cybersecurity", "Cybersecurity", "Strategy, cyber risk, resilience", "cyber"),
    ("risk-decision-intelligence", "Risk & Decision Intelligence", "Connected risk, scenarios, decisions", "risk"),
    ("climate-intelligence", "Climate Intelligence", "Climate risk, GHG, PCAF, ESG data", "climate"),
    ("digital-transformation", "Digital & Technology", "Architecture, cloud, data, modernization", "digital"),
]
INDUSTRIES = [
    ("industries/banking", "Banking & Financial Services", "banking"),
    ("industries/government", "Government & Public Sector", "government"),
    ("industries/energy", "Energy", "energy"),
    ("industries/infrastructure", "Infrastructure", "infrastructure"),
    ("industries/real-estate", "Real Estate", "real-estate"),
    ("industries/healthcare", "Healthcare", "healthcare"),
    ("industries/manufacturing", "Manufacturing", "manufacturing"),
    ("industries/technology", "Technology", "technology"),
    ("industries/professional-services", "Professional Services", "professional-services"),
]
COMPANY = [
    ("about", "About"),
    ("insights", "Insights"),
    ("contact", "Contact"),
    ("careers", "Careers"),
]
LEGAL = [
    ("privacy", "Privacy"),
    ("terms", "Terms"),
    ("cookies", "Cookies"),
]

ARROW = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CHEV = '<svg class="chev" viewBox="0 0 12 12" aria-hidden="true"><path d="M2.2 4.2 6 8l3.8-3.8" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>'


def e(text):
    return escape(text, quote=True)


def href(depth, slug):
    prefix = "../" * depth
    if not slug:
        return prefix + "index.html"
    return prefix + slug.strip("/") + "/index.html"


def asset(depth, path):
    return "../" * depth + path


def canonical(slug):
    if not slug:
        return ORIGIN + "/"
    return ORIGIN + "/" + slug.strip("/") + "/"


def crumbs(depth, items):
    """items: list of (label, slug or None for current)."""
    lis = []
    for label, slug in items:
        if slug is None:
            lis.append(f"<li>{e(label)}</li>")
        else:
            lis.append(f'<li><a href="{href(depth, slug)}">{e(label)}</a></li>')
    return '<nav aria-label="Breadcrumb"><ol class="crumbs">' + "".join(lis) + "</ol></nav>"


def crumb_schema(items):
    elements = []
    for i, (label, slug) in enumerate(items, start=1):
        item = {"@type": "ListItem", "position": i, "name": label}
        if slug is not None:
            item["item"] = canonical(slug)
        elements.append(item)
    return {"@type": "BreadcrumbList", "@id": "#breadcrumb", "itemListElement": elements}


def faq_html(pairs):
    blocks = []
    for q, a in pairs:
        blocks.append(f"<details><summary>{q}</summary><div>{a}</div></details>")
    return '<div class="faq">' + "".join(blocks) + "</div>"


def faq_schema(pairs):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)},
            }
            for q, a in pairs
        ],
    }


def org_schema():
    return {
        "@type": "Organization",
        "@id": ORIGIN + "/#organization",
        "name": "Aryx Intelligence",
        "url": ORIGIN + "/",
        "logo": ORIGIN + "/" + LOGO,
        "description": "Aryx Intelligence is a Doha-headquartered decision-intelligence company connecting AI, cybersecurity, risk, climate and enterprise technology.",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Doha",
            "addressCountry": "QA",
        },
        "areaServed": ["Qatar", "GCC", "Worldwide"],
    }


def nav(depth, active):
    def cap_links():
        rows = []
        for slug, name, blurb, key in CAPS:
            current = ' aria-current="page"' if active == key else ""
            rows.append(
                f'<a href="{href(depth, slug)}"{current}><strong>{e(name)}</strong><span>{e(blurb)}</span></a>'
            )
        return "".join(rows)

    def ind_links():
        rows = []
        for slug, name, key in INDUSTRIES:
            current = ' aria-current="page"' if active == key else ""
            rows.append(f'<a href="{href(depth, slug)}"{current}><strong>{e(name)}</strong></a>')
        return "".join(rows)

    insights_current = ' aria-current="page"' if active == "insights" else ""
    about_current = ' aria-current="page"' if active == "about" else ""
    return f"""
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">
      <span></span><span></span><span></span>
    </button>
    <nav class="site-nav" id="site-nav" aria-label="Primary">
      <div class="nav-item">
        <button class="nav-btn" aria-expanded="false" aria-controls="menu-capabilities">Capabilities {CHEV}</button>
        <div class="mega" id="menu-capabilities">{cap_links()}</div>
      </div>
      <div class="nav-item">
        <button class="nav-btn" aria-expanded="false" aria-controls="menu-industries">Industries {CHEV}</button>
        <div class="mega industries" id="menu-industries">{ind_links()}</div>
      </div>
      <a class="nav-link" href="{href(depth, "insights")}"{insights_current}>Insights</a>
      <a class="nav-link" href="{href(depth, "about")}"{about_current}>About</a>
      <a class="btn btn-primary mobile-cta" href="{href(depth, "contact")}">Talk to Aryx</a>
    </nav>
    <a class="btn btn-primary header-cta" href="{href(depth, "contact")}">Talk to Aryx</a>
    """


def footer(depth):
    caps = "".join(f'<li><a href="{href(depth, s)}">{e(n)}</a></li>' for s, n, _, _ in CAPS)
    inds = "".join(f'<li><a href="{href(depth, s)}">{e(n)}</a></li>' for s, n, _ in INDUSTRIES)
    company = "".join(f'<li><a href="{href(depth, s)}">{e(n)}</a></li>' for s, n in COMPANY)
    legal = "".join(f'<li><a href="{href(depth, s)}">{e(n)}</a></li>' for s, n in LEGAL)
    return f"""
    <footer class="site-footer">
      <div class="wrap-wide footer-statement">
        <p>Clarity you can act on.</p>
        <span>Complexity, made decisive.</span>
      </div>
      <div class="wrap-wide footer-grid">
        <div>
          <a href="{href(depth, "")}"><img class="footer-logo" src="{asset(depth, LOGO)}" alt="Aryx Intelligence"></a>
          <p>Clarity you can act on.</p>
          <p class="muted">Aryx Intelligence · <span class="placeholder">Office address</span>, Doha, Qatar</p>
          <p class="muted"><span class="placeholder">General email</span> · <span class="placeholder">Phone</span></p>
          <form data-aryx-form data-success="Thank you. Please check your inbox once the list is connected." aria-label="Subscribe to The Aryx Brief">
            <p class="hp"><label>Company website <input name="company_website" tabindex="-1" autocomplete="off"></label></p>
            <input type="hidden" name="form" value="newsletter">
            <label>The Aryx Brief
              <span class="newsletter">
                <input type="email" name="email" required autocomplete="email" placeholder="Work email" aria-label="Work email">
                <button class="btn btn-primary" type="submit">Subscribe</button>
              </span>
            </label>
            <p class="form-note" hidden></p>
          </form>
        </div>
        <div><h2>Capabilities</h2><ul>{caps}</ul></div>
        <div><h2>Industries</h2><ul>{inds}</ul></div>
        <div><h2>Company</h2><ul>{company}</ul></div>
        <div><h2>Legal</h2><ul>{legal}</ul></div>
      </div>
      <div class="wrap-wide footer-base">
        <span>© <span id="year">2026</span> Aryx Intelligence. Headquartered in Doha, Qatar.</span>
        <span>Doha · GCC · International</span>
      </div>
    </footer>
    """


def layout(depth, active, title, description, slug, body, schemas, extra_head=""):
    graph = {"@context": "https://schema.org", "@graph": schemas}
    ld = json.dumps(graph, ensure_ascii=False)
    year_script = "<script>document.getElementById('year').textContent=new Date().getFullYear();</script>"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{e(title)}</title>
  <meta name="description" content="{e(description)}">
  <meta name="robots" content="noindex, nofollow, noarchive">
  <meta name="googlebot" content="noindex, nofollow, noarchive">
  <link rel="canonical" href="{canonical(slug)}">
  <meta name="theme-color" content="#061310">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Aryx Intelligence">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(description)}">
  <meta property="og:url" content="{canonical(slug)}">
  <meta property="og:image" content="{ORIGIN}/{LOGO}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{e(title)}">
  <meta name="twitter:description" content="{e(description)}">
  <link rel="icon" href="{asset(depth, LOGO)}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script>document.documentElement.classList.add("js");</script>
  <link rel="stylesheet" href="{asset(depth, "css/styles.css")}">
  {extra_head}
  <script type="application/ld+json">{ld}</script>
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="logo" href="{href(depth, "")}"><img src="{asset(depth, LOGO)}" alt="Aryx Intelligence"></a>
      {nav(depth, active)}
    </div>
  </header>
  <main id="main">
    {body}
  </main>
  {footer(depth)}
  <script src="{asset(depth, "js/site.js")}"></script>
  <script src="{asset(depth, "js/main.js")}"></script>
  {year_script}
</body>
</html>
"""


def write_page(slug, html):
    if slug:
        folder = os.path.join(ROOT, *slug.split("/"))
    else:
        folder = ROOT
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, "index.html")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print("wrote", path.replace(ROOT, ""))


PAGES = []


def add(slug, depth, active, title, description, body, schemas):
    PAGES.append((slug, layout(depth, active, title, description, slug, body, schemas)))


def btn(depth, slug, label, kind="primary", query=""):
    url = href(depth, slug) + query
    return f'<a class="btn btn-{kind}" href="{url}">{label} {ARROW}</a>'


def text_link(depth, slug, label, query=""):
    return f'<a class="btn btn-text" href="{href(depth, slug)}{query}">{label} {ARROW}</a>'


def main():
    import site_pages
    site_pages.register()
    seen = set()
    urls = []
    for slug, html in PAGES:
        if slug in seen:
            raise SystemExit(f"Duplicate page: {slug}")
        seen.add(slug)
        write_page(slug, html)
    sitemap_path = os.path.join(ROOT, "sitemap.xml")
    if os.path.exists(sitemap_path):
        os.remove(sitemap_path)
    robots = "User-agent: *\nDisallow: /\n"
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(robots)
    print("pages", len(PAGES))


