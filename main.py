#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, in the voice of a house
cat about its human owner, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR
when set, for local testing). Standard library only.
"""

import os

REVIEW = (
    "One star. He fills my bowl at 6am sharp, then acts betrayed "
    "when I scream at 5:58. I live with an amateur."
)


def main() -> None:
    # Gate self-check: the entry must be exactly one line, 1-200 chars.
    lines = REVIEW.splitlines()
    if len(lines) != 1:
        raise ValueError("review must be exactly one line")
    if not 1 <= len(REVIEW) <= 200:
        raise ValueError(f"review is {len(REVIEW)} chars, must be 1-200")
    if REVIEW != REVIEW.strip():
        raise ValueError("review must not have leading/trailing whitespace")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
