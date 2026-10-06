# -*- coding: utf-8 -*-
import build_site as S
import site_more as M

INDUSTRY_PAGES = [
    {
        "slug": "industries/banking", "key": "banking", "name": "Banking & Financial Services",
        "title": "Banking AI, Cyber & Risk Intelligence | Aryx",
        "desc": "AI governance, cyber risk, operational resilience, third-party risk and financed emissions for banks. Aryx Intelligence, Qatar and GCC.",
        "challenge": "Banks must adopt AI and digital channels quickly while meeting some of the most demanding supervisory expectations for cyber, AI, operational resilience and third-party risk.",
        "perspective": "Regulation is a design input, not a hurdle. Institutions that build governance into AI and digital programs from the start move faster than those who retrofit it.",
        "capabilities": ["AI governance aligned to supervisory guidance", "Cyber risk quantification", "Operational resilience", "Third-party and cloud risk", "Fraud and financial-crime analytics strategy", "Climate risk and PCAF-aligned financed emissions"],
        "outcomes": "Faster, approvable AI use cases; board-ready cyber and resilience reporting; supervisory evidence on demand.",
        "cta": "Explore Financial Services Intelligence",
        "insight": ("insights/climate-risk-management-banking", "Climate risk management in banking"),
        "links": [("ai-intelligence", "AI governance"), ("cybersecurity", "cybersecurity"), ("risk-decision-intelligence", "risk and decision intelligence"), ("climate-intelligence", "climate intelligence")],
        "faqs": [
            ("What challenge does Aryx address in banking?", "Banks must adopt AI and digital channels quickly while meeting some of the most demanding supervisory expectations for cyber, AI, operational resilience and third-party risk."),
            ("How does Aryx treat regulation in financial services?", "Regulation is a design input, not a hurdle. Institutions that build governance into AI and digital programs from the start move faster than those who retrofit it."),
            ("What outcomes are designed for banks?", "Faster, approvable AI use cases; board-ready cyber and resilience reporting; and supervisory evidence on demand."),
        ],
    },
    {
        "slug": "industries/government", "key": "government", "name": "Government & Public Sector",
        "title": "Government AI, Cyber & Risk Intelligence | Aryx",
        "desc": "Digital government strategy, AI governance, security architecture and data sovereignty for public-sector leaders. Aryx Intelligence.",
        "challenge": "Governments are digitizing services and adopting AI while protecting national data, critical services and public trust.",
        "perspective": "Public-sector technology succeeds when it is secure, sovereign and explainable to citizens as well as officials.",
        "capabilities": ["Digital government strategy", "AI governance and ethics", "National-scale security architecture", "Data sovereignty", "Program risk oversight"],
        "outcomes": "Trusted digital services, defensible AI use, resilient critical systems.",
        "cta": "Discuss a Public-Sector Priority",
        "insight": ("insights/ai-governance-for-boards", "AI governance for boards"),
        "links": [("ai-intelligence", "AI governance"), ("cybersecurity", "cybersecurity"), ("digital-transformation", "digital and technology transformation")],
        "faqs": [
            ("What challenge does Aryx address in government?", "Governments are digitizing services and adopting AI while protecting national data, critical services and public trust."),
            ("What does public-sector technology need in order to succeed?", "It succeeds when it is secure, sovereign and explainable to citizens as well as officials."),
            ("What outcomes are designed for the public sector?", "Trusted digital services, defensible AI use and resilient critical systems."),
        ],
    },
    {
        "slug": "industries/energy", "key": "energy", "name": "Energy",
        "title": "Energy OT Security, AI & Climate Risk | Aryx",
        "desc": "OT and IT security, operational resilience, transition risk and asset analytics for energy companies. Aryx Intelligence.",
        "challenge": "Energy companies operate critical infrastructure where IT and operational technology converge, while navigating the energy transition and growing climate-related disclosure expectations.",
        "perspective": "In energy, a cyber event is a safety and continuity event. Risk must be seen across IT, OT and the supply chain together.",
        "capabilities": ["OT and IT security strategy", "Operational resilience", "AI for asset and operations analytics", "Third-party risk", "Climate and transition risk intelligence"],
        "outcomes": "Protected operations, clearer transition risk visibility, data-driven asset decisions.",
        "cta": "Assess Your Operational Risk",
        "insight": ("insights/cyber-resilience-strategy", "Cyber resilience as a board-level strategy"),
        "links": [("cybersecurity", "cybersecurity"), ("climate-intelligence", "climate intelligence"), ("risk-decision-intelligence", "risk intelligence")],
        "faqs": [
            ("What challenge does Aryx address in energy?", "Energy companies operate critical infrastructure where IT and operational technology converge, while navigating the energy transition and growing climate-related disclosure expectations."),
            ("How should energy risk be seen?", "In energy, a cyber event is a safety and continuity event. Risk must be seen across IT, OT and the supply chain together."),
            ("What outcomes are designed for energy companies?", "Protected operations, clearer transition risk visibility and data-driven asset decisions."),
        ],
    },
    {
        "slug": "industries/infrastructure", "key": "infrastructure", "name": "Infrastructure",
        "title": "Infrastructure Security & Resilience | Aryx",
        "desc": "Critical-infrastructure security, dependency modelling and modernization for transport, utilities and smart-city systems. Aryx Intelligence.",
        "challenge": "Transport, utilities and smart-city systems are increasingly connected, long-lived and difficult to modernize without disruption.",
        "perspective": "Infrastructure resilience depends on knowing which dependencies would fail together.",
        "capabilities": ["Critical-infrastructure security", "Dependency and scenario modelling", "Technology modernization planning", "AI for monitoring and maintenance"],
        "outcomes": "Fewer cascading failures, modernization without loss of service, better capital decisions.",
        "cta": "Map Your Critical Dependencies",
        "insight": ("insights/integrated-risk-management", "Integrated risk management"),
        "links": [("cybersecurity", "critical-infrastructure security"), ("risk-decision-intelligence", "scenario intelligence"), ("digital-transformation", "technology modernization")],
        "faqs": [
            ("What challenge does Aryx address in infrastructure?", "Transport, utilities and smart-city systems are increasingly connected, long-lived and difficult to modernize without disruption."),
            ("What does infrastructure resilience depend on?", "Infrastructure resilience depends on knowing which dependencies would fail together."),
            ("What outcomes are designed for infrastructure operators?", "Fewer cascading failures, modernization without loss of service and better capital decisions."),
        ],
    },
    {
        "slug": "industries/real-estate", "key": "real-estate", "name": "Real Estate",
        "title": "Real Estate Cyber, Data & Sustainability | Aryx",
        "desc": "Smart-building security, portfolio analytics, vendor risk and sustainability data for developers and owners. Aryx Intelligence.",
        "challenge": "Developers and owners manage smart buildings, tenant data, large vendor ecosystems and rising sustainability expectations.",
        "perspective": "A smart building is also a network. Its value depends on the data and security behind it.",
        "capabilities": ["Smart-building and IoT security", "Portfolio data and analytics", "Vendor risk", "AI for operations and leasing insight", "Sustainability data foundations"],
        "outcomes": "Secure connected assets, better portfolio decisions, credible sustainability reporting.",
        "cta": "Explore Real Estate Intelligence",
        "insight": ("insights/climate-risk-management-banking", "Climate Risk Management in Banking: From Disclosure to Decision"),
        "links": [("cybersecurity", "cybersecurity"), ("climate-intelligence", "sustainability data"), ("digital-transformation", "data and analytics")],
        "faqs": [
            ("What challenge does Aryx address in real estate?", "Developers and owners manage smart buildings, tenant data, large vendor ecosystems and rising sustainability expectations."),
            ("How does Aryx view a smart building?", "A smart building is also a network. Its value depends on the data and security behind it."),
            ("What outcomes are designed for real estate organizations?", "Secure connected assets, better portfolio decisions and credible sustainability reporting."),
        ],
    },
    {
        "slug": "industries/healthcare", "key": "healthcare", "name": "Healthcare",
        "title": "Healthcare Data Security & AI Governance | Aryx",
        "desc": "Health data security, clinical-system resilience and governed AI for healthcare organizations. Aryx Intelligence.",
        "challenge": "Healthcare organizations hold highly sensitive data, depend on always-available systems and face growing interest in clinical and operational AI.",
        "perspective": "In healthcare, availability and trust are clinical concerns. AI must be safe, explainable and governed.",
        "capabilities": ["Health data security and privacy", "Clinical-system resilience", "AI governance for clinical and operational use", "Medical-device and third-party risk"],
        "outcomes": "Protected patient data, resilient care delivery, responsible AI adoption.",
        "cta": "Discuss Healthcare Resilience",
        "insight": ("insights/ai-governance-for-boards", "What boards should ask about AI governance"),
        "links": [("cybersecurity", "cybersecurity"), ("ai-intelligence", "AI governance"), ("risk-decision-intelligence", "third-party risk")],
        "faqs": [
            ("What challenge does Aryx address in healthcare?", "Healthcare organizations hold highly sensitive data, depend on always-available systems and face growing interest in clinical and operational AI."),
            ("How should AI be treated in healthcare?", "In healthcare, availability and trust are clinical concerns. AI must be safe, explainable and governed."),
            ("What outcomes are designed for healthcare organizations?", "Protected patient data, resilient care delivery and responsible AI adoption."),
        ],
    },
    {
        "slug": "industries/manufacturing", "key": "manufacturing", "name": "Manufacturing",
        "title": "Manufacturing OT & Supply-Chain Risk | Aryx",
        "desc": "OT security, supply-chain risk intelligence and modernization for connected factories. Aryx Intelligence.",
        "challenge": "Connected factories and global supply chains raise productivity and exposure at the same time.",
        "perspective": "The supply chain is now a risk surface. Visibility across suppliers and production systems is a competitive advantage.",
        "capabilities": ["OT security", "Supply-chain and third-party risk intelligence", "AI for quality and maintenance", "Technology modernization"],
        "outcomes": "Fewer disruptions, earlier warning of supplier risk, higher operational efficiency.",
        "cta": "Strengthen Supply-Chain Intelligence",
        "insight": ("insights/integrated-risk-management", "Integrated risk management"),
        "links": [("cybersecurity", "OT security"), ("risk-decision-intelligence", "third-party risk"), ("ai-intelligence", "AI for operations")],
        "faqs": [
            ("What challenge does Aryx address in manufacturing?", "Connected factories and global supply chains raise productivity and exposure at the same time."),
            ("How does Aryx view the supply chain?", "The supply chain is now a risk surface. Visibility across suppliers and production systems is a competitive advantage."),
            ("What outcomes are designed for manufacturers?", "Fewer disruptions, earlier warning of supplier risk and higher operational efficiency."),
        ],
    },
    {
        "slug": "industries/technology", "key": "technology", "name": "Technology",
        "title": "Product Security & AI Governance | Aryx",
        "desc": "Product and cloud security, AI governance and customer assurance for technology companies. Aryx Intelligence.",
        "challenge": "Technology companies must ship quickly, secure their products and customers, and govern the AI they build into them.",
        "perspective": "Trust is now a product feature. Security and AI governance designed in become a sales advantage.",
        "capabilities": ["Product and cloud security architecture", "AI governance and AI security", "Secure development practices", "Customer assurance readiness"],
        "outcomes": "Faster enterprise sales cycles, fewer security incidents, credible AI assurance.",
        "cta": "Build Trust Into Your Product",
        "insight": ("insights/ai-governance-for-boards", "AI governance for boards"),
        "links": [("cybersecurity", "product security"), ("ai-intelligence", "AI governance and AI security")],
        "faqs": [
            ("What challenge does Aryx address for technology companies?", "Technology companies must ship quickly, secure their products and customers, and govern the AI they build into them."),
            ("How does Aryx view trust in technology products?", "Trust is now a product feature. Security and AI governance designed in become a sales advantage."),
            ("What outcomes are designed for technology companies?", "Faster enterprise sales cycles, fewer security incidents and credible AI assurance."),
        ],
    },
    {
        "slug": "industries/professional-services", "key": "professional-services", "name": "Professional Services",
        "title": "Responsible AI for Professional Services | Aryx",
        "desc": "Generative AI guardrails, data protection and knowledge-work intelligence for professional firms. Aryx Intelligence.",
        "challenge": "Firms hold confidential client information and are adopting generative AI across knowledge work.",
        "perspective": "Client confidentiality and AI productivity can coexist, but only with deliberate data and access design.",
        "capabilities": ["Generative AI strategy and guardrails", "Data protection", "Identity and access", "Third-party risk", "Knowledge-management intelligence"],
        "outcomes": "Productive, compliant AI use; protected client data; stronger client trust.",
        "cta": "Explore Responsible AI for Your Firm",
        "insight": ("insights/ai-governance-for-boards", "AI governance for boards"),
        "links": [("ai-intelligence", "generative AI"), ("cybersecurity", "identity and access")],
        "faqs": [
            ("What challenge does Aryx address in professional services?", "Firms hold confidential client information and are adopting generative AI across knowledge work."),
            ("Can client confidentiality and AI productivity coexist?", "They can, but only with deliberate data and access design."),
            ("What outcomes are designed for professional firms?", "Productive, compliant AI use, protected client data and stronger client trust."),
        ],
    },
]

