#!/usr/bin/env python3
# Entry for the make.fun bounty "The Funniest Sick-Day Excuse":
# writes a fixed one-line excuse, under 200 characters, to
# /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""Write the sick-day excuse entry to /output/entry.txt.

Entry for the make.fun bounty "The Funniest Sick-Day Excuse":
one line, under 200 characters, that someone could send to call
in sick. This program writes that line to entry.txt.
"""

import os
import sys

TEXT = "My doctor diagnosed me with acute Monday-itis and prescribed 48 hours of not answering Slack."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
