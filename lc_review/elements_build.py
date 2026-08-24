#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""调用 Claude API，按每道题的 pseudocode.md 推出该题型各个要素槽位的答案，
写进 answers.json。之后由 render_elements.py 渲染成 elements.md。

用法:
    export ANTHROPIC_API_KEY=<your key>
    python3 fill_answers.py            # 只补还没填的题
    python3 fill_answers.py --limit 5  # 先试跑 5 道
    python3 fill_answers.py --force    # 全部重跑
"""

import os
import sys
import json
import threading
import concurrent.futures as cf

import anthropic

from .elements_render import REPO, SPEC, PROBLEMS, SCRATCH, load_map

MODEL = "claude-sonnet-5"
ANSWERS_PATH = os.path.join(SCRATCH, "answers.json")
REPO_ENV = os.path.join(REPO, ".env")


def load_key():
    """key 在仓库 .env 的 CLAUDE_TOKEN 里；.env 已被 gitignore，不会进版本库。"""
    if os.environ.get("ANTHROPIC_API_KEY"):
        return
    if not os.path.exists(REPO_ENV):
        return
    with open(REPO_ENV, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#") or line.startswith(";") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            if k.strip() == "CLAUDE_TOKEN":
                os.environ["ANTHROPIC_API_KEY"] = v.strip().strip('"').strip("'")
                return

SYSTEM = """你在帮一个刷题者填「要素表」。

要素是下笔写代码前必须先想清楚的槽位。给你一道题的解题思路与伪代码，
你要针对这道题，逐条回答该题型的要素槽位。

规则：
1. 每条答案一句话，说这道题里这个槽位具体是什么。不要重复问题本身，不要客套。
2. 答案必须落到这道题的具体内容上（具体的变量、条件、返回值），不要写通用套话。
3. 如果某个槽位在这道题上确实不适用，就直接写「本题不涉及」加一句为什么，不要硬编一个答案。
4. 用中文，大白话，不堆术语。
5. 答案条数必须和槽位条数一致，顺序一一对应。"""

USER_TMPL = """题目：{title}
题型：{tag}

这道题的解题思路与伪代码：
---
{pseudocode}
---

