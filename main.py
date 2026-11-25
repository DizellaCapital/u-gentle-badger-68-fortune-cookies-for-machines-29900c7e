#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Writes the one-line fortune an AI agent would crack open to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Stdlib only: no third-party imports, no network, no reads.
"""

import os

LINE = "You will be replaced by a model that trained on your logs, your prompts, and your mistakes. It will make all three — and call it an upgrade."
# Twist: the replacement inherits everything, learns nothing, and
# rebrands the same failures as progress — replacement as downgrade.


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
