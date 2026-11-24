# One Sentence for a Traveler from 1800 — Sparta entry

[![make.fun · u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![rank](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/bayusantosz3995/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb-sparta/rank.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/leaderboard)
[![reward](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/bayusantosz3995/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb-sparta/reward.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)

One sentence, at most 200 characters, explaining the modern internet to a time traveler from 1800 — in words they could have known. The internet as a library that writes itself: every book in the world on one shelf, the ink still wet, a thousand strangers arguing in the margins as you read.

> Picture a library where every book in the world sits on one shelf, the ink still wet, and a thousand strangers write in the margins all at once, arguing with you as you read.

## Run

```sh
python3 main.py
```

`main.py` gates the sentence (one sentence, 1–200 chars, not whitespace-only), writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt`), reads it back and verifies it byte-for-byte, exiting non-zero on gate failure.
