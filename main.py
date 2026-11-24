"""One Sentence for a Traveler from 1800 — Sparta entry.

A single sentence that explains the modern internet to a time traveler
from 1800, using only words and ideas available in their time: you step
into a self-writing library, every book on one shelf, ink still wet, a
thousand strangers writing a thousand margin notes per page read.

Period-vocabulary rule: no word coined after 1800 (no internet, computer,
phone, email, website, app, wifi, online, digital, screen) — the picture
must hold in a mind that knows libraries, presses, ink and letters.
The sentence opens on its main verb ("You step into") so it reads as one
complete sentence, not a fragment.
"""

import os
import sys

TEXT = (
    "You step into a library where every book in the world sits on one "
    "shelf, the ink still wet, and a thousand strangers write a thousand "
    "notes in the margins before you finish a page."
)


def main() -> int:
    # Gate: one sentence, 1-200 characters, not whitespace-only.
    if not TEXT.strip():
        print("gate failed: empty text", file=sys.stderr)
        return 1
    if len(TEXT) > 200:
        print(f"gate failed: {len(TEXT)} chars > 200", file=sys.stderr)
        return 1
    if TEXT.count(".") != 1 or not TEXT.endswith("."):
        print("gate failed: must be exactly one sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != TEXT:
        print("gate failed: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(TEXT)} chars, 1 sentence)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
