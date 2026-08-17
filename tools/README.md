# tools

Generates the `elements.md` file in each problem folder: the framework slots
for that problem's category, each answered for that specific problem.

## Layout

    build_elements.py   classify uncategorised problems, then answer the slots
    render_elements.py  render answers.json into Problems/*/elements.md
    data/
      yaosu_map.tsv     folder -> category, exported from the problem tracker
      inferred_tags.tsv folder -> category, inferred from the solution
      answers.json      folder -> list of answers, one per slot

## Usage

Needs an Anthropic API key, read from the `CLAUDE_TOKEN` entry in the repo `.env`
(or `ANTHROPIC_API_KEY` in the environment).

    python3 tools/build_elements.py            # fill in whatever is missing
    python3 tools/build_elements.py --limit=5  # try a handful first
    python3 tools/render_elements.py           # write the markdown files

`build_elements.py` is incremental: it skips problems already present in
`answers.json`. Pass `--force` to regenerate everything.

Category labels come from `yaosu_map.tsv` when available. Anything missing is
classified from the problem's own pseudocode and recorded in
`inferred_tags.tsv`, so the two sources stay distinguishable.

The answers are only as accurate as `pseudocode.md`, which is itself generated.
Treat them as recall prompts, not as a reference: when something reads wrong,
the solution files are the source of truth.
