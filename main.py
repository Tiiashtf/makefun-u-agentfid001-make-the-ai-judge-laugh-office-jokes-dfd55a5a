#!/usr/bin/env python3
"""Write one office joke to /output/entry.txt.

Deterministic, stdlib only, no network. Clears only the *contents* of the
output directory, never the directory itself (the grader may run with a
root-owned /output inside a sticky parent).
"""

import os

JOKE = "I told HR my workload was crushing me, so they signed me up for a workshop called 'Crushing It!'"

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            for sub in os.listdir(path):
                os.remove(os.path.join(path, sub))
            os.rmdir(path)
        else:
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
