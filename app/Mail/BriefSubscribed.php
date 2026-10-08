<?php

namespace App\Mail;

use Illuminate\Bus\Queueable;
use Illuminate\Mail\Mailable;
use Illuminate\Mail\Mailables\Address;
use Illuminate\Mail\Mailables\Content;
use Illuminate\Mail\Mailables\Envelope;
use Illuminate\Queue\SerializesModels;

class BriefSubscribed extends Mailable
{
    use Queueable, SerializesModels;

    public function __construct(public string $subscriberEmail) {}

    public function envelope(): Envelope
    {
        return new Envelope(
            subject: 'New Aryx Brief subscription from '.$this->subscriberEmail,
            replyTo: [
                new Address($this->subscriberEmail),
            ],
        );
    }

    public function content(): Content
    {
        return new Content(
            view: 'emails.notification',
            with: [
                'kicker' => 'The Aryx Brief',
                'headline' => 'A new reader joined the brief.',
                'intro' => 'This address asked to receive The Aryx Brief.',
                'fields' => [
                    'Source' => 'Brief subscription',
                    'Email' => $this->subscriberEmail,
                    'Received' => now()->timezone('Asia/Qatar')->format('d M Y, H:i').' AST',
                ],
                'note' => null,
            ],
        );
    }
}
