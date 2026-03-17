# 3271. 按距离统计房屋对数目 I

**难度**: Medium | **标签**: `Breadth-First Search` `Graph Theory` `Prefix Sum`

**归类**: 8. 常用数据结构 > Breadth-First Search

## 题目描述

<p>给你三个<strong> 正整数 </strong><code>n</code> 、<code>x</code> 和 <code>y</code> 。</p>

<p>在城市中，存在编号从 <code>1</code> 到 <code>n</code> 的房屋，由 <code>n</code> 条街道相连。对所有 <code>1 &lt;= i &lt; n</code> ，都存在一条街道连接编号为 <code>i</code> 的房屋与编号为 <code>i + 1</code> 的房屋。另存在一条街道连接编号为 <code>x</code> 的房屋与编号为 <code>y</code> 的房屋。</p>

<p>对于每个 <code>k</code>（<code>1 &lt;= k &lt;= n</code>），你需要找出所有满足要求的 <strong>房屋对 </strong><code>[house<sub>1</sub>, house<sub>2</sub>]</code> ，即从 <code>house<sub>1</sub></code> 到 <code>house<sub>2</sub></code> 需要经过的<strong> 最少</strong> 街道数为 <code>k</code> 。</p>

<p>返回一个下标从 <strong>1</strong> 开始且长度为 <code>n</code> 的数组 <code>result</code> ，其中 <code>result[k]</code> 表示所有满足要求的房屋对的数量，即从一个房屋到另一个房屋需要经过的<strong> 最少 </strong>街道数为 <code>k</code> 。</p>

<p><strong>注意</strong>，<code>x</code> 与 <code>y</code> 可以 <strong>相等 </strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/20/example2.png" style="width: 474px; height: 197px;" />
<pre>
<strong>输入：</strong>n = 3, x = 1, y = 3
<strong>输出：</strong>[6,0,0]
<strong>解释：</strong>让我们检视每个房屋对
- 对于房屋对 (1, 2)，可以直接从房屋 1 到房屋 2。
- 对于房屋对 (2, 1)，可以直接从房屋 2 到房屋 1。
- 对于房屋对 (1, 3)，可以直接从房屋 1 到房屋 3。
- 对于房屋对 (3, 1)，可以直接从房屋 3 到房屋 1。
- 对于房屋对 (2, 3)，可以直接从房屋 2 到房屋 3。
- 对于房屋对 (3, 2)，可以直接从房屋 3 到房屋 2。
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/20/example3.png" style="width: 668px; height: 174px;" />
<pre>
<strong>输入：</strong>n = 5, x = 2, y = 4
<strong>输出：</strong>[10,8,2,0,0]
<strong>解释：</strong>对于每个距离 k ，满足要求的房屋对如下：
- 对于 k == 1，满足要求的房屋对有 (1, 2), (2, 1), (2, 3), (3, 2), (2, 4), (4, 2), (3, 4), (4, 3), (4, 5), 以及 (5, 4)。
- 对于 k == 2，满足要求的房屋对有 (1, 3), (3, 1), (1, 4), (4, 1), (2, 5), (5, 2), (3, 5), 以及 (5, 3)。
- 对于 k == 3，满足要求的房屋对有 (1, 5)，以及 (5, 1) 。
- 对于 k == 4 和 k == 5，不存在满足要求的房屋对。
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/20/example5.png" style="width: 544px; height: 130px;" />
<pre>
<strong>输入：</strong>n = 4, x = 1, y = 1
<strong>输出：</strong>[6,4,2,0]
<strong>解释：</strong>对于每个距离 k ，满足要求的房屋对如下：
- 对于 k == 1，满足要求的房屋对有 (1, 2), (2, 1), (2, 3), (3, 2), (3, 4), 以及 (4, 3)。
- 对于 k == 2，满足要求的房屋对有 (1, 3), (3, 1), (2, 4), 以及 (4, 2)。
- 对于 k == 3，满足要求的房屋对有 (1, 4), 以及 (4, 1)。
- 对于 k == 4，不存在满足要求的房屋对。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= x, y &lt;= n</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过构建图结构并使用广度优先搜索（BFS）或 Floyd-Warshall 算法计算所有节点对之间的最短路径，然后统计每个距离的房屋对数。

2. 综合思路：
   - **Floyd-Warshall 算法**：版本 1 使用 Floyd-Warshall 算法计算所有节点对之间的最短路径。该算法通过动态规划更新节点间的最短路径，适合于密集图。
   - **广度优先搜索（BFS）**：版本 2、3 和 4 使用 BFS 遍历图，从每个节点出发计算到其他节点的最短路径。BFS 适合于稀疏图，尤其是树结构。

3. 全量伪代码：
   - **Floyd-Warshall 算法**：
     ```
     初始化一个 n+1 x n+1 的二维数组 dist，所有值为无穷大
     对于每个节点 i，设置 dist[i][i] = 0
     对于每对相邻节点 i 和 i+1，设置 dist[i][i+1] = dist[i+1][i] = 1
     如果 x 和 y 不相等，设置 dist[x][y] = dist[y][x] = 1
     对于每个中间节点 k，更新所有节点对 (i, j) 的最短路径
     初始化结果数组 res，长度为 n，所有值为 0
     对于每对节点 (i, j)，如果 i != j，增加 res[dist[i][j] - 1] 的计数
     返回结果数组 res
     ```
   - **广度优先搜索（BFS）**：
     ```
     初始化一个 n+1 长度的邻接表 adj
     对于每对相邻节点 i 和 i+1，添加边 i <-> i+1 到 adj
     添加边 x <-> y 到 adj
     初始化结果数组 res，长度为 n，所有值为 0
     对于每个节点 j：
         初始化队列 queue，包含 (j, 0)
         初始化访问集合 visited，包含 j
         当队列不为空时：
             弹出队列头部元素 (curr, dist)
             如果 dist > 0，增加 res[dist - 1] 的计数
             对于 curr 的每个邻居 v：
                 如果 v 未访问过，将 v 添加到 visited，并将 (v, dist + 1) 添加到队列
     返回结果数组 res
     ```

4. 复杂度：
   - **Floyd-Warshall 算法**：
     - 时间复杂度：$O(n^3)$，因为需要遍历所有节点对三次。
     - 空间复杂度：$O(n^2)$，因为需要存储所有节点对之间的距离。
   - **广度优先搜索（BFS）**：
     - 时间复杂度：$O(n^2)$，因为对于每个节点都进行一次 BFS，遍历所有边。
     - 空间复杂度：$O(n)$，因为需要存储邻接表和访问集合。