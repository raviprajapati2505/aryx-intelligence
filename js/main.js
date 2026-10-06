(function () {
  var header = document.querySelector(".site-header");
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".site-nav");

  function onScroll() {
    if (!header) return;
    header.classList.toggle("is-stuck", window.scrollY > 8);
  }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });
    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      });
    });
  }

  document.querySelectorAll(".nav-btn").forEach(function (btn) {
    btn.addEventListener("click", function (event) {
      var item = btn.closest(".nav-item");
      var open = item.classList.contains("is-open");
      document.querySelectorAll(".nav-item.is-open").forEach(function (node) {
        node.classList.remove("is-open");
        var b = node.querySelector(".nav-btn");
        if (b) b.setAttribute("aria-expanded", "false");
      });
      if (!open) {
        item.classList.add("is-open");
        btn.setAttribute("aria-expanded", "true");
      }
      event.stopPropagation();
    });
  });

  document.addEventListener("click", function () {
    document.querySelectorAll(".nav-item.is-open").forEach(function (node) {
      node.classList.remove("is-open");
      var b = node.querySelector(".nav-btn");
      if (b) b.setAttribute("aria-expanded", "false");
    });
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      document.querySelectorAll(".nav-item.is-open").forEach(function (node) {
        node.classList.remove("is-open");
        var b = node.querySelector(".nav-btn");
        if (b) b.setAttribute("aria-expanded", "false");
      });
      if (nav && nav.classList.contains("is-open")) {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
        toggle.focus();
      }
    }
  });

  var motion = window.matchMedia("(prefers-reduced-motion: reduce)");
  var riseTargets = document.querySelectorAll(".reveal, .cap-row, .chain article, .approach article, .industry-card, .insight-card, .why-points article");
  if (!motion.matches && "IntersectionObserver" in window) {
    var seen = new Set();
    riseTargets.forEach(function (el) {
      if (seen.has(el)) return;
      seen.add(el);
      el.classList.add("reveal");
      var top = el.getBoundingClientRect().top;
      if (top > window.innerHeight * 0.9) el.classList.add("await-in");
    });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-in");
        entry.target.classList.remove("await-in");
        io.unobserve(entry.target);
      });
    }, { threshold: 0.16, rootMargin: "0px 0px -40px 0px" });
    seen.forEach(function (el) { io.observe(el); });
  } else {
    riseTargets.forEach(function (el) { el.classList.add("is-in"); });
  }

  document.querySelectorAll("video[data-hero]").forEach(function (video) {
    if (motion.matches) {
      video.removeAttribute("autoplay");
      video.pause();
    }
  });

  document.querySelectorAll("form[data-aryx-form]").forEach(function (form) {
    var note = form.querySelector(".form-note");
    var params = new URLSearchParams(window.location.search);
    var interest = params.get("interest");
    if (interest) {
      var select = form.querySelector("[name='interest']");
      if (select) {
        Array.prototype.forEach.call(select.options, function (opt) {
          if (opt.value === interest) select.value = interest;
        });
      }
    }

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      if (form.querySelector("[name='company_website']").value) return;

      var email = form.querySelector("[name='email']");
      if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim())) {
        setNote(note, "Enter a valid business email address.", true);
        email.focus();
        return;
      }
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      var consent = form.querySelector("[name='consent']");
      if (consent && !consent.checked) {
        setNote(note, "Please confirm you agree to the privacy policy.", true);
        consent.focus();
        return;
      }

      var endpoint = window.ARYX_FORM_ENDPOINT;
      if (!endpoint) {
        setNote(note, "This form is not connected yet. Add a delivery endpoint in js/site.js before it can send.", true);
        return;
      }

      var data = {};
      new FormData(form).forEach(function (value, key) {
        if (key !== "company_website") data[key] = value;
      });
      data.page = window.location.pathname;
      var submit = form.querySelector("[type='submit']");
      submit.disabled = true;

      fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(data)
      }).then(function (response) {
        if (!response.ok) throw new Error("Request failed");
        form.reset();
        setNote(note, form.getAttribute("data-success") || "Thank you. Your message has been received.", false);
      }).catch(function () {
        setNote(note, "The message could not be sent. Please try again in a moment.", true);
      }).finally(function () {
        submit.disabled = false;
      });
    });
  });

  function setNote(note, message, isError) {
    if (!note) return;
    note.hidden = false;
    note.textContent = message;
    note.classList.toggle("is-error", isError);
    note.classList.toggle("is-ok", !isError);
  }
})();
