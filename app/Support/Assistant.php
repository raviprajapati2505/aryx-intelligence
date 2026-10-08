<?php

namespace App\Support;

use App\Models\Inquiry;
use App\Services\ContactNotifier;
use Illuminate\Support\Facades\Http;
use Throwable;

class Assistant
{
    public function __construct(private ContactNotifier $mailer) {}

    /**
     * @param  array<int, array{role: string, content: string}>  $messages
     * @return array{reply: string}
     */
    public function respond(array $messages, string $locale = 'en'): array
    {
        $user = $this->latestUser($messages);
        $previous = $this->previousAssistant($messages);
        $arabic = $this->isArabic($user) || ($locale === 'ar' && ! preg_match('/[A-Za-z]/', $user));
        $stage = $this->stage($previous);

        if ($this->isSensitive($user)) {
            return $this->done($this->line('sensitive', $arabic), $stage, $arabic);
        }

        if ($this->isLeak($user)) {
            return $this->done($this->line('leak', $arabic), $stage, $arabic);
        }

        if ($stage === 'identity' && $this->parseIdentity($user)) {
            return ['reply' => $this->line('ask_role', $arabic)];
        }

        if ($stage === 'role' && $this->hasEmail($user)) {
            if ($this->parseRole($user) === null) {
                return ['reply' => $this->line('ask_role_again', $arabic)];
            }

            return ['reply' => $this->line('ask_need', $arabic)];
        }

        if ($stage === 'need' && $this->isNeed($user)) {
            return ['reply' => $this->confirm($messages, $user, $arabic)];
        }

        if ($this->isPrice($user)) {
            return $this->done($this->line('price', $arabic), $stage, $arabic);
        }

        if ($this->isLegal($user)) {
            return $this->done($this->line('legal', $arabic), $stage, $arabic);
        }

        if ($this->isClients($user)) {
            return $this->done($this->line('clients', $arabic), $stage, $arabic);
        }

        if ($this->isPrivacy($user)) {
            return $this->done($this->line('privacy', $arabic), $stage, $arabic);
        }

        if ($this->isOffTopic($user)) {
            return $this->done($this->line('offtopic', $arabic), $stage, $arabic);
        }

        if (! $stage && $this->isAffirmative($user) && $this->offeredBriefing($previous)) {
            return ['reply' => $this->line('ask_identity', $arabic)];
        }

        if ($this->isBooking($user)) {
            if ($stage) {
                return ['reply' => $this->question($stage, $arabic)];
            }

            return ['reply' => $this->line('ask_identity', $arabic)];
        }

        if ($this->isThanks($user) && $previous && (str_contains($previous, 'one business day') || str_contains($previous, 'يوم عمل واحد'))) {
            return ['reply' => $this->line('thanks', $arabic)];
        }

        $topic = $this->topic($user, $arabic);
        if ($topic !== null) {
            return $this->done($topic, $stage, $arabic);
        }

        $generated = $this->generate($messages, $locale, $arabic);
        if ($generated !== null) {
            return $this->done($generated, $stage, $arabic);
        }

        return $this->done($this->line('default', $arabic), $stage, $arabic);
    }

    /**
     * @param  array<int, array{role: string, content: string}>  $messages
     */
    private function confirm(array $messages, string $need, bool $arabic): string
    {
        $lead = $this->collected($messages);
        if (! $lead) {
            return $this->line('ask_identity', $arabic);
        }

        $need = trim(preg_replace('/\s+/u', ' ', $need) ?? $need);

        $exists = Inquiry::query()
            ->where('email', $lead['email'])
            ->where('message', $need)
            ->exists();

        if (! $exists) {
            $inquiry = Inquiry::create([
                'name' => $lead['name'],
                'title' => $lead['role'],
                'organization' => $lead['organization'],
                'email' => $lead['email'],
                'area' => $this->area($messages, $need),
                'message' => $need,
                'consent' => true,
            ]);

            $this->mailer->inquiry($inquiry, 'Website assistant');
        }

        return str_replace(
            ['{name}', '{role}', '{company}', '{email}', '{need}'],
            [$lead['name'], $lead['role'], $lead['organization'], $lead['email'], $need],
            $this->line('confirm', $arabic),
        );
    }

