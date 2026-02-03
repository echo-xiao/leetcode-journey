# 547. 省份数量

**难度**: Medium | **标签**: `Depth-First Search` `Breadth-First Search` `Union-Find` `Graph Theory`

**归类**: 11. 链表、树与回溯 > Depth-First Search

## 题目描述

<div class="original__bRMd">
<div>
<p>有 <code>n</code> 个城市，其中一些彼此相连，另一些没有相连。如果城市 <code>a</code> 与城市 <code>b</code> 直接相连，且城市 <code>b</code> 与城市 <code>c</code> 直接相连，那么城市 <code>a</code> 与城市 <code>c</code> 间接相连。</p>

<p><strong>省份</strong> 是一组直接或间接相连的城市，组内不含其他没有相连的城市。</p>

<p>给你一个 <code>n x n</code> 的矩阵 <code>isConnected</code> ，其中 <code>isConnected[i][j] = 1</code> 表示第 <code>i</code> 个城市和第 <code>j</code> 个城市直接相连，而 <code>isConnected[i][j] = 0</code> 表示二者不直接相连。</p>

<p>返回矩阵中 <strong>省份</strong> 的数量。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg" style="width: 222px; height: 142px;" />
<pre>
<strong>输入：</strong>isConnected = [[1,1,0],[1,1,0],[0,0,1]]
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg" style="width: 222px; height: 142px;" />
<pre>
<strong>输入：</strong>isConnected = [[1,0,0],[0,1,0],[0,0,1]]
<strong>输出：</strong>3
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 200</code></li>
	<li><code>n == isConnected.length</code></li>
	<li><code>n == isConnected[i].length</code></li>
	<li><code>isConnected[i][j]</code> 为 <code>1</code> 或 <code>0</code></li>
	<li><code>isConnected[i][i] == 1</code></li>
	<li><code>isConnected[i][j] == isConnected[j][i]</code></li>
</ul>
</div>
</div>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过并查集或图的遍历（DFS/BFS）来识别连通分量的数量，从而确定省份的数量。

2. 综合思路：
   - 并查集（Union-Find）：通过合并节点来识别连通分量，最终统计不同根节点的数量。
   - 深度优先搜索（DFS）：递归地遍历每个节点的邻居，标记访问过的节点，统计连通分量。
   - 广度优先搜索（BFS）：使用队列迭代地遍历每个节点的邻居，标记访问过的节点，统计连通分量。

3. 全量伪代码：
   - 并查集：
     ```
     初始化每个节点的父节点为自身，计数器为节点数
     对于每对节点 (i, j)，如果它们相连且不在同一集合中，则合并它们并减少计数器
     返回计数器
     ```
   - 深度优先搜索（DFS）：
     ```
     初始化访问集合和省份计数器
     对于每个节点 i，如果未访问，则递增省份计数器并调用递归函数
     递归函数：标记当前节点为已访问，递归访问所有相邻且未访问的节点
     返回省份计数器
     ```
   - 广度优先搜索（BFS）：
     ```
     初始化访问集合和省份计数器
     对于每个节点 i，如果未访问，则递增省份计数器并初始化队列
     队列处理：标记当前节点为已访问，遍历所有相邻且未访问的节点并加入队列
     返回省份计数器
     ```

4. 复杂度：
   - 并查集：
     - 时间复杂度：$O(n^2 \cdot \alpha(n))$，其中 $\alpha(n)$ 是反阿克曼函数。
     - 空间复杂度：$O(n)$。
   - 深度优先搜索（DFS）：
     - 时间复杂度：$O(n^2)$。
     - 空间复杂度：$O(n)$。
   - 广度优先搜索（BFS）：
     - 时间复杂度：$O(n^2)$。
     - 空间复杂度：$O(n)$。