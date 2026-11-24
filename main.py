#!/usr/bin/env python3
"""One-line office joke entry for the make.fun bounty
"Make the AI Judge Laugh: the Office Joke Open".

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and prints exactly the same line.
"""

import os

JOKE = "My boss called it a 'quick sync' — an hour later I'm nodding along to a spreadsheet nobody understands, including the person presenting it."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(JOKE)


if __name__ == "__main__":
    main()
