#!/usr/bin/env python3
"""Check a built Jekyll site (_site) for broken internal links and images.

Usage: python3 scripts/check-site.py [_site]

Every href/src/poster/data-src/data-image-src that points inside the site
(relative, root-relative, or https://sportstechwest.com/...) must resolve to a
file in the build. External links are not fetched. Exits 1 if anything is
broken, so it can gate CI.
"""
import collections
import os
import re
import sys
import urllib.parse

SITE_HOST = re.compile(r"^https?://(www\.)?sportstechwest\.com(?=/|$)")
ATTR = re.compile(r'(?:href|src|poster|data-src|data-image-src)\s*=\s*"([^"]*)"')
SKIP_PREFIXES = ("http://", "https://", "//", "mailto:", "tel:", "javascript:", "#", "data:")


def resolves(root, page_dir, path):
    if path.startswith("/"):
        target = os.path.join(root, path.lstrip("/"))
    else:
        target = os.path.normpath(os.path.join(page_dir, path))
    return (
        os.path.exists(target)
        or os.path.exists(target + ".html")
        or os.path.exists(os.path.join(target, "index.html"))
    )


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "_site"
    broken = collections.defaultdict(set)
    pages = 0
    for dirpath, _, files in os.walk(root):
        for name in files:
            if not name.endswith(".html"):
                continue
            pages += 1
            page = os.path.join(dirpath, name)
            html = open(page, encoding="utf-8", errors="ignore").read()
            for url in ATTR.findall(html):
                url = SITE_HOST.sub("", url.strip()) or "/"
                # skip external links and URLs assembled in inline JavaScript
                if url.startswith(SKIP_PREFIXES) or "'" in url or "+" in url or "{{" in url:
                    continue
                path = urllib.parse.unquote(url.split("#")[0].split("?")[0])
                if path and not resolves(root, dirpath, path):
                    broken[path].add(os.path.relpath(page, root))

    print(f"Checked {pages} pages.")
    if not broken:
        print("No broken internal links or images.")
        return 0
    print(f"{len(broken)} broken targets:")
    for path, where in sorted(broken.items()):
        sample = ", ".join(sorted(where)[:3])
        more = f" (+{len(where) - 3} more)" if len(where) > 3 else ""
        print(f"  {path}\n      on: {sample}{more}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
