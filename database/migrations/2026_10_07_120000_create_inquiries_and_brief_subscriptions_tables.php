<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('inquiries', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('title')->nullable();
            $table->string('organization');
            $table->string('email');
            $table->string('country')->nullable();
            $table->string('area')->nullable();
            $table->text('message');
            $table->boolean('consent')->default(false);
            $table->timestamps();
        });

        Schema::create('brief_subscriptions', function (Blueprint $table) {
            $table->id();
            $table->string('email')->unique();
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('brief_subscriptions');
        Schema::dropIfExists('inquiries');
    }
};