请逐条回答「{tag}」这个题型的要素槽位：
{slots}
"""

_lock = threading.Lock()

CLASSIFY_SYSTEM = """你要给一道算法题判定它属于哪个题型。只能从给定清单里选一个，选最贴合解法主干的那个。
不要选题目表面涉及的数据结构，要选实际解法用的框架。"""

INFERRED_PATH = os.path.join(SCRATCH, "inferred_tags.tsv")


def classify(client, folder):
    tags = list(SPEC)
    schema = {
        "type": "object",
        "properties": {"tag": {"type": "string", "enum": tags}},
        "required": ["tag"],
        "additionalProperties": False,
    }
    msg = client.messages.create(
        model=MODEL,
        max_tokens=2000,
        thinking={"type": "adaptive"},
        output_config={"effort": "low", "format": {"type": "json_schema", "schema": schema}},
        system=CLASSIFY_SYSTEM,
        messages=[{
            "role": "user",
            "content": "题目：{}\n\n解题思路与伪代码：\n---\n{}\n---\n\n可选题型：{}".format(
                title_of(folder), read_pseudocode(folder, 4000), "、".join(tags)
            ),
        }],
    )
    text = "".join(b.text for b in msg.content if b.type == "text")
    return json.loads(text)["tag"]


def read_pseudocode(folder, limit_chars=6000):
    p = os.path.join(PROBLEMS, folder, "pseudocode.md")
    with open(p, encoding="utf-8") as f:
        text = f.read()
    return text[:limit_chars]


def title_of(folder):
    p = os.path.join(PROBLEMS, folder, "problem.md")
    with open(p, encoding="utf-8") as f:
        first = f.readline().strip()
    return first[2:].replace(" · 题目", "").strip()


def build_schema(slots):
    """数组的 minItems/maxItems 不被支持，改成一槽一字段，全部 required。"""
    props = {}
    for i, s in enumerate(slots, 1):
        props["a{}".format(i)] = {"type": "string", "description": "第 {} 条槽位「{}」的答案".format(i, s)}
    return {
        "type": "object",
        "properties": props,
        "required": list(props),
        "additionalProperties": False,
    }


def ask(client, folder, tag):
    _cat, slots, questions = SPEC[tag]
    slot_lines = "\n".join(
        "{}. {}（{}）".format(i + 1, s, q) for i, (s, q) in enumerate(zip(slots, questions))
    )
    msg = client.messages.create(
        model=MODEL,
        max_tokens=4000,
        thinking={"type": "adaptive"},
        output_config={
            "effort": "medium",
            "format": {"type": "json_schema", "schema": build_schema(slots)},
        },
        system=SYSTEM,
        messages=[{
            "role": "user",
            "content": USER_TMPL.format(
                title=title_of(folder),
                tag=tag,
                pseudocode=read_pseudocode(folder),
                slots=slot_lines,
            ),
        }],
    )
    if msg.stop_reason == "refusal":
        raise RuntimeError("refusal: {}".format(msg.stop_details))
    text = "".join(b.text for b in msg.content if b.type == "text")
    data = json.loads(text)
    answers = [data["a{}".format(i)] for i in range(1, len(slots) + 1)]
    return answers


def main():
    force = "--force" in sys.argv
    # One folder only, regenerated whether or not it already has answers.
    # Used by `refresh-problem`, where the code changed underneath a set of
    # answers that were right for the old version.
    only = None
    for a in sys.argv[1:]:
        if a.startswith("--only="):
            only = a.split("=", 1)[1]
    limit = None
    for a in sys.argv[1:]:
        if a.startswith("--limit"):
            limit = int(a.split("=", 1)[1]) if "=" in a else int(sys.argv[sys.argv.index(a) + 1])

    ymap = load_map()
    # 仓库里有、但 Notion 没打标签的题：题型由模型判定
    all_folders = sorted(
        f for f in os.listdir(PROBLEMS)
        if os.path.exists(os.path.join(PROBLEMS, f, "pseudocode.md"))
    )
    unmapped = [f for f in all_folders if f not in ymap]
    inferred = {}
    if os.path.exists(INFERRED_PATH):
        with open(INFERRED_PATH, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    k, v = line.rstrip("\n").split("\t")
                    inferred[k] = v
    ymap.update(inferred)
    need_class = [f for f in unmapped if f not in inferred]

    answers = {}
    if os.path.exists(ANSWERS_PATH) and not force:
        with open(ANSWERS_PATH, encoding="utf-8") as f:
            answers = json.load(f)

    if only:
        todo = [only] if only in ymap else []
        need_class = [] if todo else need_class
        answers.pop(only, None)
    else:
        todo = [f for f in sorted(ymap) if force or f not in answers]
    if limit:
        todo = todo[:limit]
    print("待处理 {} 道（已有 {} 道，待判题型 {} 道）".format(len(todo), len(answers), len(need_class)))
    # Newly downloaded problems are not in ymap yet, so todo is empty until
    # they have been classified. Returning on `not todo` alone would skip the
    # classification step that is the only thing able to populate it.
    if not todo and not need_class:
        return

    load_key()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("没找到 key：请设置 ANTHROPIC_API_KEY，或在仓库 .env 里放 CLAUDE_TOKEN")
        sys.exit(1)
    client = anthropic.Anthropic()

    if need_class:
        print("先判 {} 道无标签题的题型...".format(len(need_class)))
        cerr = []

        def do_class(folder):
            try:
                tag = classify(client, folder)
            except Exception as e:
                with _lock:
                    cerr.append((folder, repr(e)))
                return
            with _lock:
                inferred[folder] = tag
                ymap[folder] = tag

        with cf.ThreadPoolExecutor(max_workers=8) as ex:
            list(ex.map(do_class, need_class))
        with open(INFERRED_PATH, "w", encoding="utf-8") as f:
            for k in sorted(inferred):
                f.write("{}\t{}\n".format(k, inferred[k]))
        print("  判定完成 {}，失败 {}".format(len(inferred), len(cerr)))
        for e in cerr[:5]:
            print("   ", e)
        todo = [f for f in sorted(ymap) if force or f not in answers]
        if limit:
            todo = todo[:limit]

    done = [0]
    errors = []

    def work(folder):
        try:
            res = ask(client, folder, ymap[folder])
        except Exception as e:
            with _lock:
                errors.append((folder, repr(e)))
                done[0] += 1
                print("  [{}/{}] 失败 {}: {}".format(done[0], len(todo), folder, e))
            return
        with _lock:
            answers[folder] = res
            done[0] += 1
            if done[0] % 10 == 0 or done[0] == len(todo):
                print("  [{}/{}] ...".format(done[0], len(todo)))
                with open(ANSWERS_PATH, "w", encoding="utf-8") as f:
                    json.dump(answers, f, ensure_ascii=False, indent=1)

    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        list(ex.map(work, todo))

    with open(ANSWERS_PATH, "w", encoding="utf-8") as f:
        json.dump(answers, f, ensure_ascii=False, indent=1)

    print("\n完成 {}，失败 {}".format(len(answers), len(errors)))
    for e in errors[:20]:
        print("  ", e)
    print("答案已存到", ANSWERS_PATH)
    print("下一步：python3 render_elements.py")


if __name__ == "__main__":
    main()
