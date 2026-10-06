# -*- coding: utf-8 -*-
import build_site as S
import site_more as M

ARTICLES = [
    {
        "slug": "insights/ai-governance-for-boards",
        "title": "AI Governance for Boards: The Questions That Now Define Oversight",
        "category": "AI Governance",
        "categories": ["ai-governance", "executive-perspectives"],
        "excerpt": "AI governance for boards is the board's role in appetite, accountability, assurance and adaptation. Management runs the system. The board makes sure it works.",
        "date": "2026-10-02",
        "seo_title": "AI Governance for Boards: What Directors Must Ask",
        "desc": "AI governance for boards is now a fiduciary issue. The oversight model, regulatory context and questions directors need for GCC and global enterprises.",
        "h1": "AI Governance for Boards: The Questions That Now Define Oversight",
        "alt": "Board directors reviewing AI governance for boards on a connected oversight dashboard",
    },
    {
        "slug": "insights/integrated-risk-management",
        "title": "Integrated Risk Management: Seeing the Risks Between Your Risk Registers",
        "category": "Risk Intelligence",
        "categories": ["risk-intelligence"],
        "excerpt": "Integrated risk management connects cyber, technology, third-party and operational risk so leaders see combined exposure before events connect it for them.",
        "date": "2026-10-02",
        "seo_title": "Integrated Risk Management: Beyond the GRC Tool",
        "desc": "Integrated risk management connects cyber, technology, third-party and operational risk so leaders see combined exposure. A practical model for executives.",
        "h1": "Integrated Risk Management: Seeing the Risks Between Your Risk Registers",
        "alt": "Integrated risk management map connecting cyber, technology and supplier risks to business services",
    },
    {
        "slug": "insights/climate-risk-management-banking",
        "title": "Climate Risk Management in Banking: From Disclosure to Decision",
        "category": "Climate & Sustainability",
        "categories": ["climate-sustainability"],
        "excerpt": "For GCC banks, climate risk management now spans IFRS S2, PCAF financed emissions and the credit decisions those numbers should change.",
        "date": "2026-10-02",
        "seo_title": "Climate Risk Management in Banking: A GCC Guide",
        "desc": "Climate risk management in banking now spans IFRS S2, PCAF financed emissions and stress testing. What GCC and global bank leaders need to decide next.",
        "h1": "Climate Risk Management in Banking: From Disclosure to Decision",
        "alt": "Climate risk management in banking shown as a loan portfolio mapped against GCC climate hazards",
    },
    {
        "slug": "insights/cyber-resilience-strategy",
        "title": "Cyber Resilience Strategy: Leading When Prevention Is Not Enough",
        "category": "Cybersecurity",
        "categories": ["cybersecurity", "executive-perspectives"],
        "excerpt": "A cyber resilience strategy assumes some attacks will succeed. It defines what must keep running, how recovery is proved, and how the board measures it.",
        "date": "2026-10-02",
        "seo_title": "Cyber Resilience Strategy: A Board-Level Guide",
        "desc": "A cyber resilience strategy assumes some attacks will succeed. How boards and executives define the minimum viable enterprise, measure recovery and govern it.",
        "h1": "Cyber Resilience Strategy: Leading When Prevention Is Not Enough",
        "alt": "Cyber resilience strategy illustrated by essential city services staying online during an outage",
    },
]

def register():
    article_ai()
    article_risk()
    article_climate()
    article_cyber()

def shell(meta, body_html, faqs, links_note):
    d = 2
    slug = meta["slug"]
    trail = [("Home", ""), ("Insights", "insights"), (meta["category"], None)]
    hero = M.page_hero(
        d, trail, meta["category"], S.e(meta["h1"]),
        S.e(meta["excerpt"]),
        S.text_link(d, "contact", "Discuss this with Aryx", "?interest=strategy") + S.text_link(d, "insights", "Subscribe to The Aryx Brief"),
    )
    # second text link should go to insights# newsletter - insights page has the form. OK.
    body = f"""
    {hero}
    <article class="section">
      <div class="wrap article-layout">
        <div class="prose">
          <p class="article-meta">By Dr Anjum · Published 2 October 2026 · Aryx Intelligence thought-leadership series</p>
          <figure class="media-card"><div class="ph">Placeholder image</div><figcaption class="muted" style="padding:10px 14px">{S.e(meta["alt"])}. Replace this placeholder with photography.</figcaption></figure>
          {body_html}
          <h2>Questions leaders should be asking</h2>
          {meta["questions"]}
          <h2>Aryx Intelligence perspective</h2>
          {meta["perspective"]}
          <h2>Conclusion</h2>
          {meta["conclusion"]}
          <h2>FAQ</h2>
          {S.faq_html(faqs)}
          <h2>Sources and verification</h2>
          <div class="sources">{meta["sources"]}</div>
          <p>{links_note}</p>
        </div>
        <aside class="side-card">
          <h2>What this means for leaders</h2>
          {meta["means"]}
          <p><a class="btn btn-primary" href="{S.href(d, "contact")}?interest=strategy">Start a conversation {S.ARROW}</a></p>
        </aside>
      </div>
    </article>
    """
    schemas = [
        M.web(slug, meta["seo_title"], meta["desc"]),
        {
            "@type": "Article",
            "headline": meta["h1"],
            "description": meta["desc"],
            "datePublished": meta["date"],
            "dateModified": meta["date"],
            "author": {"@type": "Person", "name": "Dr Anjum"},
            "publisher": {"@type": "Organization", "name": "Aryx Intelligence", "logo": {"@type": "ImageObject", "url": S.ORIGIN + "/" + S.LOGO}},
            "image": S.ORIGIN + "/" + S.LOGO,
            "mainEntityOfPage": S.canonical(slug),
        },
        S.faq_schema(faqs),
        S.crumb_schema(trail),
    ]
    S.add(slug, d, "insights", meta["seo_title"], meta["desc"], body, schemas)

