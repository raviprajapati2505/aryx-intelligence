<?php

/**
 * Writes the crawl files from the React page metadata:
 * resources/seo/pages.json, public/robots.txt, and public/sitemap.xml.
 */

if (realpath($_SERVER['SCRIPT_FILENAME'] ?? '') === __FILE__) {
    exportSeoArtifacts(dirname(__DIR__));
    echo "Wrote SEO files\n";
}

function exportSeoArtifacts(string $root): void
{
    $origin = 'https://aryxintelligence.com';
    $pages = [];

    foreach (glob($root.'/resources/js/pages/*Page.jsx') as $file) {
        $meta = extractPageMeta($file);
        if ($meta === null || ($meta['path'] ?? '') === '*') {
            continue;
        }
        $pages[] = [
            'path' => $meta['path'],
            'title' => $meta['title'] ?? '',
            'description' => $meta['description'] ?? '',
            'canonical' => $meta['canonical'] ?? $origin.($meta['path'] === '/' ? '/' : $meta['path']),
            'jsonLd' => $meta['jsonLd'] ?? [],
        ];
    }

    usort($pages, static function (array $a, array $b): int {
        return strlen($a['path']) <=> strlen($b['path']) ?: strcmp($a['path'], $b['path']);
    });

    $seoDir = $root.'/resources/seo';
    if (! is_dir($seoDir) && ! mkdir($seoDir, 0777, true) && ! is_dir($seoDir)) {
        fwrite(STDERR, "Cannot create {$seoDir}\n");
        exit(1);
    }

    file_put_contents(
        $seoDir.'/pages.json',
        json_encode($pages, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES).PHP_EOL
    );

    $robots = <<<TXT
User-agent: *
Allow: /

User-agent: Googlebot
Allow: /

Sitemap: {$origin}/sitemap.xml
TXT;
    file_put_contents($root.'/public/robots.txt', $robots.PHP_EOL);

    $xml = '<?xml version="1.0" encoding="UTF-8"?>'.PHP_EOL;
    $xml .= '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'.PHP_EOL;
    foreach ($pages as $page) {
        $loc = htmlspecialchars($page['canonical'], ENT_XML1 | ENT_QUOTES, 'UTF-8');
        $xml .= "  <url><loc>{$loc}</loc></url>".PHP_EOL;
    }
    $xml .= '</urlset>'.PHP_EOL;
    file_put_contents($root.'/public/sitemap.xml', $xml);
}

function extractPageMeta(string $file): ?array
{
    $source = file_get_contents($file);
    $marker = '.meta = ';
    $pos = strrpos($source, $marker);
    if ($pos === false) {
        return null;
    }

    $json = trim(substr($source, $pos + strlen($marker)));
    $json = preg_replace('/;\s*$/', '', $json) ?? $json;
    $meta = json_decode($json, true);

    return is_array($meta) ? $meta : null;
}
