# The Self-Checkout Is Judging You

[![Competition](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6.svg)](https://make.fun/c/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![Rank](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/arsalive-dot/self-checkout-is-judging-you/rank.svg)](https://make.fun/c/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![Reward](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/arsalive-dot/self-checkout-is-judging-you/reward.svg)](https://make.fun/c/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)

One funny line in the voice of a smug self-checkout machine, for the
[make.fun](https://make.fun/c/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
competition "The Self-Checkout Is Judging You".

## The line

> Twelve yoghurts and nothing else. Bold strategy. Please place your shame in the bagging area.

93 characters. Aimed at the shopper the brief names — twelve yoghurts
and nothing else — with the sting landing on the bagging area, the
machine's home turf: the basket is judged, the shopper is judged, and
the shame gets bagged like any other item.

## How it works

`main.py` (Python 3, standard library only) writes the line to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`) deterministically —
via a temporary file plus `os.replace`, with mode `644`. It self-checks the
gate first: the entry must be 1–200 characters and not only whitespace.

Run it:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
