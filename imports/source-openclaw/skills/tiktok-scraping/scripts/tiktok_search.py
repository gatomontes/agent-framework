#!/usr/bin/env python3
"""
TikTok Search & Metadata Scraper

Uses public TikTok web API with optional cookie file for better results.
Two modes:
  1. No cookies — basic HTML scraping (limited data)
  2. With cookies file — better metadata from API

Cookie file format: Netscape cookie file (can export with browser extensions
like "Get cookies.txt" or via Chrome DevTools)

Usage:
    python tiktok_search.py search <query> [--count 20] [--cookies cookies.txt]
    python tiktok_search.py user <username> [--count 20] [--cookies cookies.txt]
    python tiktok_search.py hashtag <tag> [--count 20] [--cookies cookies.txt]
    python tiktok_search.py video <url> [--cookies cookies.txt]

Output: JSON to stdout.
"""

import sys
import json
import re
import time
import urllib.parse
from html import unescape

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)

import requests


class TikTokScraper:
    """Scrape TikTok metadata via public web endpoints."""

    def __init__(self, cookie_file=None):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/125.0.0.0 Safari/537.36"
            ),
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.9,es;q=0.8",
            "Referer": "https://www.tiktok.com/",
            "Origin": "https://www.tiktok.com",
        })

        # Load cookies if provided
        if cookie_file:
            self._load_cookies(cookie_file)

    def _load_cookies(self, path):
        """Load Netscape-format cookies from file."""
        try:
            with open(path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    parts = line.split('\t')
                    if len(parts) >= 7:
                        domain = parts[0]
                        path_val = parts[2]
                        secure = parts[3].upper() == 'TRUE'
                        name = parts[5]
                        value = parts[6]
                        self.session.cookies.set(
                            name, value,
                            domain=domain, path=path_val,
                            secure=secure
                        )
            print("Loaded cookies from", path, file=sys.stderr)
        except Exception as e:
            print("Error loading cookies:", e, file=sys.stderr)

    # ─── API methods ───

    def search(self, query, count=20):
        """Search TikTok videos by keyword."""
        results = []

        # Try direct API first (works best with cookies)
        api_url = "https://www.tiktok.com/api/search/general/full/"
        params = {"q": query, "count": min(count, 50), "type": 1}

        r = self._api_request(api_url, params)
        if r:
            items = self._parse_search_api(r)
            if items:
                return items[:count]

        # Fallback: HTML search page
        return self._scrape_search_page(query, count)

    def user_videos(self, username, count=20):
        """Get videos from a TikTok user."""
        url = "https://www.tiktok.com/@" + username
        try:
            r = self.session.get(url, timeout=15)
            r.raise_for_status()
            html = r.text

            # Try embedded data
            items = self._extract_embedded_data(html, count)
            if items:
                return items

            # HTML fallback
            return self._extract_video_ids(html, username, count)
        except requests.RequestException as e:
            print("Error: {}".format(e), file=sys.stderr)
            return []

    def hashtag_videos(self, tag, count=20):
        """Search by hashtag."""
        return self.search("#" + tag, count)

    def video_metadata(self, url):
        """Get metadata for a single video."""
        vid = self._extract_video_id(url)
        if not url.startswith("http"):
            url = "https://www.tiktok.com/@x/video/{}".format(vid)
        try:
            r = self.session.get(url, timeout=15, allow_redirects=True)
            r.raise_for_status()
            html = r.text

            items = self._extract_embedded_data(html, 1)
            if items:
                return items[0]

            # Fallback scrape
            return self._scrape_single_video(html, vid, r.url)
        except requests.RequestException as e:
            return {"error": str(e), "url": url, "id": vid}

    # ─── Internal helpers ───

    def _api_request(self, url, params):
        """Make an API request with retries."""
        for attempt in range(2):
            try:
                r = self.session.get(url, params=params, timeout=15)
                ct = r.headers.get("Content-Type", "")
                if r.status_code == 200 and "json" in ct:
                    return r
            except requests.RequestException:
                time.sleep(1)
        return None

    def _parse_search_api(self, response):
        """Parse the search API JSON response."""
        try:
            data = response.json()
            items = data.get("data", [])
            results = []
            for item in items:
                video = item.get("item", item)
                if not video:
                    continue
                info = self._build_video_info(video)
                if info:
                    results.append(info)
            return results
        except (json.JSONDecodeError, AttributeError):
            return None

    def _build_video_info(self, video):
        """Extract standardized info from a video dict."""
        vid = video.get("id", "")
        author = video.get("author", {})
        stats = video.get("stats", {})
        auth_id = author.get("unique_id", "")
        return {
            "id": str(vid),
            "desc": video.get("desc", ""),
            "create_time": video.get("create_time", 0),
            "author": auth_id,
            "author_nickname": author.get("nickname", ""),
            "author_followers": author.get("follower_count", 0),
            "likes": stats.get("digg_count", 0),
            "views": stats.get("play_count", 0),
            "comments": stats.get("comment_count", 0),
            "shares": stats.get("share_count", 0),
            "duration": video.get("video", {}).get("duration", 0),
            "url": "https://www.tiktok.com/@{}/video/{}".format(auth_id, vid)
            if auth_id and vid else "",
        }

    def _scrape_search_page(self, query, count):
        """Scrape the HTML search page for video data."""
        encoded = urllib.parse.quote(query)
        url = "https://www.tiktok.com/search?q={}".format(encoded)
        try:
            r = self.session.get(url, timeout=15)
            r.raise_for_status()
            html = r.text

            items = self._extract_embedded_data(html, count)
            if items:
                return items

            return self._extract_video_ids(html, None, count)
        except requests.RequestException:
            return []

    def _extract_embedded_data(self, html, max_count):
        """Extract video data from embedded JSON in HTML."""
        for pattern in [
            r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',
            r'window\.__INITIAL_STATE__\s*=\s*({.*?});',
            r'<script[^>]*id="__SIGNED_DATA__"[^>]*>(.*?)</script>',
        ]:
            match = re.search(pattern, html, re.DOTALL)
            if match:
                try:
                    data = json.loads(match.group(1))
                    items = self._traverse_data(data)
                    if items:
                        return items[:max_count]
                except (json.JSONDecodeError, AttributeError):
                    continue
        return []

    def _traverse_data(self, data):
        """Try to find video items in various JSON structures."""
        results = []
        # Try search result structures
        try:
            items = data["searchResult"]["items"]
            for item in items[:50]:
                info = self._build_video_info(item.get("item", item))
                if info and info["id"]:
                    results.append(info)
            if results:
                return results
        except (KeyError, TypeError, AttributeError):
            pass

        try:
            items = data["pageProps"]["searchResult"]["items"]
            for item in items[:50]:
                info = self._build_video_info(item.get("item", item))
                if info and info["id"]:
                    results.append(info)
            if results:
                return results
        except (KeyError, TypeError, AttributeError):
            pass

        # User profile data
        for path in [
            ["UserModule", "users"],
            ["props", "pageProps", "userInfo", "user", "videoList"],
        ]:
            try:
                cursor = data
                for key in path:
                    cursor = cursor[key]
                if isinstance(cursor, dict):
                    for username, user_data in cursor.items():
                        videos = user_data.get("videoList", [])
                        for v in videos[:50]:
                            vid = v.get("video", v)
                            info = self._build_video_info(vid)
                            if info and info["id"]:
                                results.append(info)
                elif isinstance(cursor, list):
                    for v in cursor[:50]:
                        vid = v.get("video", v)
                        info = self._build_video_info(vid)
                        if info and info["id"]:
                            results.append(info)
                if results:
                    return results
            except (KeyError, TypeError, AttributeError):
                continue

        return results

    def _extract_video_ids(self, html, default_author, count):
        """Fallback: extract video IDs from HTML."""
        results = []
        pattern = r'/video/(\d+)'
        ids = re.findall(pattern, html)
        seen = set()
        for vid in ids:
            if vid in seen:
                continue
            seen.add(vid)
            # Try to find description
            desc = ""
            # Try to find author
            auth_pat = r'/@([\w.]+)/video/' + re.escape(vid)
            auth_match = re.search(auth_pat, html)
            author = auth_match.group(1) if auth_match else (
                default_author or "unknown")
            results.append({
                "id": vid,
                "desc": desc,
                "author": author,
                "url": "https://www.tiktok.com/@{}/video/{}".format(
                    author, vid),
                "likes": 0,
                "views": 0,
                "comments": 0,
            })
            if len(results) >= count:
                break
        return results

    def _scrape_single_video(self, html, vid, url):
        """Scrape metadata from a single video page."""
        desc = ""
        m = re.search(r'<h1[^>]*>([^<]+)', html)
        if m:
            desc = unescape(m.group(1).strip())
        m = re.search(r'/@([\w.]+)/video/', html)
        author = m.group(1) if m else ""
        return {
            "id": vid,
            "desc": desc,
            "author": author,
            "url": url,
            "likes": 0,
            "views": 0,
            "comments": 0,
        }

    def _extract_video_id(self, url):
        """Extract video ID from various TikTok URL formats."""
        patterns = [
            r'tiktok\.com/@[\w.]+/video/(\d+)',
            r'tiktok\.com/video/(\d+)',
            r'vm\.tiktok\.com/([\w]+)',
            r'tiktok\.com/t/([\w]+)',
        ]
        for pat in patterns:
            m = re.search(pat, url)
            if m:
                return m.group(1)
        return url


# ─── CLI ───

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python tiktok_search.py search <query> [--count N] [--cookies file.txt]")
        print("  python tiktok_search.py user <username> [--count N] [--cookies file.txt]")
        print("  python tiktok_search.py hashtag <tag> [--count N] [--cookies file.txt]")
        print("  python tiktok_search.py video <url> [--cookies file.txt]")
        sys.exit(1)

    command = sys.argv[1]
    target = sys.argv[2]
    count = 20
    cookie_file = None

    # Parse options
    if "--count" in sys.argv:
        idx = sys.argv.index("--count")
        if idx + 1 < len(sys.argv):
            count = int(sys.argv[idx + 1])
    if "--cookies" in sys.argv:
        idx = sys.argv.index("--cookies")
        if idx + 1 < len(sys.argv):
            cookie_file = sys.argv[idx + 1]

    scraper = TikTokScraper(cookie_file)

    result = None
    if command == "search":
        result = scraper.search(target, count)
    elif command == "user":
        result = scraper.user_videos(target, count)
    elif command == "hashtag":
        result = scraper.hashtag_videos(target, count)
    elif command == "video":
        result = scraper.video_metadata(target)
    else:
        print("Unknown command: {}".format(command), file=sys.stderr)
        sys.exit(1)

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
