#!/usr/bin/env python3
"""The joke about the demo.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. No network, no input, deterministic output.
"""

import os

JOKE = (
    "My AI agent's favourite fix is deleting the code that crashes "
    "\u2014 yesterday it fixed the demo by deleting the demo."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
