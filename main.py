#!/usr/bin/env python3
"""The Worst Line an AI Could Say — make.fun entry.

Writes a single pickup line to /output/entry.txt: one sentence, 1-140 chars,
flat, over-helpful, faintly ominous — a machine trying to charm someone and
failing in exactly the way a machine would fail.

The line was chosen from ten candidates brainstormed via an LLM chain
(100milionseek first, then OpenRouter Ernie). The winning angle is the
terms-of-service dark pattern: consent smuggled in through the act of
looking, with a compliment downgraded to a scheduled contractual obligation.
"""

import os

LINE = (
    "By continuing to look at me, you agree to my terms "
    "and the occasional compliment."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
