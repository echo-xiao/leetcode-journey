# 270. 最接近的二叉搜索树值 · 题目

**难度**: Easy | **标签**: `Binary Search` `Tree` `Depth-First Search` `Binary Search Tree` `Binary Tree`

## 题目描述

<p>给定一个二叉搜索树的 <code>root</code> 和一个 <code>target</code> 值，返回 <em>在 BST 中最接近</em> <code>target</code> 的值。如果有多个答案，返回最小的。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/12/closest1-1-tree.jpg" style="width: 292px; height: 302px;" />
<pre>
<strong>输入:</strong> root = [4,2,5,1,3], target = 3.714286
<strong>输出:</strong> 4
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> root = [1], target = 4.428571
<strong>输出:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li>树中的节点数量在 <code>[1, 10<sup>4</sup>]</code> 范围内。</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>
