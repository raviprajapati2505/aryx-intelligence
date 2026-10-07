import { Link } from 'react-router-dom';

export default function NotFoundPage() {
    return (
        <main id="top">
            <section className="dark page-hero gl-through" data-hero aria-labelledby="h1">
                <div className="wrap">
                    <div className="hero-copy">
                        <p className="eyebrow">Aryx Intelligence</p>
                        <h1 id="h1">This page is not available.</h1>
                        <p className="sub">The address does not match a page on this site.</p>
                        <div className="ctas">
                            <Link className="btn" to="/">Back to home <span className="arr" /></Link>
                        </div>
                    </div>
                </div>
            </section>
        </main>
    );
}

NotFoundPage.meta = {
    path: '*',
    title: 'Page not available | Aryx Intelligence',
    description: 'This address does not match a page on the Aryx Intelligence site.',
    canonical: 'https://aryxintelligence.com/',
    scene: null,
    pathIndex: null,
    jsonLd: [],
};
