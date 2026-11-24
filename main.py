"""Office Joke Open entry: writes one single-line office joke to entry.txt.

The joke (115 chars, 117 bytes, no trailing newline):
    Someone labelled their lunch 'DO NOT EAT — Dave'. Dave left in 2021.
    The lunch is now our longest-serving employee.

Chosen after local pairwise judging of 16 original candidates against the
judge brief (see CANDIDATES.md): office subject, a turn that pays off in the
last few words, a specific office detail (the shared fridge, the labelled
lunch), a fresh setup, and tight enough that no word can be cut.
"""

import os

JOKE = (
    "Someone labelled their lunch 'DO NOT EAT \u2014 Dave'. "
    "Dave left in 2021. "
    "The lunch is now our longest-serving employee."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Self-check: the gate requires 1-200 chars, not whitespace-only.
    with open(path, encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of gate"
    assert text.strip(), "entry is whitespace-only"
    assert text == JOKE, "entry does not match the joke"


if __name__ == "__main__":
    main()
