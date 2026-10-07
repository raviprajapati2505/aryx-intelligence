import { Link } from 'react-router-dom';

export default function IndustriesPage() {
  return (
    <main id={"top"}>
<section className={"dark page-hero gl-through"} data-hero aria-labelledby={"h1"}>
 <div className={"drag-zone"} data-drag aria-hidden={"true"}></div>
 <svg className={"fallback-emblem"} aria-hidden={"true"}><use href={"#emblem"} /></svg>
 <div className={"wrap"}><div className={"hero-copy"}>
  <nav aria-label={"Breadcrumb"}><ol className={"crumbs"}><li><Link to={"/"}>Home</Link></li><li><span aria-current={"page"}>Industries</span></li></ol></nav>
  <p className={"eyebrow"}>Industries</p>
  <h1 id={"h1"} data-split>Intelligence shaped by the realities of your sector</h1>
  <p className={"sub"}>Every sector faces the same forces: AI adoption, cyber threat and regulatory change. How they combine is specific to each one. We bring cross-sector discipline and sector-specific understanding to the decisions that matter in yours.</p>
  <div className={"ctas"}><Link className={"btn"} to={"/contact"}>Start a Strategic Conversation <span className={"arr"}></span></Link><Link className={"tlink"} to={"/enterprise-ai"}>Explore capabilities</Link></div>
  <p className={"tool-note"} style={{maxWidth: "520px"}}>Nine sector paths feed the structure. Point at a sector below to light its path.</p>
 </div></div>
 <p className={"drag-hint"}>Drag to turn the structure</p>
</section>
<div className={"cut"} aria-hidden={"true"}></div><section className={"light sec"} style={{paddingTop: "40px"}} aria-labelledby={"indsH"}><div className={"wrap"}><div className={"sec-head"}><div style={{display: "grid", gap: "18px"}}><p className={"eyebrow rv"}>Sectors</p><h2 id={"indsH"} className={"rv"}>Nine sectors, one connected view</h2></div><p className={"rv"}>Each sector page sets out the challenge, our perspective, the capabilities that apply and the outcomes we design for.</p></div><div className={"ind-cards"}><Link className={"ind-card rv"} to={"/industries-banking-financial-services"} data-path={"0"}><span className={"n"}>01 / 09</span><h3>Banking & Financial Services</h3><p>Banks must adopt AI and digital channels quickly while meeting some of the most demanding supervisory expectations for cyber, AI, operational resilience and third-party risk.</p><span className={"tlink"} style={{padding: "0"}}>Explore →</span></Link><Link className={"ind-card rv"} to={"/industries-government-public-sector"} data-path={"1"}><span className={"n"}>02 / 09</span><h3>Government & Public Sector</h3><p>Governments are digitizing services and adopting AI while protecting national data, critical services and public trust.</p><span className={"tlink"} style={{padding: "0"}}>Explore →</span></Link><Link className={"ind-card rv"} to={"/industries-energy"} data-path={"2"}><span className={"n"}>03 / 09</span><h3>Energy</h3><p>Energy companies operate critical infrastructure where IT and operational technology converge, while navigating the energy transition and growing climate-related disclosure expectations.</p><span className={"tlink"} style={{padding: "0"}}>Explore →</span></Link><Link className={"ind-card rv"} to={"/industries-infrastructure"} data-path={"3"}><span className={"n"}>04 / 09</span><h3>Infrastructure</h3><p>Transport, utilities and smart-city systems are increasingly connected, long-lived and difficult to modernize without disruption.</p><span className={"tlink"} style={{padding: "0"}}>Explore →</span></Link><Link className={"ind-card rv"} to={"/industries-real-estate"} data-path={"4"}><span className={"n"}>05 / 09</span><h3>Real Estate</h3><p>Developers and owners manage smart buildings, tenant data, large vendor ecosystems and rising sustainability expectations.</p><span className={"tlink"} style={{padding: "0"}}>Explore →</span></Link><Link className={"ind-card rv"} to={"/industries-healthcare"} data-path={"5"}><span className={"n"}>06 / 09</span><h3>Healthcare</h3><p>Healthcare organizations hold highly sensitive data, depend on always-available systems and face growing interest in clinical and operational AI.</p><span className={"tlink"} style={{padding: "0"}}>Explore →</span></Link><Link className={"ind-card rv"} to={"/industries-manufacturing"} data-path={"6"}><span className={"n"}>07 / 09</span><h3>Manufacturing</h3><p>Connected factories and global supply chains raise productivity and exposure at the same time.</p><span className={"tlink"} style={{padding: "0"}}>Explore →</span></Link><Link className={"ind-card rv"} to={"/industries-technology"} data-path={"7"}><span className={"n"}>08 / 09</span><h3>Technology</h3><p>Technology companies must ship quickly, secure their products and customers, and govern the AI they build into them.</p><span className={"tlink"} style={{padding: "0"}}>Explore →</span></Link><Link className={"ind-card rv"} to={"/industries-professional-services"} data-path={"8"}><span className={"n"}>09 / 09</span><h3>Professional Services</h3><p>Firms hold confidential client information and are adopting generative AI across knowledge work.</p><span className={"tlink"} style={{padding: "0"}}>Explore →</span></Link></div></div></section>
<section className={"dark closing gl-through"} id={"closing"} data-closing aria-labelledby={"closeH"}>
 <div className={"drag-zone"} data-drag aria-hidden={"true"}></div>
 <svg className={"fallback-emblem"} aria-hidden={"true"}><use href={"#emblem"} /></svg>
 <div className={"wrap"}><div className={"copy"}>
  <p className={"eyebrow rv"}>Your sector, your decision</p><h2 id={"closeH"} className={"rv"}>Every sector combines the same forces differently.</h2><p className={"lede rv"}>Tell us the decision in front of you, and we will show you what intelligence would change it.</p>
  <div className={"ctas rv"}><Link className={"btn"} to={"/contact"}>Discuss Your Challenge <span className={"arr"}></span></Link></div>
 </div></div>
</section>
</main>
  );
}

IndustriesPage.meta = {
    "path": "/industries",
    "title": "Industries We Serve | Aryx Intelligence",
    "description": "AI, cybersecurity and risk intelligence for banking, government, energy, infrastructure, real estate, healthcare, manufacturing and more.",
    "canonical": "https://aryxintelligence.com/industries",
    "scene": "industries",
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
                    "name": "Industries",
                    "item": "https://aryxintelligence.com/"
                }
            ]
        }
    ]
};
