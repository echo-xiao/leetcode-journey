# 86. 分隔链表

**难度**: Medium | **标签**: `Linked List` `Two Pointers`

## 题目描述

<p>给你一个链表的头节点 <code>head</code> 和一个特定值<em> </em><code>x</code> ，请你对链表进行分隔，使得所有 <strong>小于</strong> <code>x</code> 的节点都出现在 <strong>大于或等于</strong> <code>x</code> 的节点之前。</p>

<p>你应当 <strong>保留</strong> 两个分区中每个节点的初始相对位置。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/partition.jpg" style="width: 662px; height: 222px;" />
<pre>
<strong>输入：</strong>head = [1,4,3,2,5,2], x = 3
<strong>输出</strong>：[1,2,2,4,3,5]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>head = [2,1], x = 2
<strong>输出</strong>：[1,2]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中节点的数目在范围 <code>[0, 200]</code> 内</li>
	<li><code>-100 <= Node.val <= 100</code></li>
	<li><code>-200 <= x <= 200</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用两个虚拟头节点分别构建小于和大于等于给定值的链表，然后将它们连接起来。

2. 综合思路：在所有给定的版本中，采用了相同的迭代方法。通过遍历原始链表，将节点按值分配到两个新的链表中，最后将这两个链表连接起来。没有使用递归或其他数据结构的变体。

3. 全量伪代码：
   ```
   定义两个虚拟头节点 lessDummy 和 greaterDummy
   初始化两个指针 less 和 greater 指向这两个虚拟头节点
   初始化指针 curr 指向链表头部 head

   当 curr 不为空时，重复以下步骤：
       获取当前节点的值 num
       创建一个新节点 node，值为 num
       如果 num 小于给定值 x：
           将 less 的 next 指向 node
           将 less 移动到下一个节点
       否则：
           将 greater 的 next 指向 node
           将 greater 移动到下一个节点
       将 curr 移动到下一个节点

   将 less 的 next 指向 greaterDummy 的 next
   返回 lessDummy 的 next
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是链表中的节点数，因为每个节点只被访问一次。
   - 空间复杂度：$O(1)$，除了用于存储结果链表的节点外，没有使用额外的空间。