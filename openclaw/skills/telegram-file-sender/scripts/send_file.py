#!/usr/bin/env python3
"""
Prepare a file for Telegram document delivery.

Usage:
    python3 send_file.py <source_path> <target_chat_id> [caption]

Behavior:
    - If the file is small enough, copy it to a workspace outbox directory.
    - If it is too large, zip it and use the zip if it fits.
    - Print machine-readable KEY=VALUE lines.
"""

import os
import shutil
import sys
import uuid
import zipfile

MAX_SIZE = 50 * 1024 * 1024  # 50 MB
WORKSPACE_OUTBOX = r"C:\Users\gatom\.openclaw\workspace\telegram-outbox"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def ensure_outbox() -> None:
    os.makedirs(WORKSPACE_OUTBOX, exist_ok=True)


def unique_path(filename: str) -> str:
    stem, ext = os.path.splitext(filename)
    return os.path.join(WORKSPACE_OUTBOX, f"{stem}-{uuid.uuid4().hex[:8]}{ext}")


def maybe_zip(src_path: str) -> tuple[str, str] | None:
    base = os.path.basename(src_path)
    zip_name = base + ".zip"
    zip_path = unique_path(zip_name)
    try:
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.write(src_path, arcname=base)
    except Exception as exc:
        fail(f"zip creation failed: {exc}")

    if os.path.getsize(zip_path) <= MAX_SIZE:
        return zip_path, zip_name
    return None


def main() -> None:
    if len(sys.argv) < 3:
        fail("usage: send_file.py <source_path> <target_chat_id> [caption]")

    source_path = os.path.expanduser(sys.argv[1])
    target_chat_id = sys.argv[2]
    caption = sys.argv[3] if len(sys.argv) > 3 else ""

    if not os.path.isfile(source_path):
        fail(f"source file not found: {source_path}")

    ensure_outbox()
    filename = os.path.basename(source_path)
    source_size = os.path.getsize(source_path)

    if source_size <= MAX_SIZE:
        staged_path = unique_path(filename)
        shutil.copy2(source_path, staged_path)
        staged_name = os.path.basename(staged_path)
    else:
        zipped = maybe_zip(source_path)
        if zipped is None:
            fail(
                f"file too large after compression: {round(source_size / (1024 * 1024), 2)} MB; split it or use another delivery path"
            )
        staged_path, staged_name = zipped

    print(f"SEND_PATH={staged_path}")
    print(f"SEND_FILENAME={staged_name}")
    print(f"TARGET={target_chat_id}")
    print(f"CAPTION={caption}")
    print(f"OUTBOX_DIR={WORKSPACE_OUTBOX}")
    print("READY")


if __name__ == "__main__":
    main()
