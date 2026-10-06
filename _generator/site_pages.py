# -*- coding: utf-8 -*-
import build_site as S

ARROW = S.ARROW


def ph(label):
    return f'<span class="placeholder">{S.e(label)}</span>'


def icon(body):
    return (
        '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" '
        'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">' + body + "</svg>"
    )


ICONS = {
    "ai": icon('<circle cx="12" cy="12" r="3"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M18.4 5.6l-2.1 2.1M7.7 16.3l-2.1 2.1"/>'),
    "cyber": icon('<path d="M12 3 20 7v6c0 4.5-3.2 7.4-8 8-4.8-.6-8-3.5-8-8V7l8-4z"/>'),
    "risk": icon('<path d="M4 19h16M7 16l3-5 3 3 4-7"/>'),
    "climate": icon('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M19.1 4.9l-1.4 1.4M6.3 17.7l-1.4 1.4"/>'),
    "digital": icon('<path d="M4 7h16v10H4z"/><path d="M8 21h8M12 17v4"/>'),
    "data": icon('<ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v6c0 1.7 3.1 3 7 3s7-1.3 7-3V6M5 12v6c0 1.7 3.1 3 7 3s7-1.3 7-3v-6"/>'),
    "bank": icon('<path d="M4 10h16M6 10v8M10 10v8M14 10v8M18 10v8M3 18h18M12 3 3 8h18L12 3z"/>'),
    "gov": icon('<path d="M4 20h16M6 20V10M10 20V10M14 20V10M18 20V10M12 3 3 8h18L12 3z"/>'),
    "energy": icon('<path d="M13 2 4 14h7l-1 8 9-12h-7l1-8z"/>'),
    "infra": icon('<path d="M4 20V9M10 20V4M16 20v-8M20 20H2"/>'),
    "estate": icon('<path d="M4 20V10l8-6 8 6v10M9 20v-6h6v6"/>'),
    "health": icon('<path d="M8 4h8v6h6v4h-6v6H8v-6H2v-4h6V4z"/>'),
    "factory": icon('<path d="M3 20V10l6 4V10l6 4V8l6 4v8H3z"/>'),
    "tech": icon('<rect x="4" y="5" width="16" height="12" rx="2"/><path d="M8 21h8"/>'),
    "firm": icon('<path d="M8 7V5h8v2M6 7h12v12H6zM9 11h6M9 15h4"/>'),
}


def register():
    home()
    import site_more
    import site_articles
    site_more.register()
    site_articles.register()


