# 22. 括号生成

**难度**: Medium | **标签**: `String` `Dynamic Programming` `Backtracking`

**归类**: 7. 动态规划 > String

## 题目描述

<p>数字 <code>n</code>&nbsp;代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 <strong>有效的 </strong>括号组合。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>["((()))","(()())","(())()","()(())","()()()"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>["()"]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 8</code></li>
</ul>


---
## 解题思路与复盘

### 一句话直击本质

使用回溯法生成所有合法的括号组合，通过递归构建路径并在条件满足时回溯。

### 综合思路

1. **递归回溯法**：通过递归构建括号字符串，使用两个计数器分别记录左括号和右括号的数量，确保生成的字符串始终合法。每当字符串长度达到 `2 * n` 时，将其加入结果集。

2. **深度优先搜索 (DFS)**：本质上与递归回溯法相同，DFS 通过递归深入每一个可能的路径，直到满足条件后回溯。

### 全量伪代码

```plaintext
函数 generateParenthesis(n):
    初始化结果列表 res
    初始化路径列表 path
    调用 backtrack(0, 0, n, path, res)
    返回 res

函数 backtrack(left, right, n, path, res):
    如果 path 的长度等于 2 * n:
        将 path 转换为字符串并加入 res
        返回

    如果 left 小于 n:
        在 path 末尾添加 "("
        调用 backtrack(left + 1, right, n, path, res)
        移除 path 末尾的元素

    如果 right 小于 left:
        在 path 末尾添加 ")"
        调用 backtrack(left, right + 1, n, path, res)
        移除 path 末尾的元素
```

### 复杂度

- **时间复杂度**: $O(4^n / \sqrt{n})$，这是生成所有可能的括号组合的复杂度。
- **空间复杂度**: $O(n)$，用于递归调用栈和存储路径的空间。