"""Build and persist review_state.json, the local source of truth."""

from __future__ import annotations

import json
from pathlib import Path

from lc_review.classify import ORIGIN_CROSS, ORIGIN_OUTSIDE, Assignment
from lc_review.problems import SolvedProblem


def build_state(
    assignments: list[Assignment],
    solved: list[SolvedProblem],
    ai_sections_by_slug: dict[str, dict[str, str]],
    previous: dict[str, dict] | None = None,
) -> dict[str, dict]:
    """Assemble one record per solved problem, keyed by slug.

    Deliberately carries no scheduling data. Proficiency, due dates, and review
    counts live in Anki; duplicating them here would create two authorities for
    the same fact.

    ``previous`` is an existing state file (if any), keyed by the same slugs.
    Everything about the taxonomy placement is recomputed fresh from
    ``assignments`` on every call, but ``我的复盘``, ``要素卡``, ``要素卡来源``,
    and ``已生成卡片`` are hand-attached or derived by *other* commands
    (attach-fupan, build-elements, export-anki) that run after this one --
    rebuilding state must carry them forward by slug rather than reset them to
    empty, or a routine rebuild silently destroys hours of echo's own writing
    that live nowhere else (review_state.json is gitignored).
    """
    previous = previous or {}
    directory_by_slug = {problem.slug: problem.directory for problem in solved}
    state: dict[str, dict] = {}
    for assignment in assignments:
        sections = ai_sections_by_slug.get(assignment.slug, {})
        prior = previous.get(assignment.slug)
        state[assignment.slug] = {
            "id": assignment.problem_id,
            "题号来源": assignment.id_source,
            "题名": assignment.title,
            "难度分": assignment.rating,
            "题单": f"{assignment.list_no}. {assignment.list_name}",
            "章": assignment.chapter,
            "节": assignment.section,
            "归属来源": assignment.origin,
            "亦属": [list(placement) for placement in assignment.also_in],
            "要素卡": prior.get("要素卡") if prior else None,
            "要素卡来源": prior.get("要素卡来源") if prior else None,
            "代码": f"Problems/{directory_by_slug.get(assignment.slug, '')}",
            "我的复盘": prior.get("我的复盘") if prior else None,
            "AI题解": {
                "伪代码": sections.get("pseudocode", ""),
                "复杂度": sections.get("complexity", ""),
            },
            "已生成卡片": list(prior.get("已生成卡片", [])) if prior else [],
        }
    return state


def save_state(state: dict[str, dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8"
    )


def load_state(path: Path) -> dict[str, dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def render_judgment_report(
    assignments: list[Assignment], unplaceable: list[SolvedProblem]
) -> str:
    """List every placement we decided ourselves, for echo to check.

    Placements sourced straight from 灵神 are omitted: they are fact, not
    judgment, and burying our guesses among them defeats the purpose.

    Takes ``assignments`` rather than the persisted state because the tag
    similarity score and the sibling that drove a ``外-我判定`` match are
    diagnostic-only: worth showing here so echo can audit a call like
    ``missing-number -> 1/四、双序列双指针``, but not worth permanently
    bloating review_state.json with.
    """
    lines = ["# Placements decided by us, not by 灵神", ""]
    for origin, heading in (
        (ORIGIN_CROSS, "## Cross-listed: we picked the primary section"),
        (ORIGIN_OUTSIDE, "## Not in any list: we picked a section by tag similarity"),
    ):
        lines += [heading, ""]
        for assignment in sorted(
            (a for a in assignments if a.origin == origin), key=lambda a: a.problem_id
        ):
            line = (
                f"- {assignment.problem_id} `{assignment.slug}` → "
                f"{assignment.list_no}. {assignment.list_name} / "
                f"{assignment.chapter} / {assignment.section}"
            )
            if origin == ORIGIN_OUTSIDE and assignment.match_score is not None:
                line += f" (jaccard={assignment.match_score:.2f}"
                if assignment.match_evidence:
                    line += f", {assignment.match_evidence}"
                line += ")"
            lines.append(line)
        lines.append("")
    lines += ["## Could not place at all", ""]
    for problem in sorted(unplaceable, key=lambda p: p.slug):
        lines.append(f"- `{problem.slug}` (internal id {problem.internal_id})")
    lines.append("")
    return "\n".join(lines)
