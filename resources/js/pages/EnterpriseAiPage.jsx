import { Link } from 'react-router-dom';

export default function EnterpriseAiPage() {
  return (
    <main id={"top"}>
<section className={"dark page-hero gl-through"} data-hero aria-labelledby={"h1"}>
 <div className={"drag-zone"} data-drag aria-hidden={"true"}></div>
 <svg className={"fallback-emblem"} aria-hidden={"true"}><use href={"#emblem"} /></svg>
 <div className={"wrap"}><div className={"hero-copy"}>
  <nav aria-label={"Breadcrumb"}><ol className={"crumbs"}><li><Link to={"/"}>Home</Link></li><li><Link to={"/#capabilities"}>Capabilities</Link></li><li><span aria-current={"page"}>Enterprise AI</span></li></ol></nav>
  <p className={"eyebrow"}>Enterprise AI</p>
  <h1 id={"h1"} data-split>Enterprise AI that answers to the business</h1>
  <p className={"sub"}>We help organizations decide where AI creates value, build it responsibly, and govern it with the same discipline as any material risk.</p>
  <div className={"ctas"}><Link className={"btn"} to={"/contact#area-ai"}>Explore Enterprise AI <span className={"arr"}></span></Link><Link className={"tlink"} to={"/contact#area-ai"}>Assess Your AI Readiness</Link></div>
  <ul className={"anchors"} aria-label={"Capabilities on this page"}><li><a href={"#cap-ai-strategy"}>AI strategy</a></li><li><a href={"#cap-decision-intelligence"}>Decision intelligence</a></li><li><a href={"#cap-generative-ai"}>Generative AI</a></li><li><a href={"#cap-ai-agents"}>AI agents</a></li><li><a href={"#cap-ai-automation"}>AI automation</a></li><li><a href={"#cap-ai-governance"}>AI governance</a></li><li><a href={"#cap-ai-enabled-business-transformation"}>AI-enabled business transformation</a></li><li><a href={"#cap-intelligent-systems"}>Intelligent systems</a></li></ul><ul className={"legend"} data-legend aria-label={"Decisions the lattice connects to"}><li>Credit</li><li>Pricing</li><li>Resource allocation</li><li>Threat response</li></ul>
 </div></div>
 <p className={"drag-hint"}>Drag to turn the structure</p>
</section>
<div className={"cut"} aria-hidden={"true"}></div><section className={"light sec"} style={{paddingTop: "40px"}} aria-labelledby={"probH"}><div className={"wrap split"}><div><p className={"eyebrow rv"} style={{marginBottom: "16px"}}>The problem</p><h2 id={"probH"} className={"rv"}>The problem with most enterprise AI</h2><div className={"prose-lg rv"}><p>Many organizations have AI pilots. Far fewer have AI that changes how decisions are made, at scale, with controls a regulator and a board would accept. The gap is rarely the model. It is unclear ownership, weak data foundations, missing governance and use cases chosen for novelty rather than value.</p></div></div><div><div className={"defcard rv"}><p className={"eyebrow"}>What enterprise AI means at Aryx</p><p className={"def"}>Enterprise AI is the use of machine learning, generative AI and intelligent automation inside core business processes, governed so that its outputs are reliable, explainable and accountable. We judge it by one test: does it improve a decision or an outcome the business cares about?</p></div></div></div></section>
<section className={"light sec tight"} aria-labelledby={"capsH"}><div className={"wrap"}><div className={"sec-head"}><div style={{display: "grid", gap: "18px"}}><p className={"eyebrow rv"}>Capabilities</p><h2 id={"capsH"} className={"rv"}>What we do</h2></div><p className={"rv"}>8 connected services, each judged by the decision it improves.</p></div><div className={"rows"}><div className={"row rv"} id={"cap-ai-strategy"}><span className={"ix"}>01</span><h3>AI strategy</h3><p>Identify where AI creates measurable value, prioritize use cases by impact and feasibility, and build a roadmap leadership can fund with confidence.</p></div><div className={"row rv"} id={"cap-decision-intelligence"}><span className={"ix"}>02</span><h3>Decision intelligence</h3><p>Connect data, analytics and AI to specific decisions, such as credit, pricing, resource allocation or threat response, so choices become faster, more consistent and auditable.</p></div><div className={"row rv"} id={"cap-generative-ai"}><span className={"ix"}>03</span><h3>Generative AI</h3><p>Deploy large language models for knowledge work, document intelligence and customer interaction, with guardrails for accuracy, privacy and data sovereignty.</p></div><div className={"row rv"} id={"cap-ai-agents"}><span className={"ix"}>04</span><h3>AI agents</h3><p>Design agents that take bounded actions across systems, with defined permissions, human checkpoints and full audit trails.</p></div><div className={"row rv"} id={"cap-ai-automation"}><span className={"ix"}>05</span><h3>AI automation</h3><p>Automate high-volume, rules-heavy processes where AI improves accuracy and frees people for judgment-based work.</p></div><div className={"row rv"} id={"cap-ai-governance"}><span className={"ix"}>06</span><h3>AI governance</h3><p>Establish policies, risk classification, model inventories, oversight roles and assurance aligned to ISO/IEC 42001, the NIST AI Risk Management Framework and applicable regulation, including sector rules such as the Qatar Central Bank's AI Guideline for licensed entities.</p></div><div className={"row rv"} id={"cap-ai-enabled-business-transformation"}><span className={"ix"}>07</span><h3>AI-enabled business transformation</h3><p>Redesign processes and operating models around AI, so value is captured in the business, not stranded in a pilot.</p></div><div className={"row rv"} id={"cap-intelligent-systems"}><span className={"ix"}>08</span><h3>Intelligent systems</h3><p>Architect the data, platforms and integration that let AI run reliably in production.</p></div></div></div></section>
<section className={"tool"} aria-label={"Use-case prioritizer"}><div className={"wrap"}><div className={"sec-head"}><div style={{display: "grid", gap: "18px"}}><p className={"rv"}><span className={"tag"}>Interactive · illustrative</span></p><h2 className={"rv"} style={{fontSize: "clamp(32px,4vw,56px)"}}>Where should AI go first?</h2></div><p className={"rv"}>Place sample use cases by value and feasibility. The quadrant tells you how to treat each one.</p></div><div className={"tool-box"} data-prio><div className={"prio"}>
 <div className={"chips"} aria-label={"Sample use cases"}><button type={"button"} className={"chip"} data-id={"u0"} aria-pressed={"false"}>Credit decision support</button><button type={"button"} className={"chip"} data-id={"u1"} aria-pressed={"false"}>Contract review with generative AI</button><button type={"button"} className={"chip"} data-id={"u2"} aria-pressed={"false"}>Customer service agent</button><button type={"button"} className={"chip"} data-id={"u3"} aria-pressed={"false"}>Invoice matching automation</button><button type={"button"} className={"chip"} data-id={"u4"} aria-pressed={"false"}>Threat triage assistant</button><button type={"button"} className={"chip"} data-id={"u5"} aria-pressed={"false"}>Board pack summarisation</button><button type={"button"} className={"chip"} data-id={"u6"} aria-pressed={"false"}>Demand forecasting</button><button type={"button"} className={"chip"} data-id={"u7"} aria-pressed={"false"}>HR policy assistant</button></div>
 <div><div className={"grid2"} role={"group"} aria-label={"Value versus feasibility grid"}>
   <span className={"q"} style={{right: "0", top: "0"}}>Quick win</span><span className={"q"} style={{left: "0", top: "0"}}>Strategic bet</span><span className={"q"} style={{right: "0", bottom: "0"}}>Easy, low value</span><span className={"q"} style={{left: "0", bottom: "0"}}>Park it</span>
   <span className={"ax"} style={{left: "50%", bottom: "-26px", transform: "translateX(-50%)"}}>Feasibility →</span><span className={"ax"} style={{left: "-30px", top: "50%", transform: "rotate(-90deg) translateX(50%)", transformOrigin: "left"}}>Value →</span>
 </div><p className={"prio-out"} aria-live={"polite"}></p></div></div>
 <p className={"tool-note"}>Drag a use case onto the grid, or select it and click a spot. Placed items move with arrow keys. Positions are your judgement, not a scoring model.</p></div></div></section>
<section className={"light sec"} aria-labelledby={"outH"}><div className={"wrap"}><div className={"sec-head"}><div style={{display: "grid", gap: "18px"}}><p className={"eyebrow rv"}>Outcomes</p><h2 id={"outH"} className={"rv"}>Outcomes we design for</h2></div></div><div className={"outs"}><div className={"out rv"}><span className={"bar-s"}></span><h3>Faster decisions</h3><p>Shorter cycle times on approvals, investigations and analysis</p></div><div className={"out rv"}><span className={"bar-s"}></span><h3>Better decisions</h3><p>More consistent outcomes, fewer errors, clearer rationale</p></div><div className={"out rv"}><span className={"bar-s"}></span><h3>Lower risk</h3><p>AI inventoried, classified, monitored and explainable</p></div><div className={"out rv"}><span className={"bar-s"}></span><h3>Scalable value</h3><p>Use cases that move from pilot to production with known economics</p></div><div className={"out rv"}><span className={"bar-s"}></span><h3>Regulatory confidence</h3><p>Evidence ready for boards, auditors and supervisors</p></div></div></div></section>
<section className={"light sec tight"} aria-labelledby={"stpH"}><div className={"wrap"}><div className={"sec-head"}><div style={{display: "grid", gap: "18px"}}><p className={"eyebrow rv"}>How we work</p><h2 id={"stpH"} className={"rv"}>How an AI engagement works</h2></div><p className={"rv"}>Steps advance on their own while in view. Select one to stop and read.</p></div><div className={"stepper"} data-stepper><ul className={"step-nav"} role={"tablist"}><li><button role={"tab"} aria-selected={"false"} aria-controls={"stp-0"}><span className={"n"}>01</span><span className={"t"}>Readiness</span></button></li><li><button role={"tab"} aria-selected={"false"} aria-controls={"stp-1"}><span className={"n"}>02</span><span className={"t"}>Prioritization</span></button></li><li><button role={"tab"} aria-selected={"false"} aria-controls={"stp-2"}><span className={"n"}>03</span><span className={"t"}>Design</span></button></li><li><button role={"tab"} aria-selected={"false"} aria-controls={"stp-3"}><span className={"n"}>04</span><span className={"t"}>Delivery</span></button></li><li><button role={"tab"} aria-selected={"false"} aria-controls={"stp-4"}><span className={"n"}>05</span><span className={"t"}>Assurance</span></button></li></ul><div className={"step-panel"} id={"stp-0"} role={"tabpanel"} data-step hidden><p className={"big"}>Readiness</p><p>Data, technology, skills and governance assessed against the ambition.</p></div><div className={"step-panel"} id={"stp-1"} role={"tabpanel"} data-step hidden><p className={"big"}>Prioritization</p><p>Use cases scored on value, feasibility and risk.</p></div><div className={"step-panel"} id={"stp-2"} role={"tabpanel"} data-step hidden><p className={"big"}>Design</p><p>Architecture, controls and human oversight defined before build.</p></div><div className={"step-panel"} id={"stp-3"} role={"tabpanel"} data-step hidden><p className={"big"}>Delivery</p><p>Build, test and deploy, with validation evidence captured as we go.</p></div><div className={"step-panel"} id={"stp-4"} role={"tabpanel"} data-step hidden><p className={"big"}>Assurance</p><p>Monitoring for performance, drift, bias and security, reported in business terms.</p></div></div></div></section>
<section className={"light sec tight"} aria-label={"Connected capabilities"}><div className={"wrap"}><p className={"eyebrow rv"} style={{marginBottom: "22px"}}>Connected capabilities</p><div className={"related"}><Link className={"rel rv"} to={"/risk-decision-intelligence"}><small>Risk & Decision Intelligence</small><b>managing AI as an enterprise risk</b><span className={"go"}>Read more →</span></Link><Link className={"rel rv"} to={"/cybersecurity"}><small>Cybersecurity</small><b>securing AI systems</b><span className={"go"}>Read more →</span></Link><Link className={"rel rv"} to={"/digital-transformation"}><small>Digital & Technology</small><b>data foundations for AI</b><span className={"go"}>Read more →</span></Link></div></div></section>
<section className={"light sec"} aria-labelledby={"faqH"}><div className={"wrap split"}>
 <div><p className={"eyebrow rv"} style={{marginBottom: "16px"}}>FAQ</p><h2 id={"faqH"} className={"rv"} style={{fontSize: "clamp(32px,3.6vw,54px)"}}>Questions leaders ask</h2></div>
 <div className={"faq"}><details className={"rv"}><summary>Where should we start with enterprise AI?</summary><p>Start with a decision or process where value is measurable, data exists and the risk is manageable. A focused first use case builds both evidence and governance muscle.</p></details><details className={"rv"}><summary>What is AI governance?</summary><p>AI governance is the set of policies, roles, controls and oversight that ensure AI systems are used safely, lawfully and in line with business objectives across their lifecycle.</p></details><details className={"rv"}><summary>How do you keep sensitive data secure when using generative AI?</summary><p>Through data classification, architecture choices such as private or in-region deployment, access controls and output monitoring, decided before any model sees sensitive data.</p></details><details className={"rv"}><summary>What is the difference between AI automation and AI agents?</summary><p>Automation executes a defined task. An agent pursues a goal across steps and systems, choosing actions within limits, so it needs stronger permissions design and oversight.</p></details></div></div></section>
<section className={"dark closing gl-through"} id={"closing"} data-closing aria-labelledby={"closeH"}>
 <div className={"drag-zone"} data-drag aria-hidden={"true"}></div>
 <svg className={"fallback-emblem"} aria-hidden={"true"}><use href={"#emblem"} /></svg>
 <div className={"wrap"}><div className={"copy"}>
  <p className={"eyebrow rv"}>Complexity, made decisive</p><h2 id={"closeH"} className={"rv"}>Find out where AI will change your decisions, and what it will take to govern it.</h2>
  <div className={"ctas rv"}><Link className={"btn"} to={"/contact#area-ai"}>Build Your Intelligence Strategy <span className={"arr"}></span></Link></div>
 </div></div>
</section>
</main>
  );
}