def article_ai():
    meta = dict(ARTICLES[0])
    meta["questions"] = """<ol>
      <li>How many AI systems are in use across the organization, including those embedded in vendor products?</li>
      <li>Which of them would be classified as high-risk under the regulations that apply to us?</li>
      <li>Who is the accountable executive for each high-risk system?</li>
      <li>What is our board-approved risk appetite for AI, and where is it written down?</li>
      <li>When did internal audit last review an AI system, and what did it find?</li>
      <li>How would we know if a model's performance or fairness had degraded?</li>
      <li>Which regulatory deadlines affect us in the next 24 months, in the GCC and abroad?</li>
      <li>Does the board have enough AI literacy to challenge management effectively?</li>
    </ol>"""
    meta["means"] = """<ul>
      <li>AI oversight is now a named board responsibility in some jurisdictions, and a reasonable expectation everywhere.</li>
      <li>An AI register is the foundation; without it, every other control is partial.</li>
      <li>Risk appetite for AI should be explicit, approved and tied to risk tiers that mirror regulation.</li>
      <li>Assurance must continue after deployment, through monitoring and internal audit.</li>
      <li>Regulatory timelines move, but the direction toward accountability does not.</li>
    </ul>"""
    meta["perspective"] = """<p>At Aryx, we see AI governance as a decision problem before it is a compliance problem. Boards do not need to understand model architectures. They need a clear view of where AI influences decisions that matter, how much risk those decisions carry, and whether the evidence supports the confidence management expresses.</p>
    <p>That view depends on connecting information that usually sits apart: the technology estate, the risk register, vendor contracts, regulatory obligations and audit findings. When those are connected, AI governance stops being a policy document and becomes a working oversight system.</p>"""
    meta["conclusion"] = "<p>The question for boards is no longer whether to govern AI, but whether they can show that they do. The organizations that move first will not only meet regulatory expectations; they will be the ones able to adopt AI faster, because they will know where its risks are.</p>"
    meta["sources"] = """<ul>
      <li>QCB AI Guideline; EU AI Act and Regulation (EU) 2026/1744; ISO/IEC 42001; NIST AI RMF 1.0.</li>
      <li>Verify before publishing: QCB Guideline details against the official PDF; EU AI Act dates against the Official Journal text of Regulation (EU) 2026/1744.</li>
    </ul>"""
    faqs = [
        ("What is AI governance for boards?", "It is the board's role in setting AI risk appetite, assigning accountability, obtaining assurance and keeping AI oversight current. Management runs AI governance; the board ensures it is effective."),
        ("Is AI governance a legal requirement for boards?", "In some sectors and jurisdictions, yes. Qatar's central bank, for example, places AI accountability with the boards of licensed entities. Elsewhere it is increasingly a fiduciary expectation."),
        ("What is an AI register?", "An AI register is an inventory of every AI system an organization uses, recording its purpose, owner, risk level, data, vendor and controls."),
        ("Does the EU AI Act apply to companies in the GCC?", "It can. The Act applies to providers placing AI on the EU market and to deployers whose AI outputs are used in the EU, regardless of where they are based."),
        ("When do EU AI Act high-risk obligations apply?", "For stand-alone high-risk systems listed in Annex III, from 2 December 2027, following the Digital Omnibus. Transparency obligations under Article 50 have applied since 2 August 2026."),
        ("What is ISO/IEC 42001?", "ISO/IEC 42001 is the international standard for AI management systems, setting requirements for establishing, operating and improving AI governance within an organization."),
    ]
    body = """
    <p>AI governance for boards stopped being optional when regulators began naming boards directly. In Qatar, the central bank's AI Guideline for licensed entities, in force since 4 September 2024, places accountability for AI with the board of directors and senior management, and requires prior supervisory approval before high-risk AI systems go live.</p>
    <p>That is a different posture from "management will keep us informed." It means directors must be able to say what AI the organization uses, how risky it is, who owns it, and how they know it is working as intended. Most boards cannot yet answer all four.</p>
    <h2>What is AI governance?</h2>
    <p>AI governance is the system of policies, roles, controls and oversight that ensures an organization's AI is used lawfully, safely and in line with its strategy and risk appetite, across the full lifecycle from procurement or design to retirement.</p>
    <p>Board-level AI governance is narrower. It is the board's role in setting direction and appetite, holding management accountable and obtaining assurance that the system works. The board does not run AI governance; it makes sure it exists and is effective.</p>
    <h2>Why AI is now a board matter</h2>
    <p>Three shifts moved AI from the technology agenda to the boardroom.</p>
    <ul>
      <li>AI now makes or shapes consequential decisions. Credit, pricing, hiring, fraud detection and customer service increasingly run through models. Errors scale instantly and can be discriminatory, opaque or hard to reverse.</li>
      <li>Regulation is assigning accountability. Beyond Qatar's banking rules, the EU AI Act applies to organizations that place AI on the EU market or whose AI outputs are used there, including many GCC groups. Its transparency obligations under Article 50 have applied since 2 August 2026, while obligations for stand-alone high-risk systems were deferred to 2 December 2027 by the Digital Omnibus.</li>
      <li>AI arrives unannounced. Much enterprise AI is embedded in vendor software, SaaS platforms and employee tools. A board that only oversees AI projects misses most of the AI in use.</li>
    </ul>
    <h2>The Four A's of board AI oversight</h2>
    <p>Aryx uses a simple model to separate what boards must own from what management must run.</p>
    <div class="table-wrap"><table>
      <thead><tr><th>Dimension</th><th>The board's question</th><th>What good looks like</th></tr></thead>
      <tbody>
        <tr><td>Appetite</td><td>Where will we use AI, and where will we not?</td><td>A board-approved AI risk appetite, with prohibited and high-risk uses defined</td></tr>
        <tr><td>Accountability</td><td>Who owns each AI system and its outcomes?</td><td>Named executive owners, a complete AI register, clear escalation paths</td></tr>
        <tr><td>Assurance</td><td>How do we know AI is working as intended?</td><td>Independent validation, monitoring for drift and bias, internal audit coverage</td></tr>
        <tr><td>Adaptation</td><td>Are we keeping pace with technology and regulation?</td><td>Periodic review of policy, skills and regulatory exposure; board education</td></tr>
      </tbody>
    </table></div>
    <p>Each dimension fails differently. Weak appetite produces either reckless adoption or paralysis. Weak accountability produces orphaned models. Weak assurance produces confidence without evidence. Weak adaptation produces a policy written for last year's technology.</p>
    <h2>Appetite: setting the boundaries</h2>
    <p>An AI risk appetite statement translates strategy into limits. It should state which uses the organization actively pursues, which require enhanced controls and which are off-limits, for example fully automated decisions with significant effects on customers or employees.</p>
    <p>Risk classification makes the appetite usable. Both the QCB Guideline and the EU AI Act use tiered approaches, in which systems affecting access to financial services, employment or sensitive personal data attract the heaviest obligations. Aligning internal tiers with these external ones avoids running two systems.</p>
    <h2>Accountability: the AI register</h2>
    <p>You cannot govern AI you cannot see. An AI register, or inventory, records every AI system in use: its purpose, owner, risk tier, data sources, vendor, validation status and monitoring arrangements. Qatar's banking guideline requires one and its annual submission to the supervisor.</p>
    <p>The hard part is completeness. Embedded and employee-adopted AI rarely appears in project portfolios. Procurement controls, software asset data and periodic declarations from business units are usually needed to find it.</p>
    <h2>Assurance: evidence, not comfort</h2>
    <p>Boards should expect the same rigor for AI as for financial reporting. That means pre-deployment validation for high-risk systems, ongoing monitoring of performance, fairness and drift, human oversight that is real rather than nominal, and coverage in the internal audit plan.</p>
    <p>Standards help. ISO/IEC 42001 sets out requirements for an AI management system, and the NIST AI Risk Management Framework offers a widely used structure for mapping, measuring and managing AI risk. Neither replaces judgment, but both give boards a recognized benchmark.</p>
    <h2>Adaptation: governing a moving target</h2>
    <p>AI capability changes faster than most governance cycles. Agentic AI, which takes actions across systems rather than only producing outputs, raises new questions of permissions and liability. Regulation also moves: the EU's deferral shows that deadlines change while direction holds.</p>
    <p>Boards adapt by scheduling AI as a standing agenda item, investing in director education and asking management for a regular horizon scan of technology and regulation.</p>
    <h2>Common failure modes</h2>
    <ul>
      <li>Delegating AI entirely to the technology committee. AI risk is also conduct, legal, operational and strategic risk.</li>
      <li>Governing projects, not systems. Oversight ends at go-live, exactly when risk begins.</li>
      <li>Policy without inventory. A well-drafted policy covering an unknown estate gives false assurance.</li>
      <li>Treating deferral as relief. Delayed deadlines are time to build, not time to pause.</li>
    </ul>
    """
    links = 'Related: <a href="../../ai-intelligence/index.html">enterprise AI governance</a> and <a href="../../risk-decision-intelligence/index.html">managing AI as an enterprise risk</a>. An AI inventory is covered on the <a href="../../ai-intelligence/index.html#inventory">AI governance</a> section of the enterprise AI page. The planned article “Building an AI Inventory” is not published yet.'
    shell(meta, body, faqs, links)

