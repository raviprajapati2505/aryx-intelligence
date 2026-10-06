import os, re
from html.parser import HTMLParser
from urllib.parse import unquote, urlparse

root = "/home/ravi/Projects/PHP/aryx-intelligence"
missing = []
pages = []
for dirpath, _, files in os.walk(root):
    if "/.git" in dirpath or "/_generator" in dirpath:
        continue
    for name in files:
        if name.endswith(".html"):
            pages.append(os.path.join(dirpath, name))

class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "a" and "href" in d:
            self.hrefs.append(d["href"])
        if tag in ("img", "script", "link", "source") and (d.get("src") or d.get("href")):
            self.hrefs.append(d.get("src") or d.get("href"))

for page in pages:
    parser = P()
    parser.feed(open(page, encoding="utf-8").read())
    base = os.path.dirname(page)
    for href in parser.hrefs:
        if href.startswith(("#", "mailto:", "tel:", "https:", "http:")):
            continue
        path = href.split("#", 1)[0].split("?", 1)[0]
        if not path:
            continue
        target = os.path.normpath(os.path.join(base, unquote(path)))
        if not os.path.exists(target):
            missing.append((os.path.relpath(page, root), href))

print("pages", len(pages))
print("missing", len(missing))
for item in missing[:40]:
    print(item)