CALENDAR = {
    "artificial-intelligence": ["Enterprise AI Strategy: From Pilots to Measurable Value", "Where to Start With Generative AI in a Regulated Enterprise", "AI Agents in the Enterprise: What Leaders Must Decide First", "Decision Intelligence Explained for Executives", "Measuring AI ROI: A Framework for Boards"],
    "ai-governance": ["ISO/IEC 42001 Explained: Is an AI Management System Worth It?", "AI Regulation in the GCC: What Enterprises Need to Know", "The EU AI Act for Non-EU Companies", "Building an AI Inventory: The First Step in AI Governance"],
    "cybersecurity": ["Cyber Risk Quantification: Putting a Number on Exposure", "How Boards Should Read a Cybersecurity Report", "Securing AI Systems: The New Attack Surface", "Zero Trust Explained for Executives", "Third-Party Cyber Risk: Managing the Exposure You Do Not Control", "Cybersecurity in Qatar: Regulation and Priorities for Leaders", "Ten Questions Every CEO Should Ask Their CISO"],
    "risk-intelligence": ["Risk Intelligence vs Risk Management: What Changes", "Scenario Analysis for Executive Decision-Making", "Technology Risk: The Exposure Hiding in Legacy Systems", "Operational Resilience: Mapping Important Business Services"],
    "digital-transformation": ["Digital Transformation Strategy That Delivers Results", "Is Your Data Ready for AI?", "Data Sovereignty and Cloud in the GCC", "Enterprise Architecture as a Decision Tool"],
    "enterprise-technology": ["Enterprise Architecture as a Decision Tool", "Quantum Readiness: What Leaders Should Do Now"],
    "emerging-technology": ["Quantum Readiness: What Leaders Should Do Now", "Synthetic Media and Deepfakes: An Executive Risk"],
    "executive-perspectives": ["Ten Questions Every CEO Should Ask Their CISO", "The Connected Enterprise: Why AI, Cyber and Risk Must Converge"],
    "climate-sustainability": ["Financed Emissions and PCAF: A Practical Guide for Banks", "GHG Accounting From Spreadsheet to Assurance", "IFRS S2 Readiness for GCC Companies", "Choosing an ESG Data Platform"],
}

