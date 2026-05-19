#!/usr/bin/env python3
"""
VPS connection helper - run commands on pulga-test via Bitvise sexec.
Usage: python vps-exec.py <command>
"""
import subprocess
import sys
import shlex

SEXEC = r"C:\Program Files (x86)\Bitvise SSH Client\sexec.exe"
HOST = "45.61.50.129"
PORT = "2222"
USER = "boss"
PASS = "@ssh0l3"

def run(cmd: str):
    args = [
        SEXEC,
        f"-host={HOST}",
        f"-port={PORT}",
        f"-user={USER}",
        f"-pw={PASS}",
        "-cmd=" + cmd,
    ]
    result = subprocess.run(args, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result.returncode

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python vps-exec.py '<command>'", file=sys.stderr)
        sys.exit(1)
    cmd = " ".join(sys.argv[1:])
    sys.exit(run(cmd))
