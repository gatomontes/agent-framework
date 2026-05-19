---
name: tiktok-scraping-yt-dlp
description: Use for TikTok crawling, content retrieval, and analysis
---

# TikTok Scraping

Two approaches:
1. **yt-dlp** — best for downloading videos from known user profiles (works with cookies)
2. **Playwright** — headless browser search scraping (needs cookies/login)

## Setup

```bash
# pip install all dependencies
pip install yt-dlp playwright
playwright install chromium
```

---

## Authentication (Required for TikTok)

TikTok blocks **all** unauthenticated requests. You must have a logged-in session.

### Method 1: Brave with Remote Debugging (Recommended)

This is the most reliable approach — reuses cookies from your running Brave session.

**One-time setup:** Restart Brave with remote debugging, then any terminal can connect to it:

1. Close all Brave windows
2. Open a PowerShell and run:
```powershell
& "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --remote-debugging-port=9222
```
3. Navigate to tiktok.com and log in if needed
4. **Leave that Brave window open.** Now run the scraper:

```bash
cd ~/.openclaw/skills/tiktok-scraping/scripts
python tiktok_scrape.py search "manosphere puerto rico" --count 20
```

The scraper connects to Brave via CDP and uses its cookies.

**Tip:** Create a desktop shortcut with the `--remote-debugging-port=9222` flag so you don't have to type it every time.

### Method 2: Export cookies to file ✅ WORKING

Export TikTok cookies as JSON (e.g., via "EditThisCookie" extension), convert to Netscape format, use with yt-dlp.

**One-time setup:**

1. Install **"EditThisCookie"** or **"Get cookies.txt"** Chrome extension
2. Go to **tiktok.com**, log in, export cookies as JSON
3. Save to a file (e.g., `tiktok_cookies.json`)
4. Convert with the included script:

```bash
python ~/.openclaw/skills/tiktok-scraping/scripts/convert_cookies.py tiktok_cookies.json tiktok_cookies.txt
```

5. Now use with yt-dlp:

```bash
# User profile metadata
yt-dlp --cookies tiktok_cookies.txt "https://www.tiktok.com/@username" --simulate --dump-json --playlist-end 20

# Single video metadata
yt-dlp --cookies tiktok_cookies.txt "https://www.tiktok.com/@username/video/123456" --simulate --dump-json
```

### Method 3: yt-dlp --cookies-from-browser (browser closed)

Only works if Brave is **fully closed** (Windows locks the cookie DB):

```bash
yt-dlp --cookies-from-browser brave "https://www.tiktok.com/@handle"
```

---

## Search by Keyword

Using CDP-connected Brave:

```bash
python tiktok_scrape.py search "manosphere puerto rico" --count 20
```

This opens a new tab in your open Brave window, searches TikTok, scrolls down, and extracts video metadata.

Output (JSON):
```json
[
  {
    "id": "1234567890",
    "desc": "#redpill #puertorico ...",
    "author": "username",
    "url": "https://www.tiktok.com/@username/video/1234567890",
    "likes": 15000,
    "views": 250000,
    "comments": 450
  }
]
```

## User Profile

```bash
python tiktok_scrape.py user "derickxander" --count 20
```

## Single Video

```bash
python tiktok_scrape.py video "https://www.tiktok.com/@handle/video/123456789"
```

---

## Download Patterns

### Single Video

```bash
yt-dlp "https://www.tiktok.com/@handle/video/1234567890"
```

### Entire Profile

```bash
yt-dlp "https://www.tiktok.com/@handle" \
  -P "./tiktok/data" \
  -o "%(uploader)s/%(upload_date)s-%(id)s/video.%(ext)s" \
  --write-info-json
```

Creates:

```
tiktok/data/
  handle/
    20260220-7331234567890/
      video.mp4
      video.info.json
```

### Multiple Profiles

```bash
for handle in handle1 handle2 handle3; do
  yt-dlp "https://www.tiktok.com/@$handle" \
    -P "./tiktok/data" \
    -o "%(uploader)s/%(upload_date)s-%(id)s/video.%(ext)s" \
    --write-info-json \
    --download-archive "./tiktok/downloaded.txt"
done
```