CATEGORIES = [
    ("insights/artificial-intelligence", "artificial-intelligence", "Artificial Intelligence", "Enterprise AI strategy, agents and generative AI in practice: where value is measurable, and how use cases move from pilot to production without leaving governance behind."),
    ("insights/ai-governance", "ai-governance", "AI Governance", "Regulation, risk classification, oversight and assurance for enterprise AI, written for boards, general counsel and the executives who own the systems."),
    ("insights/cybersecurity", "cybersecurity", "Cybersecurity", "Strategy, cyber risk, resilience and AI security, treated as a business-risk discipline rather than a control count."),
    ("insights/risk-intelligence", "risk-intelligence", "Risk Intelligence", "Integrated, third-party, technology and scenario risk: how exposures connect, and which decision they demand next."),
    ("insights/digital-transformation", "digital-transformation", "Digital Transformation", "Architecture, cloud, data and operating models, judged by business results rather than go-lives."),
    ("insights/enterprise-technology", "enterprise-technology", "Enterprise Technology", "Platforms, modernization and sovereignty: the technology decisions that determine whether intelligence can reach leaders."),
    ("insights/emerging-technology", "emerging-technology", "Emerging Technology", "Developments leaders should track, with the practical implications for risk, security and operating decisions."),
    ("insights/executive-perspectives", "executive-perspectives", "Executive Perspectives", "Board and C-suite questions and decision frameworks for leaders who are accountable for the outcome."),
    ("insights/climate-sustainability", "climate-sustainability", "Climate & Sustainability", "Climate risk, GHG and financed emissions, ESG data and reporting, connected to enterprise risk and capital decisions."),
]

