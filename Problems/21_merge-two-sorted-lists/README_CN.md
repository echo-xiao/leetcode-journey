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

1. **一句话直击本质**：通过逐步比较两个链表的节点值，将较小的节点依次连接到新的链表中，直至合并完成。

2. **简洁的中文实现思路描述**：
   - 创建一个哑节点作为新链表的起始节点，并使用一个指针 `curr` 来跟踪新链表的末尾。
   - 遍历两个输入链表，比较当前节点的值，将较小的节点连接到新链表中，并移动相应链表的指针。
   - 当其中一个链表遍历完后，将另一个链表剩余的部分直接连接到新链表的末尾。
   - 返回哑节点的下一个节点作为合并后的链表头。

3. **通用解决方式/逻辑的中文伪代码**：
   ```
   初始化哑节点 dummy 和当前指针 curr 指向哑节点
   当 list1 和 list2 都不为空时：
       如果 list1 的值小于 list2 的值：
           将 curr 的下一个节点指向 list1
           移动 list1 到下一个节点
       否则：
           将 curr 的下一个节点指向 list2
           移动 list2 到下一个节点
       移动 curr 到下一个节点
   如果 list1 不为空：
       将 curr 的下一个节点指向 list1
   否则如果 list2 不为空：
       将 curr 的下一个节点指向 list2
   返回 dummy 的下一个节点
   ```

4. **时间复杂度和空间复杂度**：
   - 时间复杂度：$O(n + m)$，其中 $n$ 和 $m$ 分别是两个链表的长度，因为每个节点最多被访问一次。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外指针。