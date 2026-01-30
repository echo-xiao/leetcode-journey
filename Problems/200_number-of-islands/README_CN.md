# 200. 岛屿数量

**难度**: Medium | **标签**: `Array` `Depth-First Search` `Breadth-First Search` `Union-Find` `Matrix`

## 题目描述

<p>给你一个由&nbsp;<code>'1'</code>（陆地）和 <code>'0'</code>（水）组成的的二维网格，请你计算网格中岛屿的数量。</p>

<p>岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。</p>

<p>此外，你可以假设该网格的四条边均被水包围。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>grid = [
&nbsp; ['1','1','1','1','0'],
&nbsp; ['1','1','0','1','0'],
&nbsp; ['1','1','0','0','0'],
&nbsp; ['0','0','0','0','0']
]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [
&nbsp; ['1','1','0','0','0'],
&nbsp; ['1','1','0','0','0'],
&nbsp; ['0','0','1','0','0'],
&nbsp; ['0','0','0','1','1']
]
<strong>输出：</strong>3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>grid[i][j]</code> 的值为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


---
## 解题思路与复盘

### 一句话直击本质

通过遍历网格并使用深度优先搜索（DFS）、广度优先搜索（BFS）或并查集（Union-Find）来标记和合并相连的陆地，从而计算岛屿的数量。

### 综合思路

1. **DFS（深度优先搜索）**
   - 递归版：从每个未访问的陆地开始，递归地将所有相连的陆地标记为已访问。
   - 迭代版：使用栈模拟递归过程，逐步标记相连的陆地。

2. **BFS（广度优先搜索）**
   - 使用队列从每个未访问的陆地开始，逐层标记所有相连的陆地。

3. **Union-Find（并查集）**
   - 初始化每个陆地为一个独立的集合，遍历网格合并相邻的陆地集合，最终集合的数量即为岛屿数量。

### 全量伪代码

#### DFS 递归版

```
函数 numIslands(grid):
    如果 grid 为空, 返回 0
    初始化岛屿计数 cnt 为 0
    遍历每个单元格 (r, c) 在 grid 中:
        如果 grid[r][c] 是 '1':
            调用 dfs(grid, r, c)
            增加岛屿计数 cnt
    返回 cnt

函数 dfs(grid, r, c):
    如果 r 或 c 越界 或 grid[r][c] 是 '0', 返回
    将 grid[r][c] 标记为 '0'
    调用 dfs(grid, r+1, c)
    调用 dfs(grid, r-1, c)
    调用 dfs(grid, r, c+1)
    调用 dfs(grid, r, c-1)
```

#### DFS 迭代版

```
函数 dfs(grid, r, c):
    初始化栈 stack 为 [(r, c)]
    将 grid[r][c] 标记为 '0'
    当栈 stack 非空时:
        弹出栈顶元素 currR, currC
        对于每个方向 dr, dc:
            计算新位置 nxtR, nxtC
            如果 nxtR 和 nxtC 在边界内 且 grid[nxtR][nxtC] 是 '1':
                将 (nxtR, nxtC) 压入栈
                将 grid[nxtR][nxtC] 标记为 '0'
```

#### BFS

```
函数 bfs(grid, r, c):
    初始化队列 queue 为 [(r, c)]
    将 grid[r][c] 标记为 '0'
    当队列 queue 非空时:
        弹出队首元素 currR, currC
        对于每个方向 dr, dc:
            计算新位置 nxtR, nxtC
            如果 nxtR 和 nxtC 在边界内 且 grid[nxtR][nxtC] 是 '1':
                将 (nxtR, nxtC) 加入队列
                将 grid[nxtR][nxtC] 标记为 '0'
```

#### Union-Find

```
函数 numIslands(grid):
    如果 grid 为空, 返回 0
    初始化 parent 数组和岛屿计数 cnt
    遍历每个单元格 (r, c) 在 grid 中:
        如果 grid[r][c] 是 '1':
            增加岛屿计数 cnt
            初始化 parent[idx] 为 idx
    遍历每个单元格 (r, c) 在 grid 中:
        如果 grid[r][c] 是 '1':
            对于右和下方向的邻居:
                如果邻居是 '1', 调用 union 操作
                如果 union 成功, 减少岛屿计数 cnt
    返回 cnt

函数 find(parent, i):
    如果 parent[i] 是 i, 返回 i
    否则, 递归查找 parent[i] 的根, 并路径压缩

函数 union(parent, i, j):
    找到 i 和 j 的根 rootI 和 rootJ
    如果 rootI 不等于 rootJ:
        将 rootI 的根设置为 rootJ
        返回 True
    返回 False
```

### 复杂度

- **DFS 和 BFS**
  - 时间复杂度: $O(M \times N)$，其中 $M$ 和 $N$ 分别是网格的行数和列数，因为每个单元格最多被访问一次。
  - 空间复杂度: $O(M \times N)$，在最坏情况下，递归栈或队列可能需要存储整个网格。

- **Union-Find**
  - 时间复杂度: $O(M \times N \cdot \alpha(M \times N))$，其中 $\alpha$ 是反阿克曼函数，几乎是常数时间。
  - 空间复杂度: $O(M \times N)$，用于存储并查集的父节点数组。