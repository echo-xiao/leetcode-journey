# 1618. 删除链表 M 个节点之后的 N 个节点 · 题目

**难度**: Easy | **标签**: `Linked List`

## 题目描述

<p>给定一个链表的 <code>head</code> 和两个整数 <code>m</code> 和 <code>n</code>。</p>

<p>遍历链表并以以下方式删除一些节点：</p>

<ul>
	<li>从头节点开始作为当前节点。</li>
	<li>保留从当前节点开始的前 <code>m</code> 个节点。</li>
	<li>删除接下来的 <code>n</code> 个节点。</li>
	<li>重复步骤 2 和 3，直到到达链表的末尾。</li>
</ul>

<p>返回 <em>删除提到的节点后修改过的链表的头节点</em>。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/06/06/sample_1_1848.png" style="width: 600px; height: 95px;" />
<pre>
<strong>输入:</strong> head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3
<strong>输出:</strong> [1,2,6,7,11,12]
<strong>解释:</strong> 从链表的头节点开始保留前 (m = 2) 个节点 (1 -&gt;2) 显示为黑色节点。
删除接下来的 (n = 3) 个节点 (3 -&gt; 4 -&gt; 5) 显示为红色节点。
继续相同的过程，直到到达链表的尾部。
返回删除节点后的链表头节点。
</pre>

<p><strong class="example">示例 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/06/06/sample_2_1848.png" style="width: 600px; height: 123px;" />
<pre>
<strong>输入:</strong> head = [1,2,3,4,5,6,7,8,9,10,11], m = 1, n = 3
<strong>输出:</strong> [1,5,9]
<strong>解释:</strong> 返回删除节点后的链表头节点。
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li>链表中的节点数在 <code>[1, 10<sup>4</sup>]</code> 范围内。</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= m, n &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>后续问题:</strong> 你能通过原地修改链表来解决这个问题吗？</p>
