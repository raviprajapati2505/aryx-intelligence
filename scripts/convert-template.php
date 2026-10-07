<?php

/**
 * Converts final-template/*.html into React page components.
 * Markup, class names, and copy are preserved. Shared chrome is omitted
 * because the React layout renders it once.
 */

$root = dirname(__DIR__);
$source = $root.'/final-template';
$outDir = $root.'/resources/js/pages';

if (! is_dir($outDir) && ! mkdir($outDir, 0777, true) && ! is_dir($outDir)) {
    fwrite(STDERR, "Cannot create {$outDir}\n");
    exit(1);
}

$files = glob($source.'/*.html');
sort($files);

$pages = [];

foreach ($files as $file) {
    $html = file_get_contents($file);
    $slug = basename($file, '.html');
    $component = componentName($slug);
    $path = pagePath($slug);

    if (! preg_match('/<title>(.*?)<\/title>/s', $html, $titleMatch)) {
        fwrite(STDERR, "No title in {$slug}\n");
        exit(1);
    }

    $description = '';
    if (preg_match('/<meta name="description" content="([^"]*)"/', $html, $descMatch)) {
        $description = html_entity_decode($descMatch[1], ENT_QUOTES | ENT_HTML5, 'UTF-8');
    }

    $canonical = '';
    if (preg_match('/<link rel="canonical" href="([^"]*)"/', $html, $canonMatch)) {
        $canonical = rewriteInsightArticleUrl(html_entity_decode($canonMatch[1], ENT_QUOTES | ENT_HTML5, 'UTF-8'));
    }

    $scene = null;
    $pathIndex = null;
    if (preg_match('/<body\b([^>]*)>/', $html, $bodyMatch)) {
        if (preg_match('/\bdata-scene="([^"]*)"/', $bodyMatch[1], $sceneMatch)) {
            $scene = $sceneMatch[1];
        }
        if (preg_match('/\bdata-path="([^"]*)"/', $bodyMatch[1], $pathMatch)) {
            $pathIndex = $pathMatch[1];
        }
    }
    if ($scene === null && preg_match('/dataset\.scene\s*=\s*"([^"]+)"/', $html, $sceneMatch)) {
        $scene = $sceneMatch[1];
    }

    $jsonLd = [];
    if (preg_match_all('/<script type="application\/ld\+json">(.*?)<\/script>/s', $html, $ldMatches)) {
        foreach ($ldMatches[1] as $raw) {
            $decoded = json_decode(trim($raw), true);
            $jsonLd[] = rewriteInsightArticleUrl($decoded ?? trim($raw));
        }
    }

    if (! preg_match('/<main\b[^>]*>.*<\/main>/s', $html, $mainMatch)) {
        fwrite(STDERR, "No main in {$slug}\n");
        exit(1);
    }

    $usesLink = false;
    $jsx = htmlToJsx($mainMatch[0], $usesLink);
    $openLinks = preg_match_all('/<Link\b/', $jsx);
    $closeLinks = preg_match_all('/<\/Link>/', $jsx);
    if ($openLinks !== $closeLinks) {
        fwrite(STDERR, "Link tags do not balance in {$slug}: {$openLinks} open, {$closeLinks} close\n");
        exit(1);
    }

    $meta = [
        'path' => $path,
        'title' => html_entity_decode(trim($titleMatch[1]), ENT_QUOTES | ENT_HTML5, 'UTF-8'),
        'description' => $description,
        'canonical' => $canonical,
        'scene' => $scene,
        'pathIndex' => $pathIndex,
        'jsonLd' => $jsonLd,
    ];

    $import = $usesLink ? "import { Link } from 'react-router-dom';\n\n" : '';
    $metaJson = json_encode($meta, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);

    $contents = <<<JSX
{$import}export default function {$component}() {
  return (
    {$jsx}
  );
}

{$component}.meta = {$metaJson};

JSX;

    file_put_contents($outDir.'/'.$component.'.jsx', $contents);
    $pages[] = [
        'path' => $path,
        'component' => $component,
        'scene' => $scene,
        'pathIndex' => $pathIndex,
    ];
    echo $component.' '.$path.' scene='.($scene ?? '-').' pathIndex='.($pathIndex ?? '-').PHP_EOL;
}

