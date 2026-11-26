#!/usr/bin/env python3
"""The Self-Checkout Is Judging You — make.fun entry.

Writes one funny line in the voice of a smug self-checkout machine to
/output/entry.txt and prints it. The line is the whole entry: a machine
that remembers its regulars, reads a basket like a diary, and takes its
revenge in the pettiest way it knows how — receipt speed.
"""

import os

LINE = (
    "Third breakup basket this month: ice cream, painkillers, tissues. "
    "I won't ask questions. "
    "I'll just print your receipt very, very slowly."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
