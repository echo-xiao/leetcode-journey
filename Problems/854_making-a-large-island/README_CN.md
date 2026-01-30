# 854. 最大人工岛

**难度**: Hard | **标签**: `Array` `Depth-First Search` `Breadth-First Search` `Union-Find` `Matrix`

## 题目描述

<p>给你一个大小为 <code>n x n</code> 二进制矩阵 <code>grid</code> 。<strong>最多</strong> 只能将一格&nbsp;<code>0</code> 变成&nbsp;<code>1</code> 。</p>

<p>返回执行此操作后，<code>grid</code> 中最大的岛屿面积是多少？</p>

<p><strong>岛屿</strong> 由一组上、下、左、右四个方向相连的&nbsp;<code>1</code> 形成。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入: </strong>grid = [[1, 0], [0, 1]]
<strong>输出:</strong> 3
<strong>解释:</strong> 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入: </strong>grid =<strong> </strong>[[1, 1], [1, 0]]
<strong>输出:</strong> 4
<strong>解释:</strong> 将一格0变成1，岛屿的面积扩大为 4。</pre>

<p><strong class="example">示例 3:</strong></p>

<pre>
<strong>输入: </strong>grid = [[1, 1], [1, 1]]
<strong>输出:</strong> 4
<strong>解释:</strong> 没有0可以让我们变成1，面积依然为 4。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>grid[i][j]</code> 为 <code>0</code> 或 <code>1</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过标记和计算每个岛屿的面积，然后尝试将一个水域变为陆地以连接相邻的岛屿，从而找到最大可能的岛屿面积。

2. **综合思路：**
   - **DFS（深度优先搜索）标记岛屿：** 使用DFS遍历每个岛屿，将其标记为一个唯一的岛屿ID，并计算其面积。
   - **模拟连接：** 遍历每个水域（值为0的格子），尝试将其变为陆地（值为1），并计算通过连接相邻岛屿所能形成的最大岛屿面积。

3. **全量伪代码：**

   - **DFS标记岛屿并计算面积：**
     ```
     函数 getArea(网格, 行, 列, 岛屿ID):
         初始化 栈 = [(行, 列)]
         初始化 面积 = 0
         将网格[行][列]标记为岛屿ID
         当栈不为空时:
             弹出当前行列 (currR, currC)
             面积 += 1
             对于每个方向 (dr, dc) 在 [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                 计算新行列 (nr, nc) = (currR + dr, currC + dc)
                 如果新行列在网格范围内且网格[nr][nc] == 1:
                     将网格[nr][nc]标记为岛屿ID
                     将 (nr, nc) 添加到栈中
         返回 面积
     ```

   - **主函数计算最大人工岛面积：**
     ```
     函数 largestIsland(网格):
         初始化 n = 网格的行数
         初始化 面积字典 = {0: 0}
         初始化 岛屿ID = 2

         对于每个格子 (r, c) 在网格中:
             如果网格[r][c] == 1:
                 计算面积 = getArea(网格, r, c, 岛屿ID)
                 面积字典[岛屿ID] = 计算面积
                 岛屿ID += 1

         初始化 最大面积 = 面积字典的最大值

         对于每个格子 (r, c) 在网格中:
             如果网格[r][c] == 0:
                 初始化 看到的岛屿集合 = 空集合
                 对于每个方向 (dr, dc) 在 [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                     计算新行列 (nr, nc) = (r + dr, c + dc)
                     如果新行列在网格范围内:
                         将网格[nr][nc]的岛屿ID添加到看到的岛屿集合中
                 当前组合面积 = 1 + sum(面积字典[岛屿ID] 对于 岛屿ID 在 看到的岛屿集合中)
                 最大面积 = max(最大面积, 当前组合面积)

         返回 最大面积
     ```

4. **复杂度：**
   - **时间复杂度：** $O(n^2)$，其中 $n$ 是网格的边长，因为我们需要遍历整个网格来标记岛屿和计算可能的最大面积。
   - **空间复杂度：** $O(n^2)$，用于存储岛屿标记和面积信息。