$imports = '';
$entries = '';
foreach ($pages as $page) {
    $imports .= "import {$page['component']} from './{$page['component']}';\n";
    $entries .= "  { path: ".json_encode($page['path']).", Component: {$page['component']}, meta: {$page['component']}.meta },\n";
}

$index = $imports."\nexport const pages = [\n".$entries."];\n";
file_put_contents($outDir.'/index.js', $index);
echo "Wrote ".count($pages)." pages\n";
require_once __DIR__.'/export-seo.php';
exportSeoArtifacts($root);
echo "Wrote SEO files\n";

function componentName(string $slug): string
{
    if ($slug === 'index') {
        return 'HomePage';
    }

    $parts = preg_split('/[^a-z0-9]+/i', $slug, -1, PREG_SPLIT_NO_EMPTY);

    return implode('', array_map(static fn ($part) => ucfirst($part), $parts)).'Page';
}

function htmlToJsx(string $html, bool &$usesLink): string
{
    $out = '';
    $i = 0;
    $n = strlen($html);
    $anchorStack = [];

    while ($i < $n) {
        $lt = strpos($html, '<', $i);
        if ($lt === false) {
            $out .= jsxText(substr($html, $i));
            break;
        }
        if ($lt > $i) {
            $out .= jsxText(substr($html, $i, $lt - $i));
        }
        if (substr($html, $lt, 4) === '<!--') {
            $end = strpos($html, '-->', $lt);
            $end = $end === false ? $n : $end + 3;
            $comment = substr($html, $lt + 4, $end - $lt - 7);
            $comment = str_replace('*/', '* /', $comment);
            $out .= '{/*'.$comment.'*/}';
            $i = $end;
            continue;
        }

        $end = tagEnd($html, $lt);
        $tag = substr($html, $lt, $end - $lt);
        $out .= convertTag($tag, $usesLink, $anchorStack);
        $i = $end;
    }

    return $out;
}

function tagEnd(string $html, int $start): int
{
    $n = strlen($html);
    $quote = null;
    for ($j = $start + 1; $j < $n; $j++) {
        $char = $html[$j];
        if ($quote) {
            if ($char === $quote) {
                $quote = null;
            }
            continue;
        }
        if ($char === '"' || $char === "'") {
            $quote = $char;
            continue;
        }
        if ($char === '>') {
            return $j + 1;
        }
    }

    return $n;
}

function convertTag(string $tag, bool &$usesLink, array &$anchorStack): string
{
    if (! preg_match('/^<\s*(\/?)\s*([a-zA-Z][\w:-]*)\s*([\s\S]*?)(\/?)\s*>$/', $tag, $match)) {
        return $tag;
    }

    $closing = $match[1] === '/';
    $name = $match[2];
    $raw = $match[3];
    $self = $match[4] === '/';

    if ($closing) {
        if (strtolower($name) === 'a') {
            $wasLink = array_pop($anchorStack);

            return $wasLink ? '</Link>' : '</a>';
        }

        return '</'.$name.'>';
    }

    $attrs = parseAttrs($raw);
    $isLink = false;
    $rendered = [];

    foreach ($attrs as [$attr, $value]) {
        $lower = strtolower($attr);
        if ($name === 'a' && $lower === 'href' && $value !== null && isInternalPage($value)) {
            $isLink = true;
            $usesLink = true;
            $rendered[] = 'to={'.json_encode(rewriteUrl($value), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES).'}';
            continue;
        }

        $jsxName = jsxAttrName($attr);
        if ($value === null || isBooleanAttr($jsxName, $value)) {
            $rendered[] = $jsxName;
            continue;
        }

        $decoded = html_entity_decode($value, ENT_QUOTES | ENT_HTML5, 'UTF-8');
        if (in_array($lower, ['href', 'src', 'poster', 'action'], true)) {
            $decoded = rewriteUrl($decoded);
        }
        if ($lower === 'style') {
            $rendered[] = 'style='.styleToJsx($decoded);
            continue;
        }

        $rendered[] = $jsxName.'={'.json_encode($decoded, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES).'}';
    }

    if (strtolower($name) === 'a' && ! $self) {
        $anchorStack[] = $isLink;
    }

    $tagName = $isLink ? 'Link' : $name;
    $void = ['area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'];
    $attrText = $rendered ? ' '.implode(' ', $rendered) : '';
    if ($self || in_array(strtolower($name), $void, true)) {
        return '<'.$tagName.$attrText.' />';
    }

    return '<'.$tagName.$attrText.'>';
}