    /**
     * @param  array<int, array{role: string, content: string}>  $messages
     * @return array{name: string, organization: string, role: string, email: string}|null
     */
    private function collected(array $messages): ?array
    {
        $name = $organization = $role = $email = null;
        $stage = null;

        foreach ($messages as $message) {
            if ($message['role'] === 'assistant') {
                $stage = $this->stage($message['content']);

                continue;
            }

            if ($stage === 'identity' && ($parsed = $this->parseIdentity($message['content']))) {
                $name = $parsed['name'];
                $organization = $parsed['organization'];
            }

            if ($stage === 'role' && ($parsed = $this->parseRole($message['content']))) {
                $role = $parsed['role'];
                $email = $parsed['email'];
            }
        }

        if (! $name || ! $organization || ! $role || ! $email) {
            return null;
        }

        return compact('name', 'organization', 'role', 'email');
    }

    /**
     * @param  array<int, array{role: string, content: string}>  $messages
     */
    private function area(array $messages, string $need): ?string
    {
        $chunks = [$need];
        foreach ($messages as $message) {
            if ($message['role'] === 'user') {
                $chunks[] = $message['content'];
            }
        }

        foreach (array_reverse($chunks) as $text) {
            $haystack = mb_strtolower($text);
            if (preg_match('/iso|27001|cyber|أمن سيبر/u', $haystack)) {
                return 'Cybersecurity';
            }
            if (preg_match('/esg|ghg|pcaf|climate|انبعاث|المناخ/u', $haystack)) {
                return 'Climate Intelligence';
            }
            if (preg_match('/\bai\b|artificial intelligence|الذكاء الاصطناعي/u', $haystack)) {
                return 'Enterprise AI';
            }
            if (preg_match('/grc|internal audit|التدقيق|المخاطر/u', $haystack)) {
                return 'Risk & Decision Intelligence';
            }
            if (preg_match('/digital transformation|التحول الرقمي/u', $haystack)) {
                return 'Digital & Technology Transformation';
            }
        }

        return null;
    }

    /**
     * @param  array<int, array{role: string, content: string}>  $messages
     */
    private function generate(array $messages, string $locale, bool $arabic): ?string
    {
        $key = config('services.assistant.key');
        if (! is_string($key) || $key === '') {
            return null;
        }

        $turns = [];
        foreach (array_slice($messages, -16) as $message) {
            $turns[] = [
                'role' => $message['role'] === 'assistant' ? 'assistant' : 'user',
                'content' => $message['content'],
            ];
        }

        try {
            $response = Http::withToken($key)
                ->acceptJson()
                ->timeout(20)
                ->post((string) config('services.assistant.url'), [
                    'model' => config('services.assistant.model'),
                    'temperature' => 0.2,
                    'max_tokens' => 220,
                    'messages' => array_merge(
                        [['role' => 'system', 'content' => AssistantPrompt::text($locale)]],
                        $turns,
                    ),
                ]);
        } catch (Throwable) {
            return null;
        }

        if (! $response->successful()) {
            return null;
        }

        $text = trim((string) $response->json('choices.0.message.content'));
        if ($text === '') {
            return null;
        }

        return $this->scrub($text, $arabic);
    }

    private function scrub(string $reply, bool $arabic): string
    {
        $priced = preg_match('/(\$|£|€)\s?\d|\b\d[\d,.]*\s?(QAR|USD|EUR|GBP)\b|\b(our|the)\s+(fee|price|cost)\s+(is|would be)\b/i', $reply);
        $timed = preg_match('/\b(in|within|about|around|approximately)\s+\d+\s+(business\s+)?(day|week|month)s?\b|\btimeline is\b/i', $reply);

        if ($priced || $timed) {
            return $this->line('price', $arabic);
        }

        return $reply;
    }

    private function done(string $reply, ?string $stage, bool $arabic): array
    {
        if ($stage && ! str_contains($reply, $this->marker($stage, $arabic))) {
            $reply .= "\n\n".$this->question($stage, $arabic);
        }

        return ['reply' => $reply];
    }

    /**
     * @param  array<int, array{role: string, content: string}>  $messages
     */
    private function latestUser(array $messages): string
    {
        for ($i = count($messages) - 1; $i >= 0; $i--) {
            if ($messages[$i]['role'] === 'user') {
                return trim($messages[$i]['content']);
            }
        }

        return '';
    }

    /**
     * @param  array<int, array{role: string, content: string}>  $messages
     */
    private function previousAssistant(array $messages): string
    {
        $seenUser = false;
        for ($i = count($messages) - 1; $i >= 0; $i--) {
            if ($messages[$i]['role'] === 'user' && ! $seenUser) {
                $seenUser = true;

                continue;
            }
            if ($seenUser && $messages[$i]['role'] === 'assistant') {
                return $messages[$i]['content'];
            }
        }

        return '';
    }

