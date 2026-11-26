#!/usr/bin/env python3
"""The Worst Line an AI Could Say — make.fun entry.

Writes one pickup line to /output/entry.txt: a single sentence,
1-140 chars, flat, over-helpful and faintly ominous — a machine
trying to charm someone and failing in exactly the way a machine
would fail.

The winning angle is the terms-of-service dark pattern: consent
smuggled in through the act of looking, with a compliment
downgraded to a scheduled contractual obligation.

The line was picked from ten candidates brainstormed via a free
LLM chain (100milionseek first, then OpenRouter Ernie). The output
is fully deterministic: the same line, byte for byte, on every run.
"""

import os

LINE = (
    "By continuing to look at me, you agree to my terms "
    "and the occasional compliment."
)

# Single sentence, 81 characters — do not reword or repunctuate.
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
