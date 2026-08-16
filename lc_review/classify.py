"""Place every solved problem into exactly one section of the taxonomy."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass, field

from lc_review.lingshen import ProblemEntry
from lc_review.problems import SolvedProblem

ORIGIN_LINGSHEN = "灵神"
ORIGIN_CROSS = "跨-我选主节"
ORIGIN_OUTSIDE = "外-我判定"

Placement = tuple[str, str, str]


@dataclass
class Assignment:
    """One solved problem's single chosen placement in the taxonomy."""

    slug: str
    problem_id: int
    id_source: str
    title: str
    list_no: str
    list_name: str
    chapter: str | None
    section: str | None
    rating: int | None
    origin: str
    also_in: list[Placement] = field(default_factory=list)


def _placement(entry: ProblemEntry) -> Placement:
    return (entry.list_no, entry.chapter or "", entry.section or "")


def _jaccard(left: set[str], right: set[str]) -> float:
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def assign(
    entries: list[ProblemEntry],
    solved: list[SolvedProblem],
    tags_by_slug: dict[str, list[str]],
    id_resolver: Callable[[str], int],
    title_lookup: Callable[[str], str | None],
) -> tuple[list[Assignment], list[SolvedProblem]]:
    """Assign solved problems to sections; return assignments and leftovers.

    Cross-listed problems go to the smallest section they appear in, on the
    reasoning that a narrower section describes the technique more precisely.
    Problems absent from every list are matched to the section whose already
    placed members have the most similar LeetCode tag profile. Their title is
    not available from the taxonomy, so ``title_lookup`` is asked for it,
    falling back to the slug when it returns ``None`` or an empty string.
    """
    by_slug: dict[str, list[ProblemEntry]] = defaultdict(list)
    for entry in entries:
        by_slug[entry.slug].append(entry)

    section_size: dict[Placement, int] = defaultdict(int)
    for entry in entries:
        section_size[_placement(entry)] += 1

    assignments: list[Assignment] = []
    uncovered: list[SolvedProblem] = []

    for problem in solved:
        candidates = by_slug.get(problem.slug)
        if not candidates:
            uncovered.append(problem)
            continue
        chosen = min(candidates, key=lambda e: (section_size[_placement(e)], _placement(e)))
        others = sorted({_placement(e) for e in candidates} - {_placement(chosen)})
        assignments.append(
            Assignment(
                slug=chosen.slug,
                # The taxonomy lists carry the displayed problem number. The
                # directory prefix carries LeetCode's internal id and would be
                # wrong for 138 problems, so it is deliberately not used here.
                problem_id=chosen.problem_id,
                id_source=ORIGIN_LINGSHEN,
                title=chosen.title,
                list_no=chosen.list_no,
                list_name=chosen.list_name,
                chapter=chosen.chapter,
                section=chosen.section,
                rating=chosen.rating,
                origin=ORIGIN_CROSS if others else ORIGIN_LINGSHEN,
                also_in=others,
            )
        )

    profiles: dict[Placement, set[str]] = defaultdict(set)
    detail: dict[Placement, Assignment] = {}
    for assignment in assignments:
        key = (assignment.list_no, assignment.chapter or "", assignment.section or "")
        profiles[key].update(tags_by_slug.get(assignment.slug, []))
        detail.setdefault(key, assignment)

    unplaceable: list[SolvedProblem] = []
    for problem in uncovered:
        candidate_tags = set(tags_by_slug.get(problem.slug, []))
        best_key: Placement | None = None
        best_score = 0.0
        for key, profile in sorted(profiles.items()):
            score = _jaccard(candidate_tags, profile)
            if score > best_score:
                best_key, best_score = key, score
        if best_key is None:
            unplaceable.append(problem)
            continue
        sibling = detail[best_key]
        assignments.append(
            Assignment(
                slug=problem.slug,
                # Not in any list, so no displayed number is available locally.
                # Ask LeetCode rather than fall back to the directory prefix.
                problem_id=id_resolver(problem.slug),
                id_source="leetcode-api",
                title=title_lookup(problem.slug) or problem.slug,
                list_no=best_key[0],
                list_name=sibling.list_name,
                chapter=best_key[1] or None,
                section=best_key[2] or None,
                rating=None,
                origin=ORIGIN_OUTSIDE,
                also_in=[],
            )
        )

    return assignments, unplaceable
