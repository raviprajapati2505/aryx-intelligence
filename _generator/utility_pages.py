# -*- coding: utf-8 -*-
import build_site as S
import site_more as M

def register():
    contact()
    careers()
    privacy()
    terms()
    cookies()

def contact():
    d, slug = 1, "contact"
    title = "Contact Aryx Intelligence | Doha, Qatar"
    desc = "Start a strategic conversation with Aryx Intelligence about AI, cybersecurity, risk or technology decisions. Headquartered in Doha, Qatar."
    body = f"""
    {M.page_hero(d, [("Home", ""), ("Contact", None)], "Contact", "Start a strategic conversation",
      "Tell us about the decision or challenge in front of you. A senior member of our team will respond within " + M.ph("X business days") + " to arrange a conversation.")}
    <section class="section"><div class="wrap form-panel">
      <div>
        <h2>Aryx Intelligence</h2>
        <p>{M.ph("Office address")}, Doha, Qatar</p>
        <p>{M.ph("General email")}<br>{M.ph("Phone")}<br>{M.ph("LinkedIn company page")}</p>
        <p>Every conversation is confidential. We do not share your information with third parties. {M.ph("Confirm against privacy policy")}</p>
      </div>
      <form data-aryx-form data-success="Thank you. Your message has reached our leadership team. We will be in touch within the stated response window.">
        <p class="hp"><label>Company website <input name="company_website" tabindex="-1" autocomplete="off"></label></p>
        <input type="hidden" name="form" value="contact">
        <div class="fields">
          <label>Name <input name="name" required autocomplete="name"></label>
          <label>Title <input name="title" autocomplete="organization-title"></label>
          <label>Organization <input name="organization" required autocomplete="organization"></label>
          <label>Business email <input name="email" type="email" required autocomplete="email"></label>
          <label>Country <input name="country" autocomplete="country-name"></label>
          <label>Area of interest
            <select name="interest" required>
              <option value="">Select</option>
              <option value="ai">AI &amp; Intelligence</option>
              <option value="cybersecurity">Cybersecurity</option>
              <option value="risk">Risk &amp; Decision Intelligence</option>
              <option value="climate">Climate Intelligence</option>
              <option value="digital">Digital &amp; Technology Transformation</option>
              <option value="strategy">A strategic decision</option>
              <option value="other">Other</option>
            </select>
          </label>
        </div>
        <label>What decision or challenge are you facing? <textarea name="message" required></textarea></label>
        <label class="consent"><input type="checkbox" name="consent" value="yes" required> <span>I agree to the <a href="{S.href(d, "privacy")}">privacy policy</a>.</span></label>
        <button class="btn btn-primary" type="submit">Send to Aryx {S.ARROW}</button>
        <p class="form-note" hidden></p>
      </form>
    </div></section>
    """
    trail = [("Home", ""), ("Contact", None)]
    schemas = [
        M.web(slug, title, desc, "ContactPage"),
        S.crumb_schema(trail),
        S.org_schema(),
    ]
    S.add(slug, d, "contact", title, desc, body, schemas)

def careers():
    d, slug = 1, "careers"
    title = "Careers | Aryx Intelligence"
    desc = "Careers at Aryx Intelligence. Open roles will be listed here once confirmed."
    body = f"""
    {M.page_hero(d, [("Home", ""), ("Careers", None)], "Company", "Careers",
      "Open roles are not listed on this page yet. " + M.ph("Confirm careers") ,
      S.btn(d, "contact", "Talk to Aryx", query="?interest=other"))}
    <section class="section"><div class="wrap prose">
      <p>Aryx looks for senior practitioners across enterprise technology, cybersecurity, risk and sustainability. When roles are confirmed, they will be published here with the location, the work and how to apply.</p>
    </div></section>
    """
    trail = [("Home", ""), ("Careers", None)]
    S.add(slug, d, "about", title, desc, body, [M.web(slug, title, desc), S.crumb_schema(trail)])

def privacy():
    d, slug = 1, "privacy"
    title = "Privacy Policy | Aryx Intelligence"
    desc = "How Aryx Intelligence handles personal information submitted through this website."
    body = f"""
    {M.page_hero(d, [("Home", ""), ("Privacy", None)], "Legal", "Privacy",
      "This notice explains what Aryx Intelligence collects through this website and why. It should be confirmed by counsel before publication. " + M.ph("Confirm against privacy policy"))}
    <section class="section"><div class="wrap prose">
      <h2>Who we are</h2>
      <p>Aryx Intelligence is headquartered in Doha, Qatar. Contact: {M.ph("General email")}.</p>
      <h2>What we collect</h2>
      <p>If you submit a form, we collect the details you provide: name, title, organization, business email, country, area of interest and your message. The newsletter field collects a work email. A hidden field is used to reject automated submissions. We do not ask you to create an account.</p>
      <h2>Why we use it</h2>
      <p>We use contact details to reply to a conversation you asked for, and a newsletter email to send The Aryx Brief if you subscribe. We do not sell personal information.</p>
      <h2>How long we keep it</h2>
      <p>{M.ph("Retention period")}</p>
      <h2>Your choices</h2>
      <p>You may ask for access, correction or deletion of your information by writing to {M.ph("General email")}.</p>
    </div></section>
    """
    trail = [("Home", ""), ("Privacy", None)]
    S.add(slug, d, "", title, desc, body, [M.web(slug, title, desc), S.crumb_schema(trail)])

def terms():
    d, slug = 1, "terms"
    title = "Terms of Use | Aryx Intelligence"
    desc = "Terms of use for the Aryx Intelligence website."
    body = f"""
    {M.page_hero(d, [("Home", ""), ("Terms", None)], "Legal", "Terms of use",
      "These terms govern use of this website. They are a working draft for review. " + M.ph("Confirm terms"))}
    <section class="section"><div class="wrap prose">
      <p>Content on this website is for general information. It is not legal, investment, audit or supervisory advice, and it does not create a client relationship. Engagements begin only when both parties agree a scope.</p>
      <p>Regulatory references can change. Where a page marks a point for verification, that point should be checked against the primary source before you rely on it.</p>
      <p>You may not copy the site for commercial reuse without permission. The Aryx name and logo are the property of Aryx Intelligence.</p>
    </div></section>
    """
    trail = [("Home", ""), ("Terms", None)]
    S.add(slug, d, "", title, desc, body, [M.web(slug, title, desc), S.crumb_schema(trail)])

def cookies():
    d, slug = 1, "cookies"
    title = "Cookies | Aryx Intelligence"
    desc = "How the Aryx Intelligence website uses cookies and similar storage."
    body = f"""
    {M.page_hero(d, [("Home", ""), ("Cookies", None)], "Legal", "Cookies",
      "This website is built to work without advertising cookies. " + M.ph("Confirm analytics cookies before adding any"))}
    <section class="section"><div class="wrap prose">
      <p>Pages do not set a tracking cookie in this template. If analytics or an embedded service is added later, this page should name each cookie, its purpose and how long it lasts, and collect consent where the law requires it.</p>
      <p>Fonts are loaded from Google Fonts, which may receive your IP address when the typeface files are requested. {M.ph("Confirm whether to self-host fonts")}</p>
    </div></section>
    """
    trail = [("Home", ""), ("Cookies", None)]
    S.add(slug, d, "", title, desc, body, [M.web(slug, title, desc), S.crumb_schema(trail)])
