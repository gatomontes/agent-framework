#!/usr/bin/env python3
"""Fetch YouTube transcript, with optional VPN support."""

import sys
import json
import subprocess
import requests
import os
from requests.adapters import HTTPAdapter
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

VPN_INTERFACE = "wg0"
VPN_SOURCE_IP = "10.100.0.2"
LANGUAGES = ["en", "fr", "de", "es", "it", "pt", "nl"]

class SourceIPAdapter(HTTPAdapter):
    """Bind requests to a specific source IP if available."""
    
    def __init__(self, source_ip=None, **kwargs):
        self.source_ip = source_ip
        super().__init__(**kwargs)
    
    def init_poolmanager(self, *args, **kwargs):
        if self.source_ip:
            kwargs["source_address"] = (self.source_ip, 0)
        super().init_poolmanager(*args, **kwargs)

def check_vpn():
    """Check if WireGuard VPN is up and has recent handshake."""
    if not os.path.exists("C:\\Program Files\\WireGuard\\wg.exe"):
        return True, "VPN not configured, skipping"
    try:
        result = subprocess.run(["wg", "show", VPN_INTERFACE], capture_output=True, text=True, timeout=5)
        if result.returncode != 0: return False, "VPN interface not found"
        if "latest handshake" not in result.stdout: return False, "No VPN handshake established"
        return True, "VPN connected"
    except Exception as e: return False, str(e)

def bring_up_vpn():
    """Attempt to bring up VPN."""
    try:
        subprocess.run(["wg-quick", "up", VPN_INTERFACE], capture_output=True, timeout=10)
        subprocess.run(["ip", "rule", "add", "from", VPN_SOURCE_IP, "table", "51820"], capture_output=True, timeout=5)
        return check_vpn()
    except Exception as e: return False, str(e)

def extract_video_id(url_or_id):
    import re
    patterns = [r"(?:v=|/v/|youtu\.be/|/embed/)([a-zA-Z0-9_-]{11})", r"^([a-zA-Z0-9_-]{11})$"]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match: return match.group(1)
    return url_or_id

def fetch_transcript(video_id, languages=None, use_vpn=False):
    if languages is None: languages = LANGUAGES
    session = requests.Session()
    if use_vpn:
        session.mount("http://", SourceIPAdapter(VPN_SOURCE_IP))
        session.mount("https://", SourceIPAdapter(VPN_SOURCE_IP))
    else:
        session.mount("http://", SourceIPAdapter())
        session.mount("https://", SourceIPAdapter())
    
    api = YouTubeTranscriptApi(http_client=session)
    transcript = api.fetch(video_id, languages=languages)
    return [{"text": entry.text, "start": entry.start, "duration": entry.duration} for entry in transcript]

def get_video_title(video_id):
    try:
        resp = requests.get(f"https://noembed.com/embed?url=https://www.youtube.com/watch?v={video_id}", timeout=10)
        data = resp.json()
        return data.get("title", "Unknown"), data.get("author_name", "Unknown")
    except: return "Unknown", "Unknown"

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: fetch_transcript.py <video_id_or_url> [languages] [use_vpn=0|1]"}))
        sys.exit(1)
    
    video_input = sys.argv[1]
    languages = sys.argv[2].split(",") if len(sys.argv) > 2 else LANGUAGES
    use_vpn = sys.argv[3] == "1" if len(sys.argv) > 3 else False
    
    video_id = extract_video_id(video_input)
    
    if use_vpn:
        vpn_ok, vpn_msg = check_vpn()
        if not vpn_ok:
            vpn_ok, vpn_msg = bring_up_vpn()
            if not vpn_ok:
                print(json.dumps({"error": f"VPN not available: {vpn_msg}"}))
                sys.exit(1)
    
    title, author = get_video_title(video_id)
    try:
        transcript = fetch_transcript(video_id, languages, use_vpn)
        full_text = " ".join([entry["text"] for entry in transcript])
        print(json.dumps({
            "video_id": video_id, "title": title, "author": author,
            "language": languages[0] if transcript else None,
            "entries": len(transcript), "full_text": full_text
        }))
    except Exception as e:
        print(json.dumps({"error": str(e), "video_id": video_id}))
        sys.exit(1)

if __name__ == "__main__":
    main()