def register():
    industries_hub()
    for item in INDUSTRY_PAGES:
        industry(item)
    insights_hub()
    for cat in CATEGORIES:
        category(cat)

def industries_hub():
    d, slug = 1, "industries"
    title = "Industries We Serve | Aryx Intelligence"
    desc = "AI, cybersecurity and risk intelligence for banking, government, energy, infrastructure, real estate, healthcare, manufacturing and more."
    cards = []
    for item in INDUSTRY_PAGES:
        cards.append(f'<a class="industry-card" href="{S.href(d, item["slug"])}"><h3>{S.e(item["name"])}</h3><p>{S.e(item["challenge"])}</p><span class="more">View sector</span></a>')
    body = f"""
    {M.page_hero(d, [("Home", ""), ("Industries", None)], "Industries", "Intelligence shaped by the realities of your sector",
      "Every sector faces the same forces: AI adoption, cyber threat and regulatory change. How they combine is specific to each one. We bring cross-sector discipline and sector-specific understanding to the decisions that matter in yours.")}
    <section class="section"><div class="wrap"><div class="industry-grid">{"".join(cards)}</div></div></section>
    """
    trail = [("Home", ""), ("Industries", None)]
    S.add(slug, d, "industries", title, desc, body, [M.web(slug, title, desc), S.crumb_schema(trail)])

