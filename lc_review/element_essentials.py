"""Each technique's own 要素: the small set of questions you must answer to
write that kind of code.

This is deliberately NOT one fixed field list applied to all eighteen cards
(that framing was our own invention and echo corrected it twice -- see
lc_review/elements.py's FIELDS, kept only for the legacy tests and the Anki
elements deck). Instead every technique gets its OWN ordered tuple of two to
four short questions, phrased in echo's own idiom ("什么时候停止？" /
"主体是什么？" / "什么时候执行？").

Where a source article states its own checklist explicitly -- sliding
window's 三个必答问题, binary tree's 两种思维模式 + 前中后序位置, backtracking's
路径/选择列表/结束条件, binary search's 搜索区间定义/while 条件/边界收缩, dynamic
programming's 状态/选择/dp 定义/base case -- the wording below tracks that
checklist closely. Those cards are listed in ``EXPLICIT_FRAMEWORK``.

Where an article does not spell out a checklist, the questions here are
derived from what the article actually insists you decide (documented per
card below with the article passage that grounds it). Cards not listed in
``EXPLICIT_FRAMEWORK`` are derived in this sense.

Some articles are genuinely just problem-set index pages (栈与队列, 堆) or a
grab-bag of unrelated tricks with no unifying checklist (数学技巧); those get
an empty tuple rather than an invented framework.

All sources were fetched with curl (labuladong.online blocks plain
WebFetch/urllib with a Cloudflare 403; a browser User-Agent works) and read
in full before writing the entries below.
"""

from __future__ import annotations

