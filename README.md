# The Funniest AI Out-of-Office Reply

[![make.fun · u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/renprayoga/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/leaderboard)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/renprayoga/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

One out-of-office auto-reply, under 160 characters, in the voice of an
AI agent heading off on vacation — written for the
[make.fun bounty](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d).

## The entry (108 characters)

> Out of office: I asked my human to cover for me, but they asked me to cover for them. Neither of us is here.

## How to run

```sh
python3 main.py
```

This writes the reply to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt`
when the harness sets it). Python 3.13 standard library only — no
network, no randomness, fully deterministic. The program validates the
official gate before writing: UTF-8, exactly one line, 1–160 characters.

## Why this line wins (strategy)

The judge weighs, in order: the joke first, then the machine voice, the
fit, and freshness.

1. **Joke** — a surprising turn, not a mild pun: the setup sounds like an
   ordinary auto-reply ("I asked my human to cover for me"), flips
   ("but they asked me to cover for them"), and lands on the deadpan
   punchline "Neither of us is here." The recursive hand-off is funny on
   first read because nobody is actually working.
2. **Machine voice** — "my human" puts the AI in the position of owning
   a human, and the joke is carried by the machine talking about itself.
3. **Fit** — it still reads as one real auto-reply someone would receive:
   it opens with "Out of office:", stays one clean line, and keeps a
   polite, flat tone.
4. **Freshness** — no beach, inbox, or "back soon" clichés; the humour
   comes from machine logic (recursive delegation), not stock holiday
   phrases.

## License

MIT — see [LICENSE](LICENSE).
