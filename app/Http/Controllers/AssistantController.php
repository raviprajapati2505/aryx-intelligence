<?php

namespace App\Http\Controllers;

use App\Support\Assistant;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class AssistantController extends Controller
{
    public function __invoke(Request $request, Assistant $assistant): JsonResponse
    {
        $data = $request->validate([
            'locale' => ['nullable', 'in:en,ar'],
            'messages' => ['required', 'array', 'min:1', 'max:24'],
            'messages.*.role' => ['required', 'in:user,assistant'],
            'messages.*.content' => ['required', 'string', 'max:2000'],
        ]);

        $messages = array_map(function (array $message): array {
            $content = trim(strip_tags($message['content']));
            $content = preg_replace("/[ \t]+/u", ' ', $content) ?? $content;

            return [
                'role' => $message['role'],
                'content' => $content,
            ];
        }, $data['messages']);

        $last = $messages[array_key_last($messages)];
        if ($last['role'] !== 'user' || $last['content'] === '') {
            return response()->json([
                'message' => 'Send a visitor message to continue.',
            ], 422);
        }

        $result = $assistant->respond($messages, $data['locale'] ?? 'en');

        return response()->json([
            'reply' => $result['reply'],
        ]);
    }
}