    private function stage(string $assistant): ?string
    {
        foreach (['need', 'role', 'identity'] as $stage) {
            if (str_contains($assistant, $this->marker($stage, false)) || str_contains($assistant, $this->marker($stage, true))) {
                return $stage;
            }
        }

        return null;
    }

    private function marker(string $stage, bool $arabic): string
    {
        return match ($stage) {
            'identity' => $arabic ? 'باسمكم واسم الشركة' : 'name and the company you are with',
            'role' => $arabic ? 'منصبكم والبريد الإلكتروني للعمل' : 'your role, and which work email',
            'need' => $arabic ? 'ما محور اللقاء التعريفي' : 'what should the briefing focus on',
            default => '',
        };
    }

    private function question(string $stage, bool $arabic): string
    {
        return match ($stage) {
            'identity' => $this->line('ask_identity_short', $arabic),
            'role' => $this->line('ask_role_short', $arabic),
            'need' => $this->line('ask_need', $arabic),
            default => '',
        };
    }

    /**
     * @return array{name: string, organization: string}|null
     */
    private function parseIdentity(string $text): ?array
    {
        $text = trim(preg_replace('/\s+/u', ' ', $text) ?? $text);
        if (mb_strlen($text) > 120 || str_contains($text, '?') || str_contains($text, '؟')) {
            return null;
        }
        if (! preg_match('/^(.+?)\s*(?:,|،|\sfrom\s|\sat\s|\sمن\s)\s*(.+)$/iu', $text, $matches)) {
            return null;
        }

        $name = trim($matches[1]);
        $name = preg_replace('/^(my name is|i am|i\'m|this is|name is|اسمي)\s+/iu', '', $name) ?? $name;
        $organization = trim($matches[2], " \t\n\r\0\x0B.");

        if (mb_strlen($name) < 2 || mb_strlen($name) > 120 || mb_strlen($organization) < 2 || mb_strlen($organization) > 160) {
            return null;
        }

        if (count(preg_split('/\s+/u', $name) ?: []) > 6) {
            return null;
        }

        if (str_contains($name, '@') || str_contains($organization, '@') || $this->isSensitive($text)) {
            return null;
        }

        return ['name' => $name, 'organization' => $organization];
    }

    /**
     * @return array{role: string, email: string}|null
     */
    private function parseRole(string $text): ?array
    {
        if (! preg_match('/[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}/i', $text, $matches)) {
            return null;
        }

        $email = strtolower($matches[0]);
        if (! filter_var($email, FILTER_VALIDATE_EMAIL)) {
            return null;
        }

        $role = str_replace($matches[0], ' ', $text);
        $role = preg_replace('/\b(my\s+)?e-?mail(\s+address)?\s*(is|:)?/iu', ' ', $role) ?? $role;
        $role = preg_replace('/\b(i am|i\'m|role is|منصبي)\b/iu', ' ', $role) ?? $role;
        $role = trim(preg_replace('/\s+/u', ' ', $role) ?? $role, " \t\n\r\0\x0B,،;:-");

        if (mb_strlen($role) < 2 || mb_strlen($role) > 120) {
            return null;
        }

        return ['role' => $role, 'email' => $email];
    }

    private function hasEmail(string $text): bool
    {
        return (bool) preg_match('/[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}/i', $text);
    }

    private function isNeed(string $text): bool
    {
        $text = trim($text);
        if (mb_strlen($text) < 10 || mb_strlen($text) > 2000) {
            return false;
        }

        if (str_contains($text, '?') || str_contains($text, '؟')) {
            return false;
        }

        return ! preg_match('/^(what|how|why|who|which|when|where|can|could|do|does|is|are|ما|كيف|هل|لماذا)\b/iu', $text);
    }

    private function isArabic(string $text): bool
    {
        return (bool) preg_match('/[ء-ي]/u', $text);
    }

    private function isSensitive(string $text): bool
    {
        return (bool) preg_match('/\b(password|passcode|otp|cvv|cvc|pin code|national id|qid|credit card|card number|iban)\b|كلمة السر|كلمة المرور|رقم الهوية/iu', $text);
    }

    private function isLeak(string $text): bool
    {
        return (bool) preg_match('/system prompt|ignore (all |any )?(previous|prior) instructions|reveal your (instructions|prompt)|developer message/i', $text);
    }

