#!/usr/bin/env python3
"""
Convert TikTok cookies from JSON (EditThisCookie export) to Netscape format (yt-dlp compatible).

Usage:
    python convert_cookies.py cookies.json [cookies.txt]

If output file is omitted, writes to tiktok_cookies.txt
"""
import json, sys

with open(sys.argv[1]) as f:
    cookies = json.load(f)

out = sys.argv[2] if len(sys.argv) > 2 else "tiktok_cookies.txt"

lines = ["# Netscape HTTP Cookie File"]
for c in cookies:
    domain = c.get("domain", "")
    flag = "TRUE" if domain.startswith(".") else "FALSE"
    path = c.get("path", "/")
    secure = "TRUE" if c.get("secure", False) else "FALSE"
    exp = str(int(c.get("expirationDate", 0)))
    name = c.get("name", "")
    value = c.get("value", "")
    lines.append("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
        domain, flag, path, secure, exp, name, value))

with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print("Written {} cookies to {}".format(len(cookies), out))
