# 1706. 连接所有点的最小费用

**难度**: Medium | **标签**: `Array` `Union-Find` `Graph Theory` `Minimum Spanning Tree`

**归类**: 6. 图论算法 > Array

## 题目描述

<p>给你一个<code>points</code>&nbsp;数组，表示 2D 平面上的一些点，其中&nbsp;<code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>&nbsp;。</p>

<p>连接点&nbsp;<code>[x<sub>i</sub>, y<sub>i</sub>]</code> 和点&nbsp;<code>[x<sub>j</sub>, y<sub>j</sub>]</code>&nbsp;的费用为它们之间的 <strong>曼哈顿距离</strong>&nbsp;：<code>|x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>|</code>&nbsp;，其中&nbsp;<code>|val|</code>&nbsp;表示&nbsp;<code>val</code>&nbsp;的绝对值。</p>

<p>请你返回将所有点连接的最小总费用。只有任意两点之间 <strong>有且仅有</strong>&nbsp;一条简单路径时，才认为所有点都已连接。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/d.png" style="height:268px; width:214px; background:#e5e5e5" /></p>

<pre>
<strong>输入：</strong>points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
<strong>输出：</strong>20
<strong>解释：
</strong><img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/c.png" style="height:268px; width:214px; background:#e5e5e5" />
我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
注意到任意两个点之间只有唯一一条路径互相到达。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>points = [[3,12],[-2,5],[-4,1]]
<strong>输出：</strong>18
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>points = [[0,0],[1,1],[1,0],[-1,1]]
<strong>输出：</strong>4
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>points = [[-1000000,-1000000],[1000000,1000000]]
<strong>输出：</strong>4000000
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>points = [[0,0]]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= points.length &lt;= 1000</code></li>
	<li><code>-10<sup>6</sup>&nbsp;&lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
	<li>所有点&nbsp;<code>(x<sub>i</sub>, y<sub>i</sub>)</code>&nbsp;两两不同。</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：**
   - 该算法的核心逻辑是通过最小生成树算法（Kruskal 或 Prim）来计算连接所有点的最小费用。

2. **综合思路：**
   - **Kruskal 算法：** 使用并查集（Union-Find）来管理连通性，首先计算所有点对之间的距离，按距离排序后逐一尝试连接，直到形成最小生成树。
   - **Prim 算法（基于最小堆）：** 从某个起始点开始，使用优先队列（最小堆）来选择当前最小的边，逐步扩展生成树。
   - **Prim 算法（基于数组）：** 维护一个距离数组，逐步选择未访问的点中距离最小的点进行扩展。

3. **全量伪代码：**

   - **Kruskal 算法：**
     ```
     初始化 parent 数组，表示每个节点的父节点
     初始化 edges 数组，存储所有边及其权重
     对于每一对点 (i, j):
         计算曼哈顿距离并加入 edges
     将 edges 按照距离排序
     初始化 cost 为 0，cnt 为 0
     对于每条边 (dist, u, v) in edges:
         如果 u 和 v 不在同一个集合中:
             合并 u 和 v 的集合
             cost 增加 dist
             cnt 增加 1
             如果 cnt 达到 n-1:
                 结束循环
     返回 cost
     ```

   - **Prim 算法（基于最小堆）：**
     ```
     初始化 visited 数组，表示每个节点是否已访问
     初始化 minHeap 为 [(0, 0)]，表示从节点 0 开始
     初始化 cost 为 0
     当 minHeap 不为空:
         弹出 minHeap 中的最小元素 (dist, u)
         如果 u 已访问，跳过
         标记 u 为已访问
         cost 增加 dist
         对于每个未访问的节点 v:
             计算 u 到 v 的距离 newDist
             将 (newDist, v) 加入 minHeap
     返回 cost
     ```

   - **Prim 算法（基于数组）：**
     ```
     初始化 dist 数组为无穷大，dist[0] 为 0
     初始化 visited 数组，表示每个节点是否已访问
     初始化 cost 为 0
     对于 n 次迭代:
         找到未访问节点中 dist 最小的节点 u
         标记 u 为已访问
         cost 增加 dist[u]
         对于每个未访问的节点 v:
             计算 u 到 v 的距离 distance
             如果 distance 小于 dist[v]:
                 更新 dist[v] 为 distance
     返回 cost
     ```

4. **复杂度：**

   - **Kruskal 算法：**
     - 时间复杂度：$O(E \log E + E \alpha(V))$，其中 $E$ 是边的数量，$V$ 是顶点数量，$\alpha$ 是反阿克曼函数。
     - 空间复杂度：$O(E + V)$。

   - **Prim 算法（基于最小堆）：**
     - 时间复杂度：$O(E \log V)$，其中 $E$ 是边的数量，$V$ 是顶点数量。
     - 空间复杂度：$O(V)$。

   - **Prim 算法（基于数组）：**
     - 时间复杂度：$O(V^2)$，其中 $V$ 是顶点数量。
     - 空间复杂度：$O(V)$。