# 19. 删除链表的倒数第 N 个结点

**难度**: Medium | **标签**: `Linked List` `Two Pointers`

## 题目描述

<p>给你一个链表，删除链表的倒数第&nbsp;<code>n</code><em>&nbsp;</em>个结点，并且返回链表的头结点。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,4,5], n = 2
<strong>输出：</strong>[1,2,3,5]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>head = [1], n = 1
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>head = [1,2], n = 1
<strong>输出：</strong>[1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中结点的数目为 <code>sz</code></li>
	<li><code>1 &lt;= sz &lt;= 30</code></li>
	<li><code>0 &lt;= Node.val &lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= sz</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你能尝试使用一趟扫描实现吗？</p>


---
## 解题思路与复盘

1. 一句话直击本质：使用双指针技巧，先让快指针领先慢指针 n 步，然后同时移动两个指针直到快指针到达链表末尾，从而定位并删除倒数第 N 个结点。

2. 综合思路：
   - 双指针法：利用两个指针（快指针和慢指针），快指针先移动 n 步，然后两个指针同时移动，直到快指针到达链表末尾，此时慢指针指向的就是要删除结点的前一个结点。
   - 递归法：虽然在提供的代码中没有递归实现，但递归也可以用于解决此问题，通过递归返回链表的长度并在回溯时删除目标结点。

3. 全量伪代码：
   - 双指针法：
     ```
     初始化虚拟节点 dummy，指向 head
     初始化 slow 和 fast 指针指向 dummy
     让 fast 指针先移动 n 步
     当 fast 的下一个节点不为空时：
         同时移动 slow 和 fast 指针
     slow 的下一个节点指向 slow 的下下个节点（删除目标节点）
     返回 dummy 的下一个节点
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是链表的长度，因为需要遍历链表一次。
   - 空间复杂度：$O(1)$，因为只使用了常数级别的额外空间。