def article_risk():
    meta = dict(ARTICLES[1])
    meta["questions"] = """<ol>
      <li>Which of our critical services depend on the same supplier, system or cloud region?</li>
      <li>Could our risk reports show us a combined scenario, or only individual risks?</li>
      <li>How current is the data behind our board risk report?</li>
      <li>Do cyber, technology, operational and third-party risk use the same impact scales?</li>
      <li>Who owns each exposure that crosses functions?</li>
      <li>What thresholds would trigger an executive decision, and are they written down?</li>
      <li>Where would we look first if two of our top risks materialized in the same week?</li>
    </ol>"""
    meta["means"] = """<ul>
      <li>The exposures most likely to hurt you sit between functions, not within them.</li>
      <li>A single GRC tool is not integration; connections to assets, suppliers and services are.</li>
      <li>Start from important business services; they give every function a shared frame.</li>
      <li>Scenario analysis turns a list of risks into decisions.</li>
      <li>Integration should sharpen accountability, not dilute it.</li>
    </ul>"""
    meta["perspective"] = """<p>Aryx was built on the view that the most consequential risks are connective. Cyber, technology, climate, third-party and operational risk increasingly share the same assets, vendors and triggers, yet they are still managed in parallel.</p>
    <p>Our approach starts with the decisions leadership must make, then connects the signals that bear on them. The aim is not a bigger register but a clearer line of sight from signal to exposure to decision.</p>"""
    meta["conclusion"] = "<p>Risk registers record what each function knows. Integrated risk management reveals what the organization does not yet know it knows. In a world of shared suppliers and shared shocks, that difference is where resilience is won or lost.</p>"
    meta["sources"] = """<ul>
      <li>COSO ERM 2017; ISO 31000:2018; IIA Three Lines Model (2020).</li>
    </ul>"""
    faqs = [
        ("What is integrated risk management?", "Integrated risk management brings risk domains such as cyber, technology, operational and third-party risk into one framework, data model and decision process, so combined exposures are visible."),
        ("How is IRM different from GRC?", "GRC focuses on documenting risks, controls and compliance. IRM focuses on how risks connect and what decisions they require, using continuous data and scenarios."),
        ("Is integrated risk management the same as ERM?", "No. Enterprise risk management is the overall discipline and framework. IRM is the practical integration of risk data, processes and technology that lets ERM work across domains."),
        ("What is risk aggregation?", "Risk aggregation is the combining of individual risks to understand total or combined exposure, accounting for dependencies rather than simply adding scores."),
        ("Where should an organization start with IRM?", "With a common risk taxonomy and a map of important business services, linked to the assets and suppliers they depend on."),
        ("Can risk be quantified in IRM?", "Often, using scenarios and models that produce ranges. Where data is thin, stated confidence levels keep quantification honest."),
    ]
    body = """
    <p>Most serious disruptions are not one risk. They are several, arriving together through a path no single register shows. A software vendor is compromised; the same vendor supports a critical payment process; that process has no tested fallback; and a regulatory reporting deadline falls in the same week. Each risk was known. The combination was not.</p>
    <p>Integrated risk management exists to see that combination before it happens. It is less about collecting risks in one system and more about understanding how they connect.</p>
    <h2>What is integrated risk management?</h2>
    <p>Integrated risk management (IRM) is an approach that brings risk domains such as cyber, technology, operational, third-party, compliance and strategic risk into one framework, data model and decision process, so that interdependencies and combined exposures are visible to the people accountable for them.</p>
    <p>It builds on enterprise risk management frameworks such as COSO ERM and ISO 31000, which already call for risk to be considered in the context of strategy and objectives. IRM adds the operational machinery that makes that possible: shared data, common taxonomies and connected workflows.</p>
    <h2>IRM vs GRC: what is the difference?</h2>
    <p>Governance, risk and compliance (GRC) programs and tools focus on documenting risks, controls and obligations, and evidencing compliance. They are necessary. IRM changes the question from "is each risk documented?" to "what is our exposure, and how does it change when conditions change?"</p>
    <div class="table-wrap"><table>
      <thead><tr><th>Dimension</th><th>Traditional GRC</th><th>Integrated risk management</th></tr></thead>
      <tbody>
        <tr><td>Primary goal</td><td>Compliance and documentation</td><td>Decision-ready exposure</td></tr>
        <tr><td>Unit of analysis</td><td>Individual risk or control</td><td>Connections between risks, assets and services</td></tr>
        <tr><td>Cadence</td><td>Periodic assessment</td><td>Continuous signals and triggers</td></tr>
        <tr><td>Output</td><td>Registers, heat maps, attestations</td><td>Scenarios, quantified ranges, decisions with owners</td></tr>
        <tr><td>Owner</td><td>Second line, function by function</td><td>Shared across lines, visible to the executive and board</td></tr>
      </tbody>
    </table></div>
    <h2>Four ways risks connect</h2>
    <p>In practice, risks connect through four mechanisms. Mapping them is the core of integration.</p>
    <ul>
      <li><strong>Shared assets.</strong> Multiple risks depend on the same system, data store or facility. A single failure activates all of them.</li>
      <li><strong>Shared suppliers.</strong> Several services rely on one vendor, cloud region or fourth party. Concentration is invisible when vendors are assessed one contract at a time.</li>
      <li><strong>Shared processes.</strong> A critical business service crosses functions, so a cyber event becomes an operational, customer and regulatory event at once.</li>
      <li><strong>Shared triggers.</strong> One external event, such as a regional outage, a sanctions change or extreme heat, raises the likelihood of several risks simultaneously.</li>
    </ul>
    <p>A connected view links each risk to the assets, suppliers, processes and triggers behind it. That is what reveals the critical paths.</p>
    <h2>The maturity path</h2>
    <div class="table-wrap"><table>
      <thead><tr><th>Stage</th><th>What exists</th><th>What leaders can answer</th></tr></thead>
      <tbody>
        <tr><td>1. Siloed</td><td>Separate registers by function</td><td>What risks does each function hold?</td></tr>
        <tr><td>2. Aggregated</td><td>Registers in one tool with a common taxonomy</td><td>What are our top risks overall?</td></tr>
        <tr><td>3. Integrated</td><td>Risks linked to assets, suppliers and services</td><td>Which services are exposed if X fails?</td></tr>
        <tr><td>4. Intelligent</td><td>Live signals, scenarios and decision thresholds</td><td>What should we decide now, and why?</td></tr>
      </tbody>
    </table></div>
    <p>Many organizations reach stage 2 and stop, believing that a single tool means integration. The value arrives at stages 3 and 4.</p>
    <h2>What it takes to integrate</h2>
    <ul>
      <li><strong>A common taxonomy.</strong> Risk categories, impact scales and appetite measures must mean the same thing across functions, or aggregation produces noise.</li>
      <li><strong>A service-centred data model.</strong> Linking risks to important business services, and those services to assets and suppliers, gives every function the same frame of reference.</li>
      <li><strong>Signal feeds.</strong> Vulnerability scans, vendor assessments, incident logs, control tests and external intelligence should update the picture continuously rather than at quarter-end.</li>
      <li><strong>Scenario capability.</strong> Combined events need to be modelled, not just listed.</li>
      <li><strong>Decision ownership.</strong> Every material exposure needs a named owner with authority to act, and thresholds that trigger escalation.</li>
    </ul>
    <h2>Risks and limitations</h2>
    <ul>
      <li>Tool-first programs consolidate data without connecting it, adding cost without insight.</li>
      <li>False precision. Quantifying risk is useful, but ranges with stated confidence are more honest than single numbers.</li>
      <li>Ownership dilution. Integration must not blur accountability; the first line still owns its risks.</li>
      <li>Data quality. Connections are only as good as asset inventories and supplier records, which are often incomplete.</li>
    </ul>
    """
    links = 'Related: <a href="../../risk-decision-intelligence/index.html">connected risk and decision intelligence</a> and <a href="../../cybersecurity/index.html">cyber risk in business terms</a>. Third-party cyber risk is covered under cybersecurity capabilities; that standalone article is not published yet.'
    shell(meta, body, faqs, links)

