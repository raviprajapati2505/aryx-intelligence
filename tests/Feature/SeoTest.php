<?php

namespace Tests\Feature;

use Tests\TestCase;

class SeoTest extends TestCase
{
    public function test_homepage_html_includes_its_own_title_and_description(): void
    {
        $response = $this->get('/');

        $response->assertOk();
        $response->assertSee('<title>Aryx Intelligence</title>', false);
        $response->assertSee('name="description"', false);
        $response->assertSee('rel="canonical" href="https://aryxintelligence.com/"', false);
        $response->assertSee('name="robots" content="index, follow"', false);
        $response->assertSee('application/ld+json', false);
    }

    public function test_insight_article_html_uses_the_article_title(): void
    {
        $response = $this->get('/insights/ai-governance-for-boards');

        $response->assertOk();
        $response->assertSee('<title>AI Governance for Boards: What Directors Must Ask | Aryx</title>', false);
        $response->assertSee('rel="canonical" href="https://aryxintelligence.com/insights/ai-governance-for-boards"', false);
    }

    public function test_unknown_pages_are_not_indexable(): void
    {
        $this->get('/this-page-does-not-exist')
            ->assertNotFound()
            ->assertSee('name="robots" content="noindex, follow"', false);
    }

    public function test_robots_txt_allows_google_to_crawl(): void
    {
        $response = $this->get('/robots.txt');

        $response->assertOk();
        $response->assertHeader('content-type', 'text/plain; charset=UTF-8');
        $this->assertStringContainsString('User-agent: Googlebot', $response->getContent());
        $this->assertStringContainsString('Allow: /', $response->getContent());
        $this->assertStringNotContainsString('Disallow', $response->getContent());
        $this->assertStringContainsString('Sitemap: https://aryxintelligence.com/sitemap.xml', $response->getContent());
    }

    public function test_sitemap_lists_public_pages(): void
    {
        $response = $this->get('/sitemap.xml');

        $response->assertOk();
        $response->assertSee('https://aryxintelligence.com/', false);
        $response->assertSee('https://aryxintelligence.com/insights/ai-governance-for-boards', false);
        $response->assertSee('https://aryxintelligence.com/enterprise-ai', false);
    }
}
