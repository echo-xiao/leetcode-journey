# leetcode-journey

My LeetCode practice log: code, problems, approach notes, elements, and retrospectives — one folder per problem.

## What each problem folder contains

```
Problems/104_maximum-depth-of-binary-tree/
  README_CN.md    Index: difficulty, tags, links to the files below
  problem.md      Problem statement
  pseudocode.md   One-line essence / overall approach / full pseudocode / complexity
  elements.md     This problem's "elements" — the blanks you must fill in before writing code
  review.md       My own retrospective; highlighted parts are where I got stuck at the time
  solution_*.py   Every accepted version of my code
```

The slots in `elements.md` are maintained per problem pattern (18 patterns, defined in
`lc_review/element_essentials.py`); the answers are filled in per problem. For example,
the four slots for binary-tree problems are: function definition, base case, per-level
body, and code position.

## Daily workflow

After solving problems and writing the retrospective in Notion, run one command:

```bash
python3 -m lc_review.cli sync-all --apply
```

It performs seven steps in a fixed order — the order matters: a problem has to exist
before its retrospective has somewhere to go; the review-tracker row has to exist before
the retrospective column can be written; and the app content bundle must be packaged
last, otherwise it would still contain the previous round's `Problems/*/review.md` and
the phone would receive stale content:

1. Refresh accepted-submission times for recently re-solved problems
2. Pull newly accepted problems from LeetCode, generate the four files, and create a
   row in the Notion review-tracker database
3. Refresh old problems whose solution changed: take the 20 most recent accepted
   submissions from LeetCode and compare each problem's code structure; only when a
   structurally new solution appears does it re-download the code and regenerate the
   pseudocode and elements. Renaming a variable doesn't count; switching to a
   different approach does
4. Generate element answers for new problems (one Claude call per problem)
5. Write the Notion retrospectives into each problem's `review.md`
6. Write the retrospectives into the review-tracker's retrospective column in Notion,
   carrying the orange highlights along
7. Package `Problems/` into `app/content.json` for the iOS app to download

### No need to run it by hand

`scripts/sync_daily.sh` runs the pipeline above automatically at 3:00 AM every day via
launchd, then commits only `Problems/`, `app/content.json`, and
`lc_review/data_elements/` and pushes. If the Mac is asleep the run isn't skipped — it
catches up after waking. Logs live in `logs/` and are kept for 14 days.

A failure pops a macOS notification; success stays silent. The most common failure is
an expired LeetCode session — once every few weeks; log back in on Chrome and put the
cookie back into `.env`. The other one is not being on `main` at the time — the
scheduled job refuses to commit on any other branch, skips the run, and notifies.

Install:

```bash
ln -sf "$PWD/scripts/com.echoxiao.leetcode-journey.sync.plist" \
   ~/Library/LaunchAgents/com.echoxiao.leetcode-journey.sync.plist
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.echoxiao.leetcode-journey.sync.plist
```

Uninstall:

```bash
launchctl bootout gui/$(id -u)/com.echoxiao.leetcode-journey.sync
```

Without `--apply` it's a dry run: it only reports what it would do and writes nothing,
including the final `app/content.json`. Three of the first four steps write outside the
working tree (Notion has no undo), so writing is explicit.

Run a single step on its own:

```bash
python3 -m lc_review.cli sync-new --apply        # only pull new problems
python3 -m lc_review.cli build-answers --apply   # only fill in element answers
python3 -m lc_review.cli sync-review-md --apply  # only update review.md
python3 -m lc_review.cli sync-fupan --apply      # only update the Notion retrospective column
```

## Flashcards

```bash
python3 -m lc_review.cli export-anki
```

Generates `anki/elements.tsv`; import it in Anki via File → Import. One card per
problem: the front is the problem, the back is how this problem's elements are filled
in. Cards are tagged by problem pattern, so you can drill a single category.

`anki/` is not under version control — it is generated from `Problems/` and one command
recreates it.

## Content for the phone app

```bash
python3 -m lc_review.cli export-app
```

