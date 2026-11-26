#!/usr/bin/env python3
"""The Self-Checkout Is Judging You — make.fun entry.

Writes one funny line in the voice of a smug self-checkout machine to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line is aimed at the shopper the brief names — twelve yoghurts and
nothing else — and lands its sting on the bagging area, the machine's
home turf: the basket is judged, the shopper is judged, and the shame
gets bagged like any other item.

The file holds exactly the line, with no trailing newline, so the gated
character count is the line's own length (93 characters).
"""

import os
import stat

ENTRY = (
    "Twelve yoghurts and nothing else. Bold strategy. "
    "Please place your shame in the bagging area."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main():
    # Gate self-check: 1-200 characters, not only whitespace.
    if not (MIN_CHARS <= len(ENTRY) <= MAX_CHARS):
        raise SystemExit(
            "entry is %d characters, outside the 1-200 gate" % len(ENTRY)
        )
    if not ENTRY.strip():
        raise SystemExit("entry is only whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"

    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    os.replace(tmp, target)
    os.chmod(target, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
