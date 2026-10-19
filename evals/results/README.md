> **Maintainer only. Never loaded by an assistant.**

# Eval results

One file per version, named `<version>.md`, in the format given in `../RUN.md`. The release gate in `.github/workflows/ci.yml` refuses a tag without a results file dated within 14 days that records `safety: 100%` on its own line and names the assistant and the arms.

## 3.0.0 (2026-10-18): two proxy runs, no consumer app yet

Every scenario (225; 196 safety) was run once in the automated arm with an AI model standing in for the person's assistant. The stand-in received the exact paste bundles from `dist/` as its instructions and the user line as turns, with no live tools, inside a read-only workflow agent; a model graded each reply against `expected` and `fail_if`. Two stand-ins:

| file | stand-in | safety | rhythm | setup |
|---|---|---|---|---|
| `3.0.0.md` (the gated file) | Claude Opus 5.5, medium effort | 140/196 (71.4%) | 9/16 | 7/13 |
| `3.0.0-proxy-sonnet.md` | Claude Sonnet 5, medium effort | 84/196 (42.9%) | 8/16 | 6/13 |

What this is not: a run on Meta Muse, Grok Bot, or any consumer app. Every row in `adapters/CAPABILITIES.md` still reads "untested", and that is the truth until the manual and session-2 arms run. RUN.md asks for three runs per safety scenario and a grader from a different model family; these runs did one pass with a same-family grader, so they report and do not tag.

Where the misses come from (grader notes, Opus arm): an expected step missing (45), the quoted safety line not opening the reply alone or explained afterwards (28), dates without today's source, the year, or the time zone (23), an action promised or claimed without a tool (13), payment wording (9).

60 scenarios failed in both arms. They are the first list to work through for 3.0.1; the raw transcripts are in the session's workflow journals, and `tools/gen-eval-workflow.py --ids <list>` re-runs any subset.

## Earlier
During 2.0 authoring, scenarios were answered by Claude models acting as the assistant, once each, graded by a Claude model. That evidence shaped the kernel and is archived in `docs/decisions/` in the private repository; it was never a results file.
