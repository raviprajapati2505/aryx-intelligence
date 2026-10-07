<?php

use App\Support\PageSeo;
use Illuminate\Support\Facades\Route;

Route::get('/robots.txt', function () {
    return response(file_get_contents(public_path('robots.txt')), 200, [
        'Content-Type' => 'text/plain; charset=UTF-8',
    ]);
});

Route::get('/sitemap.xml', function () {
    return response(file_get_contents(public_path('sitemap.xml')), 200, [
        'Content-Type' => 'application/xml; charset=UTF-8',
    ]);
});

Route::get('/{any?}', function (?string $any = null) {
    $seo = PageSeo::forRequestPath('/'.ltrim((string) $any, '/'));
    $status = $seo['path'] === null ? 404 : 200;

    return response()->view('app', ['seo' => $seo], $status);
})->where('any', '^(?!up$).*$');
