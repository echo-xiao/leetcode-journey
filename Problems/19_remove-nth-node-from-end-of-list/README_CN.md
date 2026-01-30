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

1. 一句话直击本质：使用双指针技巧，先让一个指针领先 n 步，然后同时移动两个指针直到第一个指针到达链表末尾，从而定位并删除倒数第 n 个节点。

2. 综合思路：
   - **双指针法（迭代）**：所有版本都使用了双指针法。通过设置一个虚拟头节点（dummy node），两个指针（slow 和 fast）从虚拟头节点开始，fast 指针先移动 n 步，然后 slow 和 fast 同时移动，直到 fast 到达链表末尾。此时，slow 的下一个节点即为需要删除的节点。
   - **递归法**：虽然在提供的代码集中没有递归法，但递归法也是一种常见解法。递归法通过递归遍历到链表末尾，然后在回溯过程中计数，删除倒数第 n 个节点。

3. 全量伪代码：
   - **双指针法伪代码**：
     ```
     定义一个虚拟节点 dummy，指向 head
     初始化 slow 和 fast 指针指向 dummy
     让 fast 指针先移动 n 步
     当 fast 的下一个节点不为空时：
         同时移动 slow 和 fast 指针
     slow 的下一个节点指向其下下个节点（删除目标节点）
     返回 dummy 的下一个节点
     ```
   - **递归法伪代码（未在代码集中出现，但作为补充）**：
     ```
     定义递归函数 remove(node, n)：
         如果 node 为空，返回 0
         递归调用 remove(node.next, n)，得到返回值 count
         如果 count 等于 n，删除当前节点的下一个节点
         返回 count + 1
     调用 remove(head, n)
     如果删除的是头节点，返回 head 的下一个节点，否则返回 head
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是链表的长度，因为需要遍历链表一次。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外指针。