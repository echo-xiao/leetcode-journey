# 694. 不同岛屿的数量 · 题目

**难度**: Medium | **标签**: `Hash Table` `Depth-First Search` `Breadth-First Search` `Union-Find` `Hash Function`

## 题目描述

<p>给定一个 <code>m x n</code> 的二进制矩阵 <code>grid</code>。一个岛屿是一组 <code>1</code>（表示陆地）通过<strong>四个方向</strong>（水平或垂直）连接在一起。你可以假设矩阵的四个边缘都被水包围。</p>

<p>如果一个岛屿可以被平移（而不是旋转或反射）到另一个岛屿上，则这两个岛屿被视为相同。</p>

<p>返回 <em>不同岛屿的数量</em>。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/distinctisland1-1-grid.jpg" style="width: 413px; height: 334px;" />
<pre>
<strong>输入:</strong> grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
<strong>输出:</strong> 1
</pre>

<p><strong class="example">示例 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/distinctisland1-2-grid.jpg" style="width: 413px; height: 334px;" />
<pre>
<strong>输入:</strong> grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
<strong>输出:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>grid[i][j]</code> 只能是 <code>0</code> 或 <code>1</code>。</li>
</ul>
