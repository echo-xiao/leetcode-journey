# 2035. 统计子岛屿

**难度**: Medium | **标签**: `Array` `Depth-First Search` `Breadth-First Search` `Union-Find` `Matrix`

## 题目描述

<p>给你两个 <code>m x n</code> 的二进制矩阵 <code>grid1</code> 和 <code>grid2</code> ，它们只包含 <code>0</code> （表示水域）和 <code>1</code> （表示陆地）。一个 <strong>岛屿</strong> 是由 <strong>四个方向</strong> （水平或者竖直）上相邻的 <code>1</code> 组成的区域。任何矩阵以外的区域都视为水域。</p>

<p>如果 <code>grid2</code> 的一个岛屿，被 <code>grid1</code> 的一个岛屿 <strong>完全</strong> 包含，也就是说 <code>grid2</code> 中该岛屿的每一个格子都被 <code>grid1</code> 中同一个岛屿完全包含，那么我们称 <code>grid2</code> 中的这个岛屿为 <strong>子岛屿</strong> 。</p>

<p>请你返回 <code>grid2</code> 中 <strong>子岛屿</strong> 的 <strong>数目</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/test1.png" style="width: 493px; height: 205px;">
<pre><b>输入：</b>grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
<b>输出：</b>3
<strong>解释：</strong>如上图所示，左边为 grid1 ，右边为 grid2 。
grid2 中标红的 1 区域是子岛屿，总共有 3 个子岛屿。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/03/testcasex2.png" style="width: 491px; height: 201px;">
<pre><b>输入：</b>grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
<b>输出：</b>2 
<strong>解释：</strong>如上图所示，左边为 grid1 ，右边为 grid2 。
grid2 中标红的 1 区域是子岛屿，总共有 2 个子岛屿。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid1.length == grid2.length</code></li>
	<li><code>n == grid1[i].length == grid2[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>grid1[i][j]</code> 和 <code>grid2[i][j]</code> 都要么是 <code>0</code> 要么是 <code>1</code> 。</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质**：通过遍历 `grid2` 中的每个岛屿，使用深度优先搜索（DFS）或栈模拟的迭代方法检查该岛屿是否完全被包含在 `grid1` 的岛屿中。

2. **综合思路**：
   - **DFS 递归法**：对于每个在 `grid2` 中的岛屿，使用递归的深度优先搜索检查该岛屿的每个部分是否在 `grid1` 中也存在对应的陆地。
   - **DFS 迭代法（使用栈）**：通过栈模拟递归过程，遍历 `grid2` 中的每个岛屿，并检查其是否完全被 `grid1` 的岛屿覆盖。

3. **全量伪代码**：

   - **DFS 递归法**：
     ```
     初始化计数器 cnt 为 0
     对于 grid2 中的每个元素 (r, c):
         如果 grid2[r][c] 是陆地:
             如果 dfs 检查函数返回 True:
                 增加计数器 cnt
     返回计数器 cnt

     函数 dfs(grid1, grid2, r, c):
         如果 (r, c) 超出边界或 grid2[r][c] 是水:
             返回 True
         检查 grid1[r][c] 是否是陆地，记录为 isValid
         将 grid2[r][c] 标记为水
         递归检查上下左右四个方向
         返回 isValid 和四个方向的递归结果的逻辑与
     ```

   - **DFS 迭代法（使用栈）**：
     ```
     初始化计数器 cnt 为 0
     对于 grid2 中的每个元素 (r, c):
         如果 grid2[r][c] 是陆地:
             如果 floor 检查函数返回 True:
                 增加计数器 cnt
     返回计数器 cnt

     函数 floor(grid1, grid2, r, c):
         初始化栈 stack 并将 (r, c) 入栈
         将 grid2[r][c] 标记为水
         初始化 isSub 为 True
         当栈不为空时:
             弹出栈顶元素 (cr, cc)
             如果 grid1[cr][cc] 是水:
                 将 isSub 标记为 False
             对于上下左右四个方向:
                 如果新位置 (nr, nc) 在边界内且 grid2[nr][nc] 是陆地:
                     将 grid2[nr][nc] 标记为水
                     将 (nr, nc) 入栈
         返回 isSub
     ```

4. **复杂度**：
   - 时间复杂度：对于两种方法，时间复杂度均为 $O(m \times n)$，其中 $m$ 和 $n$ 分别是 `grid2` 的行数和列数，因为每个元素最多被访问一次。
   - 空间复杂度：递归方法的空间复杂度为 $O(m \times n)$（最坏情况下递归栈深度），而迭代方法的空间复杂度为 $O(m \times n)$（最坏情况下栈的大小）。