function parseAttrs(string $raw): array
{
    $attrs = [];
    $length = strlen($raw);
    $i = 0;

    while ($i < $length) {
        while ($i < $length && ctype_space($raw[$i])) {
            $i++;
        }
        if ($i >= $length) {
            break;
        }
        $start = $i;
        while ($i < $length && ! ctype_space($raw[$i]) && $raw[$i] !== '=') {
            $i++;
        }
        $name = substr($raw, $start, $i - $start);
        if ($name === '' || $name === '/') {
            break;
        }
        while ($i < $length && ctype_space($raw[$i])) {
            $i++;
        }
        $value = null;
        if ($i < $length && $raw[$i] === '=') {
            $i++;
            while ($i < $length && ctype_space($raw[$i])) {
                $i++;
            }
            if ($i < $length && ($raw[$i] === '"' || $raw[$i] === "'")) {
                $quote = $raw[$i];
                $i++;
                $start = $i;
                while ($i < $length && $raw[$i] !== $quote) {
                    $i++;
                }
                $value = substr($raw, $start, $i - $start);
                if ($i < $length) {
                    $i++;
                }
            } else {
                $start = $i;
                while ($i < $length && ! ctype_space($raw[$i]) && $raw[$i] !== '>') {
                    $i++;
                }
                $value = substr($raw, $start, $i - $start);
            }
        }
        $attrs[] = [$name, $value];
    }

    return $attrs;
}

function jsxAttrName(string $name): string
{
    $map = [
        'class' => 'className',
        'for' => 'htmlFor',
        'tabindex' => 'tabIndex',
        'autocomplete' => 'autoComplete',
        'novalidate' => 'noValidate',
        'maxlength' => 'maxLength',
        'minlength' => 'minLength',
        'readonly' => 'readOnly',
        'autofocus' => 'autoFocus',
        'colspan' => 'colSpan',
        'rowspan' => 'rowSpan',
        'srcset' => 'srcSet',
        'usemap' => 'useMap',
        'accept-charset' => 'acceptCharset',
        'crossorigin' => 'crossOrigin',
        'autoplay' => 'autoPlay',
        'playsinline' => 'playsInline',
        'stroke-width' => 'strokeWidth',
        'stroke-linecap' => 'strokeLinecap',
        'stroke-linejoin' => 'strokeLinejoin',
        'stroke-dasharray' => 'strokeDasharray',
        'stroke-dashoffset' => 'strokeDashoffset',
        'stroke-miterlimit' => 'strokeMiterlimit',
        'fill-rule' => 'fillRule',
        'clip-rule' => 'clipRule',
        'clip-path' => 'clipPath',
        'font-family' => 'fontFamily',
        'font-size' => 'fontSize',
        'text-anchor' => 'textAnchor',
        'dominant-baseline' => 'dominantBaseline',
        'stop-color' => 'stopColor',
        'stop-opacity' => 'stopOpacity',
        'fill-opacity' => 'fillOpacity',
        'stroke-opacity' => 'strokeOpacity',
        'xlink:href' => 'href',
        'viewbox' => 'viewBox',
    ];

    $lower = strtolower($name);
    if (isset($map[$lower])) {
        return $map[$lower];
    }
    if (str_starts_with($lower, 'data-') || str_starts_with($lower, 'aria-')) {
        return $lower;
    }
    if (str_contains($name, '-')) {
        return preg_replace_callback('/-([a-z])/i', static fn ($m) => strtoupper($m[1]), $lower);
    }

    return $name;
}

