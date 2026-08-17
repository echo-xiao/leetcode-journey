# 261. 以图判树 · 题目

**难度**: Medium | **标签**: `Depth-First Search` `Breadth-First Search` `Union-Find` `Graph Theory`

## 题目描述

<p>你有一个包含 <code>n</code> 个节点的图，这些节点的标签从 <code>0</code> 到 <code>n - 1</code>。给定一个整数 n 和一个 <code>edges</code> 列表，其中 <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示图中节点 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code> 之间存在一条无向边。</p>

<p>如果给定图的边构成一个有效的树，则返回 <code>true</code>，否则返回 <code>false</code>。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/12/tree1-graph.jpg" style="width: 222px; height: 302px;" />
<pre>
<strong>输入:</strong> n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
<strong>输出:</strong> true
</pre>

<p><strong class="example">示例 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/12/tree2-graph.jpg" style="width: 382px; height: 222px;" />
<pre>
<strong>输入:</strong> n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
<strong>输出:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2000</code></li>
	<li><code>0 &lt;= edges.length &lt;= 5000</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>没有自环或重复边。</li>
</ul>
