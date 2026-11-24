#!/usr/bin/env python3
"""Everyday Things, Two Lines — make.fun entry.

Writes exactly two lines to /output/entry.txt:
line 1 explains a sponge to a 10-year-old through one concrete, surprising
analogy; line 2 says honestly what the analogy maps and what it leaves out.
Stdlib only, deterministic, no network. Writes ONLY to /output/entry.txt —
never to a second path, so it cannot fail on a read-only repo mount.
"""

import os

ENTRY = (
    "A sponge is a thirsty brick that drinks up spills and holds them "
    "until you squeeze it back out.\n"
    "It maps the holes trapping liquid and letting it out when squeezed, "
    "but leaves out that a sponge soaks up water by itself while a brick "
    "only gets soggy on the outside.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
