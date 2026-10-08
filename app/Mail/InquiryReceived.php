<?php

namespace App\Mail;

use App\Models\Inquiry;
use Illuminate\Bus\Queueable;
use Illuminate\Mail\Mailable;
use Illuminate\Mail\Mailables\Address;
use Illuminate\Mail\Mailables\Content;
use Illuminate\Mail\Mailables\Envelope;
use Illuminate\Queue\SerializesModels;

class InquiryReceived extends Mailable
{
    use Queueable, SerializesModels;

    public function __construct(
        public Inquiry $inquiry,
        public string $source,
    ) {}

    public function envelope(): Envelope
    {
        return new Envelope(
            subject: sprintf('New inquiry from %s, %s', $this->inquiry->name, $this->inquiry->organization),
            replyTo: [
                new Address($this->inquiry->email, $this->inquiry->name),
            ],
        );
    }

    public function content(): Content
    {
        $fields = array_filter([
            'Source' => $this->source,
            'Name' => $this->inquiry->name,
            'Title' => $this->inquiry->title,
            'Organization' => $this->inquiry->organization,
            'Email' => $this->inquiry->email,
            'Country' => $this->inquiry->country,
            'Area of interest' => $this->inquiry->area,
            'Received' => now()->timezone('Asia/Qatar')->format('d M Y, H:i').' AST',
        ], fn ($value) => filled($value));

        return new Content(
            view: 'emails.notification',
            with: [
                'kicker' => $this->source,
                'headline' => 'A new conversation is waiting.',
                'intro' => 'Someone shared a decision they want to make clearer. Reply to this email to reach them directly.',
                'fields' => $fields,
                'note' => $this->inquiry->message,
            ],
        );
    }
}
