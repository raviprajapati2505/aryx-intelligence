import { useLayoutEffect } from 'react';
import { Outlet, useLocation, useMatches } from 'react-router-dom';
import Header from './Header';
import Footer from './Footer';
import { mountGl } from '../gl/stage';
import { mountSite } from '../lib/site';

const AREAS = {
    'area-ai': 'Enterprise AI',
    'area-cyber': 'Cybersecurity',
    'area-risk': 'Risk & Decision Intelligence',
    'area-climate': 'Climate Intelligence',
    'area-digital': 'Digital & Technology Transformation',
    'area-other': 'Other',
};

function ensureMeta(name) {
    let node = document.querySelector(`meta[name="${name}"]`);
    if (!node) {
        node = document.createElement('meta');
        node.setAttribute('name', name);
        document.head.appendChild(node);
    }
    return node;
}

function ensureOg(property) {
    let node = document.querySelector(`meta[property="${property}"]`);
    if (!node) {
        node = document.createElement('meta');
        node.setAttribute('property', property);
        document.head.appendChild(node);
    }
    return node;
}

function ensureCanonical() {
    let node = document.querySelector('link[rel="canonical"]');
    if (!node) {
        node = document.createElement('link');
        node.rel = 'canonical';
        document.head.appendChild(node);
    }
    return node;
}

export default function Layout() {
    const location = useLocation();
    const matches = useMatches();
    const meta = matches[matches.length - 1]?.handle ?? {};

    useLayoutEffect(() => {
        document.title = meta.title || 'Aryx Intelligence';
        ensureMeta('description').setAttribute('content', meta.description || '');
        ensureOg('og:type').setAttribute('content', 'website');
        ensureOg('og:title').setAttribute('content', meta.title || 'Aryx Intelligence');
        ensureOg('og:description').setAttribute('content', meta.description || '');
        ensureOg('og:url').setAttribute('content', meta.canonical || 'https://aryxintelligence.com/');
        ensureMeta('twitter:card').setAttribute('content', 'summary_large_image');
        if (meta.canonical) {
            ensureCanonical().href = meta.canonical;
        }
        document.querySelectorAll('script[data-ld]').forEach((node) => node.remove());
        (meta.jsonLd || []).forEach((data) => {
            const script = document.createElement('script');
            script.type = 'application/ld+json';
            script.dataset.ld = '1';
            script.textContent = typeof data === 'string' ? data : JSON.stringify(data);
            document.head.appendChild(script);
        });
    }, [meta]);

    useLayoutEffect(() => {
        if (location.hash) {
            const el = document.getElementById(decodeURIComponent(location.hash.slice(1)));
            if (el) el.scrollIntoView();
            else window.scrollTo(0, 0);
        } else {
            window.scrollTo(0, 0);
        }
        const area = document.getElementById('fArea');
        if (area && AREAS[location.hash.slice(1)]) {
            area.value = AREAS[location.hash.slice(1)];
        }
    }, [location.pathname, location.hash]);

    useLayoutEffect(() => {
        document.documentElement.classList.add('js');
        if (meta.scene) document.body.dataset.scene = meta.scene;
        else delete document.body.dataset.scene;
        if (meta.pathIndex != null && meta.pathIndex !== '') document.body.dataset.path = String(meta.pathIndex);
        else delete document.body.dataset.path;

        const nav = document.getElementById('nav');
        nav?.classList.remove('menu-open');
        const menuBtn = document.getElementById('menuBtn');
        if (menuBtn) {
            menuBtn.setAttribute('aria-expanded', 'false');
            menuBtn.textContent = 'Menu';
        }
        document.querySelectorAll('[data-mega]').forEach((button) => {
            button.setAttribute('aria-expanded', 'false');
            document.getElementById(button.getAttribute('aria-controls'))?.classList.remove('open');
        });

        const stopSite = mountSite();
        const stopGl = mountGl();
        return () => {
            stopSite();
            stopGl();
        };
    }, [location.pathname, meta.scene, meta.pathIndex]);

    return (
        <>
            <video className="bg-video" autoPlay muted loop playsInline aria-hidden="true">
                <source src="/assets/1.mp4" type="video/mp4" />
            </video>
            <div className="bg-shade" aria-hidden="true" />
            <canvas key={location.pathname} id="gl" aria-hidden="true" />
            <svg width="0" height="0" style={{ position: 'absolute' }} aria-hidden="true">
                <defs>
                    <symbol id="emblem" viewBox="0 0 206 131">
                        <polygon fill="#00483F" points="0,126 98,5 98,46" />
                        <polygon fill="#00352E" points="5,128 98,59 97,91" />
                        <polygon fill="#008775" points="108,2 205,126 107,44 107,24" />
                        <polygon fill="#00685A" points="108,59 201,128 108,90" />
                    </symbol>
                </defs>
            </svg>
            <Header />
            <Outlet />
            <Footer />
        </>
    );
}
