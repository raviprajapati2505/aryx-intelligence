<?php

namespace Tests\Feature;

use App\Mail\BriefSubscribed;
use App\Mail\InquiryReceived;
use App\Models\BriefSubscription;
use App\Models\Inquiry;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\Mail;
use Tests\TestCase;

class ContactApiTest extends TestCase
{
    use RefreshDatabase;

    protected function setUp(): void
    {
        parent::setUp();

        config([
            'services.brevo.key' => 'test-key',
            'services.contact.email' => 'anjumarshad07@gmail.com',
        ]);

        Mail::fake();
    }

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
        Mail::assertSent(InquiryReceived::class, function (InquiryReceived $mail) {
            return $mail->hasTo('anjumarshad07@gmail.com')
                && $mail->source === 'Contact form'
                && $mail->inquiry->email === 'amina@example.com'
                && str_contains($mail->render(), 'Gulf National Bank')
                && str_contains($mail->render(), 'Cybersecurity')
                && str_contains($mail->render(), 'board meeting');
        });
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
        Mail::assertNothingSent();
    }

    public function test_brief_subscription_is_stored_once(): void
    {
        $payload = ['email' => 'Leader@Example.com'];

        $this->postJson('/api/brief-subscriptions', $payload)->assertOk();
        $this->postJson('/api/brief-subscriptions', $payload)->assertOk();

        $this->assertSame(1, BriefSubscription::count());
        $this->assertDatabaseHas('brief_subscriptions', ['email' => 'leader@example.com']);
        Mail::assertSent(BriefSubscribed::class, 2);
        Mail::assertSent(BriefSubscribed::class, function (BriefSubscribed $mail) {
            return $mail->hasTo('anjumarshad07@gmail.com')
                && $mail->subscriberEmail === 'leader@example.com';
        });
    }

    public function test_mail_is_skipped_when_brevo_is_not_configured(): void
    {
        config(['services.brevo.key' => null]);

        $this->postJson('/api/inquiries', [
            'name' => 'Amina Rahman',
            'organization' => 'Gulf National Bank',
            'email' => 'amina@example.com',
            'message' => 'We need a clearer view of cyber exposure before the next board meeting.',
            'consent' => true,
        ])->assertOk();

        Mail::assertNothingSent();
    }
}
