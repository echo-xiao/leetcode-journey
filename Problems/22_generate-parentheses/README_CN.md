# 22. 括号生成

**难度**: Medium | **标签**: `String` `Dynamic Programming` `Backtracking`

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

1. 一句话直击本质：利用回溯算法生成所有可能的括号组合，通过递归构建合法的括号序列。

2. 综合思路：
   - **回溯法（Backtracking）**：通过递归构建括号序列，使用两个计数器分别记录左括号和右括号的使用数量，确保生成的序列始终合法。
   - **深度优先搜索（DFS）**：回溯法本质上是一种深度优先搜索，通过递归深入每一个可能的括号组合路径。
   - **剪枝优化**：在递归过程中，通过条件判断（如右括号数量不能超过左括号）进行剪枝，避免不必要的递归。

3. 全量伪代码：
   ```plaintext
   定义函数 generateParenthesis(n):
       初始化结果列表 res
       初始化路径列表 path
       调用回溯函数 backtrack(0, 0, n, path, res)
       返回结果列表 res

   定义回溯函数 backtrack(left, right, n, path, res):
       如果路径长度等于 2 * n:
           将路径转换为字符串并添加到结果列表 res
           返回

       如果左括号数量小于 n:
           在路径中添加左括号
           递归调用 backtrack(left + 1, right, n, path, res)
           从路径中移除最后一个字符（回溯）

       如果右括号数量小于左括号数量:
           在路径中添加右括号
           递归调用 backtrack(left, right + 1, n, path, res)
           从路径中移除最后一个字符（回溯）
   ```

4. 复杂度：
   - 时间复杂度：$O(4^n / \sqrt{n})$，这是生成所有可能的括号组合的复杂度。
   - 空间复杂度：$O(n)$，用于存储递归调用栈和路径。