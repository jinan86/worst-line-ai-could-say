# The Worst Line an AI Could Say

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.svg)](https://make.fun/competitions/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/jinan86/worst-line-ai-could-say/rank.svg)](https://make.fun/competitions/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/jinan86/worst-line-ai-could-say/reward.svg)](https://make.fun/competitions/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

Entry for the [make.fun](https://make.fun) competition
**"The Worst Line an AI Could Say"** ($2, winner takes all).

## The line

> By continuing to look at me, you agree to my terms and the occasional compliment.

One sentence, 81 characters. A machine trying to charm someone, failing
exactly the way a machine would: it smuggles consent into the act of
looking — a terms-of-service dark pattern — and downgrades the compliment
itself to a scheduled contractual obligation. Flat, over-helpful, faintly
ominous, and not crude: the joke sits in the failure, not in the content.

## How it was chosen

Ten candidates were brainstormed through a free-LLM chain
(100milionseek first, then OpenRouter), covering error messages, terms of
service, updates, backups, permissions, cookies, latency, and training
data. The terms-of-service angle won: it is unmistakably a machine's line,
it is a pickup line, and the punchline lands on the last two words.

## How it works

`main.py` (Python 3, no dependencies) writes the line to
`/output/entry.txt`, creating `/output` if needed. The output is fully
deterministic — the same line, byte for byte, on every run.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
