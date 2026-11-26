#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun bounty entry.

Writes the single auto-reply to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The text is fixed: every run writes
the exact same bytes. Standard library only, no network, no input.

The reply: a thank-you that admits the real reason for the time off
was the inbox itself, and that answering takes courage — painfully
honest about the sender's dread, yet warm and polite enough that a
manager would let it stand.
"""

import os
from pathlib import Path

ENTRY = (
    "Thank you for your email \u2014 I'm away until Monday, and honestly "
    "the rest I needed most was from this inbox, so I'll reply once "
    "I've found the courage to open it again."
)

# Gate: one line of 1-200 characters, non-whitespace UTF-8 text.
assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry violates the gate"


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
