# 79. 单词搜索

**难度**: Medium | **标签**: `Array` `String` `Backtracking` `Depth-First Search` `Matrix`

## 题目描述

<p>给定一个&nbsp;<code>m x n</code> 二维字符网格&nbsp;<code>board</code> 和一个字符串单词&nbsp;<code>word</code> 。如果&nbsp;<code>word</code> 存在于网格中，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word2.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>输入：</strong>board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCCED"
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>输入：</strong>board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "SEE"
<strong>输出：</strong>true
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/word3.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>输入：</strong>board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCB"
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n = board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 6</code></li>
	<li><code>1 &lt;= word.length &lt;= 15</code></li>
	<li><code>board</code> 和 <code>word</code> 仅由大小写英文字母组成</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你可以使用搜索剪枝的技术来优化解决方案，使其在 <code>board</code> 更大的情况下可以更快解决问题？</p>


---
## 解题思路与复盘

1. 一句话直击本质：利用深度优先搜索（DFS）结合回溯法在二维网格中查找路径以匹配给定单词。

2. 综合思路：
   - 深度优先搜索（DFS）与回溯：所有版本都使用DFS结合回溯法，通过递归探索每个可能的路径，尝试匹配单词的每个字符。
   - 递归实现：通过递归函数调用来实现DFS，逐步检查每个字符是否匹配，并在不匹配时回溯。

3. 全量伪代码：
   ```plaintext
   定义函数 exist(board, word):
       获取行数 row 和列数 col
       遍历每个单元格 (i, j) 在 board 中:
           如果 board[i][j] 等于 word 的第一个字符:
               如果调用 dfs(board, word, i, j, 0) 返回 True:
                   返回 True
       返回 False

   定义函数 dfs(board, word, r, c, idx):
       如果 idx 等于 word 的长度:
           返回 True  // 找到完整单词
       如果 r 或 c 超出边界 或 board[r][c] 不等于 word[idx]:
           返回 False  // 不匹配或越界
       保存当前字符 board[r][c] 到临时变量 tmp
       将 board[r][c] 标记为已访问（例如设置为 '#'）
       递归调用 dfs 函数检查四个方向:
           向右 (r, c+1)
           向左 (r, c-1)
           向上 (r-1, c)
           向下 (r+1, c)
       如果任一方向找到匹配:
           返回 True
       恢复 board[r][c] 为原始字符 tmp
       返回 False
   ```

4. 复杂度：
   - 时间复杂度：$O(N \times 3^L)$，其中 $N$ 是网格中的单元格总数，$L$ 是单词的长度。每个单元格最多被访问一次，并且每次递归调用最多有三个方向可选（因为一个方向已经被访问过）。
   - 空间复杂度：$O(L)$，主要由递归调用栈的深度决定，最坏情况下递归深度为单词的长度。