# 131. 分割回文串

**难度**: Medium | **标签**: `String` `Dynamic Programming` `Backtracking`

## 题目描述

<p>给你一个字符串 <code>s</code>，请你将<em> </em><code>s</code><em> </em>分割成一些 <span data-keyword="substring-nonempty">子串</span>，使每个子串都是 <strong><span data-keyword="palindrome-string">回文串</span></strong> 。返回 <code>s</code> 所有可能的分割方案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "aab"
<strong>输出：</strong>[["a","a","b"],["aa","b"]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "a"
<strong>输出：</strong>[["a"]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 16</code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过深度优先搜索（DFS）遍历字符串的所有可能分割，判断每个分割是否为回文，并记录所有回文分割方案。

2. 综合思路：
   - **递归与DFS**：所有版本均使用递归结合深度优先搜索的方法，逐步尝试从字符串的起始位置进行分割，判断每个分割是否为回文，若是则继续递归处理剩余部分。
   - **数据结构**：使用列表（`List`）来存储当前路径（`path`）和最终结果（`res`），通过回溯法在递归中动态维护当前路径。

3. 全量伪代码：
   ```
   定义函数 partition(s: 字符串) -> 列表:
       初始化结果列表 res
       初始化路径列表 path
       调用 dfs(s, 0, path, res)
       返回 res

   定义函数 dfs(s: 字符串, start: 整数, path: 列表, res: 列表):
       如果 start 等于 s 的长度:
           将 path 的副本添加到 res
           返回

       对于 i 从 start 到 s 的长度 - 1:
           取子串 seg = s 从 start 到 i+1
           如果 seg 是回文:
               将 seg 添加到 path
               调用 dfs(s, i+1, path, res)
               从 path 移除最后一个元素
   ```

4. 复杂度：
   - 时间复杂度：$O(n \cdot 2^n)$，其中 $n$ 是字符串的长度。每个字符可以单独成为一个回文，或者与其他字符组合成回文，导致指数级的分割可能性。
   - 空间复杂度：$O(n)$，用于存储递归调用栈和路径列表。