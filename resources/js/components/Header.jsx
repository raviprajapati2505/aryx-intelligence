import { Link, useLocation } from 'react-router-dom';

const capabilityPaths = new Set([
    '/enterprise-ai',
    '/cybersecurity',
    '/risk-decision-intelligence',
    '/climate-intelligence',
    '/digital-transformation',
]);

export default function Header() {
    const { pathname } = useLocation();
    const onCapability = capabilityPaths.has(pathname);
    const onIndustry = pathname === '/industries' || pathname.startsWith('/industries-');
    const onInsights = pathname === '/insights' || pathname.startsWith('/insights-');
    const onAbout = pathname === '/about';

    return (
        <header className="nav" id="nav">
            <div className="wrap nav-in">
                <Link className="logo" to="/" aria-label="Aryx Intelligence, home"><img src="/assets/images/aryx-logo.png" alt="" /></Link>
                <button className="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="navLinks">Menu</button>
                <ul className="nav-links" id="navLinks">
                    <li>
                        <button className="nl" aria-expanded="false" aria-controls="megaCap" data-mega {...(onCapability ? { 'aria-current': 'page' } : {})}>Capabilities <span className="car" /></button>
                        <div className="mega" id="megaCap">
                            <Link to="/enterprise-ai"><b>Enterprise AI</b><span>Strategy, agents and AI governance</span></Link>
                            <Link to="/cybersecurity"><b>Cybersecurity</b><span>Strategy, cyber risk and resilience</span></Link>
                            <Link to="/risk-decision-intelligence"><b>Risk &amp; Decision Intelligence</b><span>Connected risk, scenarios and decisions</span></Link>
                            <Link to="/climate-intelligence"><b>Climate Intelligence</b><span>Climate risk, GHG, PCAF and ESG data</span></Link>
                            <Link to="/digital-transformation"><b>Digital &amp; Technology Transformation</b><span>Architecture, cloud, data and modernization</span></Link>
                        </div>
                    </li>
                    <li>
                        <button className="nl" aria-expanded="false" aria-controls="megaInd" data-mega {...(onIndustry ? { 'aria-current': 'page' } : {})}>Industries <span className="car" /></button>
                        <div className="mega cols" id="megaInd">
                            <Link to="/industries"><b>All industries</b></Link>
                            <Link to="/industries-banking-financial-services">Banking &amp; Financial Services</Link>
                            <Link to="/industries-government-public-sector">Government &amp; Public Sector</Link>
                            <Link to="/industries-energy">Energy</Link>
                            <Link to="/industries-infrastructure">Infrastructure</Link>
                            <Link to="/industries-real-estate">Real Estate</Link>
                            <Link to="/industries-healthcare">Healthcare</Link>
                            <Link to="/industries-manufacturing">Manufacturing</Link>
                            <Link to="/industries-technology">Technology</Link>
                            <Link to="/industries-professional-services">Professional Services</Link>
                        </div>
                    </li>
                    <li><Link className="nl" to="/insights" {...(onInsights ? { 'aria-current': 'page' } : {})}>Insights</Link></li>
                    <li><Link className="nl" to="/about" {...(onAbout ? { 'aria-current': 'page' } : {})}>About</Link></li>
                    <li><Link className="btn sm" to="/contact">Talk to Aryx <span className="arr" /></Link></li>
                </ul>
            </div>
        </header>
    );
}
