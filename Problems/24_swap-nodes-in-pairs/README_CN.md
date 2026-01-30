# 24. 两两交换链表中的节点

**难度**: Medium | **标签**: `Linked List` `Recursion`

## 题目描述

<p>给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg" style="width: 422px; height: 222px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,4]
<strong>输出：</strong>[2,1,4,3]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>head = []
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>head = [1]
<strong>输出：</strong>[1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中节点的数目在范围 <code>[0, 100]</code> 内</li>
	<li><code>0 &lt;= Node.val &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过迭代或递归的方式，成对地交换链表中的节点。

2. 综合思路：
   - 迭代法：使用一个虚拟头节点和三个指针（prev, first, second）来遍历链表，逐对交换节点。
   - 递归法：递归地交换每一对节点，直到链表末尾。

3. 全量伪代码：
   - 迭代法：
     ```
     如果链表为空或只有一个节点，则返回头节点
     创建一个虚拟头节点 dummy，指向链表头
     初始化三个指针 prev 指向 dummy，first 指向头节点，second 指向头节点的下一个节点
     当 second 不为空时，重复以下步骤：
         保存 second 的下一个节点为 nxt
         将 second 的 next 指向 first
         将 first 的 next 指向 nxt
         将 prev 的 next 指向 second
         更新 prev 为 first
         更新 first 为 nxt
         如果 first 不为空，则更新 second 为 first 的下一个节点
     返回 dummy 的 next
     ```

   - 递归法（未在给定代码中出现，但为常见解法）：
     ```
     如果链表为空或只有一个节点，则返回头节点
     设定 first 为头节点，second 为头节点的下一个节点
     递归调用 swapPairs 处理 second 的下一个节点，并将结果赋给 first 的 next
     将 second 的 next 指向 first
     返回 second
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是链表的节点数，因为每个节点被访问一次。
   - 空间复杂度：迭代法为 $O(1)$，递归法为 $O(n)$（递归栈的空间）。