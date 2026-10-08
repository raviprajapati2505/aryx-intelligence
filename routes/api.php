<?php

use App\Http\Controllers\AssistantController;
use App\Http\Controllers\ContactController;
use Illuminate\Support\Facades\Route;

Route::post('/assistant/messages', AssistantController::class)->middleware('throttle:30,1');
Route::post('/inquiries', [ContactController::class, 'store'])->middleware('throttle:30,1');
Route::post('/brief-subscriptions', [ContactController::class, 'subscribe'])->middleware('throttle:30,1');
