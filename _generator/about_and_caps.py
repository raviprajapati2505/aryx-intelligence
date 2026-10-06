# -*- coding: utf-8 -*-
import build_site as S
import site_more as M

def register():
    about()
    ai()
    cyber()
    digital()
    risk()
    climate()

def about():
    d, slug = 1, "about"
    title = "About Aryx Intelligence | Decision Intelligence, Qatar"
    desc = "Aryx Intelligence is a Doha-headquartered decision-intelligence company connecting AI, cybersecurity and risk to help leaders decide with clarity."
    body = f"""
    {M.page_hero(d, [("Home", ""), ("About", None)], "About Aryx", "We exist to make complex decisions clearer",
      "Aryx Intelligence was founded on a simple observation: the most consequential failures in modern organizations rarely come from a lack of information. They come from information that never connected.",
      S.btn(d, "contact", "Talk to Aryx") + S.text_link(d, "insights", "Read Insights"))}
    <section class="section"><div class="wrap prose">
      <p>A security team sees an anomaly. A risk team logs a vendor concern. A technology team plans a migration. A board approves an AI initiative. Each decision is reasonable on its own. Together, they can create an exposure no one saw, because no one was looking across them.</p>
      <p>Aryx was built to look across. We bring the disciplines of AI, cybersecurity, risk and enterprise technology into one line of sight, and we orient that view toward the decisions leaders actually make. {M.ph("Founding year and founding context")}</p>
      <h2>Mission</h2>
      <p>To help organizations turn complexity into intelligence, and intelligence into decisions they can act on and defend.</p>
      <h2>Vision</h2>
      <p>A world where institutions anticipate rather than react: where leaders see their risks, technology and opportunities as one connected picture, and act with confidence.</p>
      <h2>What “intelligence” means to Aryx</h2>
      <p>Intelligence is not data, and it is not technology. It is understanding that is timely, relevant and trustworthy enough to act on. For Aryx, intelligence has four tests:</p>
      <ul>
        <li><strong>Connected</strong> — it draws on every signal that bears on the decision, across functions.</li>
        <li><strong>Contextual</strong> — it is interpreted for this organization, its strategy and its risk appetite.</li>
        <li><strong>Accountable</strong> — its sources, assumptions and confidence are clear, so it can be defended.</li>
        <li><strong>Actionable</strong> — it arrives in time and in a form that changes what happens next.</li>
      </ul>
      <h2>Our philosophy</h2>
      <ul>
        <li><strong>Decisions before dashboards.</strong> We start with the question leadership needs answered, then build only what serves it.</li>
        <li><strong>Governance is a design choice.</strong> Trust in AI, data and security is earned through controls designed in from the start.</li>
        <li><strong>Technology serves judgment.</strong> AI and automation extend human judgment. They do not replace accountability.</li>
        <li><strong>Resilience is continuous.</strong> Risk does not wait for an annual review, so neither does our view of it.</li>
      </ul>
      <h2>How we work</h2>
      <p>We work as an extension of the leadership team, not as an outside vendor. Engagements are scoped around a decision or an outcome, staffed by senior practitioners, and measured against results the client defines. We transfer capability as we go, so organizations keep the intelligence they build.</p>
      <h2>Leadership</h2>
      <p>Aryx is led by practitioners who have built, secured and governed enterprise technology at scale. Our leadership combines experience across enterprise IT, cybersecurity, risk, audit and sustainability technology.</p>
      <div class="two">
        <article class="note"><h3>{M.ph("Leader name, title")}</h3><p>{M.ph("Short bio: domains, years of experience, verifiable credentials and recognitions")}</p></article>
        <article class="note"><h3>{M.ph("Leader name, title")}</h3><p>{M.ph("Short bio")}</p></article>
      </div>
      <h2>Global ambition</h2>
      <p>Aryx is headquartered in Doha, Qatar, a regional center for finance, energy and public-sector investment. We bring a deep understanding of GCC regulation, culture and pace of change, and we work to international standards. Our ambition is to be the intelligence partner that institutions in the region and beyond trust with their most consequential decisions. {M.ph("Confirm offices or delivery presence outside Qatar")}</p>
    </div></section>
    <section class="section section-ink"><div class="wrap cta-band"><div><h2>Every partnership begins with a question worth answering.</h2></div>{S.btn(d, "contact", "Talk to Aryx")}</div></section>
    """
    trail = [("Home", ""), ("About", None)]
    S.add(slug, d, "about", title, desc, body, [web_about(title, desc), S.crumb_schema(trail)])

