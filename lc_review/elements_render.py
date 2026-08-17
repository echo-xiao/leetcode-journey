#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用 answers.json 里逐题的答案重写 elements.md。
answers.json 结构: {"<folder>": ["答案1", "答案2", ...], ...}
答案条数必须和该题型的要素简槽位数一致，否则报错不写。
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
    """Notion 标注的题型 + 模型判定的题型（后者补 Notion 没打标签的题）。"""
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


def inferred_set():
    p = os.path.join(SCRATCH, "inferred_tags.tsv")
    if not os.path.exists(p):
        return set()
    with open(p, encoding="utf-8") as f:
        return {l.split("\t")[0] for l in f if l.strip()}


def title_of(folder):
    p = os.path.join(PROBLEMS, folder, "problem.md")
    with open(p, encoding="utf-8") as f:
        first = f.readline().strip()
    return first[2:].replace(" · 题目", "").strip()


def render(folder, tag, answers, tag_inferred=False):
    cat, slots, questions = SPEC[tag]
    if len(answers) != len(slots):
        raise ValueError("{}: 需要 {} 条答案，给了 {} 条".format(folder, len(slots), len(answers)))
    title = title_of(folder)
    rows = []
    for i, (slot, a) in enumerate(zip(slots, answers), 1):
        label = slot.split("（")[0].strip()
        rows.append("{}. {}：{}".format(i, label, a.strip()))
    return "# {} · 要素\n\n{}\n".format(title, "\n\n".join(rows))


def main():
    ymap = load_map()
    inferred = inferred_set()
    with open(os.path.join(SCRATCH, "answers.json"), encoding="utf-8") as f:
        answers = json.load(f)
    written = 0
    errs = []
    for folder, ans in sorted(answers.items()):
        tag = ymap.get(folder)
        if not tag:
            errs.append((folder, "无要素标签"))
            continue
        try:
            content = render(folder, tag, ans, folder in inferred)
        except Exception as e:
            errs.append((folder, str(e)))
            continue
        with open(os.path.join(PROBLEMS, folder, "elements.md"), "w", encoding="utf-8") as f:
            f.write(content)
        written += 1
    print("写入 {} 个 elements.md，失败 {} 个".format(written, len(errs)))
    for e in errs:
        print("  ", e)
    done = set(answers)
    todo = [f for f, t in ymap.items() if f not in done]
    print("还没填答案的题目数:", len(todo))


if __name__ == "__main__":
    main()
