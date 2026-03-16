# 694. 不同岛屿的数量

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

---
## 解题思路与复盘

1. **一句话直击本质：** 通过深度优先搜索（DFS）或广度优先搜索（BFS）遍历每个岛屿，并记录其相对形状以识别不同的岛屿。

2. **综合思路：**
   - **DFS 递归：** 使用递归的深度优先搜索来遍历每个岛屿，记录路径方向（如上下左右）来表示岛屿的形状。
   - **DFS 迭代：** 使用栈进行迭代的深度优先搜索，记录每个岛屿的相对坐标来表示形状。
   - **BFS 迭代：** 虽然在给定代码集中未明确使用 BFS，但可以通过队列实现类似的遍历和形状记录。
   - **数据结构：** 使用集合（set）存储岛屿的形状，以便自动去重并计算不同岛屿的数量。

3. **全量伪代码：**

   - **初始化：**
     ```
     如果 grid 为空或 grid[0] 为空，返回 0
     初始化行数 rows 和列数 cols
     初始化集合 ans 用于存储不同的岛屿形状
     ```

   - **遍历网格：**
     ```
     对于每个单元格 (r, c) 在 grid 中：
         如果 grid[r][c] == 1：
             初始化 path 或 stack
             调用 traverse 或 dfs 函数
             将返回的形状添加到 ans 中
     返回 ans 的大小
     ```

   - **DFS 递归：**
     ```
     函数 dfs(grid, r, c, path, direction):
         如果 (r, c) 越界或 grid[r][c] == 0，返回
         将 direction 添加到 path
         将 grid[r][c] 置为 0
         递归调用 dfs(grid, r, c+1, path, 'right')
         递归调用 dfs(grid, r, c-1, path, 'left')
         递归调用 dfs(grid, r+1, c, path, 'down')
         递归调用 dfs(grid, r-1, c, path, 'up')
         将 'b' 添加到 path 表示回溯
     ```

   - **DFS 迭代：**
     ```
     函数 traverse(grid, sr, sc):
         初始化 stack 为 [(sr, sc)]
         将 grid[sr][sc] 置为 0
         初始化 currIsland 为 []
         当 stack 非空时：
             弹出 stack 顶部元素 (cr, cc)
             将 (cr - sr, cc - sc) 添加到 currIsland
             对于每个方向 dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]：
                 计算新坐标 (nr, nc)
                 如果 (nr, nc) 在边界内且 grid[nr][nc] == 1：
                     将 grid[nr][nc] 置为 0
                     将 (nr, nc) 添加到 stack
         返回排序后的 currIsland 作为元组
     ```

4. **复杂度：**

   - **时间复杂度：** $O(R \times C)$，其中 $R$ 是网格的行数，$C$ 是网格的列数。每个单元格最多被访问一次。
   - **空间复杂度：** $O(R \times C)$，用于存储访问状态和岛屿形状。