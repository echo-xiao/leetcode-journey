"""Read the locally solved problems out of the Problems/ directory tree."""

from __future__ import annotations

import json
import re
import urllib.request
from dataclasses import dataclass
from pathlib import Path

def _section_marker(number: str, name: str) -> re.Pattern[str]:
    """Build a regex matching a section marker line in any of its real forms.

    The generator writes the same marker three different ways across the
    corpus: plain (``3. 全量伪代码：``), bold (``3. **全量伪代码：**``), and as
    a markdown heading (``### 全量伪代码`` or ``### 3. 全量伪代码``, no colon).
    All three must match so the section is never silently treated as absent.
    """
    return re.compile(
        rf"^(?:###\s*)?(?:{number}\.\s*)?\*{{0,2}}{name}\*{{0,2}}：?\*{{0,2}}\s*$",
        re.MULTILINE,
    )


PSEUDOCODE_START_RE = _section_marker("3", "全量伪代码")
COMPLEXITY_START_RE = _section_marker("4", "复杂度")

# A level-2 heading (exactly ``## ``, not ``### ``) marks the start of the
# next major README section (e.g. the next problem's own retrospective
# block). Deeper headings like ``#### DFS 递归版`` are legitimate structure
# *inside* the pseudocode section and must not truncate it.
TOP_HEADING_RE = re.compile(r"^##(?!#)\s", re.MULTILINE)


@dataclass(frozen=True)
class SolvedProblem:
    """A problem echo has an accepted solution for, on disk.

    ``internal_id`` is the number in the directory name, which is LeetCode's
    internal ``questionId``. It is *not* the problem number and must never be
    shown to a human or used to match a retrospective.
    """

    internal_id: int
    slug: str
    directory: str


def scan(problems_dir: Path) -> tuple[list[SolvedProblem], list[str]]:
    """Return solved problems plus the names of directories we could not parse.

    Malformed names are reported rather than repaired. Two directories in this
    repo begin with the literal string ``None`` because the original scraper
    lost the number; guessing one from the slug would be fabrication.
    """
    solved: list[SolvedProblem] = []
    malformed: list[str] = []
    for entry in sorted(problems_dir.iterdir()):
        if not entry.is_dir():
            continue
        head, _, slug = entry.name.partition("_")
        if not slug or not head.isdigit():
            malformed.append(entry.name)
            continue
        solved.append(SolvedProblem(int(head), slug, entry.name))
    solved.sort(key=lambda problem: problem.internal_id)
    return solved, malformed


FRONTEND_ID_QUERY = (
    "query q($t:String!){ question(titleSlug:$t){ questionId questionFrontendId } }"
)


def resolve_frontend_id(slug: str) -> int:
    """Ask LeetCode for the problem number people actually see.

    Needed because the directory prefix is the internal id and disagrees with
    the displayed number for 138 of the 372 solved problems. The endpoint needs
    no authentication.
    """
    payload = json.dumps({"query": FRONTEND_ID_QUERY, "variables": {"t": slug}}).encode()
    request = urllib.request.Request(
        "https://leetcode.cn/graphql/",
        data=payload,
        headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        body = json.loads(response.read())
    question = body["data"]["question"]
    if question is None:
        raise ValueError(f"LeetCode does not know the slug {slug!r}")
    return int(question["questionFrontendId"])


def read_ai_sections(readme: Path) -> dict[str, str]:
    """Extract the GPT-generated pseudocode and complexity parts of a README.

    These are parts 3 and 4 of the ``## 解题思路与复盘`` block. Parts 1 and 2
    are prose summaries we deliberately discard: they read like a retrospective
    but are machine-written, and mixing them with echo's real retrospectives
    would blur which is which.
    """
    if not readme.exists():
        return {"pseudocode": "", "complexity": ""}
    text = readme.read_text(encoding="utf-8")

    pseudocode_start = PSEUDOCODE_START_RE.search(text)
    complexity_start = COMPLEXITY_START_RE.search(text)

    pseudocode = ""
    if pseudocode_start:
        start = pseudocode_start.end()
        end_candidates = [len(text)]
        if complexity_start and complexity_start.start() > pseudocode_start.start():
            end_candidates.append(complexity_start.start())
        top_heading = TOP_HEADING_RE.search(text, start)
        if top_heading:
            end_candidates.append(top_heading.start())
        pseudocode = text[start : min(end_candidates)].strip()

    complexity = text[complexity_start.end() :].strip() if complexity_start else ""

    return {"pseudocode": pseudocode, "complexity": complexity}
