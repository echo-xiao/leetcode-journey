# 1982. 从未排序的链表中移除重复元素 · 题目

**难度**: Medium | **标签**: `Hash Table` `Linked List`

## 题目描述

<p>给定一个链表的 <code>head</code>，找出链表中出现<strong>超过一次</strong>的所有值，并删除包含这些值的节点。</p>

<p>返回<em>删除后的链表。</em></p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/21/tmp-linked-list.jpg" style="width: 422px; height: 222px;" />
<pre>
<strong>输入:</strong> head = [1,2,3,2]
<strong>输出:</strong> [1,3]
<strong>解释:</strong> 2 在链表中出现了两次，因此所有的 2 应该被删除。删除所有的 2 后，我们剩下 [1,3]。
</pre>

<p><strong class="example">示例 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/21/tmp-linked-list-1.jpg" style="width: 422px; height: 151px;" />
<pre>
<strong>输入:</strong> head = [2,1,1,2]
<strong>输出:</strong> []
<strong>解释:</strong> 2 和 1 都出现了两次。所有元素都应该被删除。
</pre>

<p><strong class="example">示例 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/21/tmp-linked-list-2.jpg" style="width: 500px; height: 142px;" />
<pre>
<strong>输入:</strong> head = [3,2,2,1,3,2,4]
<strong>输出:</strong> [1,4]
<strong>解释:</strong> 3 出现了两次，2 出现了三次。删除所有的 3 和 2 后，我们剩下 [1,4]。
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li>链表中的节点数在范围&nbsp;<code>[1, 10<sup>5</sup>]</code>内</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>
