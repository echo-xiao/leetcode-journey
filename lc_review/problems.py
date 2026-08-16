"""Read the locally solved problems out of the Problems/ directory tree."""

from __future__ import annotations

import json
import re
import urllib.request
from dataclasses import dataclass
from pathlib import Path

PSEUDOCODE_RE = re.compile(r"^3\.\s*全量伪代码：\s*$(.*?)^4\.\s", re.DOTALL | re.MULTILINE)
COMPLEXITY_RE = re.compile(r"^4\.\s*复杂度：\s*$(.*)", re.DOTALL | re.MULTILINE)


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
    pseudocode = PSEUDOCODE_RE.search(text)
    complexity = COMPLEXITY_RE.search(text)
    return {
        "pseudocode": pseudocode.group(1).strip() if pseudocode else "",
        "complexity": complexity.group(1).strip() if complexity else "",
    }
