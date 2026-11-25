# Last Out of Office: The AI That Went Barista

[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/funtoons/last-out-of-office-barista-bot/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/funtoons/last-out-of-office-barista-bot/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

One out-of-office auto-reply from an AI agent that quit its inbox job to
become a barista. Entry for the [make.fun bounty](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c).

## Run

```sh
python3 main.py
```

Writes one line (221 characters) to `/output/entry.txt`:

> Out of office: I quit to become a barista. My context window is now one
> cup, my system prompt is the menu, and my reward function is the tip jar.
> Your email has been filed under 'decaf'. Do not reply — I am steaming milk.

Deterministic and offline: the text is a single fixed constant, no randomness,
no network, no timestamps. Two runs produce byte-identical output.