def web_about(title, desc):
    data = M.web("about", title, desc, "AboutPage")
    data["about"] = {"@id": S.ORIGIN + "/#organization"}
    return data

def ai():
    d, slug = 1, "ai-intelligence"
    title = "Enterprise AI Strategy & Governance | Aryx Intelligence"
    desc = "Enterprise AI strategy, AI agents, decision intelligence and AI governance built around measurable outcomes. Aryx Intelligence, Qatar and GCC."
    faqs = [
        ("Where should we start with enterprise AI?", "Start with a decision or process where value is measurable, data exists and the risk is manageable. A focused first use case builds both evidence and governance muscle."),
        ("What is AI governance?", "AI governance is the set of policies, roles, controls and oversight that ensure AI systems are used safely, lawfully and in line with business objectives across their lifecycle."),
        ("How do you keep sensitive data secure when using generative AI?", "Through data classification, architecture choices such as private or in-region deployment, access controls and output monitoring, decided before any model sees sensitive data."),
        ("What is the difference between AI automation and AI agents?", "Automation executes a defined task. An agent pursues a goal across steps and systems, choosing actions within limits, so it needs stronger permissions design and oversight."),
    ]
    caps = [
        ("ai-strategy", "AI strategy", "Identify where AI creates measurable value, prioritize use cases by impact and feasibility, and build a roadmap leadership can fund with confidence."),
        ("decision-intelligence", "Decision intelligence", "Connect data, analytics and AI to specific decisions, such as credit, pricing, resource allocation or threat response, so choices become faster, more consistent and auditable."),
        ("generative-ai", "Generative AI", "Deploy large language models for knowledge work, document intelligence and customer interaction, with guardrails for accuracy, privacy and data sovereignty."),
        ("ai-agents", "AI agents", "Design agents that take bounded actions across systems, with defined permissions, human checkpoints and full audit trails."),
        ("ai-automation", "AI automation", "Automate high-volume, rules-heavy processes where AI improves accuracy and frees people for judgment-based work."),
        ("inventory", "AI governance", "Establish policies, risk classification, model inventories, oversight roles and assurance aligned to ISO/IEC 42001, the NIST AI Risk Management Framework and applicable regulation, including sector rules such as the Qatar Central Bank's AI Guideline for licensed entities."),
        ("transformation", "AI-enabled business transformation", "Redesign processes and operating models around AI, so value is captured in the business, not stranded in a pilot."),
        ("systems", "Intelligent systems", "Architect the data, platforms and integration that let AI run reliably in production."),
    ]
    cap_html = "".join(f'<article id="{i}" class="cap-row"><span class="idx">{n:02d}</span><div><h3>{t}</h3><p>{p}</p></div></article>' for n, (i, t, p) in enumerate(caps, 1))
    anchors = "".join(f'<a href="#{i}">{t}</a>' for i, t, _ in caps)
    body = f"""
    {M.page_hero(d, [("Home", ""), ("AI & Intelligence", None)], "AI & Intelligence", "Enterprise AI that answers to the business",
      "We help organizations decide where AI creates value, build it responsibly, and govern it with the same discipline as any material risk.",
      S.btn(d, "contact", "Explore Enterprise AI", query="?interest=ai") + S.text_link(d, "contact", "Assess Your AI Readiness", "?interest=ai"))}
    <section class="section-tight"><div class="wrap"><div class="anchor-strip">{anchors}</div></div></section>
    <section class="section"><div class="wrap prose">
      <h2>The problem with most enterprise AI</h2>
      <p>Many organizations have AI pilots. Far fewer have AI that changes how decisions are made, at scale, with controls a regulator and a board would accept. The gap is rarely the model. It is unclear ownership, weak data foundations, missing governance and use cases chosen for novelty rather than value.</p>
      <h2>What enterprise AI means at Aryx</h2>
      <p>Enterprise AI is the use of machine learning, generative AI and intelligent automation inside core business processes, governed so that its outputs are reliable, explainable and accountable. We judge it by one test: does it improve a decision or an outcome the business cares about?</p>
    </div></section>
    <section class="section section-porcelain"><div class="wrap">
      <div class="section-head"><h2>Capabilities</h2></div>
      <div class="cap-list">{cap_html}</div>
    </div></section>
    <section class="section"><div class="wrap">
      <div class="section-head"><h2>Outcomes we design for</h2></div>
      <div class="table-wrap"><table>
        <thead><tr><th>Outcome</th><th>What it looks like</th></tr></thead>
        <tbody>
          <tr><td>Faster decisions</td><td>Shorter cycle times on approvals, investigations and analysis</td></tr>
          <tr><td>Better decisions</td><td>More consistent outcomes, fewer errors, clearer rationale</td></tr>
          <tr><td>Lower risk</td><td>AI inventoried, classified, monitored and explainable</td></tr>
          <tr><td>Scalable value</td><td>Use cases that move from pilot to production with known economics</td></tr>
          <tr><td>Regulatory confidence</td><td>Evidence ready for boards, auditors and supervisors</td></tr>
        </tbody>
      </table></div>
      <div class="prose">
        <h2>How an AI engagement works</h2>
        <ol>
          <li><strong>Readiness</strong> — Data, technology, skills and governance assessed against the ambition.</li>
          <li><strong>Prioritization</strong> — Use cases scored on value, feasibility and risk.</li>
          <li><strong>Design</strong> — Architecture, controls and human oversight defined before build.</li>
          <li><strong>Delivery</strong> — Build, test and deploy, with validation evidence captured as we go.</li>
          <li><strong>Assurance</strong> — Monitoring for performance, drift, bias and security, reported in business terms.</li>
        </ol>
        <p>Related work: <a href="{S.href(d, "risk-decision-intelligence")}">managing AI as an enterprise risk</a>, <a href="{S.href(d, "cybersecurity")}">securing AI systems</a>, and <a href="{S.href(d, "digital-transformation")}">data foundations for AI</a>.</p>
        <p>For boards, read <a href="{S.href(d, "insights/ai-governance-for-boards")}">AI governance for boards</a>.</p>
      </div>
    </div></section>
    <section class="section section-ink"><div class="wrap cta-band"><div><h2>Find out where AI will change your decisions, and what it will take to govern it.</h2></div>{S.btn(d, "contact", "Build Your Intelligence Strategy", query="?interest=ai")}</div></section>
    <section class="section"><div class="wrap"><div class="section-head"><h2>Questions leaders ask</h2></div>{S.faq_html(faqs)}</div></section>
    """
    trail = [("Home", ""), ("AI & Intelligence", None)]
    S.add(slug, d, "ai", title, desc, body, [M.web(slug, title, desc), M.service("Enterprise AI strategy and governance", desc, slug), S.faq_schema(faqs), S.crumb_schema(trail)])