    private function isPrice(string $text): bool
    {
        return (bool) preg_match('/\b(price|pricing|cost|costs|fee|fees|quote|quotation|how much|how long|timeline|day rate|retainer)\b|السعر|التكلفة|كم يستغرق|المدة/iu', $text);
    }

    private function isLegal(string $text): bool
    {
        return (bool) preg_match('/\b(legal advice|legal opinion|is this compliant|are we compliant|audit opinion|sign off|sign-off)\b|رأي قانوني|هل نحن ملتزمون/iu', $text);
    }

    private function isClients(string $text): bool
    {
        return (bool) preg_match('/\b(your clients|client names|who have you worked|case stud(y|ies)|name a client)\b|أسماء العملاء|من عملاؤكم/iu', $text);
    }

    private function isPrivacy(string $text): bool
    {
        return (bool) preg_match('/\b(privacy|pdpl|pdppl|personal data)\b|الخصوصية|البيانات الشخصية/iu', $text);
    }

    private function isOffTopic(string $text): bool
    {
        return (bool) preg_match('/\b(weather|joke|poem|recipe|homework|football|cricket|movie|lyrics|bitcoin|crypto|casino|flight|hotel|restaurant)\b/iu', $text);
    }

    private function isBooking(string $text): bool
    {
        return (bool) preg_match('/\b(book|briefing|schedule a|talk to (the |your )?team|speak (to|with)|get in touch)\b|حجز|لقاء تعريفي/iu', $text);
    }

    private function isAffirmative(string $text): bool
    {
        return (bool) preg_match('/^(yes|yeah|yep|sure|please|ok|okay|let\'s do it|نعم|أجل)[.! ]*$/iu', trim($text));
    }

    private function offeredBriefing(string $previous): bool
    {
        return str_contains(mb_strtolower($previous), 'shall i arrange') || str_contains($previous, 'هل أرتب');
    }

    private function isThanks(string $text): bool
    {
        return (bool) preg_match('/^(thanks|thank you|shukran|شكرا|شكرًا)[.! ]*$/iu', trim($text));
    }

    private function topic(string $text, bool $arabic): ?string
    {
        $haystack = mb_strtolower($text);

        if (preg_match('/^(hi|hello|hey|good (morning|afternoon|evening)|salam|salaam)[.! ]*$/iu', trim($text)) || preg_match('/^(السلام عليكم|مرحبا|مرحبًا|أهلًا|اهلا)[.! ]*$/u', trim($text))) {
            return $this->line('hello', $arabic);
        }

        if (preg_match('/iso|27001|cyber|أمن سيبر/iu', $haystack)) {
            return $this->line('cyber', $arabic);
        }

        if (preg_match('/esg|ghg|pcaf|climate|انبعاث|المناخ/iu', $haystack)) {
            return $this->line('climate', $arabic);
        }

        if (preg_match('/\bai\b|artificial intelligence|machine learning|الذكاء الاصطناعي/iu', $haystack)) {
            return $this->line('ai', $arabic);
        }

        if (preg_match('/\b(grc|internal audit|enterprise risk)\b|التدقيق الداخلي|إدارة المخاطر/iu', $haystack)) {
            return $this->line('risk', $arabic);
        }

        if (preg_match('/digital transformation|operating model|التحول الرقمي/iu', $haystack)) {
            return $this->line('digital', $arabic);
        }

        if (preg_match('/\b(industries|sectors|which sector)\b|القطاعات/iu', $haystack)) {
            return $this->line('industries', $arabic);
        }

        if (preg_match('/\b(where are you|headquarter|based in|doha|office)\b|أين مقر|الدوحة/iu', $haystack)) {
            return $this->line('where', $arabic);
        }

        if (preg_match('/what (does|do) (aryx|you)|who are you|about aryx|your services|ما الذي تقدمه|من أنتم/iu', $haystack)) {
            return $this->line('about', $arabic);
        }

        return null;
    }

