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

1. 一句话直击本质：通过迭代遍历链表，逐对交换相邻节点，并使用一个虚拟头节点来简化边界条件处理。

2. 综合思路：
   - 迭代法：使用一个虚拟头节点来简化链表的操作，逐对交换相邻节点，通过调整指针来实现节点的交换。
   - 递归法（未在提供的代码中出现，但常见于此类问题）：递归地交换每对节点，处理完当前一对后，将递归结果连接到当前交换后的节点上。

3. 全量伪代码：
   - 迭代法：
     ```
     如果链表为空或只有一个节点，返回头节点
     创建一个虚拟头节点，指向头节点
     初始化三个指针：prev指向虚拟头节点，first指向头节点，second指向头节点的下一个节点
     当second不为空时，重复以下步骤：
         保存second的下一个节点为nxt
         将second的next指向first
         将first的next指向nxt
         将prev的next指向second
         将prev更新为first
         将first更新为nxt
         如果first不为空，将second更新为first的下一个节点，否则将second置为None
     返回虚拟头节点的next
     ```
   - 递归法（伪代码，未在提供的代码中出现）：
     ```
     如果链表为空或只有一个节点，返回头节点
     保存head的下一个节点为second
     递归调用swapPairs处理second的下一个节点，并将结果赋给head的next
     将second的next指向head
     返回second
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是链表的节点数，因为每个节点访问一次。
   - 空间复杂度：$O(1)$，因为使用了常数个额外指针。
   - 递归法的空间复杂度为 $O(n)$，因为递归调用栈的深度为链表的长度。