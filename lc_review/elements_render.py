#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rewrite elements.md from the per-problem answers in answers.json.
answers.json layout: {"<folder>": ["<answer 1>", "<answer 2>", ...], ...}
The number of answers must match the pattern's slot count, otherwise it
errors out and writes nothing.
"""

import os
import json
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROBLEMS = os.path.join(REPO, "Problems")
SCRATCH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data_elements")

# The single definition lives in element_essentials; this view just reshapes it
# into (family, slots, questions) for rendering.
from .element_essentials import ESSENTIALS, FAMILIES, SLOTS

SPEC = {
    name: (FAMILIES[name], list(SLOTS[name]), list(ESSENTIALS[name]))
    for name in ESSENTIALS
}


def load_map():
    """Patterns tagged in Notion + model-inferred ones (the latter cover untagged problems)."""
    m = {}
    for name in ("yaosu_map.tsv", "inferred_tags.tsv"):
        p = os.path.join(SCRATCH, name)
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if line:
                    k, v = line.split("\t")
                    m.setdefault(k, v)
    return m


def title_of(folder):
    p = os.path.join(PROBLEMS, folder, "problem.md")
    with open(p, encoding="utf-8") as f:
        first = f.readline().strip()
    return first[2:].replace(" · 题目", "").strip()


def render(folder, tag, answers):
    _, slots, _ = SPEC[tag]
    if len(answers) != len(slots):
        raise ValueError("{}: expected {} answers, got {}".format(folder, len(slots), len(answers)))
    title = title_of(folder)
    rows = []
    for i, (slot, a) in enumerate(zip(slots, answers), 1):
        label = slot.split("（")[0].strip()
        rows.append("{}. {}：{}".format(i, label, a.strip()))
    return "# {} · 要素\n\n{}\n".format(title, "\n\n".join(rows))


def main():
    ymap = load_map()
    with open(os.path.join(SCRATCH, "answers.json"), encoding="utf-8") as f:
        answers = json.load(f)
    written = 0
    errs = []
    for folder, ans in sorted(answers.items()):
        tag = ymap.get(folder)
        if not tag:
            errs.append((folder, "no pattern tag"))
            continue
        try:
            content = render(folder, tag, ans)
        except Exception as e:
            errs.append((folder, str(e)))
            continue
        with open(os.path.join(PROBLEMS, folder, "elements.md"), "w", encoding="utf-8") as f:
            f.write(content)
        written += 1
    print("wrote {} elements.md files, {} failed".format(written, len(errs)))
    for e in errs:
        print("  ", e)
    done = set(answers)
    todo = [f for f, t in ymap.items() if f not in done]
    print("problems still without answers:", len(todo))


if __name__ == "__main__":
    main()