def home():
    d = 0
    faqs = [
        ("What is Aryx Intelligence?", "Aryx Intelligence is a Qatar-headquartered decision-intelligence company. It connects AI, cybersecurity, risk, climate and enterprise technology to help organizations make clearer, defensible decisions."),
        ("What is decision intelligence?", "Decision intelligence is the discipline of connecting data, analytics and AI to specific business decisions. It focuses on improving the quality, speed and accountability of choices rather than producing reports."),
        ("How is Aryx different from a cybersecurity or AI consultancy?", "Aryx treats AI, cyber and risk as connected disciplines. Instead of solving one domain in isolation, it focuses on the decisions that depend on all of them."),
        ("Which organizations does Aryx work with?", "Aryx serves boards, executives and public-sector leaders in sectors including banking, government, energy, infrastructure, healthcare and real estate, in Qatar, the GCC and internationally."),
        ("Does Aryx work outside Qatar?", f"Yes. Aryx is headquartered in Doha and works with organizations across the GCC and internationally. {ph('Confirm delivery geography')}"),
        ("How does an engagement with Aryx begin?", "Most engagements begin with a strategic conversation about a specific decision or risk. From there, Aryx proposes a scoped assessment, strategy or implementation."),
    ]
    body = f"""
    <section class="hero">
      <video data-hero autoplay muted loop playsinline poster="{S.asset(d, "assets/placeholders/command.svg")}">
        <source src="{S.asset(d, S.VIDEO)}" type="video/mp4">
      </video>
      <div class="hero-scrim"></div>
      <div class="hero-inner">
        <div class="hero-copy">
          <p class="eyebrow reveal">Decision intelligence for AI, cybersecurity and risk</p>
          <h1 class="reveal d1">Every major decision deserves the full picture.</h1>
          <p class="lead reveal d2">Aryx Intelligence brings AI, cybersecurity, risk, climate and enterprise technology together, so leaders decide with clarity rather than assumptions.</p>
          <div class="hero-actions reveal d3">
            {S.btn(d, "contact", "Start a Strategic Conversation", query="?interest=strategy")}
            <a class="btn btn-ghost" href="#approach">Explore Our Approach {ARROW}</a>
          </div>
          <p class="signature reveal d4">Complexity, made decisive.</p>
        </div>
        <div class="hero-stage reveal d2">
          <img class="hero-photo" src="{S.asset(d, "assets/placeholders/command.svg")}" alt="Placeholder image for the homepage banner. Replace with photography.">
          <span class="float-chip c1">{ICONS["ai"]} Artificial intelligence</span>
          <span class="float-chip c2">{ICONS["cyber"]} Cybersecurity</span>
          <span class="float-chip c3">{ICONS["risk"]} Risk</span>
          <span class="float-chip c4">{ICONS["climate"]} Climate</span>
          <span class="float-chip c5">{ICONS["digital"]} Enterprise technology</span>
        </div>
      </div>
      <div class="hero-foot" aria-hidden="true">
        <div class="marquee-track">
          {"".join(f"<span>{ICONS[key]} {label}</span>" for key, label in [("ai","Artificial intelligence"),("cyber","Cybersecurity"),("risk","Risk"),("climate","Climate"),("digital","Enterprise technology")] * 2)}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap split">
        <div>
          <p class="kicker">Positioning</p>
          <h2>A decision-intelligence company, headquartered in Doha.</h2>
          <img class="shot" src="{S.asset(d, "assets/placeholders/signals.svg")}" alt="Placeholder image of connected signals. Replace with photography.">
        </div>
        <div>
          <p class="lead">Aryx Intelligence is a decision-intelligence company headquartered in Doha, Qatar. We help boards, executives and public-sector leaders turn fragmented data, technology and risk information into intelligence they can act on and defend.</p>
          <p>Organizations collect more signals than ever: threat alerts, system telemetry, market data, regulatory change, third-party exposures. Each is managed by a different function, in a different language. Aryx connects them. We interpret what they mean for your organization, frame the decisions they demand, and help put those decisions into action through the right technology, governance and controls.</p>
          <p>Read <a href="{S.href(d, "about")}">how Aryx Intelligence works</a>.</p>
        </div>
      </div>
      <div class="wrap">
        <div class="chain" aria-label="The Aryx chain of value">
          <article><span class="ico">{ICONS["data"]}</span><p class="step">01</p><h3>Data</h3><p>Signals from systems, threats, markets, operations and third parties. Most stall at volume without context.</p></article>
          <article><span class="ico">{ICONS["ai"]}</span><p class="step">02</p><h3>Intelligence</h3><p>Signals connected, verified and prioritized. Most stall when this stays siloed by function.</p></article>
          <article><span class="ico">{ICONS["risk"]}</span><p class="step">03</p><h3>Insight</h3><p>What the intelligence means for this organization, now. Technical language alone has no business meaning.</p></article>
          <article><span class="ico">{ICONS["cyber"]}</span><p class="step">04</p><h3>Decision</h3><p>A clear choice with known trade-offs and owners. Escalation without options is where many stop.</p></article>
          <article><span class="ico">{ICONS["digital"]}</span><p class="step">05</p><h3>Action</h3><p>Execution through people, process and technology, so plans reach operations.</p></article>
          <article><span class="ico">{ICONS["climate"]}</span><p class="step">06</p><h3>Resilience</h3><p>The capacity to absorb shocks and adapt, measured continuously rather than once a year.</p></article>
        </div>
      </div>
    </section>

    <section class="section section-porcelain" id="capabilities">
      <div class="wrap">
        <div class="section-head">
          <p class="kicker">Core capabilities</p>
          <h2>Five disciplines. One connected perspective.</h2>
          <p>Aryx is the layer that makes these disciplines inform one another and inform leadership. Not an IT services firm, not an AI agency, and not a cybersecurity consultancy standing alone.</p>
        </div>
        <div class="cap-list">
          <article class="cap-row"><span class="idx">{ICONS["ai"]}</span><div><h3>AI &amp; Intelligence</h3><p>Enterprise AI strategy, decision intelligence, AI agents and AI governance, designed around measurable business outcomes.</p><a href="{S.href(d, "ai-intelligence")}">enterprise AI strategy and governance</a></div><span class="go" aria-hidden="true">{ARROW}</span></article>
          <article class="cap-row"><span class="idx">{ICONS["cyber"]}</span><div><h3>Cybersecurity</h3><p>Security strategy, architecture, threat intelligence and resilience, managed as a business-risk discipline.</p><a href="{S.href(d, "cybersecurity")}">cybersecurity as a business-risk discipline</a></div><span class="go" aria-hidden="true">{ARROW}</span></article>
          <article class="cap-row"><span class="idx">{ICONS["risk"]}</span><div><h3>Risk &amp; Decision Intelligence</h3><p>A connected view of technology, cyber, operational, third-party and strategic risk, built for executive decisions.</p><a href="{S.href(d, "risk-decision-intelligence")}">connected risk and decision intelligence</a></div><span class="go" aria-hidden="true">{ARROW}</span></article>
          <article class="cap-row"><span class="idx">{ICONS["climate"]}</span><div><h3>Climate Intelligence</h3><p>Climate risk, GHG accounting, financed emissions (PCAF) and ESG data, built to the standard of financial decisions and assurance.</p><a href="{S.href(d, "climate-intelligence")}">climate risk and emissions intelligence</a></div><span class="go" aria-hidden="true">{ARROW}</span></article>
          <article class="cap-row"><span class="idx">{ICONS["digital"]}</span><div><h3>Digital &amp; Technology Transformation</h3><p>Architecture, cloud, data and operating models that make the enterprise faster and more resilient.</p><a href="{S.href(d, "digital-transformation")}">technology strategy and modernization</a></div><span class="go" aria-hidden="true">{ARROW}</span></article>
        </div>
        <p style="margin-top:28px">{S.btn(d, "contact", "Start a Strategic Conversation", query="?interest=strategy")}</p>
      </div>
    </section>

    <section class="section" id="approach">
      <div class="wrap">
        <div class="section-head">
          <p class="kicker">Our intelligence-driven approach</p>
          <h2>A sharper view. A defensible choice. A path to act.</h2>
        </div>
        <div class="approach">
          <article><span class="ico">{ICONS["risk"]}</span><p class="n">01 — Frame</p><h3>Define the decision</h3><p>Define the decision, the stakes and who owns it.</p></article>
          <article><span class="ico">{ICONS["data"]}</span><p class="n">02 — Connect</p><h3>Bring the signals together</h3><p>Bring together the data, systems and risk signals that bear on it.</p></article>
          <article><span class="ico">{ICONS["ai"]}</span><p class="n">03 — Interpret</p><h3>Turn signals into meaning</h3><p>Turn signals into business meaning: exposure, opportunity, trade-off.</p></article>
          <article><span class="ico">{ICONS["cyber"]}</span><p class="n">04 — Decide</p><h3>Make the options explicit</h3><p>Give leadership clear options with consequences and confidence levels.</p></article>
          <article><span class="ico">{ICONS["digital"]}</span><p class="n">05 — Act</p><h3>Put the decision to work</h3><p>Implement through technology, process and governance.</p></article>
          <article><span class="ico">{ICONS["climate"]}</span><p class="n">06 — Sustain</p><h3>Monitor and adapt</h3><p>Monitor, learn and adapt as conditions change.</p></article>
        </div>
      </div>
    </section>

    <section class="section section-porcelain">
      <div class="wrap why-grid">
        <div>
          <p class="kicker">Why Aryx</p>
          <h2>Connected work, aimed at the decision.</h2>
          <p>Where Aryx sits is the layer between the disciplines. Every future product or platform fits the same promise: it turns complexity into decisions.</p>
        </div>
        <div class="why-points">
          <article><svg viewBox="0 0 32 32" aria-hidden="true"><path d="M6 16h8M18 16h8M16 6v8M16 18v8" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="16" cy="16" r="3" fill="currentColor"/></svg><div><h3>Connected, not siloed</h3><p>We work across AI, cyber, risk, climate and technology, because the most consequential risks sit between them.</p></div></article>
          <article><svg viewBox="0 0 32 32" aria-hidden="true"><path d="M8 22 14 10l4 7 3-4 5 9" fill="none" stroke="currentColor" stroke-width="1.6"/></svg><div><h3>Decision-first</h3><p>Every engagement starts with the decision leadership needs to make, then works back to the data.</p></div></article>
          <article><svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 6 26 11v8c0 6-4.2 9.2-10 11-5.8-1.8-10-5-10-11v-8L16 6z" fill="none" stroke="currentColor" stroke-width="1.6"/></svg><div><h3>Governance built in</h3><p>Controls, accountability and assurance are designed in from the start, not retrofitted.</p></div></article>
          <article><svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M16 8v8l5 3" fill="none" stroke="currentColor" stroke-width="1.6"/></svg><div><h3>Regional depth, global standards</h3><p>Grounded in GCC regulatory and business realities, aligned to international frameworks such as ISO/IEC 27001, ISO/IEC 42001 and the NIST frameworks.</p></div></article>
          <article><svg viewBox="0 0 32 32" aria-hidden="true"><path d="M8 16h16M16 8v16" fill="none" stroke="currentColor" stroke-width="1.6"/></svg><div><h3>Independent perspective</h3><p>Our advice is shaped by your outcome, not by a product we need to sell. {ph("Confirm vendor-neutrality policy and any technology partnerships")}</p></div></article>
        </div>
      </div>
    </section>

    <section class="section" id="industries">
      <div class="wrap">
        <div class="section-head">
          <p class="kicker">Industries served</p>
          <h2>Intelligence shaped by the sector in front of you.</h2>
          <p>Banking &amp; Financial Services · Government &amp; Public Sector · Energy · Infrastructure · Real Estate · Healthcare · Manufacturing · Technology · Professional Services.</p>
          <p><a href="{S.href(d, "industries")}">Explore Industries</a></p>
        </div>
        <div class="industry-grid">
          {"".join(f'<a class="industry-card" href="{S.href(d, slug)}"><span class="ico">{ICONS[key]}</span><h3>{S.e(name)}</h3><p>{S.e(blurb)}</p><span class="more">View sector</span></a>' for slug, name, blurb, key in HOME_INDUSTRIES)}
        </div>
      </div>
    </section>

    <section class="section section-porcelain">
      <div class="wrap split">
        <div>
          <p class="kicker">Technology &amp; innovation</p>
          <h2>Intelligence has to reach the moment of decision.</h2>
        </div>
        <div>
          <img class="shot" src="{S.asset(d, "assets/placeholders/systems.svg")}" alt="Placeholder image of enterprise systems. Replace with photography.">
          <p>Aryx designs and builds the systems that make that possible: AI models and agents that work within governance boundaries, risk platforms that connect cyber and business data, and architectures that keep sensitive information sovereign and secure.</p>
          <p>{ph("Name proprietary platforms or products once launched")}</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap split">
        <div>
          <p class="kicker">Trust &amp; credibility</p>
          <h2>Practitioner-led. Standards-aligned.</h2>
          <p>Leadership with {ph("years")} years across enterprise IT, cybersecurity, risk and sustainability technology.</p>
          <p>Practitioner credentials including {ph("certifications, for example CISM, ISO 27001 Lead Auditor")}.</p>
          <p>Recognition: {ph("awards")}. Client marks are shown only with written permission.</p>
        </div>
        <div>
          <p>Frameworks we work with:</p>
          <div class="frameworks">
            <span class="chip">ISO/IEC 27001</span><span class="chip">ISO/IEC 42001</span><span class="chip">ISO 31000</span>
            <span class="chip">NIST CSF 2.0</span><span class="chip">NIST AI RMF</span><span class="chip">COSO ERM</span>
            <span class="chip">GHG Protocol</span><span class="chip">PCAF</span><span class="chip">IFRS S2</span>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-porcelain" id="insights">
      <div class="wrap">
        <div class="section-head">
          <p class="kicker">Thought leadership</p>
          <h2>Perspectives for leaders navigating AI, cyber and risk decisions.</h2>
          <p><a href="{S.href(d, "insights")}">Read Insights</a></p>
        </div>
        <div class="insight-grid">
          <a class="insight-card" href="{S.href(d, "insights/ai-governance-for-boards")}">
            <img class="ph" src="{S.asset(d, "assets/placeholders/board.svg")}" alt="Placeholder image for the AI governance article.">
            <div class="body"><p class="cat">AI Governance</p><h3>What Boards Should Ask About AI Governance</h3><p>The questions boards should ask about AI governance, accountability and risk, and what good answers sound like.</p></div>
          </a>
          <a class="insight-card" href="{S.href(d, "insights/integrated-risk-management")}">
            <img class="ph" src="{S.asset(d, "assets/placeholders/network.svg")}" alt="Placeholder image for the integrated risk article.">
            <div class="body"><p class="cat">Risk Intelligence</p><h3>Integrated Risk Management: Beyond the GRC Tool</h3><p>Why risk registers miss connected exposures, and how integrated risk management gives leaders a decision-ready view.</p></div>
          </a>
          <a class="insight-card" href="{S.href(d, "insights/cyber-resilience-strategy")}">
            <img class="ph" src="{S.asset(d, "assets/placeholders/city.svg")}" alt="Placeholder image for the cyber resilience article.">
            <div class="body"><p class="cat">Cybersecurity</p><h3>Cyber Resilience as a Board-Level Strategy</h3><p>Why cyber resilience, not only prevention, belongs on the board agenda, and how to measure it in business terms.</p></div>
          </a>
        </div>
      </div>
    </section>

    <section class="section section-ink">
      <div class="wrap cta-band">
        <div>
          <h2>The decisions are getting harder. The picture can get clearer.</h2>
          <p>Tell us the decision in front of you. We will show you what intelligence would change it.</p>
        </div>
        {S.btn(d, "contact", "Discuss Your Challenge", query="?interest=strategy")}
      </div>
    </section>

    <section class="section" id="faq">
      <div class="wrap">
        <div class="section-head"><p class="kicker">Questions</p><h2>Homepage FAQ</h2></div>
        {S.faq_html(faqs)}
      </div>
    </section>
    """
    schemas = [
        S.org_schema(),
        {"@type": "WebSite", "name": "Aryx Intelligence", "url": S.ORIGIN + "/", "publisher": {"@id": S.ORIGIN + "/#organization"}},
        {"@type": "WebPage", "name": "Aryx Intelligence | AI, Cyber & Risk Intelligence", "description": HOME_DESC, "url": S.canonical("")},
        S.faq_schema(faqs),
    ]
    S.add("", d, "home", "Aryx Intelligence | AI, Cyber & Risk Intelligence", HOME_DESC, body, schemas)


HOME_DESC = "Aryx Intelligence connects AI, cyber, risk, climate and enterprise technology to help leaders make clearer, faster, defensible decisions. Based in Qatar."

HOME_INDUSTRIES = [
    ("industries/banking", "Banking & Financial Services", "AI, cyber, operational resilience and third-party risk under demanding supervision.", "bank"),
    ("industries/government", "Government & Public Sector", "Digital services and AI that stay secure, sovereign and explainable.", "gov"),
    ("industries/energy", "Energy", "IT, operational technology and the energy transition, seen together.", "energy"),
    ("industries/infrastructure", "Infrastructure", "Connected, long-lived systems and the dependencies that fail together.", "infra"),
    ("industries/real-estate", "Real Estate", "Smart buildings, tenant data, vendors and sustainability expectations.", "estate"),
    ("industries/healthcare", "Healthcare", "Sensitive data, always-available systems and governed clinical AI.", "health"),
    ("industries/manufacturing", "Manufacturing", "Connected factories and supply chains as a single risk surface.", "factory"),
    ("industries/technology", "Technology", "Product security and AI governance designed in as a trust feature.", "tech"),
    ("industries/professional-services", "Professional Services", "Client confidentiality and generative AI, designed to coexist.", "firm"),
]