def cyber():
    d, slug = 1, "cybersecurity"
    title = "Cybersecurity Strategy & Cyber Risk | Aryx Intelligence"
    desc = "Cybersecurity strategy, cyber risk, architecture and resilience, managed as a business-risk discipline. Aryx Intelligence advises leaders in Qatar and the GCC."
    faqs = [
        ("What is the difference between cybersecurity and cyber resilience?", "Cybersecurity aims to prevent compromise. Cyber resilience assumes some attacks will succeed and focuses on continuing critical operations and recovering quickly."),
        ("How should a board oversee cyber risk?", "By setting risk appetite, receiving reporting in business terms, testing incident readiness and ensuring accountability is clear between management and the board."),
        ("What is a cybersecurity maturity assessment?", "A structured review of governance, controls and capabilities against a recognized framework, showing current maturity, gaps and a prioritized improvement plan."),
        ("How does AI change cybersecurity?", "AI creates new assets to protect, new attack techniques for adversaries and new tools for defenders. All three need to be in the security strategy."),
    ]
    caps = [
        ("strategy", "Cybersecurity strategy", "A security strategy and roadmap tied to business priorities, risk appetite and regulatory obligations."),
        ("quantification", "Cyber risk quantification and reporting", "Exposure expressed in terms executives and boards can weigh against other risks and investments."),
        ("architecture", "Security architecture", "Zero-trust principles, segmentation and secure design patterns across on-premises, cloud and hybrid estates."),
        ("grc", "Governance, risk and compliance", f"Policies, control frameworks and evidence aligned to ISO/IEC 27001, NIST CSF 2.0 and regional requirements such as Qatar's National Information Assurance standards and sector regulators' cyber rules. {M.ph('Verify current regulatory names before publishing')}"),
        ("threat", "Threat intelligence", "Relevant, prioritized intelligence on the actors and techniques most likely to target your sector and region."),
        ("assessments", "Security assessments", "Maturity, architecture and control assessments that show where you stand and what to fix first."),
        ("vulnerability", "Vulnerability management", "Risk-based prioritization so remediation effort goes to the exposures that matter."),
        ("identity", "Identity and access", "Identity as the control plane: privileged access, lifecycle management and strong authentication."),
        ("cloud", "Cloud security", "Configuration, workload and data protection across major cloud platforms, with in-region data considerations."),
        ("operations", "Security operations", "Detection and response design, playbooks and metrics that measure outcomes, not alert volume."),
        ("ai-security", "AI security", "Protecting AI systems from data poisoning, prompt injection, model theft and misuse, and using AI to strengthen defense."),
        ("resilience", "Enterprise resilience", "Incident response, crisis management and recovery planning tested through realistic exercises."),
    ]
    cap_html = "".join(f'<article id="{i}" class="cap-row"><span class="idx">{n:02d}</span><div><h3>{t}</h3><p>{p}</p></div></article>' for n, (i, t, p) in enumerate(caps, 1))
    body = f"""
    {M.page_hero(d, [("Home", ""), ("Cybersecurity", None)], "Cybersecurity", "Cybersecurity as a business-risk discipline",
      "We help leaders understand their cyber exposure in business terms, invest where it matters, and build organizations that keep operating under pressure.",
      S.btn(d, "contact", "Assess Your Cyber Risk", query="?interest=cybersecurity") + S.text_link(d, "contact", "Discuss Your Security Strategy", "?interest=cybersecurity"))}
    <section class="section"><div class="wrap prose">
      <h2>Why security needs an intelligence lens</h2>
      <p>Most security programs can report how many controls they run. Few can say which business outcomes those controls protect, or what a credible attack would cost. Boards are asked to fund security without a clear view of the return. Aryx closes that gap by connecting threats, vulnerabilities and controls to the processes, data and revenue they put at risk.</p>
      <h2>What cyber risk means</h2>
      <p>Cyber risk is the potential for financial, operational, legal or reputational harm arising from the failure or compromise of information systems. Managing it well means understanding likelihood and impact in business terms, not only counting technical findings.</p>
      <p>See also <a href="{S.href(d, "insights/cyber-resilience-strategy")}">cyber resilience as a board-level strategy</a> and <a href="{S.href(d, "industries/banking")}">banking and financial services</a>.</p>
    </div></section>
    <section class="section section-porcelain"><div class="wrap"><div class="section-head"><h2>Capabilities</h2></div><div class="cap-list">{cap_html}</div></div></section>
    <section class="section"><div class="wrap prose">
      <h2>Outcomes</h2>
      <ul>
        <li>A security posture leadership can explain and defend</li>
        <li>Investment directed by risk, not by the latest headline</li>
        <li>Faster detection, containment and recovery</li>
        <li>Regulatory evidence ready when supervisors ask</li>
        <li>AI adoption that does not open new, unmanaged attack surfaces</li>
      </ul>
      <p>Practitioner credentials: {M.ph("certifications")}. Case evidence: {M.ph("case study")}.</p>
      <p>Connected work includes <a href="{S.href(d, "risk-decision-intelligence")}">cyber risk quantification</a>, <a href="{S.href(d, "ai-intelligence")}">AI-enabled security operations</a> and <a href="{S.href(d, "digital-transformation")}">secure cloud transformation</a>.</p>
    </div></section>
    <section class="section section-ink"><div class="wrap cta-band"><div><h2>Know what you are protecting, what threatens it and what it is worth.</h2></div>{S.btn(d, "contact", "Assess Your Cyber Risk", query="?interest=cybersecurity")}</div></section>
    <section class="section"><div class="wrap"><div class="section-head"><h2>Questions leaders ask</h2></div>{S.faq_html(faqs)}</div></section>
    """
    trail = [("Home", ""), ("Cybersecurity", None)]
    S.add(slug, d, "cyber", title, desc, body, [M.web(slug, title, desc), M.service("Cybersecurity strategy and cyber risk", desc, slug), S.faq_schema(faqs), S.crumb_schema(trail)])

