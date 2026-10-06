# -*- coding: utf-8 -*-
import build_site as S

def ph(label):
    return f'<span class="placeholder">{S.e(label)}</span>'

def page_hero(depth, trail, kicker, title, lead, actions=""):
    return f"""
    <header class="page-hero">
      <div class="page-hero-mark" aria-hidden="true"></div>
      <div class="wrap page-hero-inner">
        {S.crumbs(depth, trail)}
        <p class="kicker">{kicker}</p>
        <h1>{title}</h1>
        <p class="lead">{lead}</p>
        <div class="hero-actions">{actions}</div>
      </div>
    </header>
    """

def web(slug, title, description, kind="WebPage"):
    return {"@type": kind, "name": title, "description": description, "url": S.canonical(slug), "isPartOf": {"@type": "WebSite", "name": "Aryx Intelligence", "url": S.ORIGIN + "/"}}

def service(name, description, slug):
    return {
        "@type": "Service",
        "name": name,
        "description": description,
        "url": S.canonical(slug),
        "provider": {"@id": S.ORIGIN + "/#organization"},
        "areaServed": ["Qatar", "GCC", "Worldwide"],
    }

def register():
    import about_and_caps
    import industries_and_insights
    import utility_pages
    about_and_caps.register()
    industries_and_insights.register()
    utility_pages.register()