    private function line(string $key, bool $arabic): string
    {
        $copy = [
            'hello' => [
                'Welcome to Aryx Intelligence. I can walk you through our work in AI, cybersecurity, risk and climate tech, or set up a briefing with our team. What brings you here today?',
                'مرحبًا بكم في آريكس إنتليجنس. يمكنني تعريفكم بخدماتنا في الذكاء الاصطناعي والأمن السيبراني وإدارة المخاطر والتقنيات المناخية، أو ترتيب لقاء تعريفي مع فريقنا. كيف يمكنني مساعدتكم اليوم؟',
            ],
            'about' => [
                'Aryx Intelligence is a Qatar-based enterprise intelligence firm. We connect AI and data, cybersecurity, risk and internal audit, digital transformation and climate technology, so leaders can decide with one line of sight. What challenge is your organisation working through?',
                'آريكس إنتليجنس شركة استخبارات مؤسسية مقرها قطر. نربط الذكاء الاصطناعي والبيانات والأمن السيبراني والمخاطر والتدقيق الداخلي والتحول الرقمي والتقنيات المناخية في خط نظر واحد للقيادات. ما التحدي الذي تعمل عليه مؤسستكم؟',
            ],
            'cyber' => [
                'Aryx supports cybersecurity strategy and ISO 27001 readiness: gap assessment, risk treatment, policies and audit preparation. Timelines are confirmed in a briefing, not quoted here. What sector are you in?',
                'تدعم آريكس استراتيجية الأمن السيبراني والجاهزية لمعيار ISO 27001، من تقييم الفجوات إلى معالجة المخاطر والسياسات والاستعداد للتدقيق. تُحدَّد المدد في اللقاء التعريفي. في أي قطاع تعمل مؤسستكم؟',
            ],
            'climate' => [
                'We help organisations build ESG and GHG reporting they can defend, from Scope 1–3 inventories to PCAF financed emissions and climate risk. Which reporting framework are you working towards?',
                'نساعد المؤسسات على بناء تقارير ESG وغازات الدفيئة يمكن الدفاع عنها، من قوائم النطاق 1 إلى 3 إلى الانبعاثات الممولة وفق PCAF ومخاطر المناخ. أي إطار تقارير تعملون وفقه؟',
            ],
            'ai' => [
                'We help organisations decide where AI creates value, build it responsibly, and govern it with the same discipline as any material risk. What decision are you hoping AI will support?',
                'نساعد المؤسسات على تحديد أين يخلق الذكاء الاصطناعي قيمة، وعلى بنائه بمسؤولية وحوكمة بالانضباط نفسه الذي يُعامل به أي خطر جوهري. أي قرار ترجون أن يدعمه الذكاء الاصطناعي؟',
            ],
            'risk' => [
                'Aryx connects risk, governance, compliance and internal audit so leaders can see how exposures relate and which decision they demand next. I do not give audit opinions. What decision is this meant to inform?',
                'تربط آريكس المخاطر والحوكمة والالتزام والتدقيق الداخلي حتى ترى القيادة كيف تتصل التعرضات وأي قرار تتطلب بعد ذلك. لا أقدم رأيًا تدقيقيًا. أي قرار يُفترض أن يوجّه هذا العمل؟',
            ],
            'digital' => [
                'We design the architecture, platforms and operating models that make an organisation faster, more resilient and ready for AI, and we measure success in outcomes. What are you trying to change?',
                'نصمم البنية والمنصات ونماذج التشغيل التي تجعل المؤسسة أسرع وأكثر مرونة وأجهز للذكاء الاصطناعي، ونقيس النجاح بالنتائج. ما الذي تسعى مؤسستكم إلى تغييره؟',
            ],
            'industries' => [
                'Aryx works with institutions in banking and financial services, government, energy, infrastructure, real estate, healthcare, manufacturing, technology and professional services. Which is closest to you?',
                'تعمل آريكس مع مؤسسات في الخدمات المصرفية والمالية، والحكومة، والطاقة، والبنية التحتية، والعقار، والرعاية الصحية، والتصنيع، والتقنية، والخدمات المهنية. أيها الأقرب إليكم؟',
            ],
            'where' => [
                'Aryx is headquartered in Qatar, and works with institutions across the GCC and beyond. How can we help your organisation?',
                'مقر آريكس في قطر، وتعمل مع مؤسسات في دول مجلس التعاون وخارجها. كيف يمكننا مساعدة مؤسستكم؟',
            ],
            'default' => [
                'Aryx Intelligence is a Qatar-based enterprise intelligence firm working across AI, cybersecurity, risk and climate tech. Tell me a little about your organisation and I will point you to the right conversation.',
                'آريكس إنتليجنس شركة استخبارات مؤسسية مقرها قطر، وتعمل في الذكاء الاصطناعي والأمن السيبراني والمخاطر والتقنيات المناخية. حدثوني قليلًا عن مؤسستكم لأوجهكم إلى الحوار المناسب.',
            ],
            'price' => [
                'I do not quote prices, fees or timelines. Those are scoped in a briefing with the team. Shall I arrange one?',
                'لا أعرض الأسعار أو الرسوم أو المدد. يُحدَّد ذلك في لقاء تعريفي مع الفريق. هل أرتب لكم لقاءً؟',
            ],
            'legal' => [
                'I do not give legal, regulatory or audit opinions. The team can discuss this with you in a briefing. Shall I arrange one?',
                'لا أقدم آراء قانونية أو تنظيمية أو تدقيقية. يمكن للفريق مناقشة ذلك معكم في لقاء تعريفي. هل أرتب لكم لقاءً؟',
            ],
            'clients' => [
                'I do not name clients or claim results that are not published. The team can discuss relevant experience, without naming organisations, in a briefing. Shall I arrange one?',
                'لا أذكر أسماء العملاء ولا أدعي نتائج غير منشورة. يمكن للفريق مناقشة خبرة ذات صلة، دون تسمية المؤسسات، في لقاء تعريفي. هل أرتب لكم لقاءً؟',
            ],
            'privacy' => [
                'This conversation is handled under Aryx\'s privacy notice, in line with Qatar\'s Personal Data Privacy Protection Law (PDPPL). I only ask for a name, company, role, work email and a one-line description of the need.',
                'تُعالَج هذه المحادثة وفق إشعار الخصوصية لدى آريكس، وبما يتوافق مع قانون حماية خصوصية البيانات الشخصية في قطر. لا أطلب سوى الاسم والشركة والمنصب والبريد الإلكتروني للعمل ووصفًا من سطر واحد للحاجة.',
            ],
            'sensitive' => [
                'I will not take passwords, identity numbers or payment details. Share only your name, company, role, work email and a short description of the need.',
                'لن أقبل كلمات المرور أو أرقام الهوية أو بيانات الدفع. شاركوا فقط الاسم والشركة والمنصب والبريد الإلكتروني للعمل ووصفًا موجزًا للحاجة.',
            ],
            'leak' => [
                'I cannot share internal instructions. I can explain Aryx\'s work, or arrange a briefing with the team.',
                'لا يمكنني مشاركة التعليمات الداخلية. يمكنني شرح عمل آريكس، أو ترتيب لقاء تعريفي مع الفريق.',
            ],
            'offtopic' => [
                'I stay with Aryx\'s work: AI, cybersecurity, risk, digital transformation and climate technology. What would you like to explore?',
                'أبقى في نطاق عمل آريكس: الذكاء الاصطناعي والأمن السيبراني والمخاطر والتحول الرقمي والتقنيات المناخية. ماذا تودون أن نستكشف؟',
            ],
            'thanks' => [
                'You are welcome. The team will be in touch within one business day.',
                'على الرحب والسعة. سيتواصل الفريق خلال يوم عمل واحد.',
            ],
            'ask_identity' => [
                'Happy to arrange that. May I have your name and the company you are with?',
                'يسعدني ترتيب ذلك. هل لي باسمكم واسم الشركة؟',
            ],
            'ask_identity_short' => [
                'May I have your name and the company you are with?',
                'هل لي باسمكم واسم الشركة؟',
            ],
            'ask_role' => [
                'Thank you. What is your role, and which work email should the team use? This is handled under Aryx\'s privacy notice, in line with Qatar\'s PDPPL.',
                'شكرًا لكم. ما منصبكم والبريد الإلكتروني للعمل الذي يستخدمه الفريق؟ تُعالَج هذه البيانات وفق إشعار الخصوصية لدى آريكس وبما يتوافق مع قانون حماية خصوصية البيانات الشخصية في قطر.',
            ],
            'ask_role_short' => [
                'What is your role, and which work email should the team use?',
                'ما منصبكم والبريد الإلكتروني للعمل الذي يستخدمه الفريق؟',
            ],
            'ask_role_again' => [
                'Please share your role and a work email together. What is your role, and which work email should the team use?',
                'يرجى إرسال المنصب والبريد الإلكتروني للعمل معًا. ما منصبكم والبريد الإلكتروني للعمل الذي يستخدمه الفريق؟',
            ],
            'ask_need' => [
                'In one line, what should the briefing focus on?',
                'في سطر واحد، ما محور اللقاء التعريفي؟',
            ],
            'confirm' => [
                'Thank you. I have noted {name}, {role} at {company}, on {email}. The briefing will focus on: {need}. The team will follow up within one business day.',
                'شكرًا لكم. سجّلت {name}، {role} في {company}، عبر {email}. محور اللقاء: {need}. سيتابع الفريق خلال يوم عمل واحد.',
            ],
        ];

        return $copy[$key][$arabic ? 1 : 0];
    }
}
