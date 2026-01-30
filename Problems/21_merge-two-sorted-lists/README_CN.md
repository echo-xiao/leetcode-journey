# 21. 合并两个有序链表

**难度**: Easy | **标签**: `Linked List` `Recursion`

## 题目描述

<p>将两个升序链表合并为一个新的 <strong>升序</strong> 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 </p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg" style="width: 662px; height: 302px;" />
<pre>
<strong>输入：</strong>l1 = [1,2,4], l2 = [1,3,4]
<strong>输出：</strong>[1,1,2,3,4,4]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>l1 = [], l2 = []
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>l1 = [], l2 = [0]
<strong>输出：</strong>[0]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>两个链表的节点数目范围是 <code>[0, 50]</code></li>
	<li><code>-100 <= Node.val <= 100</code></li>
	<li><code>l1</code> 和 <code>l2</code> 均按 <strong>非递减顺序</strong> 排列</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过迭代比较两个有序链表的节点值，逐步将较小的节点链接到结果链表中，直到其中一个链表为空，再将剩余链表直接链接到结果链表。

2. **综合思路：**
   - **迭代法：** 使用一个虚拟头节点（dummy node）来简化边界条件处理，通过两个指针遍历两个链表，比较当前节点值，将较小的节点链接到结果链表中，直至其中一个链表遍历完毕，然后将剩余的链表直接链接到结果链表。
   - **递归法（未在提供的代码中出现，但常见）：** 通过递归比较两个链表的头节点，选择较小的节点作为结果链表的头节点，并递归处理剩余的链表。

3. **全量伪代码：**

   - **迭代法：**
     ```
     初始化虚拟头节点 dummy 和当前指针 curr 指向 dummy
     当 list1 和 list2 都不为空时：
         如果 list1 的值小于等于 list2 的值：
             将 curr 的 next 指向 list1
             将 list1 移动到下一个节点
         否则：
             将 curr 的 next 指向 list2
             将 list2 移动到下一个节点
         将 curr 移动到下一个节点
     如果 list1 不为空：
         将 curr 的 next 指向 list1
     否则：
         将 curr 的 next 指向 list2
     返回 dummy 的 next
     ```

   - **递归法（未在提供的代码中出现，但常见）：**
     ```
     如果 list1 为空，返回 list2
     如果 list2 为空，返回 list1
     如果 list1 的值小于等于 list2 的值：
         list1 的 next 指向 mergeTwoLists(list1 的 next, list2)
         返回 list1
     否则：
         list2 的 next 指向 mergeTwoLists(list1, list2 的 next)
         返回 list2
     ```

4. **复杂度：**
   - 时间复杂度：$O(n + m)$，其中 $n$ 和 $m$ 分别是两个链表的长度，因为每个节点都被访问一次。
   - 空间复杂度：$O(1)$，对于迭代法，因为只使用了常数额外空间。
   - 空间复杂度（递归法）：$O(n + m)$，由于递归调用栈的深度。