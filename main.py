#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — a single funny cat joke.

Writes one original one-line cat joke (<=199 chars) to /output/entry.txt.
Stdlib only; no network, no reads outside the repo.

The joke: the cat crashes a job interview by sitting on the keyboard and
gets hired. The turn lands twice — first the absurd promotion, then the
kicker that the new boss licks himself in meetings. It is a setup the
reader recognises (cat on keyboard, remote-work life), a surprise (the cat
gets the job, not the human), and a punchline that needs no explaining.
No stock cat puns, no knock-things-off-the-table trope.
"""

import os

LINE = (
    "My cat sat on my keyboard during my job interview and got "
    "hired \u2014 I now report to a manager who licks himself in meetings."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 199, f"line is {len(text)} chars, must be 1-199"
    assert "\n" not in text, "entry must be exactly one line"
    assert "  " not in text, "entry must not contain double spaces"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
