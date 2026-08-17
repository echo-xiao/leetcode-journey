# 1609. 寻找所有的独生节点 · 题目

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`

## 题目描述

<p>在二叉树中，<strong>孤独</strong>节点是指其父节点唯一的子节点。树的根节点不是孤独的，因为它没有父节点。</p>

<p>给定一个二叉树的 <code>root</code>，返回 <em>一个包含树中所有孤独节点值的数组</em>。返回的列表 <strong>可以是任意顺序</strong>。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/06/03/e1.png" style="width: 203px; height: 202px;" />
<pre>
<strong>输入:</strong> root = [1,2,3,null,4]
<strong>输出:</strong> [4]
<strong>解释:</strong> 浅蓝色节点是唯一的孤独节点。
节点 1 是根节点，不是孤独的。
节点 2 和 3 具有相同的父节点，不是孤独的。
</pre>

<p><strong class="example">示例 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/06/03/e2.png" style="width: 442px; height: 282px;" />
<pre>
<strong>输入:</strong> root = [7,1,4,6,null,5,3,null,null,null,null,null,2]
<strong>输出:</strong> [6,2]
<strong>解释:</strong> 浅蓝色节点是孤独节点。
请记住顺序无关紧要，[2,6] 也是一个可接受的答案。
</pre>

<p><strong class="example">示例 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/06/03/tree.png" style="width: 363px; height: 202px;" />
<pre>
<strong>输入:</strong> root = [11,99,88,77,null,null,66,55,null,null,44,33,null,null,22]
<strong>输出:</strong> [77,55,33,66,44,22]
<strong>解释:</strong> 节点 99 和 88 共享相同的父节点。节点 11 是根节点。
所有其他节点都是孤独的。
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li>树中节点的数量在 <code>[1, 1000].</code> 范围内。</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>6</sup></code></li>
</ul>
