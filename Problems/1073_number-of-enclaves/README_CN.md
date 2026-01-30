# 1073. 飞地的数量

**难度**: Medium | **标签**: `Array` `Depth-First Search` `Breadth-First Search` `Union-Find` `Matrix`

## 题目描述

<p>给你一个大小为 <code>m x n</code> 的二进制矩阵 <code>grid</code> ，其中 <code>0</code> 表示一个海洋单元格、<code>1</code> 表示一个陆地单元格。</p>

<p>一次 <strong>移动</strong> 是指从一个陆地单元格走到另一个相邻（<strong>上、下、左、右</strong>）的陆地单元格或跨过 <code>grid</code> 的边界。</p>

<p>返回网格中<strong> 无法 </strong>在任意次数的移动中离开网格边界的陆地单元格的数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/enclaves1.jpg" style="height: 200px; width: 200px;" />
<pre>
<strong>输入：</strong>grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
<strong>输出：</strong>3
<strong>解释：</strong>有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/enclaves2.jpg" style="height: 200px; width: 200px;" />
<pre>
<strong>输入：</strong>grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
<strong>输出：</strong>0
<strong>解释：</strong>所有 1 都在边界上或可以到达边界。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>grid[i][j]</code> 的值为 <code>0</code> 或 <code>1</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：利用深度优先搜索（DFS）从边界开始淹没所有与边界相连的陆地，最后统计剩余的陆地数量。

2. 综合思路：
   - **DFS递归解法**：从边界的陆地开始，通过递归的深度优先搜索将所有与边界相连的陆地标记为水（即淹没），最后遍历整个网格统计未被淹没的陆地数量。
   - **BFS迭代解法（未在提供的代码中出现，但为常见变体）**：使用队列从边界的陆地开始，迭代地将所有与边界相连的陆地标记为水，最后统计剩余陆地数量。

3. 全量伪代码：
   ```plaintext
   初始化行数和列数
   初始化边界列表和计数器

   遍历网格的每个单元格
       如果单元格在边界且是陆地
           将其坐标加入边界列表

   当边界列表不为空时
       弹出边界列表中的一个坐标
       调用DFS函数淹没该坐标及其相连的陆地

   遍历网格的每个单元格
       如果单元格是陆地
           增加计数器

   返回计数器

   DFS函数(grid, r, c)
       如果坐标超出边界或不是陆地
           返回
       将当前坐标标记为水
       递归调用DFS函数处理上下左右相邻的坐标
   ```

4. 复杂度：
   - 时间复杂度：$O(m \times n)$，其中 $m$ 和 $n$ 分别是网格的行数和列数，因为每个单元格最多被访问一次。
   - 空间复杂度：$O(m \times n)$，在最坏情况下，递归调用栈的深度可能达到整个网格的大小。