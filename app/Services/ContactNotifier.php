<?php

namespace App\Services;

use App\Mail\BriefSubscribed;
use App\Mail\InquiryReceived;
use App\Models\Inquiry;
use Illuminate\Mail\Mailable;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\Mail;
use Throwable;

class ContactNotifier
{
    public function inquiry(Inquiry $inquiry, string $source): void
    {
        $this->send(new InquiryReceived($inquiry, $source));
    }

    public function subscription(string $email): void
    {
        $this->send(new BriefSubscribed($email));
    }

    private function send(Mailable $mailable): void
    {
        $to = trim((string) config('services.contact.email', ''));
        $key = trim((string) config('services.brevo.key', ''));

        if ($to === '' || $key === '') {
            return;
        }

        try {
            Mail::mailer('brevo')->to($to)->send($mailable);
        } catch (Throwable $exception) {
            Log::error('Contact mail failed.', [
                'message' => $exception->getMessage(),
            ]);
        }
    }
}
