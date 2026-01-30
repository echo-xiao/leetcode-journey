# 1380. 统计封闭岛屿的数目

**难度**: Medium | **标签**: `Array` `Depth-First Search` `Breadth-First Search` `Union-Find` `Matrix`

## 题目描述

<p>二维矩阵 <code>grid</code>&nbsp;由 <code>0</code>&nbsp;（土地）和 <code>1</code>&nbsp;（水）组成。岛是由最大的4个方向连通的 <code>0</code>&nbsp;组成的群，封闭岛是一个&nbsp;<code>完全</code> 由1包围（左、上、右、下）的岛。</p>

<p>请返回 <em>封闭岛屿</em> 的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/10/31/sample_3_1610.png" style="height: 151px; width: 240px;" /></p>

<pre>
<strong>输入：</strong>grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
<strong>输出：</strong>2
<strong>解释：</strong>
灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。</pre>

<p><strong>示例 2：</strong></p>

<p><img src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/11/07/sample_4_1610.png" style="height: 98px; width: 160px;" /></p>

<pre>
<strong>输入：</strong>grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>grid = [[1,1,1,1,1,1,1],
&nbsp;            [1,0,0,0,0,0,1],
&nbsp;            [1,0,1,1,1,0,1],
&nbsp;            [1,0,1,0,1,0,1],
&nbsp;            [1,0,1,1,1,0,1],
&nbsp;            [1,0,0,0,0,0,1],
             [1,1,1,1,1,1,1]]
<strong>输出：</strong>2
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= grid.length, grid[0].length &lt;= 100</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;=1</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法通过深度优先搜索（DFS）遍历将边界上的所有陆地标记为水，然后统计剩余的封闭岛屿数。

2. 综合思路：
   - **DFS递归法**：首先使用DFS遍历将所有与边界相连的陆地（0）标记为水（1），然后再次遍历整个网格，统计剩余的封闭岛屿数。
   - **BFS迭代法**（未在提供的代码中出现，但常见于此类问题）：类似于DFS，使用队列进行广度优先搜索来标记边界相连的陆地。

3. 全量伪代码：
   ```plaintext
   方法 closedIsland(网格):
       获取网格的行数和列数
       初始化边界队列
       初始化封闭岛屿计数为0

       对于每个边界上的单元格:
           如果单元格是陆地:
               将其坐标加入边界队列

       当边界队列不为空时:
           弹出队列中的一个坐标
           调用DFS函数标记该坐标及其相连的陆地

       对于网格中的每个单元格:
           如果单元格是陆地:
               增加封闭岛屿计数
               调用DFS函数标记该坐标及其相连的陆地

       返回封闭岛屿计数

   方法 DFS(网格, 行, 列):
       如果坐标超出网格范围或单元格是水:
           返回

       将当前单元格标记为水

       递归调用DFS函数处理上下左右四个方向的邻居
   ```

4. 复杂度：
   - 时间复杂度：$O(m \times n)$，其中 $m$ 和 $n$ 分别是网格的行数和列数，因为每个单元格最多被访问一次。
   - 空间复杂度：$O(m \times n)$，在最坏情况下，递归调用栈的深度可能达到整个网格的大小。