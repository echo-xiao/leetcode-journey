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

1. **一句话直击本质：** 通过迭代的方式，逐对交换链表中的节点，并使用虚拟头节点来简化边界条件处理。

2. **简洁的中文实现思路描述：**
   - 如果链表为空或只有一个节点，直接返回头节点。
   - 创建一个虚拟头节点 `dummy`，其 `next` 指向链表的头节点，以便于处理头节点的交换。
   - 使用三个指针 `prev`、`first` 和 `second`，分别指向前一个节点、当前要交换的第一个节点和第二个节点。
   - 迭代链表，交换 `first` 和 `second`，并调整指针以准备下一次交换。
   - 返回 `dummy.next` 作为新的头节点。

3. **总结AC版本所有的通用解决方式/逻辑的中文伪代码：**

```plaintext
函数 swapPairs(head):
    如果 head 为空 或 head.next 为空:
        返回 head

    创建虚拟节点 dummy，dummy.next 指向 head
    初始化 prev 为 dummy
    初始化 first 为 head
    初始化 second 为 head.next

    当 second 不为空时:
        保存 second.next 为 nxt
        将 second.next 指向 first
        将 first.next 指向 nxt
        将 prev.next 指向 second

        更新 prev 为 first
        更新 first 为 nxt
        如果 first 不为空:
            更新 second 为 first.next
        否则:
            second 设为 None

    返回 dummy.next
```

4. **时间复杂度和空间复杂度：**

   - 时间复杂度：$O(n)$，其中 $n$ 是链表的节点数，因为每个节点在迭代中被访问一次。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外指针。