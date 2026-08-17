# 156. 上下翻转二叉树 · 题目

**难度**: Medium | **标签**: `Tree` `Depth-First Search` `Binary Tree`

## 题目描述

<p>给定一个二叉树的 <code>root</code>，将树翻转并返回 <em>新的根节点</em>。</p>

<p>你可以通过以下步骤将二叉树翻转：</p>

<ol>
	<li>原来的左子节点变成新的根节点。</li>
	<li>原来的根节点变成新的右子节点。</li>
	<li>原来的右子节点变成新的左子节点。</li>
</ol>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/29/main.jpg" style="width: 600px; height: 95px;" />
<p>上述步骤是逐层进行的。<strong>保证</strong>每个右节点都有一个兄弟节点（同一父节点的左节点），并且没有子节点。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/29/updown.jpg" style="width: 800px; height: 161px;" />
<pre>
<strong>输入:</strong> root = [1,2,3,4,5]
<strong>输出:</strong> [4,5,2,null,null,3,1]
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> root = []
<strong>输出:</strong> []
</pre>

<p><strong class="example">示例 3:</strong></p>

<pre>
<strong>输入:</strong> root = [1]
<strong>输出:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li>树中的节点数量范围为 <code>[0, 10]</code>。</li>
	<li><code>1 &lt;= Node.val &lt;= 10</code></li>
	<li>树中的每个右节点都有一个兄弟节点（共享同一父节点的左节点）。</li>
	<li>树中的每个右节点没有子节点。</li>
</ul>