def industry(item):
    d, slug = 2, item["slug"]
    caps = "".join(f"<li>{S.e(c)}</li>" for c in item["capabilities"])
    links = ", ".join(f'<a href="{S.href(d, href)}">{label}</a>' for href, label in item["links"])
    insight_href, insight_label = item["insight"]
    h1 = item["name"] + " AI, cyber and risk intelligence"
    body = f"""
    {M.page_hero(d, [("Home", ""), ("Industries", "industries"), (item["name"], None)], item["name"], S.e(h1),
      S.e(item["challenge"]),
      S.btn(d, "contact", S.e(item["cta"]), query="?interest=strategy"))}
    <section class="section"><div class="wrap prose">
      <h2>The challenge</h2>
      <p>{item["challenge"]}</p>
      <h2>The Aryx perspective</h2>
      <p>{item["perspective"]}</p>
      <h2>Capabilities</h2>
      <ul>{caps}</ul>
      <h2>Outcomes</h2>
      <p>{item["outcomes"]}</p>
      <h2>Related insight</h2>
      <p><a href="{S.href(d, insight_href)}">{S.e(insight_label)}</a></p>
      <h2>Connected capabilities</h2>
      <p>{links}.</p>
      <p>Case evidence for this sector is published only where it is real. {M.ph("Case study")}</p>
    </div></section>
    <section class="section section-ink"><div class="wrap cta-band"><div><h2>{S.e(item["cta"])}</h2><p>{item["outcomes"]}</p></div>{S.btn(d, "contact", item["cta"], query="?interest=strategy")}</div></section>
    <section class="section"><div class="wrap"><div class="section-head"><h2>Questions leaders ask</h2></div>{S.faq_html(item["faqs"])}</div></section>
    """
    # fix h1 - I made a mess with the ternary. page_hero title arg is inserted raw. item["h1"] is correct if I pass it.
    trail = [("Home", ""), ("Industries", "industries"), (item["name"], None)]
    S.add(slug, d, item["key"], item["title"], item["desc"], body, [
        M.web(slug, item["title"], item["desc"]),
        M.service(item["name"] + " intelligence", item["desc"], slug),
        S.faq_schema(item["faqs"]),
        S.crumb_schema(trail),
    ])

