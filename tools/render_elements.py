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
SCRATCH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

# 题型 -> (分类, 要素简槽位列表, 完整要素问句列表)
SPEC = {
    "回溯": ("递归系", ["路径", "选择列表", "结束条件", "撤销"], [
        "路径是什么（已经做出的选择）？", "选择列表是什么（当前可以做的选择）？",
        "结束条件是什么（到达决策树底层、无法再选的时候）？", "撤销的是什么（递归返回后要还原的状态）？"]),
    "并查集": ("洞察系", ["union 连谁", "connected 判据", "优化方式"], [
        "union 连接的是哪两个元素？", "connected 怎么判断两个节点已经连通（根节点是否相同）？",
        "要不要做按秩合并/路径压缩，防止树退化成链表？"]),
    "动态规划": ("递归系", ["状态", "选择", "dp 定义", "base case", "遍历顺序"], [
        "状态是什么（会随选择改变的变量）？", "每个状态下有哪些选择？", "dp 数组/函数的定义是什么？",
        "base case 是什么？", "遍历顺序是什么（保证转移时用到的子问题已经算好）？"]),
    "贪心": ("洞察系", ["贪心策略", "局部最优判据", "正确性理由"], [
        "贪心策略是什么（按哪个维度排序或取最值）？", "每一步的局部最优怎么判定（不用看后续结果）？",
        "局部最优能推出全局最优的理由是什么？"]),
    "递归思维": ("递归系", ["遍历还是分解", "函数定义", "base case", "单层主体"], [
        "该用「遍历」思维还是「分解问题」思维？", "递归函数的定义是什么（参数含义、返回什么）？",
        "base case 是什么？", "单层主体是什么（只看这一层做什么，相信子问题已算对）？"]),
    "图论": ("递归系 / 循环系", ["图的表示", "遍历状态", "拓扑排序", "最短路松弛"], [
        "图怎么表示（有向还是无向，邻接表还是矩阵）？", "遍历要维护哪些状态（只需 visited 去重，还是加 onPath 检环）？",
        "需不需要拓扑排序（Kahn 入度法还是 DFS 三色标记）？", "若求最短路，distTo 怎么初始化、怎么松弛更新？"]),
    "BFS": ("循环系", ["节点与邻居", "起点与终点", "visited 时机", "是否分层"], [
        "怎么把这个场景抽象成图（谁是节点，谁是邻居）？", "起点是什么？到达终点的判断条件是什么？",
        "visited 什么时候标记，防止重复访问/死循环？", "要不要分层（每轮先固定住当前队列长度）？"]),
    "分治": ("递归系", ["拆分方式", "base case", "合并方式"], [
        "怎么把原问题拆成互相独立的子问题？", "拆到什么规模就直接返回（base case）？",
        "子问题的解怎么合并成原问题的解？"]),
    "数学技巧": ("洞察系", ["数学结构", "枚举范围", "数值边界"], [
        "问题背后的数学结构是什么（可以直接套的结论、公式或性质）？",
        "枚举的范围是什么（能不能缩到 sqrt(n)、只看质因数、只看奇偶）？",
        "数值边界是什么（会不会溢出，要不要取模）？"]),
    "数组双指针": ("循环系", ["指针类型", "slow 含义", "停止条件"], [
        "该用左右指针（相向而行）还是快慢指针（同向而行）？",
        "快慢指针场景里，slow 指向的是什么位置（下一个待写入的位置）？",
        "fast/right 什么时候停（越界还是相遇）？"]),
    "堆（优先级队列）": ("循环系", ["存什么", "序（大顶/小顶）", "容量", "进出时机"], [
        "堆里存的是什么（值、下标还是元组）？", "序是什么（大顶还是小顶，比较器按哪个字段）？",
        "堆的容量有没有上限（求第 K 大就固定 k）？", "push 和 pop 分别发生在什么时候？"]),
    "栈与队列": ("循环系", ["栈还是队列", "存什么", "进出时机", "剩余元素含义"], [
        "用栈（后进先出）还是队列（先进先出）？", "里面存的是什么（值、下标还是配对信息）？",
        "入和出的时机分别是什么？", "循环结束后剩下的元素代表什么？"]),
    "链表双指针": ("循环系", ["要不要 dummy", "指针关系", "停止条件"], [
        "是不是在创造一条新链表？要不要用 dummy 虚拟头结点简化边界？",
        "fast 和 slow 之间要维持什么固定关系（步数差/速度差）？",
        "fast 走到哪里就该停（fast == null 还是 fast.next == null）？"]),
    "二叉树": ("递归系", ["函数定义", "base case", "单层主体", "代码位置（前/中/后序）"], [
        "递归函数的定义是什么（参数含义、返回值代表什么）？", "base case 是什么（空节点返回什么）？",
        "单层主体是什么（只看当前节点做什么，子树当已经算对）？", "主体代码写在前序、中序还是后序位置？"]),
    "二分搜索": ("循环系", ["区间定义", "while 条件", "判定条件", "边界收缩"], [
        "搜索区间怎么定义——两端都闭还是左闭右开？", "while 条件用 <= 还是 <？",
        "判定条件是什么（等于 target，还是某个单调的 check 函数）？",
        "三种情况下边界各自怎么收缩（命中时直接返回还是继续找边界）？"]),
    "单调栈": ("循环系", ["单调方向", "存下标还是值", "弹栈条件", "遍历方向"], [
        "栈内要保持单调递增还是单调递减？", "栈里存的是下标还是值？",
        "while 弹栈的条件是什么（谁该被淘汰）？", "正着遍历还是倒着遍历？"]),
    "前缀和与差分": ("洞察系", ["前缀和还是差分", "preSum[0] 定义", "差分下标位置"], [
        "是原数组不变、要频繁查询区间和（前缀和），还是要频繁对区间做增减（差分）？",
        "preSum[0] 定义为多少，能不能靠它省掉 left = 0 的特判？",
        "区间 [i, j] 的增减该写在 diff 的哪两个下标上（diff[i] 与 diff[j+1]）？"]),
    "滑动窗口": ("循环系", ["定长还是变长", "进窗口更新", "出窗口时机", "记结果时机"], [
        "窗口是定长还是变长？", "什么时候移动 right 扩大窗口？加入元素时应该更新哪些数据？",
        "什么时候移动 left 缩小窗口？移出元素时应该更新哪些数据？", "什么时候应该更新结果？"]),
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
