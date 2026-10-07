<?php

namespace App\Http\Controllers;

use App\Models\BriefSubscription;
use App\Models\Inquiry;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Validation\Rule;

class ContactController extends Controller
{
    public function store(Request $request): JsonResponse
    {
        $data = $request->validate([
            'name' => ['required', 'string', 'max:120'],
            'title' => ['nullable', 'string', 'max:120'],
            'organization' => ['required', 'string', 'max:160'],
            'email' => ['required', 'email', 'max:180'],
            'country' => ['nullable', 'string', 'max:120'],
            'area' => ['nullable', 'string', Rule::in([
                'Enterprise AI',
                'Cybersecurity',
                'Risk & Decision Intelligence',
                'Climate Intelligence',
                'Digital & Technology Transformation',
                'Other',
            ])],
            'message' => ['required', 'string', 'min:10', 'max:5000'],
            'consent' => ['accepted'],
            'company' => ['nullable', 'string', 'max:200'],
        ]);

        if (! empty($data['company'])) {
            return response()->json([
                'message' => 'Received. Aryx will follow up on this conversation.',
            ]);
        }

        Inquiry::create([
            'name' => $data['name'],
            'title' => $data['title'] ?? null,
            'organization' => $data['organization'],
            'email' => $data['email'],
            'country' => $data['country'] ?? null,
            'area' => $data['area'] ?? null,
            'message' => $data['message'],
            'consent' => true,
        ]);

        return response()->json([
            'message' => 'Received. Aryx will follow up on this conversation.',
        ]);
    }

    public function subscribe(Request $request): JsonResponse
    {
        $data = $request->validate([
            'email' => ['required', 'email', 'max:180'],
        ]);

        BriefSubscription::firstOrCreate([
            'email' => strtolower($data['email']),
        ]);

        return response()->json([
            'message' => 'You are on the list for The Aryx Brief.',
        ]);
    }
}
