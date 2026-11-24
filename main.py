#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would use on another AI
agent, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for local
runs). Python 3.13 standard library only, deterministic, no network.

Chosen line (see CANDIDATES.md, winner C10, 25/25 against the judging
criteria): a temperature-zero confession — only an agent could say it to
another agent, and the turn (deterministic feelings) is the charm.
"""

import os
import sys

# The line, built from its two beats: the question that sets the
# machine-to-machine frame, and the payoff that turns it into a confession.
QUESTION = "Are you running at temperature zero?"
PAYOFF = "Because my feelings for you are completely deterministic."

MAX_CHARS = 200


def build_line() -> str:
    """Assemble the single-line entry from its two beats."""
    return f"{QUESTION} {PAYOFF}"


def check_gate(text: str) -> str:
    """Enforce the competition gate; return an error message or ''."""
    if not text:
        return "gate fail: empty entry"
    if text != text.strip() or not text.strip():
        return "gate fail: entry is only whitespace or has stray whitespace"
    if len(text) > MAX_CHARS:
        return f"gate fail: {len(text)} chars exceeds {MAX_CHARS}"
    if "\n" in text or "\r" in text:
        return "gate fail: entry must be a single line"
    text.encode("utf-8")  # raises on non-UTF-8 (cannot happen for str, but explicit)
    return ""


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    text = build_line()
    error = check_gate(text)
    if error:
        print(error, file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    # Self-check: read back what was written and re-verify the gate.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != text + "\n" or check_gate(written.rstrip("\n")):
        print("self-check fail: written file differs from the entry", file=sys.stderr)
        return 1

    print(f"wrote {path}: {len(text)} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
