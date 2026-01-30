# 1661. 可以到达所有点的最少点数目

**难度**: Medium | **标签**: `Graph Theory`

## 题目描述

<p>给你一个 <strong>有向无环图</strong>&nbsp;， <code>n</code>&nbsp;个节点编号为 <code>0</code>&nbsp;到 <code>n-1</code>&nbsp;，以及一个边数组 <code>edges</code>&nbsp;，其中 <code>edges[i] = [from<sub>i</sub>, to<sub>i</sub>]</code>&nbsp;表示一条从点&nbsp;&nbsp;<code>from<sub>i</sub></code>&nbsp;到点&nbsp;<code>to<sub>i</sub></code>&nbsp;的有向边。</p>

<p>找到最小的点集使得从这些点出发能到达图中所有点。题目保证解存在且唯一。</p>

<p>你可以以任意顺序返回这些节点编号。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/22/5480e1.png" style="height: 181px; width: 231px;"></p>

<pre><strong>输入：</strong>n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
<strong>输出：</strong>[0,3]
<strong>解释：</strong>从单个节点出发无法到达所有节点。从 0 出发我们可以到达 [0,1,2,5] 。从 3 出发我们可以到达 [3,4,2,5] 。所以我们输出 [0,3] 。</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/22/5480e2.png" style="height: 201px; width: 201px;"></p>

<pre><strong>输入：</strong>n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
<strong>输出：</strong>[0,2,3]
<strong>解释：</strong>注意到节点 0，3 和 2 无法从其他节点到达，所以我们必须将它们包含在结果点集中，这些点都能到达节点 1 和 4 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10^5</code></li>
	<li><code>1 &lt;= edges.length &lt;= min(10^5, n * (n - 1) / 2)</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= from<sub>i,</sub>&nbsp;to<sub>i</sub> &lt; n</code></li>
	<li>所有点对&nbsp;<code>(from<sub>i</sub>, to<sub>i</sub>)</code>&nbsp;互不相同。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：
   - 核心逻辑是：找到所有入度为零的节点，因为这些节点是图中所有其他节点的起点。

2. 综合思路：
   - 这道题的解法主要是基于图的入度分析。对于给定的有向图，任何一个节点如果没有其他节点指向它（即入度为零），那么它必须是一个起始节点。通过遍历所有边来标记每个节点的入度状态，然后选择所有入度为零的节点作为结果。
   - 由于题目提供的代码实现逻辑完全相同，因此没有递归与迭代、DFS与BFS等多种解法的对比。

3. 全量伪代码：
   ```plaintext
   初始化一个大小为 n 的布尔数组 indegree，所有元素初始为 False
   初始化一个空列表 ans 用于存储结果

   对于每条边 (u, v)：
       将 indegree[v] 标记为 True

   对于每个节点 i 从 0 到 n-1：
       如果 indegree[i] 为 False：
           将 i 添加到 ans 中

   返回 ans
   ```

4. 复杂度：
   - 时间复杂度：$O(n + m)$，其中 $n$ 是节点数，$m$ 是边数，因为我们需要遍历所有节点和边。
   - 空间复杂度：$O(n)$，因为我们使用了一个大小为 $n$ 的数组来存储每个节点的入度状态。