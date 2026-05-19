---
name: youtube-transcript-fetcher
description: Skill to fetch YouTube video transcripts by URL. Uses a Python script to extract and parse metadata and text content from available video transcripts.
---

# YouTube Transcript Fetcher

## Metadata

| Property | Value |
|----------|-------|
| Skill ID | YOUTUBE-TRANSCRIPT-01 |
| Version | 1.0 |
| Last Updated | 2026-04-10 |

## Overview
This skill fetches the text transcript of a YouTube video given its URL. It relies on the `youtube_transcript_api` and handles language fallbacks automatically.

## Usage
To use this skill, call the script directly with the YouTube video URL:

```bash
python3 ~/.openclaw/skills/youtube-transcript-fetcher/scripts/fetch_transcript.py <youtube_url>
```

## Setup & Dependencies
- Requires `requests` and `youtube-transcript-api` Python packages.
- Ensure your environment has network access (or configure the script's VPN/proxy settings if required by your specific network environment).

## Behavioral Rules
1. **Always** check if the URL provided is a valid YouTube link.
2. **Handle errors** gracefully, specifically `TranscriptsDisabled` and `NoTranscriptFound`.
3. **Output** is a JSON object containing the `title`, `author`, `language`, and the `full_text` of the transcript.

## Version History
| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-04-10 | Initial installation based on version 1.0.1 source. |
