<?php

namespace Tests\Feature;

use App\Models\BriefSubscription;
use App\Models\Inquiry;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class ContactApiTest extends TestCase
{
    use RefreshDatabase;

    public function test_inquiry_is_stored(): void
    {
        $response = $this->postJson('/api/inquiries', [
            'name' => 'Amina Rahman',
            'title' => 'Chief Risk Officer',
            'organization' => 'Gulf National Bank',
            'email' => 'amina@example.com',
            'country' => 'Qatar',
            'area' => 'Cybersecurity',
            'message' => 'We need a clearer view of cyber exposure before the next board meeting.',
            'consent' => true,
        ]);

        $response->assertOk()->assertJsonPath('message', 'Received. Aryx will follow up on this conversation.');
        $this->assertDatabaseHas('inquiries', [
            'email' => 'amina@example.com',
            'organization' => 'Gulf National Bank',
        ]);
        $this->assertSame(1, Inquiry::count());
    }

    public function test_honeypot_inquiry_is_not_stored(): void
    {
        $this->postJson('/api/inquiries', [
            'name' => 'Bot',
            'organization' => 'Spam Co',
            'email' => 'bot@example.com',
            'message' => 'This is an automated message that should be dropped.',
            'consent' => true,
            'company' => 'filled-by-bot',
        ])->assertOk();

        $this->assertSame(0, Inquiry::count());
    }

    public function test_brief_subscription_is_stored_once(): void
    {
        $payload = ['email' => 'Leader@Example.com'];

        $this->postJson('/api/brief-subscriptions', $payload)->assertOk();
        $this->postJson('/api/brief-subscriptions', $payload)->assertOk();

        $this->assertSame(1, BriefSubscription::count());
        $this->assertDatabaseHas('brief_subscriptions', ['email' => 'leader@example.com']);
    }
}
