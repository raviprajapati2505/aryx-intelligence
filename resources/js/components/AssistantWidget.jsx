import { useEffect, useId, useRef, useState } from 'react';
import { Link } from 'react-router-dom';

const COPY = {
    en: {
        hello: 'Welcome to Aryx Intelligence. I can walk you through our work in AI, cybersecurity, risk and climate tech, or set up a briefing with our team. What brings you here today?',
        chips: ['What does Aryx do?', 'We need ISO 27001 readiness', 'Help with ESG and GHG reporting', 'Book a briefing'],
        placeholder: 'Ask about AI, cyber, risk or climate tech…',
        send: 'Send',
        launch: 'Ask Aryx',
        close: 'Close assistant',
        thinking: 'Thinking…',
        error: 'I could not reply just now. Please try again.',
        note: 'Brief answers. No passwords or payment details.',
        contact: 'Contact the team',
    },
    ar: {
        hello: 'مرحبًا بكم في آريكس إنتليجنس. يمكنني تعريفكم بخدماتنا في الذكاء الاصطناعي والأمن السيبراني وإدارة المخاطر والتقنيات المناخية، أو ترتيب لقاء تعريفي مع فريقنا. كيف يمكنني مساعدتكم اليوم؟',
        chips: ['ما الذي تقدمه آريكس؟', 'نحتاج إلى الجاهزية لمعيار ISO 27001', 'تقارير ESG والانبعاثات', 'حجز لقاء تعريفي'],
        placeholder: 'اكتب سؤالك هنا…',
        send: 'إرسال',
        launch: 'اسأل آريكس',
        close: 'إغلاق المساعد',
        thinking: '…',
        error: 'تعذر إرسال الرد الآن. يرجى المحاولة مرة أخرى.',
        note: 'إجابات موجزة. لا كلمات مرور ولا بيانات دفع.',
        contact: 'تواصل مع الفريق',
    },
};

const isArabic = (text) => /[ء-ي]/.test(text);

function greeting(locale) {
    return [{ role: 'assistant', content: COPY[locale].hello }];
}