def article_climate():
    meta = dict(ARTICLES[2])
    meta["questions"] = """<ol>
      <li>Who on our board and executive team is accountable for climate risk?</li>
      <li>What share of our financed emissions is based on reported rather than estimated data?</li>
      <li>Which sectors and counterparties drive most of our transition-risk exposure?</li>
      <li>Which collateral and borrower assets are most exposed to heat, water and coastal hazards?</li>
      <li>Has climate scenario analysis changed any credit limit or lending decision yet?</li>
      <li>Would our emissions data survive external assurance today?</li>
      <li>How will we meet different reporting requirements across the GCC markets where we operate?</li>
      <li>Where are the transition-finance opportunities in our existing client base?</li>
    </ol>"""
    meta["means"] = """<ul>
      <li>For QCB-regulated banks, financial year 2026 data is already being collected for the first IFRS S2 report.</li>
      <li>Financed emissions are central, and PCAF's third edition is the current method to align with.</li>
      <li>Data quality, not methodology, will be the main constraint for GCC portfolios.</li>
      <li>Climate is credit risk in a new form, and belongs in credit policy and capital planning.</li>
      <li>Multi-jurisdiction groups face different GCC regimes and should design data once, report many times.</li>
    </ul>"""
    meta["perspective"] = """<p>Climate risk in banking is often presented as a new discipline. We see it as a familiar one, risk management, applied to unfamiliar data. The banks that progress fastest will be those that connect sustainability, credit, risk and technology teams around one data foundation instead of building a parallel reporting function.</p>
    <p>At Aryx, we treat emissions and climate exposure data with the same rigour as any other decision-critical data: governed, traceable and connected to the decisions it should inform.</p>"""
    meta["conclusion"] = "<p>The first IFRS S2 reports will show which banks can measure climate risk. The years that follow will show which banks can manage it. The difference will be whether climate data reaches the credit committee, not just the annual report.</p>"
    meta["sources"] = """<ul>
      <li>QCB Sustainability Reporting Framework; PCAF Part A third edition; IFRS S2; NGFS scenarios; GHG Protocol.</li>
      <li>Verify before publishing: QCB framework details against the official circular; UAE Climate Law scope and deadline; Saudi status; PCAF Part A edition details against the PCAF site.</li>
    </ul>"""
    faqs = [
        ("What is climate risk management in banking?", "It is the identification, measurement, monitoring and control of financial risks from climate change, integrated into credit, market, operational and strategic risk management."),
        ("What are financed emissions?", "Financed emissions are greenhouse gas emissions attributable to a financial institution's loans and investments. They fall under Scope 3, Category 15 of the GHG Protocol."),
        ("What is the PCAF standard?", "PCAF's Global GHG Accounting and Reporting Standard sets methods for financial institutions to measure financed, facilitated and insurance-associated emissions. Part A, on financed emissions, reached its third edition in December 2025."),
        ("Is IFRS S2 mandatory for banks in Qatar?", "Yes. QCB-regulated banks and insurers must report under IFRS S1 and S2 for financial years beginning on or after 1 January 2026, with first reports in 2027."),
        ("What is the difference between physical and transition risk?", "Physical risk comes from climate hazards such as heat, flooding and water stress. Transition risk comes from policy, technology and market shifts toward a lower-carbon economy."),
        ("What is a PCAF data quality score?", "A score from 1 to 5 indicating the reliability of emissions data used for each exposure, from verified reported emissions (1) to broad estimates (5)."),
    ]
    body = """
    <p>For GCC banks, 2026 is the year climate moved from voluntary narrative to regulated reporting. The Qatar Central Bank's Sustainability Reporting Framework, issued in December 2025, requires banks and insurers to report under IFRS S1 and S2 for financial years beginning on or after 1 January 2026, with first reports due in 2027. Qatar's financial centre regulator and stock exchange have aligned to the same standards.</p>
    <p>IFRS S2 asks banks to explain how climate affects their strategy, risk management and financial position, and to report greenhouse gas emissions including, in practice, the emissions they finance. That makes climate risk management in banking a data, risk and governance problem at once. Banks that treat it only as a reporting deadline will produce a document. Banks that treat it as risk management will produce better lending decisions.</p>
    <h2>What is climate risk in banking?</h2>
    <p>Climate risk in banking is the potential for climate change, and society's response to it, to cause financial losses through a bank's lending, investments and operations. It is not a separate risk type. It shows up through existing ones: credit, market, liquidity, operational and reputational risk.</p>
    <ul>
      <li><strong>Physical risk</strong> — losses from climate hazards, either acute (floods, storms) or chronic (heat stress, water scarcity, sea-level rise), affecting borrowers' assets, operations and collateral values.</li>
      <li><strong>Transition risk</strong> — losses from the shift to a lower-carbon economy, through policy, carbon pricing, technology change, shifting demand and legal action, affecting borrowers' business models and asset values.</li>
    </ul>
    <h2>How ESG, GHG accounting and PCAF fit together</h2>
    <div class="table-wrap"><table>
      <thead><tr><th>Term</th><th>What it is</th><th>Role for a bank</th></tr></thead>
      <tbody>
        <tr><td>ESG</td><td>A broad set of environmental, social and governance factors</td><td>The overall framing for sustainability risk and reporting</td></tr>
        <tr><td>Climate risk</td><td>A specific financial risk within ESG</td><td>Integrated into credit, capital and strategy</td></tr>
        <tr><td>GHG accounting</td><td>Measuring emissions under the GHG Protocol across Scopes 1, 2 and 3</td><td>The bank's own footprint, and the basis for financed emissions</td></tr>
        <tr><td>Financed emissions</td><td>Scope 3, Category 15: emissions attributable to loans and investments</td><td>Usually the largest part of a bank's footprint, and a transition-risk indicator</td></tr>
        <tr><td>PCAF</td><td>The Global GHG Accounting and Reporting Standard for the financial industry</td><td>The industry method for calculating financed emissions</td></tr>
        <tr><td>IFRS S2</td><td>The ISSB's climate-related disclosure standard</td><td>How climate risks, opportunities and metrics are reported</td></tr>
      </tbody>
    </table></div>
    <h2>PCAF and financed emissions: what changed</h2>
    <p>The Partnership for Carbon Accounting Financials published the third edition of its financed-emissions standard (Part A) in December 2025. It expands coverage from seven to ten asset classes and adds methodologies for use-of-proceeds structures, securitisations and structured products, sub-sovereign debt and an optional approach for undrawn loan commitments consistent with IFRS S1 and S2.</p>
    <p>The method itself is now well established: attribute a share of each borrower's emissions to the bank in proportion to its financing. The hard part is data. PCAF scores data quality from 1, verified reported emissions, to 5, broad estimates. In markets where few borrowers report emissions, early portfolios will lean heavily on estimates. That is acceptable if it is disclosed and if the bank has a plan to improve it.</p>
    <h2>The GCC context</h2>
    <ul>
      <li><strong>Qatar:</strong> IFRS S1 and S2 mandatory for QCB-regulated banks and insurers from financial year 2026. The QCB's 2024 ESG and Sustainability Strategy also sets out plans for climate risk stress testing and ESG disclosure.</li>
      <li><strong>UAE:</strong> Federal climate legislation requires GHG measurement and reporting, with a first compliance deadline reported as 30 May 2026. Verify current scope and any extensions.</li>
      <li><strong>Saudi Arabia:</strong> General sustainability disclosure remains voluntary, with SOCPA reviewing IFRS S1 and S2 and capital-market authorities signalling convergence.</li>
    </ul>
    <p>The region's exposures also differ from Europe's. Physical risk centres on extreme heat, water stress and coastal assets. Transition risk is shaped by economies with significant hydrocarbon activity and ambitious diversification programmes, which affect both the risks and the transition-finance opportunities in loan books.</p>
    <h2>The Climate Intelligence Stack</h2>
    <p>Aryx uses a five-layer model to move from disclosure to decision. Each layer depends on the one below it.</p>
    <div class="table-wrap"><table>
      <thead><tr><th>Layer</th><th>Question it answers</th><th>Key capabilities</th></tr></thead>
      <tbody>
        <tr><td>5. Decisions</td><td>What do we do differently?</td><td>Pricing, limits, client engagement, transition finance, capital planning</td></tr>
        <tr><td>4. Risk integration</td><td>Where does climate change our risk profile?</td><td>Climate in credit policy, ICAAP, risk appetite, collateral valuation</td></tr>
        <tr><td>3. Scenarios</td><td>What happens under different futures?</td><td>Scenario analysis and stress testing, often using NGFS scenarios</td></tr>
        <tr><td>2. Exposure</td><td>Where are we exposed?</td><td>Physical hazard mapping, sector and counterparty transition assessment</td></tr>
        <tr><td>1. Data</td><td>What do we actually know?</td><td>GHG inventory, PCAF financed emissions, counterparty and asset data, lineage and controls</td></tr>
      </tbody>
    </table></div>
    <p>Most banks are building layers 1 and 2 for their first IFRS S2 report. The value lies in reaching layers 4 and 5, where climate changes lending and strategy.</p>
    <h2>Implementation priorities for 2026–2027</h2>
    <ul>
      <li><strong>Governance first.</strong> Board and management responsibilities for climate risk, documented and reflected in committee mandates.</li>
      <li><strong>A financed-emissions baseline.</strong> Prioritize the highest-emitting sectors and largest exposures; record PCAF data quality scores honestly.</li>
      <li><strong>Data you can defend.</strong> Treat emissions data like financial data: sources, lineage, controls and review.</li>
      <li><strong>Scenario analysis that informs credit.</strong> Start with material sectors and a small set of scenarios; connect results to sector limits and client reviews.</li>
      <li><strong>Client engagement.</strong> Collect borrower emissions and transition plans through onboarding and annual reviews.</li>
    </ul>
    <h2>Risks and limitations</h2>
    <ul>
      <li>Estimate-heavy baselines can mislead if presented with false precision. Disclose methods and quality scores.</li>
      <li>Scenario outputs depend heavily on assumptions; use them to explore vulnerability, not to predict losses.</li>
      <li>Siloed sustainability teams produce reports the risk function does not use. Climate needs to sit inside risk governance.</li>
      <li>Greenwashing exposure rises when targets and green-finance labels outrun evidence.</li>
    </ul>
    """
    links = 'Related: <a href="../../climate-intelligence/index.html">climate risk and emissions intelligence</a>, <a href="../../industries/banking/index.html">financed emissions for banks</a> and <a href="../../risk-decision-intelligence/index.html">climate risk inside enterprise risk</a>.'
    shell(meta, body, faqs, links)