EnterpriseAiPage.meta = {
    "path": "/enterprise-ai",
    "title": "Enterprise AI Strategy & Governance | Aryx Intelligence",
    "description": "Enterprise AI strategy, AI agents, decision intelligence and AI governance built around measurable outcomes. Aryx Intelligence, Qatar and GCC.",
    "canonical": "https://aryxintelligence.com/enterprise-ai",
    "scene": "ai",
    "pathIndex": null,
    "jsonLd": [
        {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": "Aryx Intelligence",
            "url": "https://aryxintelligence.com",
            "logo": "https://aryxintelligence.com/logo.png",
            "description": "Aryx Intelligence is a Qatar-headquartered decision-intelligence company connecting AI, cybersecurity, risk, climate and enterprise technology.",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Doha",
                "addressCountry": "QA"
            }
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Home",
                    "item": "https://aryxintelligence.com/"
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": "Capabilities",
                    "item": "https://aryxintelligence.com/#capabilities"
                },
                {
                    "@type": "ListItem",
                    "position": 3,
                    "name": "Enterprise AI",
                    "item": "https://aryxintelligence.com/"
                }
            ]
        },
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": "Enterprise AI",
            "description": "Enterprise AI strategy, AI agents, decision intelligence and AI governance built around measurable outcomes. Aryx Intelligence, Qatar and GCC.",
            "provider": {
                "@type": "Organization",
                "name": "Aryx Intelligence"
            },
            "areaServed": [
                "Qatar",
                "GCC"
            ]
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "Where should we start with enterprise AI?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Start with a decision or process where value is measurable, data exists and the risk is manageable. A focused first use case builds both evidence and governance muscle."
                    }
                },
                {
                    "@type": "Question",
                    "name": "What is AI governance?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "AI governance is the set of policies, roles, controls and oversight that ensure AI systems are used safely, lawfully and in line with business objectives across their lifecycle."
                    }
                },
                {
                    "@type": "Question",
                    "name": "How do you keep sensitive data secure when using generative AI?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Through data classification, architecture choices such as private or in-region deployment, access controls and output monitoring, decided before any model sees sensitive data."
                    }
                },
                {
                    "@type": "Question",
                    "name": "What is the difference between AI automation and AI agents?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "Automation executes a defined task. An agent pursues a goal across steps and systems, choosing actions within limits, so it needs stronger permissions design and oversight."
                    }
                }
            ]
        }
    ]
};