def digital():
    d, slug = 1, "digital-transformation"
    title = "Digital Transformation & Technology Strategy | Aryx"
    desc = "Technology strategy, enterprise architecture, cloud, data and operating models designed for measurable results. Aryx Intelligence, Qatar and GCC."
    faqs = [
        ("What should a technology strategy include?", "Business objectives, current-state assessment, target architecture, investment priorities, a sequenced roadmap, governance and the metrics that will show progress."),
        ("How do we know if we are ready for AI?", "AI readiness depends mostly on data quality and access, platform maturity, governance and skills. A readiness assessment tests each before significant investment."),
        ("How do you measure digital transformation success?", "Against business outcomes agreed at the start, such as cost, speed, quality or risk, tracked through delivery and after."),
    ]
    caps = [
        ("Technology strategy", "A technology direction aligned to business strategy, with clear investment priorities and a sequenced roadmap."),
        ("Enterprise architecture", "Business, data, application and technology architecture that reduces complexity and keeps future options open."),
        ("Cloud transformation", "Cloud strategy, migration planning and landing-zone design, with security, cost governance and data residency built in."),
        ("Data and analytics", "Data strategy, governance, platforms and analytics that turn data into a shared, trusted asset and the foundation for AI."),
        ("Intelligent automation", "Process redesign combined with automation and AI where it improves speed, accuracy or control."),
        ("Enterprise platforms", "Selection and implementation guidance for core platforms such as ERP, CRM and GRC, judged by fit and outcome rather than feature lists."),
        ("Technology modernization", "Retiring legacy risk and cost through planned modernization of applications and infrastructure."),
        ("Digital operating models", "Structures, roles, governance and skills that let technology and business teams deliver together."),
    ]
    cap_html = "".join(f'<article class="cap-row"><span class="idx">{n:02d}</span><div><h3>{t}</h3><p>{p}</p></div></article>' for n, (t, p) in enumerate(caps, 1))
    body = f"""
    {M.page_hero(d, [("Home", ""), ("Digital & Technology", None)], "Digital & Technology", "Digital transformation measured by business results",
      "We design the architecture, platforms and operating models that make organizations faster, more resilient and ready for AI, and we measure success in outcomes, not go-lives.",
      S.btn(d, "contact", "Plan Your Modernization", query="?interest=digital") + S.text_link(d, "contact", "Review Your Technology Strategy", "?interest=digital"))}
    <section class="section"><div class="wrap prose">
      <h2>Why transformation programs stall</h2>
      <p>Transformation programs often deliver new systems without delivering new results. Common causes are familiar: technology chosen before the business problem is defined, data left fragmented, security added late and operating models left unchanged. The outcome is cost and complexity without the expected return.</p>
      <h2>What digital transformation means at Aryx</h2>
      <p>Digital transformation is the redesign of how an organization creates value using technology, data and new ways of working. It succeeds when it changes measurable outcomes such as cycle time, cost to serve, customer experience or risk exposure.</p>
    </div></section>
    <section class="section section-porcelain"><div class="wrap"><div class="section-head"><h2>Capabilities</h2></div><div class="cap-list">{cap_html}</div></div></section>
    <section class="section"><div class="wrap">
      <div class="section-head"><h2>Outcomes</h2></div>
      <div class="table-wrap"><table>
        <thead><tr><th>Measure</th><th>Example of what improves</th></tr></thead>
        <tbody>
          <tr><td>Speed</td><td>Shorter time from idea to production</td></tr>
          <tr><td>Cost</td><td>Lower run cost through rationalization and automation</td></tr>
          <tr><td>Resilience</td><td>Fewer single points of failure, faster recovery</td></tr>
          <tr><td>Data</td><td>One trusted version of key data, ready for AI</td></tr>
          <tr><td>Control</td><td>Security, compliance and cost governance built into platforms</td></tr>
        </tbody>
      </table></div>
      <div class="prose">
        <p>Methodology note: frameworks such as TOGAF are referenced only where actually used. {M.ph("Confirm")}. {M.ph("Case study")}.</p>
        <p>Continue with an <a href="{S.href(d, "ai-intelligence")}">AI readiness assessment</a>, <a href="{S.href(d, "cybersecurity")}#cloud">cloud security</a> and <a href="{S.href(d, "risk-decision-intelligence")}">technology risk</a>.</p>
      </div>
    </div></section>
    <section class="section section-ink"><div class="wrap cta-band"><div><h2>Build the foundations your next decade will run on.</h2></div>{S.btn(d, "contact", "Plan Your Modernization", query="?interest=digital")}</div></section>
    <section class="section"><div class="wrap"><div class="section-head"><h2>Questions leaders ask</h2></div>{S.faq_html(faqs)}</div></section>
    """
    trail = [("Home", ""), ("Digital & Technology", None)]
    S.add(slug, d, "digital", title, desc, body, [M.web(slug, title, desc), M.service("Digital transformation and technology strategy", desc, slug), S.faq_schema(faqs), S.crumb_schema(trail)])