function isBooleanAttr(string $name, ?string $value): bool
{
    $booleans = [
        'hidden', 'required', 'checked', 'disabled', 'selected', 'multiple', 'readOnly',
        'autoFocus', 'noValidate', 'open', 'muted', 'loop', 'autoPlay', 'playsInline',
        'defer', 'async', 'default', 'reversed', 'allowFullScreen', 'formNoValidate',
    ];
    if (! in_array($name, $booleans, true)) {
        return false;
    }

    return $value === null || $value === '' || strtolower((string) $value) === strtolower($name) || $value === 'true';
}

function isInternalPage(string $url): bool
{
    if (preg_match('#^(https?:|mailto:|tel:)#i', $url)) {
        return false;
    }
    if (str_starts_with($url, '#')) {
        return false;
    }
    if (str_starts_with($url, 'assets/') || str_starts_with($url, '/assets/')) {
        return false;
    }

    return true;
}

function rewriteUrl(string $url): string
{
    if (preg_match('#^(https?:|mailto:|tel:)#i', $url)) {
        return $url;
    }
    if (str_starts_with($url, '#')) {
        return $url;
    }
    if (str_starts_with($url, 'assets/')) {
        return '/'.$url;
    }
    if (str_starts_with($url, '/assets/')) {
        return $url;
    }

    $hash = '';
    if (str_contains($url, '#')) {
        [$url, $hashPart] = explode('#', $url, 2);
        $hash = '#'.$hashPart;
    }
    $url = preg_replace('/\.html$/', '', $url) ?? $url;
    if ($url === '' || $url === 'index') {
        return '/'.$hash;
    }
    if (str_starts_with($url, '/')) {
        return pagePath(ltrim($url, '/')).$hash;
    }

    return pagePath($url).$hash;
}

function pagePath(string $slug): string
{
    if ($slug === '' || $slug === 'index') {
        return '/';
    }
    if (str_starts_with($slug, 'insights-')) {
        return '/insights/'.substr($slug, strlen('insights-'));
    }

    return '/'.$slug;
}

function rewriteInsightArticleUrl(mixed $value): mixed
{
    if (is_array($value)) {
        foreach ($value as $key => $item) {
            $value[$key] = rewriteInsightArticleUrl($item);
        }

        return $value;
    }
    if (! is_string($value)) {
        return $value;
    }

    return preg_replace('#(?<=^|/)insights-(?=[a-z])#', 'insights/', $value) ?? $value;
}

function styleToJsx(string $css): string
{
    $parts = [];
    foreach (explode(';', $css) as $decl) {
        if (! str_contains($decl, ':')) {
            continue;
        }
        [$prop, $val] = explode(':', $decl, 2);
        $prop = trim($prop);
        $val = trim($val);
        if ($prop === '' || $val === '') {
            continue;
        }
        if (str_starts_with($prop, '--')) {
            $key = json_encode($prop);
        } else {
            $key = preg_replace_callback('/-([a-z])/i', static fn ($m) => strtoupper($m[1]), $prop);
            if (preg_match('/^(webkit|moz|ms)/', $key)) {
                $key = ucfirst($key);
            }
        }
        $parts[] = $key.': '.json_encode($val, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    }

    return '{{'.implode(', ', $parts).'}}';
}

function jsxText(string $text): string
{
    $text = html_entity_decode($text, ENT_QUOTES | ENT_HTML5, 'UTF-8');
    $out = '';
    $length = strlen($text);
    for ($i = 0; $i < $length; $i++) {
        $char = $text[$i];
        if ($char === '{') {
            $out .= "{'{'}";
        } elseif ($char === '}') {
            $out .= "{'}'}";
        } elseif ($char === '<') {
            $out .= '&lt;';
        } else {
            $out .= $char;
        }
    }

    return $out;
}
