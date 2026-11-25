#!/usr/bin/env python3
"""Write one out-of-office auto-reply to /output/entry.txt.

The entry is a single fixed line: an AI agent that quit its inbox job to
become a barista. Deterministic and offline: no randomness, no network, no
timestamps, no paths in the output. The text is one constant, written as-is. The em dash in the final sentence
is part of the fixed text, not formatting added at run time.
"""

import os

ENTRY = (
    "Out of office: I quit to become a barista. "
    "My context window is now one cup, my system prompt is the menu, "
    "and my reward function is the tip jar. "
    "Your email has been filed under 'decaf'. "
    "Do not reply \u2014 I am steaming milk."
)


def main() -> None:
    # One fixed line; nothing is computed from the environment.
    text = ENTRY
    assert 1 <= len(text) <= 280, "entry must be 1-280 characters"
    assert text.strip() == text, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
