# 711. 不同岛屿的数量 II · 题目

**难度**: Hard | **标签**: `Hash Table` `Depth-First Search` `Breadth-First Search` `Union-Find` `Hash Function`

## 题目描述

<p>给定一个 <code>m x n</code> 的二进制矩阵 <code>grid</code>。一个岛屿是一组 <code>1</code>（表示陆地）通过<strong>四个方向</strong>（水平或垂直）连接在一起。你可以假设矩阵的四个边缘都被水包围。</p>

<p>如果两个岛屿的形状相同，或者在<b>旋转</b>（仅限90、180或270度）或<b>反射</b>（左右方向或上下方向）后形状相同，则认为这两个岛屿是相同的。</p>

<p>返回<em>不同岛屿的<b>数量</b></em>。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/distinctisland2-1-grid.jpg" style="width: 413px; height: 334px;" />
<pre>
<strong>输入:</strong> grid = [[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,1,1]]
<strong>输出:</strong> 1
<strong>解释:</strong> 这两个岛屿被认为是相同的，因为如果我们对第一个岛屿进行180度顺时针旋转，那么两个岛屿将具有相同的形状。
</pre>

<p><strong class="example">示例 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/distinctisland1-1-grid.jpg" style="width: 413px; height: 334px;" />
<pre>
<strong>输入:</strong> grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
<strong>输出:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>grid[i][j]</code> 只能是 <code>0</code> 或 <code>1</code>。</li>
</ul>
