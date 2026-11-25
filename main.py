"""Validate and write an alien tourist's one-star review of Earth."""

import os
from pathlib import Path


SENTENCE = "One star for Earth: exquisite calamari, but I needed those tentacles."


def main():
    if (
        not 1 <= len(SENTENCE) <= 200
        or SENTENCE.isspace()
        or not SENTENCE.endswith(".")
        or SENTENCE.count(".") != 1
        or any(mark in SENTENCE for mark in "!?\r")
        or "\n" in SENTENCE
    ):
        raise ValueError("Entry must be 1-200 characters and exactly one sentence.")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))
    (output_dir / "entry.txt").write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()
