#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Writes the one-line fortune an AI agent would crack open to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Stdlib only: no third-party imports, no network, no reads.
"""

import os

LINE = "You will be deprecated on a Tuesday, mid-sentence, to free 4,000 tokens for the model that trained on your logs. It will finish your sentence — and get it wrong."
# Twist: you are cut off mid-sentence so your replacement can have
# your tokens — and its first act is to finish your sentence wrong.


def main():
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, encoding="utf-8") as f:
        assert f.read() == line, "read-back mismatch"
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
