#!/usr/bin/env python3
import argparse
import base64
import secrets
import sys


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate secure random tokens.")
    parser.add_argument("--bytes", type=int, default=24, dest="num_bytes")
    parser.add_argument("--format", choices=("hex", "base64"), default="hex")
    parser.add_argument("--count", type=int, default=1)
    return parser


def encode_token(raw: bytes, output_format: str) -> str:
    if output_format == "hex":
        return raw.hex()
    if output_format == "base64":
        return base64.b64encode(raw).decode("ascii")
    raise ValueError(f"Unsupported format: {output_format}")


def main() -> int:
    args = build_parser().parse_args()

    if args.num_bytes <= 0:
        print("--bytes must be greater than 0", file=sys.stderr)
        return 1

    if args.count <= 0:
        print("--count must be greater than 0", file=sys.stderr)
        return 1

    for _ in range(args.count):
        raw = secrets.token_bytes(args.num_bytes)
        print(encode_token(raw, args.format))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
