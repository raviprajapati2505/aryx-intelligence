import { Link } from 'react-router-dom';

export default function ContactPage() {
  return (
    <main id={"top"}>
<section className={"dark contact-hero gl-through"} data-hero aria-labelledby={"h1"}><div className={"wrap contact-grid"}>
 <div style={{display: "grid", gap: "24px", alignContent: "start", position: "relative", zIndex: "2"}}><nav aria-label={"Breadcrumb"}><ol className={"crumbs"}><li><Link to={"/"}>Home</Link></li><li><span aria-current={"page"}>Contact</span></li></ol></nav><p className={"eyebrow"}>Contact</p><h1 id={"h1"} data-split style={{fontSize: "clamp(42px,5.6vw,84px)"}}>Start a strategic conversation</h1><p className={"sub"} style={{color: "#C9D4CF", maxWidth: "480px"}}>Tell us about the decision or challenge in front of you. A senior member of our team will respond within <span className={"ph"}>[X business days]</span> to arrange a conversation.</p>
  <div className={"cdetails"}><div><span>Company</span><p>Aryx Intelligence</p></div><div><span>Office</span><p><span className={"ph"}>[Office address]</span>, Doha, Qatar</p></div><div><span>Email</span><p><span className={"ph"}>[General email]</span></p></div><div><span>Phone</span><p><span className={"ph"}>[Phone]</span></p></div><div><span>LinkedIn</span><p><span className={"ph"}>[LinkedIn company page]</span></p></div></div>
 </div>
 <div className={"contact-card"} id={"contact"}><h2 style={{fontSize: "28px", marginBottom: "22px"}}>What decision are you trying to make clearer?</h2><form data-contact noValidate>
 <div className={"f"}><label htmlFor={"fName"}>Name</label><input id={"fName"} autoComplete={"name"} required /><span className={"err"}></span></div>
 <div className={"f"}><label htmlFor={"fTitle"}>Title</label><input id={"fTitle"} autoComplete={"organization-title"} /><span className={"err"}></span></div>
 <div className={"f"}><label htmlFor={"fOrg"}>Organization</label><input id={"fOrg"} autoComplete={"organization"} required /><span className={"err"}></span></div>
 <div className={"f"}><label htmlFor={"fEmail"}>Business email</label><input id={"fEmail"} type={"email"} autoComplete={"email"} required /><span className={"err"}></span></div>
 <div className={"f"}><label htmlFor={"fCountry"}>Country</label><input id={"fCountry"} autoComplete={"country-name"} /><span className={"err"}></span></div>
 <div className={"f"}><label htmlFor={"fArea"}>Area of interest</label><select id={"fArea"}><option value={""}>Choose an area</option><option>Enterprise AI</option><option>Cybersecurity</option><option>Risk & Decision Intelligence</option><option>Climate Intelligence</option><option>Digital & Technology Transformation</option><option>Other</option></select><span className={"err"}></span></div>
 <div className={"f full"}><label htmlFor={"fMsg"}>What decision or challenge are you facing?</label><textarea id={"fMsg"} required></textarea><span className={"err"}></span></div>
 <input className={"hp"} id={"fHp"} tabIndex={"-1"} autoComplete={"off"} aria-hidden={"true"} />
 <label className={"consent"} htmlFor={"fConsent"}><input type={"checkbox"} id={"fConsent"} required /> I agree to the privacy policy.</label>
 <div className={"form-foot"}><button className={"btn"} type={"submit"}>Send to Aryx <span className={"arr"}></span></button><span className={"reassure"}>Every conversation is confidential. <span className={"ph"}>[CONFIRM]</span></span></div>
 <div className={"status"} data-status hidden></div>
</form></div>
</div></section>
</main>
  );
}

ContactPage.meta = {
    "path": "/contact",
    "title": "Contact Aryx Intelligence | Doha, Qatar",
    "description": "Start a strategic conversation with Aryx Intelligence about AI, cybersecurity, risk or technology decisions. Headquartered in Doha, Qatar.",
    "canonical": "https://aryxintelligence.com/contact",
    "scene": "contact",
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
                    "name": "Contact",
                    "item": "https://aryxintelligence.com/"
                }
            ]
        },
        {
            "@context": "https://schema.org",
            "@type": "ContactPage",
            "name": "Contact Aryx Intelligence | Doha, Qatar"
        }
    ]
};