export default function AssistantWidget() {
    const titleId = useId();
    const logRef = useRef(null);
    const inputRef = useRef(null);
    const launchRef = useRef(null);
    const closeTimer = useRef(null);
    const [open, setOpen] = useState(false);
    const [present, setPresent] = useState(false);
    const [entered, setEntered] = useState(false);
    const [locale, setLocale] = useState('en');
    const [messages, setMessages] = useState(() => greeting('en'));
    const [draft, setDraft] = useState('');
    const [busy, setBusy] = useState(false);
    const [error, setError] = useState('');
    const copy = COPY[locale];

    useEffect(() => () => clearTimeout(closeTimer.current), []);

    useEffect(() => {
        const log = logRef.current;
        if (log) log.scrollTop = log.scrollHeight;
    }, [messages, open, busy]);

    useEffect(() => {
        if (!open) return undefined;
        inputRef.current?.focus();
        const onKey = (event) => {
            if (event.key === 'Escape') closeWidget();
        };
        document.addEventListener('keydown', onKey);
        return () => document.removeEventListener('keydown', onKey);
    }, [open, locale]);

    function openWidget() {
        clearTimeout(closeTimer.current);
        setPresent(true);
        setOpen(true);
        requestAnimationFrame(() => {
            requestAnimationFrame(() => setEntered(true));
        });
    }

    function closeWidget() {
        setOpen(false);
        setEntered(false);
        launchRef.current?.focus();
        const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        clearTimeout(closeTimer.current);
        closeTimer.current = setTimeout(() => setPresent(false), reduce ? 0 : 420);
    }

    function chooseLocale(next) {
        if (next === locale) return;
        setLocale(next);
        setMessages(greeting(next));
        setDraft('');
        setError('');
    }

    async function ask(text) {
        const content = text.trim();
        if (!content || busy) return;

        const history = [...messages, { role: 'user', content }];
        setMessages(history);
        setDraft('');
        setError('');
        setBusy(true);

        try {
            const response = await fetch('/api/assistant/messages', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    Accept: 'application/json',
                },
                body: JSON.stringify({ locale, messages: history }),
            });
            const body = await response.json().catch(() => ({}));
            if (!response.ok) {
                const first = body.errors ? Object.values(body.errors)[0] : null;
                throw new Error((Array.isArray(first) ? first[0] : first) || body.message || copy.error);
            }
            setMessages([...history, { role: 'assistant', content: body.reply }]);
        } catch (err) {
            setMessages(messages);
            setDraft(content);
            setError(err.message || copy.error);
        } finally {
            setBusy(false);
            inputRef.current?.focus();
        }
    }

    return (
        <div className="ax">
            {present && (
                <section className={entered ? 'ax-panel in' : 'ax-panel'} role="dialog" aria-labelledby={titleId} dir={locale === 'ar' ? 'rtl' : 'ltr'}>
                    <header className="ax-head">
                        <div className="ax-avatar" aria-hidden="true">A</div>
                        <div className="ax-who">
                            <b id={titleId}>Aryx Assistant</b>
                            <small><span className="ax-dot" />Enterprise intelligence, Qatar</small>
                        </div>
                        <div className="ax-lang" role="group" aria-label="Language">
                            <button type="button" aria-pressed={locale === 'en'} onClick={() => chooseLocale('en')}>EN</button>
                            <button type="button" aria-pressed={locale === 'ar'} onClick={() => chooseLocale('ar')}>ع</button>
                        </div>
                        <button type="button" className="ax-x" onClick={closeWidget} aria-label={copy.close} />
                    </header>
                    <div className="ax-log" ref={logRef} aria-live="polite">
                        {messages.map((message, index) => (
                            <div
                                key={`${message.role}-${index}`}
                                className={`ax-msg ${message.role === 'user' ? 'me' : 'bot'}${index === messages.length - 1 ? ' ax-in' : ''}`}
                                dir={isArabic(message.content) ? 'rtl' : 'ltr'}
                            >
                                {message.content}
                            </div>
                        ))}
                        {busy && (
                            <div className="ax-msg bot ax-in ax-typing" aria-label={copy.thinking}>
                                <span /><span /><span />
                            </div>
                        )}
                    </div>
                    <div className="ax-chips">
                        {copy.chips.map((chip) => (
                            <button key={chip} type="button" dir={locale === 'ar' ? 'rtl' : 'ltr'} onClick={() => ask(chip)} disabled={busy}>
                                {chip}
                            </button>
                        ))}
                    </div>
                    <form
                        onSubmit={(event) => {
                            event.preventDefault();
                            ask(draft);
                        }}
                    >
                        <input
                            ref={inputRef}
                            value={draft}
                            onChange={(event) => setDraft(event.target.value)}
                            placeholder={copy.placeholder}
                            aria-label={copy.placeholder}
                            dir={locale === 'ar' ? 'rtl' : 'ltr'}
                            autoComplete="off"
                            maxLength={2000}
                            disabled={busy}
                        />
                        <button type="submit" disabled={busy || !draft.trim()}>{copy.send}</button>
                    </form>
                    <p className="ax-note">
                        {error || copy.note}{' '}
                        <Link to="/contact">{copy.contact}</Link>
                    </p>
                </section>
            )}
            <button
                ref={launchRef}
                type="button"
                className="ax-launch"
                aria-expanded={open}
                aria-label={open ? copy.close : copy.launch}
                onClick={() => (open ? closeWidget() : openWidget())}
            >
                {open ? (
                    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6 L18 18 M18 6 L6 18" /></svg>
                ) : (
                    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 6.5h14v8.2H9.2L5 18.2V6.5Z" /></svg>
                )}
                {!open && <span className="ax-launch-label">{copy.launch}</span>}
            </button>
        </div>
    );
}
