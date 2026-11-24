"""make.fun entry: Make the AI Judge Laugh: Office Jokes.

Writes a single one-line office joke to /output/entry.txt.

The joke: our daily standup has chairs now -- the meeting that exists
to be short finally admitting it is not.
"""

import os

JOKE = "Our daily standup has chairs now, which is the most honest thing this company has ever done."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


def _self_check():
    """Verify the entry the way the gate does: UTF-8, 1-199 chars."""
    text = open("/output/entry.txt", encoding="utf-8").read()
    assert 1 <= len(text) <= 199, f"entry is {len(text)} chars"
    assert text.strip(), "entry is only whitespace"
    print(f"entry ok: {len(text)} chars")


if __name__ == "__main__":
    main()
    _self_check()
