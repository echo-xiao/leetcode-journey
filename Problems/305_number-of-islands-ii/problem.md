# 305. 岛屿数量 II · 题目

**难度**: Hard | **标签**: `Array` `Hash Table` `Union-Find`

## 题目描述

<p>给定一个大小为 <code>m x n</code> 的空 2D 二进制网格 <code>grid</code>。该网格表示一个地图，其中 <code>0</code> 代表水，<code>1</code> 代表陆地。最初，<code>grid</code> 的所有单元格都是水单元格（即，所有单元格都是 <code>0</code>）。</p>

<p>我们可以执行一个添加陆地的操作，将指定位置的水变为陆地。给定一个数组 <code>positions</code>，其中 <code>positions[i] = [r<sub>i</sub>, c<sub>i</sub>]</code> 是我们应该在第 <code>i<sup>th</sup></code> 次操作中进行操作的位置 <code>(r<sub>i</sub>, c<sub>i</sub>)</code>。</p>

<p>返回一个整数数组 <em>answer</em>，其中 <code>answer[i]</code> <em>是在将单元格</em> <code>(r<sub>i</sub>, c<sub>i</sub>)</code> <em>变为陆地后岛屿的数量</em>。</p>

<p><strong>岛屿</strong> 被水包围，并通过水平或垂直连接相邻的陆地形成。你可以假设网格的四个边缘都被水包围。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/tmp-grid.jpg" style="width: 500px; height: 294px;" />
<pre>
<strong>输入:</strong> m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
<strong>输出:</strong> [1,1,2,3]
<strong>解释:</strong>
最初，2D 网格被水填充。
- 操作 #1: addLand(0, 0) 将 grid[0][0] 的水变为陆地。我们有 1 个岛屿。
- 操作 #2: addLand(0, 1) 将 grid[0][1] 的水变为陆地。我们仍然有 1 个岛屿。
- 操作 #3: addLand(1, 2) 将 grid[1][2] 的水变为陆地。我们有 2 个岛屿。
- 操作 #4: addLand(2, 1) 将 grid[2][1] 的水变为陆地。我们有 3 个岛屿。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> m = 1, n = 1, positions = [[0,0]]
<strong>输出:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>1 &lt;= m, n, positions.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>4</sup></code></li>
	<li><code>positions[i].length == 2</code></li>
	<li><code>0 &lt;= r<sub>i</sub> &lt; m</code></li>
	<li><code>0 &lt;= c<sub>i</sub> &lt; n</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>后续问题:</strong> 你能在时间复杂度 <code>O(k log(mn))</code> 的情况下解决它吗，其中 <code>k == positions.length</code>？</p>