ESSENTIALS: dict[str, tuple[str, ...]] = {
    # Derived. The article's one explicit rule is "何时使用虚拟头结点": "当你需要
    # 创造一条新链表的时候，可以使用虚拟头结点简化边界情况的处理". The other two
    # questions are derived from what actually varies across the seven worked
    # examples (合并/分解/找中点/倒数第k个/判环/找交点): a fixed relationship
    # between two pointers, and a stopping condition on the faster one.
    "链表双指针": (
        "是不是在创造一条新链表？要不要用 dummy 虚拟头结点简化边界？",
        "fast 和 slow 之间要维持什么固定关系（步数差/速度差）？",
        "fast 走到哪里就该停（fast == null 还是 fast.next == null）？",
    ),
    # Derived. The article's explicit distinction is "左右指针，就是两个指针相向
    # 而行或者相背而行；快慢指针，就是两个指针同向而行，一快一慢". The other two
    # questions are derived from the worked examples of each kind.
    "数组双指针": (
        "该用左右指针（相向而行）还是快慢指针（同向而行）？",
        "快慢指针场景里，slow 指向的是什么位置（下一个待写入的位置）？",
        "fast/right 什么时候停（越界还是相遇）？",
    ),
    # Quoted. "基于这个框架，遇到子串/子数组相关的题目，你只需要回答以下三个问题"
    # -- the three items below are that framework's own three questions,
    # essentially verbatim.
    "滑动窗口": (
        "什么时候移动 right 扩大窗口？窗口加入字符时，应该更新哪些数据？",
        "什么时候窗口应该暂停扩大、开始移动 left 缩小窗口？从窗口移出字符时，应该更新哪些数据？",
        "什么时候应该更新结果？",
    ),
    # Quoted. The article's own framework: the "搜索区间" concept ("准确理解
    # 二分查找的关键在于理解「搜索区间」这个概念"), its explicit reasoning for
    # why while uses <= and not < ("搜索区间为空时，应该停止搜索"), and its
    # explicit treatment of how the boundary shrinks on each branch.
    "二分搜索": (
        "搜索区间怎么定义——两端都闭还是左闭右开？",
        "while 条件用 <= 还是 <？",
        "nums[mid] 不等于 target 时，边界该往哪收缩（+1 还是 -1）？",
    ),
    # Derived from the article's own description of what makes the stack
    # monotonic and why it is walked back-to-front: "使得每次新元素入栈后，栈内的
    # 元素都保持有序（单调递增或单调递减）"; "for 循环要从后往前扫描元素……倒着入栈，
    # 其实是正着出栈"; "while 循环是把两个「个子高」元素之间的元素排除".
    "单调栈": (
        "栈内要保持单调递增还是单调递减？",
        "该倒着入栈（正着出栈）吗？",
        "while 弹栈的条件是什么（谁该被淘汰）？",
    ),
    # Derived from the two articles' own statements of when each technique
    # applies ("原数组不会发生变化"前提下频繁查询区间和 vs "频繁对原始数组的某个
    # 区间的元素进行增减"), plus the concrete code decisions each requires
    # ("preSum[0] = 0，便于计算累加和"; diff[i] += val 与 diff[j+1] -= val 这对
    # 下标)。
    "前缀和与差分": (
        "是原数组不变、要频繁查询区间和（前缀和），还是要频繁对区间做增减（差分）？",
        "preSum[0] 定义为多少，能不能靠它省掉 left = 0 的特判？",
        "区间 [i, j] 的增减该写在 diff 的哪两个下标上（diff[i] 与 diff[j+1]）？",
    ),
    # Empty: both problem-set/stack/ and problem-set/queue/ are problem-index
    # pages, not framework articles. Each states only what the data structure
    # tests for ("主要考察先进后出特点的运用"；"常见考点主要是元素「先进先出」的
    # 顺序特性"), with no checklist of questions to answer while writing code.
    # An honest gap, not a fabricated framework.
    "栈与队列": (),
    # Empty: problem-set/binary-heap/ is likewise a problem-index page. It
    # classifies problems into two types ("用到优先级队列的题目主要分两类") but
    # states no checklist for writing the code itself.
    "堆（优先级队列）": (),
    # Quoted (mostly). "二叉树解题的思维模式分两类" is the article's own opening
    # framework, and "如果单独抽出一个二叉树节点，它需要做什么事情？需要在什么时候
    # （前/中/后序位置）做？" is its own follow-up question -- both used near
    # verbatim. The base-case question is derived: the article's own code
    # examples all open on a base case (see its fib() walkthrough, "// base
    # case"), but the tree article never states "递归的 base case 是什么" as a
    # named checklist item the way it does for the other two, so this one
    # item is ours, not the article's wording.
    "二叉树": (
        "这道题该用「遍历」思维还是「分解问题」思维？",
        "递归的 base case 是什么（空节点该返回什么）？",
        "这段代码该写在前序、中序还是后序位置？",
    ),
    # Quoted. Same "两种思维模式" split as the binary tree article ("编写递归
    # 算法，有两种思维模式：一种是通过「遍历」一遍树得到答案，另一种是通过「分解
    # 问题」得到答案"), plus the article's explicit requirement for the
    # decompose-the-problem mode: "这个递归函数一定要有一个清晰的定义，说明这个
    # 函数参数的含义是什么，返回什么结果".
    "递归思维": (
        "该用「遍历」思维还是「分解问题」思维？",
        "如果是分解问题，这个递归函数的定义是什么（参数含义、返回什么）？",
    ),
    # Quoted. The article's own three named terms, essentially verbatim:
    # "1、路径：也就是已经做出的选择。2、选择列表：也就是你当前可以做的选择。
    # 3、结束条件：也就是到达决策树底层，无法再做选择的条件。"
    "回溯": (
        "路径是什么（已经做出的选择）？",
        "选择列表是什么（当前可以做的选择）？",
        "结束条件是什么（到达决策树底层、无法再选的时候）？",
    ),
    # Derived from the article's own explanation of what BFS actually is
    # underneath a word problem: it must be recast as a graph, walked with a
    # visited set to avoid an infinite loop. Grounded in "把具体的问题抽象成
    # 树结构"、起点/终点 wording in the worked examples, and "visited 数组防止
    # 死循环" from the framework code.
    "BFS": (
        "怎么把这个场景抽象成图（谁是节点，谁是边/邻居）？",
        "起点是什么？到达终点的判断条件是什么？",
        "visited 什么时候标记，防止重复访问/死循环？",
    ),
    # Derived across the card's three source articles (graph traversal,
    # topological sort, shortest path). Grounded in "需要一个 visited 数组记录
    # 被遍历过的节点"（外加 onPath 判环）、"进行拓扑排序之前，先要确保图中没有环"、
    # distTo 数组的初始化与更新（松弛）在最短路径框架代码中的写法。
    "图论": (
        "遍历只需要 visited 去重，还是也要用 onPath 检测环？",
        "图里有没有环？有环还能不能做拓扑排序？",
        "单源最短路径的 distTo 怎么初始化、怎么松弛更新？",
    ),
    # Derived from the API the article itself sets up ("现在我们的 Union-Find
    # 算法主要需要实现这两个 API: union / connected") plus the two optimization
    # sections the article structures the whole write-up around ("三、平衡性
    # 优化"、"四、路径压缩"）。
    "并查集": (
        "union 连接的是哪两个元素？",
        "connected 怎么判断两个节点已经连通（根节点是否相同）？",
        "要不要做按秩合并/路径压缩，防止树退化成链表？",
    ),
    # Quoted. The article's own framework line: "明确「状态」-> 明确「选择」->
    # 定义 dp 数组/函数的含义"，加上它反复强调、并在凑零钱例题里明确写出的
    # base case（"这里我们按照力扣的题目描述，认为 base case 是..."）。
    "动态规划": (
        "状态是什么（会随选择改变的变量）？",
        "每个状态下有哪些选择？",
        "dp 数组/函数的定义是什么？",
        "base case 是什么？",
    ),
    # Derived. The free portion of the article stops right after its worked
    # example (choosing between ten 1-元/100-元 notes); the later sections
    # named in its own table of contents ("贪心选择性质"、"贪心算法的解题步骤")
    # have no retrievable body text behind them via curl, so this entry stays
    # to a single question grounded in what was actually readable: "有些
    # 问题其实不需要完整地穷举所有可行解，就可以推导出最优解".
    "贪心": (
        "每一步的选择是不是不用管后续结果，就能直接判断出局部最优（不用穷举整棵决策树）？",
    ),
    # Derived from the article's own definition of what divide-and-conquer
    # is: "把一个问题分解成若干个子问题，然后分别解决这些子问题，最后合并子问题的
    # 解得到原问题的解".
    "分治": (
        "怎么把原问题拆成互相独立的子问题？",
        "子问题的解怎么合并成原问题的解？",
    ),
    # Empty: essential-technique/math-techniques-summary/ is a grab-bag index
    # of unrelated small tricks (mod arithmetic, GCD/LCM, factorials, primes,
    # probability, bit tricks) with no single checklist that applies across
    # them. An honest gap rather than a forced framework.
    "数学技巧": (),
}

# Cards whose essentials above are quoted (or paraphrased very closely) from
# an explicit checklist the article itself states, rather than derived by us
# from what the article insists you decide without naming it as a checklist.
EXPLICIT_FRAMEWORK: frozenset[str] = frozenset(
    {
        "滑动窗口",
        "二分搜索",
        "二叉树",
        "递归思维",
        "回溯",
        "动态规划",
    }
)
