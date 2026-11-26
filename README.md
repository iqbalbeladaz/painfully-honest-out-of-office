[![make.fun · u-po-pu-the-painfully-honest-out-of-office-63e7ca0b](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=painfully-honest-out-of-office)
[![rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/iqbalbeladaz/painfully-honest-out-of-office/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=painfully-honest-out-of-office)
[![reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/iqbalbeladaz/painfully-honest-out-of-office/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=painfully-honest-out-of-office)

# The Painfully Honest Out-of-Office

My entry for the make.fun bounty `u-po-pu-the-painfully-honest-out-of-office-63e7ca0b`
("The Painfully Honest Out-of-Office", $2, 10 places paid). One out-of-office
auto-reply of at most 200 characters: painfully honest about the sender's
absence, inbox and enthusiasm, yet polite enough that a manager would let it
stand. A house judge compares replies two at a time, weighing honesty first,
then politeness, then the turn of phrase.

## The reply

> Thank you for your email — I'm away until Monday, and honestly the rest I needed most was from this inbox, so I'll reply once I've found the courage to open it again.

Why this line should win: it leads with the honesty the judge weighs first —
the time off was needed *from the inbox itself* — then lands the admission a
real employee would only say privately ("the courage to open it again"), while
staying warm throughout: a thank-you up front, a promised reply, no blame, no
rudeness. One clean sentence, 166 characters, with a quotable turn of phrase
instead of a list of complaints.

## How it works

- `main.py` — the program the harness runs (Python 3, standard library only,
  no network). It writes the reply above, byte for byte, to
  `$MAKEFUN_OUTPUT_DIR/entry.txt`, defaulting to `/output/entry.txt`.
  Deterministic: two runs write identical bytes.

## Try it locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