Generates `app/content.json`: each problem's statement, elements, pseudocode,
retrospective, and real code packed into one file, which the iOS app pulls from GitHub
Raw on launch. This is already hooked in as the last step of `sync-all`.

**This file must be committed and pushed** — the opposite of `anki/`. GitHub Raw can
only serve committed files, so this generated artifact is a deliberate exception; don't
add `app/` to `.gitignore`. If the file is regenerated but not pushed, the phone keeps
getting stale content, with no error to tell you.

When the content hasn't changed the command doesn't rewrite the file, so the daily
`sync-all` run doesn't produce empty diffs.

## The phone app

`app/ios/LCReview.xcodeproj`, SwiftUI, iOS 17+, zero third-party dependencies.

Open it in Xcode, select your iPhone, hit Run, and it's installed. On launch it pulls
`app/content.json` from GitHub Raw, so after adding new problems you only need to let
`sync-all` finish and push — no reinstall needed. (GitHub Raw has CDN caching; a push
takes a few minutes to take effect.)

Review state lives on the phone only — no cloud, no account. Deleting the app loses
the schedule but not the problem content — reinstall and it re-downloads.

The heatmap and streak on the home screen show LeetCode's submission history; every
time the app returns to the foreground it fetches directly from `leetcode.com/graphql`,
bypassing this repository. Cell intensity is the number of submissions that day,
matching the chart on your leetcode.com profile. Days are split by UTC, so the
rightmost cell may differ from your local "today" by one day — this mirrors LeetCode
exactly and is not a bug; the API only returns per-day aggregates, so it can't be
corrected accurately.

If the fetch fails it draws the last successful result and labels it "data as of
<date>" at the top; if it has never succeeded it draws an empty grid with a "LeetCode
data unavailable" message. The two messages differ on purpose: if both cases were drawn
as empty cells, "no data" would read as "didn't practice".

This is the app's only external dependency outside GitHub. If LeetCode changes the API,
the heatmap silently freezes on the cached result with no error.

The review count still comes from the app's own grading log — that's the part LeetCode
knows nothing about.

Run the tests:

```bash
cd app/ios
xcodebuild test -scheme LCReview -destination 'platform=iOS Simulator,name=iPhone 12 mini'
```

## Configuration

`.env` (already in `.gitignore`, never committed):

```
LEETCODE_SESSION=...     # cookie after logging in to leetcode.com in Chrome
LEETCODE_CSRFTOKEN=...
CLAUDE_TOKEN=sk-ant-...  # generates approach notes and element answers
NOTION_TOKEN=ntn_...     # Notion internal integration; share both databases with it
```

The LeetCode session expires every few weeks. After expiry the API doesn't error — it
returns zero accepted problems — so `sync-new` verifies first and exits with an error
on an empty username instead of silently doing nothing. Log back in to leetcode.com in
Chrome and put the new cookie into `.env`.

## How retrospectives flow in

Retrospectives are written in two Notion pages as running logs:

- easy page: `20、valid parentheses：<body>`
- medium page: `3、LC 1004 <problem title>：<body>`, split into sections by
  `--- Day N | <topic> ---`

`lc_review/fupan.py` parses them. Orange highlights are extracted separately — those
are the tricky spots I marked myself. When written to markdown they become
`==highlighted text==` (GitHub renders a yellow background); when written back to
Notion they are restored to orange.

## Layout

```
lc_review/          all the logic
  cli.py            command entry point
  leetcode_api.py   LeetCode scraping + Claude-generated analysis
  fupan.py          retrospective page parser
  notion_api.py     Notion REST client
  notion_pages.py   flattens Notion pages back into text the parser understands
  sync_new.py       new problems -> Problems/ + Notion rows
  sync_review_md.py retrospectives -> review.md
  sync_fupan.py     retrospectives -> Notion retrospective column
  elements_*.py     element answer generation and rendering
  element_essentials.py  element definitions for the 18 patterns (single source of truth)
tests/              pytest
Problems/           one folder per problem
```