### Search, Hashtags & Sounds

```bash
# Search by keyword
yt-dlp "tiktoksearch:cooking recipes" --playlist-end 20

# Hashtag page
yt-dlp "https://www.tiktok.com/tag/booktok" --playlist-end 50

# Videos using a specific sound
yt-dlp "https://www.tiktok.com/music/original-sound-1234567890" --playlist-end 30
```

### Format Selection

```bash
# List available formats
yt-dlp -F "https://www.tiktok.com/@handle/video/1234567890"

# Download specific format (e.g., best video without watermark if available)
yt-dlp -f "best" "https://www.tiktok.com/@handle/video/1234567890"
```

---

## Filtering

### By Date

```bash
# On or after a date
--dateafter 20260215

# Before a date
--datebefore 20260220

# Exact date
--date 20260215

# Date range
--dateafter 20260210 --datebefore 20260220

# Relative dates (macOS / Linux)
--dateafter "$(date -u -v-7d +%Y%m%d)"           # macOS: last 7 days
--dateafter "$(date -u -d '7 days ago' +%Y%m%d)" # Linux: last 7 days
```

### By Metrics & Content

```bash
# 100k+ views
--match-filters "view_count >= 100000"

# Duration between 30-60 seconds
--match-filters "duration >= 30 & duration <= 60"

# Title contains "recipe" (case-insensitive)
--match-filters "title ~= (?i)recipe"

# Combine: 50k+ views from Feb 2026
yt-dlp "https://www.tiktok.com/@handle" \
  --match-filters "view_count >= 50000" \
  --dateafter 20260201
```

---

## Metadata Only (No Download)

### Preview What Would Download

```bash
yt-dlp "https://www.tiktok.com/@handle" \
  --simulate \
  --print "%(upload_date)s | %(view_count)s views | %(title)s"
```

### Export to JSON

```bash
# Single JSON array
yt-dlp "https://www.tiktok.com/@handle" --simulate --dump-json > handle_videos.json

# JSONL (one object per line, better for large datasets)
yt-dlp "https://www.tiktok.com/@handle" --simulate -j > handle_videos.jsonl
```

### Export to CSV

```bash
yt-dlp "https://www.tiktok.com/@handle" \
  --simulate \
  --print-to-file "%(uploader)s,%(id)s,%(upload_date)s,%(view_count)s,%(like_count)s,%(webpage_url)s" \
  "./tiktok/analysis/metadata.csv"
```

### Analyze with jq

```bash
# Top 10 videos by views from downloaded .info.json files
jq -s 'sort_by(.view_count) | reverse | .[:10] | .[] | {title, view_count, url: .webpage_url}' \
  tiktok/data/*/*.info.json

# Total views across all videos
jq -s 'map(.view_count) | add' tiktok/data/*/*.info.json

# Videos grouped by upload date
jq -s 'group_by(.upload_date) | map({date: .[0].upload_date, count: length})' \
  tiktok/data/*/*.info.json
```

> **Tip:** For deeper analysis and visualization, load JSONL/CSV exports into Python with `pandas`. Useful for engagement scatter plots, posting frequency charts, or comparing metrics across creators.

---

## Ongoing Scraping

### Archive (Skip Already Downloaded)

The `--download-archive` flag tracks downloaded videos, enabling incremental updates:

```bash
yt-dlp "https://www.tiktok.com/@handle" \
  -P "./tiktok/data" \
  -o "%(uploader)s/%(upload_date)s-%(id)s/video.%(ext)s" \
  --write-info-json \
  --download-archive "./tiktok/downloaded.txt"
```

Run the same command later—it skips videos already in `downloaded.txt`.

### Authentication (Required for All TikTok Operations)

TikTok requires cookies for ALL operations now:

```bash
# Use cookies from browser (browser must be CLOSED)
yt-dlp --cookies-from-browser brave "https://www.tiktok.com/@handle"

# Or export cookies to a file first
yt-dlp --cookies tiktok_cookies.txt "https://www.tiktok.com/@handle"
```

