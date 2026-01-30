# 310. 最小高度树

**难度**: Medium | **标签**: `Depth-First Search` `Breadth-First Search` `Graph Theory` `Topological Sort`

## 题目描述

<p>树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，任何一个没有简单环路的连通图都是一棵树。</p>

<p>给你一棵包含&nbsp;<code>n</code>&nbsp;个节点的树，标记为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code> 。给定数字&nbsp;<code>n</code>&nbsp;和一个有 <code>n - 1</code> 条无向边的 <code>edges</code>&nbsp;列表（每一个边都是一对标签），其中 <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示树中节点 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code> 之间存在一条无向边。</p>

<p>可选择树中任何一个节点作为根。当选择节点 <code>x</code> 作为根节点时，设结果树的高度为 <code>h</code> 。在所有可能的树中，具有最小高度的树（即，<code>min(h)</code>）被称为 <strong>最小高度树</strong> 。</p>

<p>请你找到所有的 <strong>最小高度树</strong> 并按 <strong>任意顺序</strong> 返回它们的根节点标签列表。</p>
树的 <strong>高度</strong> 是指根节点和叶子节点之间最长向下路径上边的数量。

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/01/e1.jpg" style="height: 213px; width: 800px;" />
<pre>
<strong>输入：</strong>n = 4, edges = [[1,0],[1,2],[1,3]]
<strong>输出：</strong>[1]
<strong>解释：</strong>如图所示，当根是标签为 1 的节点时，树的高度是 1 ，这是唯一的最小高度树。</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/01/e2.jpg" style="height: 321px; width: 800px;" />
<pre>
<strong>输入：</strong>n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
<strong>输出：</strong>[3,4]
</pre>

<p>&nbsp;</p>

<ul>
</ul>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>所有 <code>(a<sub>i</sub>, b<sub>i</sub>)</code> 互不相同</li>
	<li>给定的输入 <strong>保证</strong> 是一棵树，并且 <strong>不会有重复的边</strong></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质**：通过找到图的直径路径的中点或通过拓扑排序逐层剥离叶节点来确定最小高度树的根节点。

2. **综合思路**：
   - **DFS 直径法**：通过两次深度优先搜索（DFS）找到图的直径路径，然后返回该路径的中点作为最小高度树的根节点。
   - **BFS 拓扑排序法**：使用广度优先搜索（BFS）逐层剥离叶节点，直到剩下最后的一个或两个节点，这些节点即为最小高度树的根节点。

3. **全量伪代码**：

   - **DFS 直径法**：
     ```
     如果 n <= 2，返回 [0, 1, ..., n-1]
     构建邻接表 adj
     从节点 0 开始，使用 DFS 找到最远的节点 node_A
     从 node_A 开始，使用 DFS 找到最远的节点 node_B，并记录路径
     从 node_B 回溯到 node_A，重建路径
     如果路径长度为奇数，返回路径中点
     否则，返回路径中间的两个节点
     ```

   - **BFS 拓扑排序法**：
     ```
     如果 n <= 2，返回 [0, 1, ..., n-1]
     构建邻接表 adj 和入度数组 indegree
     将所有入度为 1 的节点（叶节点）加入队列 queue
     初始化剩余节点数 rem 为 n
     当 rem > 2 时，重复以下步骤：
       - 记录当前队列大小 size
       - 将 rem 减去 size
       - 对于队列中的每个节点，移除该节点并更新其邻居的入度
       - 如果邻居的入度变为 1，将其加入队列
     返回队列中的节点
     ```

4. **复杂度**：
   - **DFS 直径法**：
     - 时间复杂度：$O(n)$，因为每个节点和边都被访问两次。
     - 空间复杂度：$O(n)$，用于存储邻接表和递归栈。
   
   - **BFS 拓扑排序法**：
     - 时间复杂度：$O(n)$，因为每个节点和边都被访问一次。
     - 空间复杂度：$O(n)$，用于存储邻接表和队列。