#!/usr/bin/env python3
"""
TikTok Scraper — connects to your already-running Brave via CDP.

Brave must be started with --remote-debugging-port=9222.
Since you already have it open, close all windows and restart with:

    & "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --remote-debugging-port=9222

Then this script will connect and scrape TikTok.
"""

import sys, json, re, os
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright

BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
CDP_PORT = 9222

class TikTokCDPScraper:
    def __init__(self):
        pass

    def _connect(self, playwright):
        """Connect to already-running Brave via CDP."""
        try:
            browser = playwright.chromium.connect_over_cdp(
                "http://localhost:{}".format(CDP_PORT)
            )
            print("Connected to Brave! Default context:", browser.contexts, file=sys.stderr)
            # Use the default context (has all the cookies)
            if browser.contexts:
                context = browser.contexts[0]
            else:
                context = browser.new_context()
            return browser, context
        except Exception as e:
            print("Failed to connect. Is Brave running with --remote-debugging-port=9222?", file=sys.stderr)
            print("Error:", e, file=sys.stderr)
            return None, None

    def search(self, query, count=20):
        """Search TikTok."""
        url = "https://www.tiktok.com/search?q={}".format(
            query.replace(" ", "%20"))
        return self._scrape(url, count)

    def user_videos(self, username, count=20):
        """Get user's videos."""
        url = "https://www.tiktok.com/@{}".format(username)
        return self._scrape(url, count)

    def video_metadata(self, url):
        """Single video metadata."""
        with sync_playwright() as p:
            browser, context = self._connect(p)
            if not browser:
                return {"error": "Could not connect to Brave"}

            page = context.new_page()
            try:
                page.goto(url, wait_until="networkidle", timeout=30000)
                page.wait_for_timeout(5000)

                html = page.content()
                desc = ""
                m = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]+)"', html)
                if m:
                    desc = unescape(m.group(1).strip())

                author = ""
                m = re.search(r'/@([\w.]+)/', url)
                if m:
                    author = m.group(1)

                vid = re.search(r'/video/(\d+)', html)
                if not vid:
                    vid = re.search(r'/video/(\d+)', url)

                result = {
                    "id": vid.group(1) if vid else "",
                    "desc": desc[:200],
                    "author": author,
                    "url": url,
                    "likes": 0,
                    "views": 0,
                    "comments": 0,
                }
            except Exception as e:
                result = {"error": str(e), "url": url}
            finally:
                page.close()

        return result

    def _scrape(self, url, count):
        """Scrape a search or profile page."""
        with sync_playwright() as p:
            browser, context = self._connect(p)
            if not browser:
                return []

            page = context.new_page()
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=30000)
                page.wait_for_timeout(3000)

                # Scroll to load content
                for _ in range(5):
                    page.evaluate("window.scrollBy(0, 600)")
                    page.wait_for_timeout(2000)

                html = page.content()

                # Extract from embedded JSON
                results = self._extract_from_json(html)

                if not results:
                    results = self._extract_from_dom(page, html)

            except Exception as e:
                print("Error: {}".format(e), file=sys.stderr)
                results = []
            finally:
                page.close()

        return results[:count]

    def _extract_from_json(self, html):
        """Try to get video data from JSON in page."""
        results = []
        json_re = r'<script[^>]*>(.*?)</script>'
        for match in re.finditer(json_re, html, re.DOTALL):
            text = match.group(1).strip()
            if not text.startswith("{"):
                continue
            try:
                data = json.loads(text)
                found = self._find_videos(data)
                if found:
                    results.extend(found)
            except (json.JSONDecodeError, UnicodeDecodeError):
                continue
            if len(results) > 50:
                break
        return results

    def _find_videos(self, data, depth=0):
        """Recursive video search in JSON."""
        if depth > 4 or not isinstance(data, dict):
            return []

        results = []

        # Check if this is a video item
        if "id" in data and ("desc" in data or "createTime" in data):
            item = data
            vid = item.get("id", "")
            author = item.get("author", {})
            stats = item.get("stats", {})
            if isinstance(author, dict):
                author_id = author.get("unique_id", author.get("id", author.get("secUid", "")))
            else:
                author_id = str(author)

            results.append({
                "id": str(vid),
                "desc": item.get("desc", ""),
                "author": author_id,
                "url": "https://www.tiktok.com/@{}/video/{}".format(author_id, vid),
                "likes": stats.get("digg_count", 0) if isinstance(stats, dict) else 0,
                "views": stats.get("play_count", 0) if isinstance(stats, dict) else 0,
                "comments": stats.get("comment_count", 0) if isinstance(stats, dict) else 0,
                "source": "json_deep",
            })

        # Search common keys
        for key in ["itemList", "items", "videos", "data", "videoList",
                     "results", "contents", "cards", "posts", "list"]:
            val = data.get(key)
            if isinstance(val, list):
                for item in val:
                    if isinstance(item, dict):
                        found = self._find_videos(item, depth + 1)
                        results.extend(found)
            elif isinstance(val, dict):
                found = self._find_videos(val, depth + 1)
                results.extend(found)

        return results

    def _extract_from_dom(self, page, html):
        """Extract from rendered DOM elements."""
        results = []

        # Get video links
        links = page.eval_on_selector_all(
            "a[href*='/video/']",
            "els => els.map(el => el.href)"
        )
        descs = page.eval_on_selector_all(
            "[data-e2e='video-card-desc'], .tiktok-video-card-desc, div[class*='desc']",
            "els => els.map(el => el.textContent)"
        )

        seen = set()
        for i, link in enumerate(links):
            vid = re.search(r'/video/(\d+)', link)
            if not vid or vid.group(1) in seen:
                continue
            seen.add(vid.group(1))

            author = re.search(r'/@([\w.]+)/', link)
            desc = descs[i].strip() if i < len(descs) else ""

            results.append({
                "id": vid.group(1),
                "desc": desc,
                "author": author.group(1) if author else "",
                "url": link,
                "likes": 0,
                "views": 0,
                "comments": 0,
                "source": "dom",
            })

        return results


from html import unescape

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python tiktok_scrape.py search <query> [--count N]")
        print("  python tiktok_scrape.py user <username> [--count N]")
        print("  python tiktok_scrape.py video <url>")
        print("")
        print("Before running: restart Brave with remote debugging:")
        print('  & "' + BRAVE_PATH + '" --remote-debugging-port=' + str(CDP_PORT))
        sys.exit(1)

    command = sys.argv[1]
    target = sys.argv[2]
    count = 20

    if "--count" in sys.argv:
        idx = sys.argv.index("--count")
        if idx + 1 < len(sys.argv):
            count = int(sys.argv[idx + 1])

    scraper = TikTokCDPScraper()

    result = None
    if command == "search":
        result = scraper.search(target, count)
    elif command == "user":
        result = scraper.user_videos(target, count)
    elif command == "video":
        result = scraper.video_metadata(target)
    else:
        print("Unknown command: {}".format(command), file=sys.stderr)
        sys.exit(1)

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
