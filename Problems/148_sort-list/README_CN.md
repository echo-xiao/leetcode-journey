# 148. 排序链表

**难度**: Medium | **标签**: `Linked List` `Two Pointers` `Divide and Conquer` `Sorting` `Merge Sort`

## 题目描述

<p>给你链表的头结点&nbsp;<code>head</code>&nbsp;，请将其按 <strong>升序</strong> 排列并返回 <strong>排序后的链表</strong> 。</p>

<ul>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg" style="width: 450px;" />
<pre>
<b>输入：</b>head = [4,2,1,3]
<b>输出：</b>[1,2,3,4]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg" style="width: 550px;" />
<pre>
<b>输入：</b>head = [-1,5,3,4,0]
<b>输出：</b>[-1,0,3,4,5]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>head = []
<b>输出：</b>[]
</pre>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li>链表中节点的数目在范围&nbsp;<code>[0, 5 * 10<sup>4</sup>]</code>&nbsp;内</li>
	<li><code>-10<sup>5</sup>&nbsp;&lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><b>进阶：</b>你可以在&nbsp;<code>O(n&nbsp;log&nbsp;n)</code> 时间复杂度和常数级空间复杂度下，对链表进行排序吗？</p>


---
## 解题思路与复盘

1. 一句话直击本质：该算法使用归并排序的思想，通过递归地将链表分成两半，分别排序后再合并，以实现链表的排序。

2. 综合思路：
   - 递归归并排序：通过快慢指针找到链表的中点，将链表分成两半，递归地对每一半进行排序，然后合并两个已排序的子链表。
   - 迭代归并排序：虽然未在提供的代码中出现，但另一种常见的方法是使用迭代的方式进行归并排序，通过逐步合并小的已排序链表段来实现。

3. 全量伪代码：
   - 递归归并排序：
     ```
     定义函数 sortList(head):
         如果 head 是空或 head 只有一个节点:
             返回 head
         
         使用快慢指针找到链表的中点
         将链表分成两半
         递归地对左半部分排序
         递归地对右半部分排序
         合并两个已排序的子链表
         返回合并后的链表

     定义函数 mergeTwoSortedList(left, right):
         创建一个虚拟头节点 dummy
         初始化 curr 指向 dummy
         
         当 left 和 right 都不为空时:
             如果 left 的值小于 right 的值:
                 将 curr 的 next 指向 left
                 移动 left 到下一个节点
             否则:
                 将 curr 的 next 指向 right
                 移动 right 到下一个节点
             移动 curr 到下一个节点
         
         如果 left 不为空:
             将 curr 的 next 指向 left
         如果 right 不为空:
             将 curr 的 next 指向 right
         
         返回 dummy 的 next
     ```

4. 复杂度：
   - 时间复杂度：$O(n \log n)$，因为每次将链表分成两半需要 $O(\log n)$ 次递归调用，每次合并操作需要 $O(n)$。
   - 空间复杂度：$O(\log n)$，由于递归调用栈的深度为 $O(\log n)$。