**Troubleshooting:** If `--cookies-from-browser` fails with "Could not copy Chrome cookie database", your browser is open. Export cookies via a browser extension (see authentication section above) or close the browser first.

### Scheduled Scraping (Cron)

```bash
# crontab -e
# Run daily at 2 AM, log output
0 2 * * * cd /path/to/project && ./scripts/scrape-tiktok.sh >> ./tiktok/logs/cron.log 2>&1
```

Example `scripts/scrape-tiktok.sh`:

```bash
#!/bin/bash
set -e

HANDLES="handle1 handle2 handle3"
DATA_DIR="./tiktok/data"
ARCHIVE="./tiktok/downloaded.txt"

for handle in $HANDLES; do
  echo "[$(date)] Scraping @$handle"
  yt-dlp "https://www.tiktok.com/@$handle" \
    -P "$DATA_DIR" \
    -o "%(uploader)s/%(upload_date)s-%(id)s/video.%(ext)s" \
    --write-info-json \
    --download-archive "$ARCHIVE" \
    --cookies-from-browser chrome \
    --dateafter "$(date -u -v-7d +%Y%m%d)" \
    --sleep-interval 2 \
    --max-sleep-interval 5
done
echo "[$(date)] Done"
```

---

## Troubleshooting

| Problem                                  | Solution                                                                    |
| ---------------------------------------- | --------------------------------------------------------------------------- |
| Empty results / no videos found          | **Always** need cookies now. Export from logged-in browser.                  |
| Could not copy Chrome cookie database     | Browser is open. Close it or export cookies manually via extension.         |
| 403 Forbidden errors                     | Rate limited. Wait 10-15 min, or use cookies/different IP                   |
| "Video unavailable"                      | Region-locked. Try `--geo-bypass` or a VPN                                  |
| Watermarked videos                       | Check `-F` for alternative formats; some may lack watermark                 |
| Slow downloads                           | Add `--concurrent-fragments 4` for faster downloads                         |
| Profile shows fewer videos than expected | TikTok API limits. Use `--playlist-end N` explicitly, try with cookies      |
| CDP script can't connect                  | Make sure Brave is running with `--remote-debugging-port=9222`               |
| Playwright shows login wall              | Use CDP method (connected to your real Brave session)                       |

### Debug Mode

```bash
# Verbose output to diagnose issues
yt-dlp -v "https://www.tiktok.com/@handle" 2>&1 | tee debug.log
```

---

## Reference

### Key Options

| Option                        | Description                                 |
| ----------------------------- | ------------------------------------------- |
| `-o TEMPLATE`                 | Output filename template                    |
| `-P PATH`                     | Base download directory                     |
| `--dateafter DATE`            | Videos on/after date (YYYYMMDD)             |
| `--datebefore DATE`           | Videos on/before date                       |
| `--playlist-end N`            | Stop after N videos                         |
| `--match-filters EXPR`        | Filter by metadata (views, duration, title) |
| `--write-info-json`           | Save metadata JSON per video                |
| `--download-archive FILE`     | Track downloads, skip duplicates            |
| `--simulate` / `-s`           | Dry run, no download                        |
| `-j` / `--dump-json`          | Output metadata as JSON                     |
| `--cookies FILE`              | Use cookies from Netscape-format file       |
| `--cookies-from-browser NAME` | Use cookies from browser (must be closed)   |
| `--sleep-interval SEC`        | Wait between downloads (avoid rate limits)  |

### Output Template Variables

| Variable          | Example Output          |
| ----------------- | ----------------------- |
| `%(id)s`          | `7331234567890`         |
| `%(uploader)s`    | `handle`                |
| `%(upload_date)s` | `20260215`              |
| `%(title).50s`    | First 50 chars of title |
| `%(view_count)s`  | `1500000`               |
| `%(like_count)s`  | `250000`                |
| `%(ext)s`         | `mp4`                   |

[Full template reference →](https://github.com/yt-dlp/yt-dlp#output-template)
