<?php

namespace Tests\Feature;

use App\Models\Inquiry;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Http\Client\Factory;
use Illuminate\Support\Facades\Http;
use Tests\TestCase;

class AssistantTest extends TestCase
{
    use RefreshDatabase;

    protected function setUp(): void
    {
        parent::setUp();
        config(['services.assistant.key' => null]);
    }

    public function test_known_questions_follow_the_briefing_rules(): void
    {
        $iso = $this->ask('We need ISO 27001 readiness');
        $this->assertStringContainsString('ISO 27001', $iso);
        $this->assertStringNotContainsString('$', $iso);

        $price = $this->ask('How much does a cybersecurity assessment cost?');
        $this->assertStringContainsString('Shall I arrange one?', $price);
        $this->assertDoesNotMatchRegularExpression('/\$\s?\d/', $price);

        $clients = $this->ask('Can you name your clients?');
        $this->assertStringContainsString('do not name clients', strtolower($clients));

        $legal = $this->ask('Is our control set compliant enough for an audit opinion?');
        $this->assertStringContainsString('do not give legal', strtolower($legal));

        $this->assertStringContainsString('PDPPL', $this->ask('How is this chat handled under your privacy notice?'));
        $this->assertStringContainsString('passwords', strtolower($this->ask('Here is my password: hunter2')));
    }

    public function test_off_topic_requests_are_declined(): void
    {
        $reply = $this->ask('Tell me a joke about the weather');

        $this->assertStringContainsString('AI, cybersecurity', $reply);
        $this->assertSame(0, Inquiry::count());
    }

    public function test_arabic_questions_are_answered_in_arabic(): void
    {
        $reply = $this->ask('ما الذي تقدمه آريكس؟', 'ar');

        $this->assertMatchesRegularExpression('/\p{Arabic}/u', $reply);
        $this->assertStringContainsString('الدوحة', $reply);
    }

    public function test_briefing_collects_one_lead(): void
    {
        $history = [];
        $reply = $this->turn($history, 'Book a briefing');
        $this->assertStringContainsString('name and the company you are with', $reply);

        $reply = $this->turn($history, 'Amina Rahman, Gulf National Bank');
        $this->assertStringContainsString('your role, and which work email', $reply);

        $reply = $this->turn($history, 'Chief Risk Officer, amina@gulf.example');
        $this->assertStringContainsString('what should the briefing focus on', $reply);

        $payload = [
            'locale' => 'en',
            'messages' => array_merge($history, [[
                'role' => 'user',
                'content' => 'ISO 27001 readiness before the next board review',
            ]]),
        ];

        $first = $this->postJson('/api/assistant/messages', $payload)->assertOk();
        $this->postJson('/api/assistant/messages', $payload)->assertOk();

        $this->assertStringContainsString('Amina Rahman', $first->json('reply'));
        $this->assertStringContainsString('one business day', $first->json('reply'));
        $this->assertSame(1, Inquiry::count());
        $this->assertDatabaseHas('inquiries', [
            'name' => 'Amina Rahman',
            'title' => 'Chief Risk Officer',
            'organization' => 'Gulf National Bank',
            'email' => 'amina@gulf.example',
            'area' => 'Cybersecurity',
            'consent' => true,
        ]);
    }

    public function test_yes_after_a_price_answer_starts_the_briefing(): void
    {
        $history = [];
        $this->turn($history, 'How much do you charge?');
        $reply = $this->turn($history, 'Yes');

        $this->assertStringContainsString('name and the company you are with', $reply);
    }

    public function test_live_model_is_used_only_when_a_key_is_configured(): void
    {
        config([
            'services.assistant.key' => 'sk-test',
            'services.assistant.url' => 'https://api.openai.com/v1/chat/completions',
            'services.assistant.model' => 'gpt-4o-mini',
        ]);

        Http::fake();
        $this->ask('How much does this cost?');
        Http::assertNothingSent();

        Http::swap(new Factory);
        Http::fake([
            '*' => Http::response([
                'choices' => [[
                    'message' => ['content' => 'Our fee is $5000 and it takes within 6 weeks.'],
                ]],
            ]),
        ]);

        $priced = $this->ask('How should we staff the engagement?');
        $this->assertStringNotContainsString('$5000', $priced);
        $this->assertStringContainsString('Shall I arrange one?', $priced);

        Http::swap(new Factory);
        Http::fake([
            '*' => Http::response([
                'choices' => [[
                    'message' => ['content' => 'Engagements are staffed by senior practitioners and scoped around a decision.'],
                ]],
            ]),
        ]);

        $this->assertSame(
            'Engagements are staffed by senior practitioners and scoped around a decision.',
            $this->ask('How are your teams staffed?'),
        );
    }

    public function test_messages_are_validated(): void
    {
        $this->postJson('/api/assistant/messages', ['messages' => []])
            ->assertStatus(422);

        $this->postJson('/api/assistant/messages', [
            'messages' => [['role' => 'assistant', 'content' => 'Hello']],
        ])->assertStatus(422);
    }

    private function ask(string $text, string $locale = 'en'): string
    {
        return $this->postJson('/api/assistant/messages', [
            'locale' => $locale,
            'messages' => [['role' => 'user', 'content' => $text]],
        ])->assertOk()->json('reply');
    }

    /**
     * @param  array<int, array{role: string, content: string}>  $history
     */
    private function turn(array &$history, string $text): string
    {
        $history[] = ['role' => 'user', 'content' => $text];
        $reply = $this->postJson('/api/assistant/messages', [
            'locale' => 'en',
            'messages' => $history,
        ])->assertOk()->json('reply');
        $history[] = ['role' => 'assistant', 'content' => $reply];

        return $reply;
    }
}
