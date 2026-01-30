# 203. 移除链表元素

**难度**: Easy | **标签**: `Linked List` `Recursion`

## 题目描述

给你一个链表的头节点 <code>head</code> 和一个整数 <code>val</code> ，请你删除链表中所有满足 <code>Node.val == val</code> 的节点，并返回 <strong>新的头节点</strong> 。
<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg" style="width: 500px; height: 142px;" />
<pre>
<strong>输入：</strong>head = [1,2,6,3,4,5,6], val = 6
<strong>输出：</strong>[1,2,3,4,5]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>head = [], val = 1
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>head = [7,7,7,7], val = 7
<strong>输出：</strong>[]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>列表中的节点数目在范围 <code>[0, 10<sup>4</sup>]</code> 内</li>
	<li><code>1 <= Node.val <= 50</code></li>
	<li><code>0 <= val <= 50</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：
   - 使用一个哑节点（dummy node）来简化链表头节点的删除操作，并通过遍历链表删除所有匹配值的节点。

2. 综合思路：
   - 迭代法：所有版本均采用迭代法，通过一个哑节点来处理链表头节点的特殊情况，遍历链表并删除值等于给定值的节点。
   - 递归法：虽然在提供的代码集中没有递归版本，但递归法也是一种常见解法，通过递归遍历链表并在回溯时删除匹配的节点。

3. 全量伪代码：
   - 迭代法：
     ```
     定义一个哑节点 dummy，其 next 指向链表头 head
     初始化 curr 指针指向 dummy
     当 curr 的下一个节点不为空时，重复以下操作：
         如果 curr 的下一个节点的值等于目标值 val：
             将 curr 的 next 指针指向 curr 的下一个节点的下一个节点（跳过当前节点）
         否则：
             将 curr 指针移动到下一个节点
     返回 dummy 的下一个节点
     ```
   - 递归法（未在代码集中出现，但作为补充）：
     ```
     如果 head 为空，返回 None
     递归调用 removeElements 处理 head 的下一个节点
     如果 head 的值等于目标值 val：
         返回 head 的下一个节点（跳过当前节点）
     否则：
         将 head 的 next 指针指向递归调用的结果
         返回 head
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是链表的节点数，因为每个节点最多被访问一次。
   - 空间复杂度：$O(1)$，因为使用了常数个额外的指针。
   - 递归法的空间复杂度为 $O(n)$，因为递归调用会使用栈空间。