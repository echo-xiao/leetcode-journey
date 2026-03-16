# 305. 岛屿数量 II

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

---
## 解题思路与复盘

1. 一句话直击本质：该算法使用并查集（Union-Find）数据结构来动态管理和合并岛屿，从而高效地计算每次添加陆地后的岛屿数量。

2. 综合思路：
   - 并查集（Union-Find）：使用并查集数据结构来管理每个陆地的连通性，通过路径压缩和按秩合并来优化查询和合并操作的效率。
   - 其他可能解法（未在提供的代码中出现）：可以使用DFS或BFS来遍历和标记岛屿，但这些方法在动态添加陆地的情况下效率较低。

3. 全量伪代码：
   ```plaintext
   初始化并查集 parent 数组，大小为 m * n，初始值为自身索引
   初始化 isLand 数组，大小为 m * n，初始值为 False
   初始化岛屿计数器 cnt 为 0
   初始化结果列表 res

   对于每个位置 (r, c) 在 positions 中：
       计算该位置的索引 idx = r * n + c
       如果该位置已经是陆地：
           将当前岛屿数量 cnt 添加到结果列表 res
           继续下一个位置

       将该位置标记为陆地 isLand[idx] = True
       增加岛屿计数器 cnt

       对于每个方向 (dr, dc) 在 [(0, 1), (0, -1), (1, 0), (-1, 0)] 中：
           计算新位置 (nr, nc) = (r + dr, c + dc)
           计算新位置的索引 nidx = nr * n + nc
           如果新位置在边界内且是陆地：
               合并当前索引 idx 和新索引 nidx

       将当前岛屿数量 cnt 添加到结果列表 res

   返回结果列表 res

   函数 find(i):
       如果 parent[i] 不是 i：
           递归查找 parent[i] 的根，并路径压缩
       返回根节点

   函数 union(i, j):
       找到 i 和 j 的根节点 rooti 和 rootj
       如果 rooti 和 rootj 不同：
           将 rooti 的父节点设为 rootj
           减少岛屿计数器 cnt
   ```

4. 复杂度：
   - 时间复杂度：$O(k \cdot \alpha(m \cdot n))$，其中 $k$ 是 positions 的长度，$\alpha$ 是反阿克曼函数，表示并查集操作的均摊时间复杂度。
   - 空间复杂度：$O(m \cdot n)$，用于存储并查集的父节点数组和陆地标记数组。