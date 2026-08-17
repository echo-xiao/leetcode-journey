# 323. 无向图中连通分量的数目 · 题目

**难度**: Medium | **标签**: `Depth-First Search` `Breadth-First Search` `Union-Find` `Graph Theory`

## 题目描述

<p>你有一个包含 <code>n</code> 个节点的图。给定一个整数 <code>n</code> 和一个数组 <code>edges</code>，其中 <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示图中存在一条连接 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code> 的边。</p>

<p>返回 <em>图中连接组件的数量</em>。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/conn1-graph.jpg" style="width: 382px; height: 222px;" />
<pre>
<strong>输入:</strong> n = 5, edges = [[0,1],[1,2],[3,4]]
<strong>输出:</strong> 2
</pre>

<p><strong class="example">示例 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/conn2-graph.jpg" style="width: 382px; height: 222px;" />
<pre>
<strong>输入:</strong> n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
<strong>输出:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2000</code></li>
	<li><code>1 &lt;= edges.length &lt;= 5000</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub> &lt;= b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>没有重复的边。</li>
</ul>
