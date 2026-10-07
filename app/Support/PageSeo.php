<?php

namespace App\Support;

class PageSeo
{
    public static function forRequestPath(string $path): array
    {
        $path = self::normalize($path);
        foreach (self::pages() as $page) {
            if ($page['path'] === $path) {
                $page['robots'] = 'index, follow';

                return $page;
            }
        }

        return self::notFound();
    }

    public static function notFound(): array
    {
        return [
            'path' => null,
            'title' => 'Page not available | Aryx Intelligence',
            'description' => 'This address does not match a page on the Aryx Intelligence site.',
            'canonical' => 'https://aryxintelligence.com/',
            'jsonLd' => [],
            'robots' => 'noindex, follow',
        ];
    }

    public static function pages(): array
    {
        $path = resource_path('seo/pages.json');
        if (! is_file($path)) {
            return [];
        }

        $pages = json_decode((string) file_get_contents($path), true);

        return is_array($pages) ? $pages : [];
    }

    public static function normalize(string $path): string
    {
        $path = '/'.trim($path, '/');

        return $path === '/' ? '/' : rtrim($path, '/');
    }
}