def risk():
    d, slug = 1, "risk-decision-intelligence"
    title = "Risk Intelligence & Decision Intelligence | Aryx"
    desc = "Connect technology, cyber, operational, third-party and strategic risk into one executive view. Risk and decision intelligence from Aryx Intelligence."
    faqs = [
        ("What is the difference between risk management and risk intelligence?", "Risk management is the overall discipline. Risk intelligence is its forward-looking, connected layer: it interprets changing signals so leaders can act before risks materialize."),
        ("What is integrated risk management?", "Integrated risk management brings risk domains such as cyber, technology, operational and third-party risk into one framework and view, so interdependencies are visible."),
        ("Can risk be quantified?", "Many risks can be estimated in financial or operational terms using scenarios and models. Where data is limited, the honest answer is a range with stated confidence."),
        ("Does Aryx replace our GRC platform?", "No. Aryx works with existing GRC tools and data, adding the connection, interpretation and decision layer that registers alone do not provide."),
    ]
    caps = [
        ("Enterprise risk intelligence", "A connected view of risk aligned to recognized frameworks such as ISO 31000 and COSO ERM, built for executive use."),
        ("Technology risk", "Exposure from legacy systems, concentration, change and technical debt, expressed in business terms."),
        ("Cyber risk", "Threat and control data translated into likelihood and impact on critical services."),
        ("Operational risk", "Process, people and system failures mapped to the services the organization cannot afford to lose."),
        ("Third-party risk", "Visibility into vendors, cloud providers and supply chains, including fourth-party and concentration exposure."),
        ("Strategic risk", "Risks to strategy itself: market shifts, regulatory direction, technology change and geopolitical exposure."),
        ("Scenario intelligence", "Structured scenarios and stress tests that show how combined events would play out and where thresholds would be crossed."),
        ("Decision intelligence", "Decision models that set out options, consequences and confidence for leadership choices."),
        ("Executive risk visibility", "Board and C-suite reporting that shows exposure, trend and required decisions on one page."),
        ("Resilience", "Mapping important business services, impact tolerances and recovery capability, and testing them."),
    ]
    cap_html = "".join(f'<article class="cap-row"><span class="idx">{n:02d}</span><div><h3>{t}</h3><p>{p}</p></div></article>' for n, (t, p) in enumerate(caps, 1))
    body = f"""
    {M.page_hero(d, [("Home", ""), ("Risk & Decision Intelligence", None)], "Risk & Decision Intelligence", "Risk intelligence that leads to better decisions",
      "Most organizations can list their risks. Few can see how they connect, what they mean together, or which decision they demand next. That is the gap we close.",
      S.btn(d, "contact", "See Your Risk Clearly", query="?interest=risk") + S.text_link(d, "contact", "Start a Strategic Conversation", "?interest=risk"))}
    <section class="section"><div class="wrap prose">
      <h2>Beyond the risk register</h2>
      <p>Traditional governance, risk and compliance programs are built to document risk. They produce registers, heat maps and attestations, and they are necessary. But they are slow, static and siloed. A cyber incident at a supplier, a cloud outage and a regulatory change can combine into one serious exposure that no single register shows.</p>
      <p>Risk intelligence is different in purpose. It is designed to inform decisions while there is still time to act.</p>
      <h2>Definitions</h2>
      <p><strong>Risk intelligence</strong> is the continuous collection, connection and interpretation of risk signals across an organization and its ecosystem, so leaders understand their exposure as it changes.</p>
      <p><strong>Decision intelligence</strong> is the discipline of linking data, analytics, AI and human judgment to specific decisions, with clear options, trade-offs and accountability.</p>
      <p>Together they answer three questions: What is our exposure now? What could change it? What should we decide?</p>
    </div></section>
    <section class="section section-porcelain"><div class="wrap">
      <div class="section-head"><h2>How Aryx differs from a GRC consultancy</h2></div>
      <div class="table-wrap"><table>
        <thead><tr><th>Traditional GRC</th><th>Aryx risk and decision intelligence</th></tr></thead>
        <tbody>
          <tr><td>Documents risks by function</td><td>Connects risks across functions and third parties</td></tr>
          <tr><td>Periodic assessment</td><td>Continuous signals and triggers</td></tr>
          <tr><td>Compliance as the goal</td><td>Better decisions as the goal, compliance as a result</td></tr>
          <tr><td>Heat maps</td><td>Scenarios, quantified exposure and options</td></tr>
          <tr><td>Reports to committees</td><td>Decisions with owners, thresholds and actions</td></tr>
        </tbody>
      </table></div>
    </div></section>
    <section class="section"><div class="wrap"><div class="section-head"><h2>Capabilities</h2></div><div class="cap-list">{cap_html}</div></div></section>
    <section class="section section-porcelain"><div class="wrap prose">
      <h2>The Aryx decision loop</h2>
      <ol>
        <li><strong>Sense</strong> — Gather signals from cyber, technology, operations, third parties and the external environment.</li>
        <li><strong>Connect</strong> — Link signals to assets, services and objectives so their combined meaning is visible.</li>
        <li><strong>Assess</strong> — Quantify exposure where possible and state confidence honestly where not.</li>
        <li><strong>Decide</strong> — Present options with trade-offs, owners and thresholds.</li>
        <li><strong>Act and learn</strong> — Track actions and outcomes, and feed what is learned back into the model.</li>
      </ol>
      <p>Go further on <a href="{S.href(d, "cybersecurity")}">cyber risk in business terms</a>, <a href="{S.href(d, "ai-intelligence")}#inventory">AI governance and oversight</a>, <a href="{S.href(d, "climate-intelligence")}">physical and transition risk</a>, <a href="{S.href(d, "industries/banking")}">banking</a> and <a href="{S.href(d, "industries/government")}">government</a>.</p>
      <p>Read <a href="{S.href(d, "insights/integrated-risk-management")}">integrated risk management beyond the GRC tool</a>.</p>
    </div></section>
    <section class="section section-ink"><div class="wrap cta-band"><div><h2>See how your risks connect, before events connect them for you.</h2></div>{S.btn(d, "contact", "See Your Risk Clearly", query="?interest=risk")}</div></section>
    <section class="section"><div class="wrap"><div class="section-head"><h2>Questions leaders ask</h2></div>{S.faq_html(faqs)}</div></section>
    """
    trail = [("Home", ""), ("Risk & Decision Intelligence", None)]
    S.add(slug, d, "risk", title, desc, body, [M.web(slug, title, desc), M.service("Risk and decision intelligence", desc, slug), S.faq_schema(faqs), S.crumb_schema(trail)])