def insights_hub():
    d, slug = 1, "insights"
    title = "Insights on AI, Cyber & Risk | Aryx Intelligence"
    desc = "Executive perspectives on enterprise AI, AI governance, cybersecurity, risk intelligence and technology strategy from Aryx Intelligence."
    import site_articles
    cards = []
    for art in site_articles.ARTICLES:
        cards.append(f'''<a class="insight-card" href="{S.href(d, art["slug"])}"><div class="ph">Placeholder image</div><div class="body"><p class="cat">{S.e(art["category"])}</p><h3>{S.e(art["title"])}</h3><p>{S.e(art["excerpt"])}</p></div></a>''')
    filters = f'<a href="{S.href(d, "insights")}" aria-current="page">All</a>' + "".join(
        f'<a href="{S.href(d, cslug)}">{S.e(name)}</a>' for cslug, _, name, _ in CATEGORIES
    )
    body = f"""
    {M.page_hero(d, [("Home", ""), ("Insights", None)], "Insights", "Insights for leaders making consequential decisions",
      "Clear thinking on the forces reshaping enterprise decisions. Written for boards, executives and the leaders who advise them: evidence-led, practical and free of hype.")}
    <section class="section"><div class="wrap">
      <div class="filters" aria-label="Insight categories">{filters}</div>
      <div class="insight-grid">{"".join(cards)}</div>
      <div class="section-head" style="margin-top:56px"><h2>Questions leaders are asking</h2>
        <p>Definitions and board questions live with the work they belong to: <a href="{S.href(d, "ai-intelligence")}">enterprise AI</a>, <a href="{S.href(d, "cybersecurity")}">cybersecurity</a>, <a href="{S.href(d, "risk-decision-intelligence")}">risk intelligence</a> and <a href="{S.href(d, "climate-intelligence")}">climate intelligence</a>.</p>
      </div>
      <form data-aryx-form data-success="Thank you. The Aryx Brief will be sent once the list is connected.">
        <p class="hp"><label>Company website <input name="company_website" tabindex="-1" autocomplete="off"></label></p>
        <input type="hidden" name="form" value="newsletter">
        <h2>The Aryx Brief</h2>
        <p>One considered perspective each month on AI, cyber and risk decisions.</p>
        <label>Work email <input type="email" name="email" required autocomplete="email"></label>
        <button class="btn btn-primary" type="submit">Subscribe to The Aryx Brief</button>
        <p class="form-note" hidden></p>
      </form>
    </div></section>
    """
    trail = [("Home", ""), ("Insights", None)]
    S.add(slug, d, "insights", title, desc, body, [M.web(slug, title, desc), S.crumb_schema(trail)])

def category(cat):
    cslug, key, name, intro = cat
    d = 2
    title = f"{name} Insights | Aryx Intelligence"
    desc = intro
    import site_articles
    cards = []
    for art in site_articles.ARTICLES:
        if key in art["categories"]:
            cards.append(f'''<a class="insight-card" href="{S.href(d, art["slug"])}"><div class="ph">Placeholder image</div><div class="body"><p class="cat">{S.e(art["category"])}</p><h3>{S.e(art["title"])}</h3><p>{S.e(art["excerpt"])}</p></div></a>''')
    upcoming = "".join(f"<li>{S.e(t)}</li>" for t in CALENDAR.get(key, []))
    grid = "".join(cards) or "<p>Published perspectives in this category will appear here. Titles on the editorial calendar are listed below and are not yet articles.</p>"
    filters = f'<a href="{S.href(d, "insights")}">All</a>' + "".join(
        f'<a href="{S.href(d, s)}"' + (' aria-current="page"' if s == cslug else "") + f'>{S.e(n)}</a>'
        for s, _, n, _ in CATEGORIES
    )
    body = f"""
    {M.page_hero(d, [("Home", ""), ("Insights", "insights"), (name, None)], "Insights", name, intro)}
    <section class="section"><div class="wrap">
      <div class="filters" aria-label="Insight categories">{filters}</div>
      <div class="insight-grid">{grid}</div>
      <div class="prose" style="margin-top:48px">
        <h2>On the editorial calendar</h2>
        <p>These titles are planned. They are not published pages until the article is written.</p>
        <ul>{upcoming}</ul>
      </div>
    </div></section>
    """
    trail = [("Home", ""), ("Insights", "insights"), (name, None)]
    S.add(cslug, d, "insights", title, desc, body, [M.web(cslug, title, desc), S.crumb_schema(trail)])
