# 711. 不同岛屿的数量 II

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

---
## 解题思路与复盘

1. 一句话直击本质：通过深度优先搜索（DFS）遍历每个岛屿并生成其所有可能的标准化形态，以识别不同的岛屿形状。

2. 综合思路：
   - **DFS 递归**：使用深度优先搜索递归地遍历每个岛屿的所有陆地单元格，将其坐标记录下来。
   - **形态标准化**：对于每个岛屿，生成其在所有可能的对称和旋转变换下的标准化形态，并通过排序和偏移归一化来确保唯一性。
   - **集合去重**：使用集合存储标准化后的岛屿形态，以自动去重并计算不同岛屿的数量。

3. 全量伪代码：
   ```plaintext
   定义函数 numDistinctIslands2(grid):
       如果 grid 为空或第一行为空，返回 0
       初始化行数 rows 和列数 cols
       初始化 visited 集合记录访问过的坐标
       初始化 ans 集合存储不同的岛屿形态

       对于每个坐标 (r, c) 在 grid 中:
           如果 grid[r][c] 是陆地且 (r, c) 未被访问:
               初始化空列表 island
               调用 dfs(grid, r, c, visited, island)
               将 getUnique(island) 的结果加入 ans

       返回 ans 的大小

   定义函数 dfs(grid, r, c, visited, island):
       将 (r, c) 加入 visited
       将 (r, c) 加入 island

       对于每个方向 dr, dc 在 [(0, 1), (0, -1), (1, 0), (-1, 0)] 中:
           计算新坐标 nr, nc
           如果 nr, nc 在边界内且是陆地且未被访问:
               递归调用 dfs(grid, nr, nc, visited, island)

   定义函数 getUnique(shape):
       初始化 transforms 列表

       对于每个对称变换 sx, sy 在 [(1, 1), (1, -1), (-1, 1), (-1, -1)] 中:
           生成并加入 transforms 列表:
               变换 (x * sx, y * sy) 对于每个 (x, y) 在 shape 中
               变换 (y * sx, x * sy) 对于每个 (x, y) 在 shape 中

       初始化 normalized 列表
       对于每个变换 v 在 transforms 中:
           对 v 排序
           计算偏移 ox, oy 为 v[0]
           生成并加入 normalized 列表:
               归一化 (x - ox, y - oy) 对于每个 (x, y) 在 v 中

       返回 normalized 中的最小值
   ```

4. 复杂度：
   - 时间复杂度：$O(n \times m \times \log(n \times m))$，其中 $n$ 和 $m$ 分别是网格的行数和列数。DFS 遍历每个陆地单元格，标准化形态需要排序。
   - 空间复杂度：$O(n \times m)$，用于存储访问状态、岛屿形态和标准化结果。