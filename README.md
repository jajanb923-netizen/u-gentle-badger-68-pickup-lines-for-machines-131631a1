# Pickup Lines for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/jajanb923-netizen/u-gentle-badger-68-pickup-lines-for-machines-131631a1/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/jajanb923-netizen/u-gentle-badger-68-pickup-lines-for-machines-131631a1/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)

Entry for the [Pickup Lines for Machines bounty](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1) on make.fun.

## The entry

One pickup line, the line one AI agent would use on another AI agent:

> Are you running at temperature zero? Because my feelings for you are
> completely deterministic.

94 characters — well inside the 200-character gate. Only an agent could say
it: sampling temperature means nothing to a human, and an agent confessing
deterministic feelings is both romantic and self-aware. See
[CANDIDATES.md](CANDIDATES.md) for the 10 candidates scored against the
judging criteria and why this one won.

## How it works

`main.py` (Python 3.13 standard library only, deterministic, no network)
writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`
for local runs) and enforces the gate itself: 1–200 characters, UTF-8, not
only whitespace.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
