import { memo } from 'react';
import { Link } from 'react-router-dom';

function Footer() {
    return (
        <footer>
            <div className="wrap">
                <div className="ft-top">
                    <div className="ft-brand">
                        <svg aria-hidden="true"><use href="#emblem" /></svg>
                        <p className="sig">Complexity, made decisive.</p>
                        <form className="news">
                            <label className="sr" htmlFor="fNews">Email for The Aryx Brief</label>
                            <input id="fNews" type="email" placeholder="The Aryx Brief, monthly" />
                            <button type="submit">Subscribe</button>
                        </form>
                    </div>
                    <div className="ft-col">
                        <h4>Capabilities</h4>
                        <ul>
                            <li><Link to="/enterprise-ai">Enterprise AI</Link></li>
                            <li><Link to="/cybersecurity">Cybersecurity</Link></li>
                            <li><Link to="/risk-decision-intelligence">Risk &amp; Decision Intelligence</Link></li>
                            <li><Link to="/climate-intelligence">Climate Intelligence</Link></li>
                            <li><Link to="/digital-transformation">Digital &amp; Technology Transformation</Link></li>
                        </ul>
                    </div>
                    <div className="ft-col">
                        <h4>Industries</h4>
                        <ul>
                            <li><Link to="/industries-banking-financial-services">Banking &amp; Financial Services</Link></li>
                            <li><Link to="/industries-government-public-sector">Government &amp; Public Sector</Link></li>
                            <li><Link to="/industries-energy">Energy</Link></li>
                            <li><Link to="/industries-infrastructure">Infrastructure</Link></li>
                            <li><Link to="/industries-real-estate">Real Estate</Link></li>
                            <li><Link to="/industries-healthcare">Healthcare</Link></li>
                            <li><Link to="/industries-manufacturing">Manufacturing</Link></li>
                            <li><Link to="/industries-technology">Technology</Link></li>
                            <li><Link to="/industries-professional-services">Professional Services</Link></li>
                        </ul>
                    </div>
                    <div className="ft-col">
                        <h4>Company</h4>
                        <ul>
                            <li><Link to="/about">About</Link></li>
                            <li><Link to="/insights">Insights</Link></li>
                            <li><Link to="/contact">Contact</Link></li>
                            <li><Link to="/about">Careers <span className="ph">[TBC]</span></Link></li>
                        </ul>
                    </div>
                    <div className="ft-col">
                        <h4>Legal</h4>
                        <ul>
                            <li><Link to="/contact">Privacy</Link></li>
                            <li><Link to="/contact">Terms</Link></li>
                            <li><Link to="/contact">Cookies</Link></li>
                        </ul>
                    </div>
                </div>
                <div className="ft-bot">
                    <span className="promise">Clarity you can act on.</span>
                    <span>Doha, Qatar · <span className="ph">[OFFICE ADDRESS]</span> · <a href="https://www.linkedin.com/" rel="noopener">LinkedIn</a></span>
                    <span>© 2026 Aryx Intelligence</span>
                </div>
            </div>
        </footer>
    );
}

export default memo(Footer);
