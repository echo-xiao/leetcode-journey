# 445. 两数相加 II

**难度**: Medium | **标签**: `Linked List` `Math` `Stack`

## 题目描述

<p>给你两个 <strong>非空 </strong>链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。</p>

<p>你可以假设除了数字 0 之外，这两个数字都不会以零开头。</p>

<p>&nbsp;</p>

<p><strong>示例1：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1626420025-fZfzMX-image.png" style="width: 302px; " /></p>

<pre>
<strong>输入：</strong>l1 = [7,2,4,3], l2 = [5,6,4]
<strong>输出：</strong>[7,8,0,7]
</pre>

<p><strong>示例2：</strong></p>

<pre>
<strong>输入：</strong>l1 = [2,4,3], l2 = [5,6,4]
<strong>输出：</strong>[8,0,7]
</pre>

<p><strong>示例3：</strong></p>

<pre>
<strong>输入：</strong>l1 = [0], l2 = [0]
<strong>输出：</strong>[0]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表的长度范围为<code> [1, 100]</code></li>
	<li><code>0 &lt;= node.val &lt;= 9</code></li>
	<li>输入数据保证链表代表的数字无前导 0</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>如果输入链表不能翻转该如何解决？</p>


---
## 解题思路与复盘

### 一句话直击本质
通过反转链表，将问题转化为从最低位到最高位逐位相加，并处理进位。

### 综合思路
1. **反转链表法**：首先反转两个输入链表，然后从最低位开始逐位相加，处理进位，最后将结果链表再反转得到最终结果。
   - **步骤**：
     - 反转输入链表 `l1` 和 `l2`。
     - 初始化一个哑节点 `dummy` 和进位 `carry`。
     - 遍历反转后的链表，逐位相加，处理进位。
     - 将结果链表再反转，返回结果。
   
2. **栈法**（未在给定代码中出现，但常见于此类问题）：利用栈的后进先出特性，先将链表节点值压入栈中，再逐位弹出相加，处理进位。

### 全量伪代码
```plaintext
函数 addTwoNumbers(l1, l2):
    curr1 = 反转链表(l1)
    curr2 = 反转链表(l2)
    初始化 dummy 节点为 ListNode(0)
    初始化 carry 为 0

    当 curr1 不为空 或 curr2 不为空 或 carry 不为 0 时:
        如果 curr1 为空, v1 = 0, 否则 v1 = curr1.val
        如果 curr2 为空, v2 = 0, 否则 v2 = curr2.val

        ttl = v1 + v2 + carry
        carry = ttl // 10
        val = ttl % 10

        创建新节点 curr = ListNode(val)
        将 curr 插入到 dummy 之后

        如果 curr1 不为空, curr1 = curr1.next
        如果 curr2 不为空, curr2 = curr2.next

    返回 dummy.next

函数 反转链表(head):
    初始化 prev 为 None
    初始化 curr 为 head

    当 curr 不为空 时:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    返回 prev
```

### 复杂度
- **时间复杂度**：$O(n + m)$，其中 $n$ 和 $m$ 分别是链表 `l1` 和 `l2` 的长度，因为需要遍历两次链表（反转和相加）。
- **空间复杂度**：$O(1)$，除了用于存储结果链表的空间外，使用了常数级别的额外空间。