def climate():
    d, slug = 1, "climate-intelligence"
    title = "Climate Risk & Climate Intelligence | Aryx Intelligence"
    desc = "Climate risk, emissions data, ESG reporting and transition intelligence connected to enterprise risk and decisions. Aryx Intelligence, Qatar and GCC."
    faqs = [
        ("What is the difference between climate risk and ESG?", "ESG is a broad set of environmental, social and governance factors. Climate risk is a specific financial risk: the physical and transition impacts of climate change on an organization's value."),
        ("What are physical and transition risks?", "Physical risks come from climate hazards such as heat, flooding or water stress. Transition risks come from the shift to a low-carbon economy: policy, carbon pricing, technology and market changes."),
        ("What are financed emissions?", "Financed emissions are the greenhouse gas emissions associated with a financial institution's loans and investments. They are usually the largest part of a bank's or investor's footprint."),
        ("Why connect climate to enterprise risk management?", "Because climate risk shows up through existing risk types such as credit, operational, market and reputational risk. Managed separately, its effects are underestimated."),
    ]
    caps = [
        ("Climate risk assessment", "Physical and transition risk analysis across assets, operations, portfolios and supply chains, using recognized climate scenarios."),
        ("GHG accounting and emissions data", f"Scope 1, 2 and 3 inventories built on the GHG Protocol, with data lineage and controls that support assurance. {M.ph('Confirm ISO 14064 verification capability')}"),
        ("Financed emissions", "Methodology, data sourcing and calculation approaches for banks and investors, aligned to the PCAF Global GHG Accounting and Reporting Standard."),
        ("Sustainability reporting readiness", f"Gap analysis and data design for frameworks such as IFRS S1 and S2, GRI and regional exchange or regulator requirements. {M.ph('Verify current GCC requirements before publishing')}"),
        ("Climate scenario analysis", "Scenario and stress-test design that shows how climate pathways affect revenue, costs, asset values and credit risk."),
        ("ESG data platforms", "Architecture and selection for sustainability data platforms, integrated with finance, operations and risk systems."),
        ("AI for climate and sustainability", "AI for data extraction, supplier data quality, anomaly detection and emissions estimation, governed like any other material AI use."),
        ("Value-chain intelligence", "Visibility into supplier emissions and climate exposure, connected to third-party risk management."),
    ]
    cap_html = "".join(f'<article class="cap-row"><span class="idx">{n:02d}</span><div><h3>{t}</h3><p>{p}</p></div></article>' for n, (t, p) in enumerate(caps, 1))
    body = f"""
    {M.page_hero(d, [("Home", ""), ("Climate Intelligence", None)], "Climate Intelligence", "Climate intelligence for decisions, not just disclosures",
      "Climate is now a financial, operational and regulatory risk. We help organizations measure it credibly, connect it to enterprise risk and use it to make better capital and strategy decisions.",
      S.btn(d, "contact", "Assess Your Climate Exposure", query="?interest=climate") + S.text_link(d, "contact", "Discuss Your Climate Data Strategy", "?interest=climate"))}
    <section class="section"><div class="wrap prose">
      <h2>Why climate needs an intelligence approach</h2>
      <p>Many organizations treat climate as a reporting exercise: collect data once a year, publish a report, repeat. Meanwhile the exposures it describes, such as heat stress on assets, carbon costs, transition risk in a loan book or supplier disruption, keep moving. Disclosure-only programs produce documents. They rarely change decisions.</p>
      <p>Climate belongs in the same connected view as cyber, technology and operational risk. The data problems are similar too: fragmented sources, weak lineage and numbers that do not survive an auditor's questions.</p>
      <h2>What climate intelligence means</h2>
      <p>Climate intelligence is the use of emissions data, climate scenarios, physical and transition risk analysis and sustainability information to inform business, investment and risk decisions. It turns climate from a disclosure obligation into decision input.</p>
      <p>Climate tech, in Aryx's sense, is the data, platforms, analytics and AI that make that possible: emissions accounting systems, climate risk models, sustainability data platforms and the controls that make their outputs auditable.</p>
    </div></section>
    <section class="section section-porcelain"><div class="wrap"><div class="section-head"><h2>Capabilities</h2></div><div class="cap-list">{cap_html}</div></div></section>
    <section class="section"><div class="wrap">
      <div class="section-head"><h2>Outcomes</h2></div>
      <div class="table-wrap"><table>
        <thead><tr><th>Outcome</th><th>What it looks like</th></tr></thead>
        <tbody>
          <tr><td>Credible numbers</td><td>Emissions and climate metrics with lineage an assurer can test</td></tr>
          <tr><td>Integrated risk</td><td>Climate exposure visible beside cyber, operational and credit risk</td></tr>
          <tr><td>Better capital decisions</td><td>Investment, lending and asset choices tested against climate scenarios</td></tr>
          <tr><td>Reporting readiness</td><td>Disclosures produced from governed data, not spreadsheets</td></tr>
          <tr><td>Transition clarity</td><td>A decarbonization path linked to cost, technology and strategy</td></tr>
        </tbody>
      </table></div>
      <div class="prose">
        <p>Frameworks in this work include the GHG Protocol, PCAF, IFRS S2 and ISO 14064. Leadership sustainability credentials: {M.ph("confirm")}. {M.ph("Case study")}.</p>
        <p>See <a href="{S.href(d, "risk-decision-intelligence")}">climate risk inside enterprise risk</a>, <a href="{S.href(d, "digital-transformation")}">ESG data platforms</a>, <a href="{S.href(d, "ai-intelligence")}">AI for sustainability</a>, <a href="{S.href(d, "industries/banking")}">financed emissions for banks</a>, plus <a href="{S.href(d, "industries/energy")}">energy</a> and <a href="{S.href(d, "industries/real-estate")}">real estate</a>.</p>
        <p>Read <a href="{S.href(d, "insights/climate-risk-management-banking")}">climate risk management in banking</a>.</p>
      </div>
    </div></section>
    <section class="section section-ink"><div class="wrap cta-band"><div><h2>Make climate data strong enough to decide with.</h2></div>{S.btn(d, "contact", "Assess Your Climate Exposure", query="?interest=climate")}</div></section>
    <section class="section"><div class="wrap"><div class="section-head"><h2>Questions leaders ask</h2></div>{S.faq_html(faqs)}</div></section>
    """
    trail = [("Home", ""), ("Climate Intelligence", None)]
    S.add(slug, d, "climate", title, desc, body, [M.web(slug, title, desc), M.service("Climate risk and climate intelligence", desc, slug), S.faq_schema(faqs), S.crumb_schema(trail)])
