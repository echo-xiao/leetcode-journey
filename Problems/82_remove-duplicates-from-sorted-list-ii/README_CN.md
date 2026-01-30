# 82. 删除排序链表中的重复元素 II

**难度**: Medium | **标签**: `Linked List` `Two Pointers`

## 题目描述

<p>给定一个已排序的链表的头&nbsp;<code>head</code> ，&nbsp;<em>删除原始链表中所有重复数字的节点，只留下不同的数字</em>&nbsp;。返回 <em>已排序的链表</em>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg" style="height: 142px; width: 500px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,3,4,4,5]
<strong>输出：</strong>[1,2,5]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg" style="height: 164px; width: 400px;" />
<pre>
<strong>输入：</strong>head = [1,1,1,2,3]
<strong>输出：</strong>[2,3]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中节点数目在范围 <code>[0, 300]</code> 内</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li>题目数据保证链表已经按升序 <strong>排列</strong></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过使用一个虚拟头节点和双指针遍历链表，跳过所有重复元素以删除排序链表中的重复元素。

2. **综合思路：**
   - **迭代法：** 使用一个虚拟头节点（dummy）和两个指针（prev 和 curr）来遍历链表。curr 指针用于检测重复元素，prev 指针用于连接不重复的元素。通过比较 curr 和 curr.next 的值来判断是否存在重复，并在发现重复时跳过这些节点。
   - **递归法：** 虽然在提供的代码中没有递归实现，但递归方法可以通过递归地处理链表的剩余部分来实现相同的逻辑：如果当前节点与下一个节点值相同，跳过所有相同值的节点，然后递归处理后续节点。

3. **全量伪代码：**

   - **迭代法伪代码：**
     ```
     初始化虚拟头节点 dummy，指向 head
     初始化 prev 指针指向 dummy
     初始化 curr 指针指向 head

     当 curr 和 curr.next 都不为空时，重复以下步骤：
         如果 curr.val 等于 curr.next.val：
             当 curr.next 不为空且 curr.val 等于 curr.next.val 时：
                 将 curr 移动到 curr.next
             将 prev.next 指向 curr.next 以跳过重复元素
             将 curr 移动到 curr.next
         否则：
             将 prev 移动到 prev.next
             将 curr 移动到 curr.next

     返回 dummy.next
     ```

   - **递归法伪代码（假设）：**
     ```
     定义递归函数 deleteDuplicates(head):
         如果 head 为空或 head.next 为空，返回 head
         如果 head.val 等于 head.next.val：
             跳过所有与 head.val 相同的节点
             递归调用 deleteDuplicates 处理剩余链表
         否则：
             head.next = 递归调用 deleteDuplicates 处理 head.next
         返回 head
     ```

4. **复杂度：**
   - 时间复杂度：$O(n)$，因为每个节点最多被访问两次。
   - 空间复杂度：$O(1)$，因为只使用了常数级别的额外空间（不考虑递归栈空间）。