# 2121. 寻找图中是否存在路径

**难度**: Easy | **标签**: `Depth-First Search` `Breadth-First Search` `Union-Find` `Graph Theory`

## 题目描述

<p>有一个具有 <code>n</code> 个顶点的 <strong>双向</strong> 图，其中每个顶点标记从 <code>0</code> 到 <code>n - 1</code>（包含 <code>0</code> 和 <code>n - 1</code>）。图中的边用一个二维整数数组 <code>edges</code> 表示，其中 <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> 表示顶点 <code>ui</code> 和顶点 <code>vi</code> 之间的双向边。 每个顶点对由 <strong>最多一条</strong> 边连接，并且没有顶点存在与自身相连的边。</p>

<p>请你确定是否存在从顶点 <code>source</code> 开始，到顶点 <code>destination</code> 结束的 <strong>有效路径</strong> 。</p>

<p>给你数组 <code>edges</code> 和整数 <code>n</code>、<code>source</code> 和 <code>destination</code>，如果从 <code>source</code> 到 <code>destination</code> 存在 <strong>有效路径</strong> ，则返回 <code>true</code>，否则返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/14/validpath-ex1.png" style="width: 141px; height: 121px;" />
<pre>
<strong>输入：</strong>n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
<strong>输出：</strong>true
<strong>解释：</strong>存在由顶点 0 到顶点 2 的路径:
- 0 → 1 → 2 
- 0 → 2
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/14/validpath-ex2.png" style="width: 281px; height: 141px;" />
<pre>
<strong>输入：</strong>n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
<strong>输出：</strong>false
<strong>解释：</strong>不存在由顶点 0 到顶点 5 的路径.
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>0 &lt;= edges.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li><code>0 &lt;= source, destination &lt;= n - 1</code></li>
	<li>不存在重复边</li>
	<li>不存在指向顶点自身的边</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用深度优先搜索（DFS）遍历图，判断从起点到终点是否存在路径。

2. 综合思路：
   - 递归 DFS：使用递归的方式进行深度优先搜索，遍历每个节点的邻居节点，直到找到目标节点或者遍历完所有可能路径。
   - 迭代 DFS：可以使用栈来模拟递归的过程，逐步探索每个节点的邻居。
   - BFS（广度优先搜索）：虽然在提供的代码中没有实现，但可以使用队列来逐层遍历节点，适合寻找最短路径。
   - 数据结构：使用字典（`defaultdict`）来存储图的邻接表，使用集合或列表来记录访问过的节点。

3. 全量伪代码：
   ```plaintext
   初始化邻接表 mapp 为 defaultdict(list)
   遍历 edges 列表，构建邻接表 mapp
   初始化 visited 列表或集合，记录访问过的节点
   设置目标节点 destination

   定义递归函数 traverse 或 dfs(curr):
       如果当前节点 curr 是目标节点 destination，返回 True
       如果当前节点 curr 已访问过，返回 False
       标记当前节点 curr 为已访问
       遍历 curr 的所有邻居节点:
           如果邻居节点可以到达目标节点，返回 True
       返回 False

   调用 traverse 或 dfs 从 source 开始
   返回结果
   ```

4. 复杂度：
   - 时间复杂度：$O(n + m)$，其中 $n$ 是节点数，$m$ 是边数，因为每个节点和边最多访问一次。
   - 空间复杂度：$O(n)$，用于存储访问状态和递归调用栈。