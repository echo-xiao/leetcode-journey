# 206. 反转链表

**难度**: Easy | **标签**: `Linked List` `Recursion`

## 题目描述

给你单链表的头节点 <code>head</code> ，请你反转链表，并返回反转后的链表。
<div class="original__bRMd">
<div>
<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,4,5]
<strong>输出：</strong>[5,4,3,2,1]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg" style="width: 182px; height: 222px;" />
<pre>
<strong>输入：</strong>head = [1,2]
<strong>输出：</strong>[2,1]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>head = []
<strong>输出：</strong>[]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中节点的数目范围是 <code>[0, 5000]</code></li>
	<li><code>-5000 <= Node.val <= 5000</code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong>链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？</p>
</div>
</div>


---
## 解题思路与复盘

### 一句话直击本质
通过逐步反转链表节点的指针方向，实现链表的逆序。

### 综合思路
1. **迭代法**：通过遍历链表，逐个反转节点的指针方向，直到遍历完整个链表。
2. **递归法**：通过递归调用，将链表分解为子问题，逐层反转指针方向，最终实现链表逆序。

### 全量伪代码

#### 迭代法
```plaintext
函数 reverseList(链表头节点 head):
    如果 head 是空:
        返回 head

    初始化 left 为 None
    初始化 right 为 head

    当 right 的下一个节点不为空时:
        保存 right 的下一个节点为 helper
        将 right 的下一个节点指向 left
        将 left 更新为 right
        将 right 更新为 helper

    将 head 更新为 right
    将 head 的下一个节点指向 left
    返回 head
```

#### 递归法
```plaintext
函数 reverseList(链表头节点 head):
    如果 head 是空或 head 的下一个节点是空:
        返回 head

    递归调用 reverseList(head 的下一个节点) 并保存为 newHead
    将 head 的下一个节点的下一个指针指向 head
    将 head 的下一个节点指向空
    返回 newHead
```

### 复杂度
- **时间复杂度**: $O(n)$，其中 $n$ 是链表的节点数量，因为每个节点都被访问一次。
- **空间复杂度**: 
  - 迭代法：$O(1)$，因为只使用了常数级别的额外空间。
  - 递归法：$O(n)$，因为递归调用栈的深度为 $n$。