def article_cyber():
    meta = dict(ARTICLES[3])
    meta["questions"] = """<ol>
      <li>Which services make up our Minimum Viable Enterprise, and has the board agreed them?</li>
      <li>How long can each of those services be unavailable before harm becomes unacceptable?</li>
      <li>When did we last restore a critical system from backup at realistic scale, and how long did it take?</li>
      <li>Could an attacker reach our backups from our production network?</li>
      <li>Which suppliers could stop our critical services, and what is our fallback for each?</li>
      <li>Have we decided, in advance, how we would approach a ransom demand?</li>
      <li>When did the executive team last rehearse a severe cyber crisis together?</li>
      <li>Do our board reports show outcomes or only activity?</li>
    </ol>"""
    meta["means"] = """<ul>
      <li>Success in cybersecurity is increasingly judged by continuity and recovery, not only prevention.</li>
      <li>Define the Minimum Viable Enterprise; it turns cyber investment into a business decision.</li>
      <li>Testing is the difference between a plan and a capability.</li>
      <li>Third-party dependencies are part of your resilience whether contracts acknowledge it or not.</li>
      <li>Boards should ask for outcome metrics, not activity counts.</li>
    </ul>"""
    meta["perspective"] = """<p>We see cyber resilience as an intelligence problem as much as a technical one. Organizations rarely lack security tools; they lack a connected picture of which services matter, what they depend on, and how exposure changes as threats and suppliers change.</p>
    <p>Aryx connects cyber, technology, third-party and operational risk around the services that keep an organization running, so leaders can invest, test and decide with that picture in front of them.</p>"""
    meta["conclusion"] = "<p>No organization can promise it will never be breached. Every organization can decide what it will keep running, prove it can recover, and lead calmly when it matters. That is what a cyber resilience strategy delivers, and what boards will increasingly be judged on.</p>"
    meta["sources"] = """<ul>
      <li>NIST CSF 2.0; NCSA Qatar NIA standard; EU DORA (Regulation (EU) 2022/2554).</li>
      <li>Verify before publishing: NIA version and scope against the NCSA site; sector regulators' current cyber requirements; DORA application date.</li>
    </ul>"""
    faqs = [
        ("What is a cyber resilience strategy?", "A cyber resilience strategy is a plan to keep critical services running and recover quickly from cyber attacks, combining prioritization, protection, testing and recovery."),
        ("What is the difference between cybersecurity and cyber resilience?", "Cybersecurity aims to prevent attacks. Cyber resilience assumes some will succeed and focuses on continuing operations and recovering."),
        ("What is the Minimum Viable Enterprise?", "It is the smallest set of services, systems, data and people an organization needs to keep operating through a severe incident, used to prioritize resilience investment."),
        ("How should boards measure cyber resilience?", "With outcome metrics such as tested recovery times for critical services, time to contain incidents, supplier fallbacks and the results of crisis exercises."),
        ("What is NIST CSF 2.0's Govern function?", "Govern is the function added in NIST Cybersecurity Framework 2.0 that covers cyber risk strategy, roles, policy and oversight within enterprise risk management."),
        ("Is the NIA standard mandatory in Qatar?", "The National Information Assurance standard is mandatory for government entities and critical infrastructure operators in Qatar and is maintained by the National Cyber Security Agency. Other organizations often adopt it as best practice."),
    ]
    body = """
    <p>Every board has been told that cybersecurity is a top risk. Fewer have been asked the harder question: if a serious attack succeeds tomorrow, which services must keep running, how long can each be down, and how do we know we can restore them?</p>
    <p>A cyber resilience strategy is built around that question. It accepts that some attacks will get through, and it measures success by continuity and recovery, not only by threats blocked.</p>
    <h2>What is cyber resilience?</h2>
    <p>Cyber resilience is an organization's ability to anticipate, withstand, recover from and adapt to cyber attacks and failures while continuing to deliver its most important services.</p>
    <p>Cybersecurity aims to prevent compromise. Cyber resilience assumes compromise is possible and ensures the business can still operate. The two are complementary: strong security reduces how often resilience is tested; strong resilience limits the damage when it is.</p>
    <h2>Why it belongs on the board agenda</h2>
    <ul>
      <li><strong>Attacks now target continuity.</strong> Ransomware and destructive attacks aim to stop operations, not only to steal data. Their impact is measured in hours of downtime and lost revenue.</li>
      <li><strong>Dependencies have multiplied.</strong> Cloud platforms, managed service providers and software supply chains mean a single third-party incident can disable many organizations at once.</li>
      <li><strong>Regulators have shifted to outcomes.</strong> NIST's Cybersecurity Framework 2.0 added a Govern function that places cyber risk within enterprise risk and leadership accountability. In the EU, the Digital Operational Resilience Act has applied to financial entities since January 2025. In Qatar, the National Information Assurance standard, maintained by the National Cyber Security Agency, sets mandatory controls for government entities and critical infrastructure operators, and sits within the National Cyber Security Strategy 2024–2030. Sector regulators, including central banks, add their own expectations. Verify current GCC sector rules at publication.</li>
    </ul>
    <h2>The Minimum Viable Enterprise</h2>
    <p>Resilience starts with a clear answer to one question: what is the smallest set of services, systems, data and people the organization needs to keep operating through a severe incident? Aryx calls this the Minimum Viable Enterprise.</p>
    <ul>
      <li>Which services matter most to customers, revenue, safety and regulators?</li>
      <li>What is the maximum tolerable disruption for each?</li>
      <li>Which systems, data, suppliers and people does each depend on?</li>
      <li>What is the fallback if the primary path is unavailable?</li>
    </ul>
    <p>Once defined, the Minimum Viable Enterprise becomes the organizing principle for investment. Protection, monitoring, backup and recovery effort concentrate where they keep the organization alive.</p>
    <h2>Four pillars of a cyber resilience strategy</h2>
    <div class="table-wrap"><table>
      <thead><tr><th>Pillar</th><th>Purpose</th><th>Key practices</th></tr></thead>
      <tbody>
        <tr><td>Prioritize</td><td>Know what must survive</td><td>Map important services and dependencies; set impact tolerances</td></tr>
        <tr><td>Protect</td><td>Make compromise harder and smaller</td><td>Identity-first security, segmentation, privileged access control, secure configuration</td></tr>
        <tr><td>Prove</td><td>Show it works before it is needed</td><td>Recovery testing, crisis exercises, red-team and scenario tests</td></tr>
        <tr><td>Recover and adapt</td><td>Restore and improve</td><td>Immutable backups, clean-room recovery, playbooks, post-incident learning</td></tr>
      </tbody>
    </table></div>
    <p>Prioritize is where most programmes are weakest. Without it, controls are spread evenly across systems of very different value. Protect emphasizes containment. Prove separates confidence from evidence. Recover and adapt requires backups attackers cannot reach, a clean environment to restore into, and decisions made in advance about ransom, disclosure and communication.</p>
    <h2>A board resilience scorecard</h2>
    <p>Boards often receive security metrics that measure activity: alerts processed, patches applied, training completed. Resilience needs outcome metrics.</p>
    <div class="table-wrap"><table>
      <thead><tr><th>Metric</th><th>What it tells the board</th></tr></thead>
      <tbody>
        <tr><td>Critical services with tested recovery within tolerance</td><td>Whether the Minimum Viable Enterprise can actually be restored</td></tr>
        <tr><td>Time to detect and contain significant incidents</td><td>How quickly damage is limited</td></tr>
        <tr><td>Critical suppliers with assessed and tested fallbacks</td><td>Exposure to third-party failure</td></tr>
        <tr><td>Coverage of strong authentication on privileged and remote access</td><td>Exposure to the most common attack paths</td></tr>
        <tr><td>Date and outcome of the last executive crisis exercise</td><td>Readiness of leadership, not just technology</td></tr>
        <tr><td>Open high-severity findings past due date</td><td>Whether known gaps are being closed</td></tr>
      </tbody>
    </table></div>
    <h2>Risks and limitations</h2>
    <ul>
      <li>Resilience as rebranding. Renaming the security programme without redefining priorities changes nothing.</li>
      <li>Untested backups. Backups that are connected to the production network or never restored at scale may fail when needed.</li>
      <li>Third-party blind spots. Contracts rarely guarantee a supplier's recovery time; fallbacks must be planned.</li>
      <li>Exercise theatre. Scripted exercises that avoid hard decisions give false comfort.</li>
    </ul>
    """
    links = 'Related: <a href="../../cybersecurity/index.html">cybersecurity as a business-risk discipline</a> and <a href="../../risk-decision-intelligence/index.html">operational resilience</a>. The planned article “Ten Questions Every CEO Should Ask Their CISO” is not published yet; the board questions on this page cover the same conversation.'
    shell(meta, body, faqs, links)
