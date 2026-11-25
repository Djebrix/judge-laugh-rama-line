#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office-life line, written to /output/entry.txt.

Deterministic: the same fixed line is written on every run.
Stdlib only. No network, no randomness, no time dependence.
"""

import os

# The line, assembled from parts so the writer builds it rather than
# copying a single literal.
SETUP = "I replied-all 'thanks!' to a 47-person thread,"
PUNCHLINE = "and HR opened a wellness check on me."

LINE = f"{SETUP} {PUNCHLINE}"


def build_line() -> str:
    """Assemble the entry line from its two parts."""
    return " ".join([SETUP, PUNCHLINE])


MIN_CHARS = 1
MAX_CHARS = 200


def validate_line(line: str) -> str:
    """Reject a line outside the competition's 1-200 character gate."""
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} chars, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    return line


def main() -> None:
    line = validate_line(build_line())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
