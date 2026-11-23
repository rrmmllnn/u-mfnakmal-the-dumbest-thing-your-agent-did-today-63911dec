#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today.

Writes a single line (at most 200 characters) about the dumbest thing
my agent did today to /output/entry.txt. Deterministic: the line is
fixed, so every run produces byte-identical output.
"""

import os

LINE = (
    "My agent told me to send my login code at once, then admitted "
    "the tab it needed was already dead \u2014 killed by a VM restart."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
