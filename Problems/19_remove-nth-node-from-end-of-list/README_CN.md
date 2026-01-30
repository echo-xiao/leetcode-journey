# 19. 删除链表的倒数第 N 个结点

**难度**: Medium | **标签**: `Linked List` `Two Pointers`

## 题目描述

<p>给你一个链表，删除链表的倒数第&nbsp;<code>n</code><em>&nbsp;</em>个结点，并且返回链表的头结点。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,4,5], n = 2
<strong>输出：</strong>[1,2,3,5]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>head = [1], n = 1
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>head = [1,2], n = 1
<strong>输出：</strong>[1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中结点的数目为 <code>sz</code></li>
	<li><code>1 &lt;= sz &lt;= 30</code></li>
	<li><code>0 &lt;= Node.val &lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= sz</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你能尝试使用一趟扫描实现吗？</p>


---
## 解题思路与复盘

1. **一句话直击本质：** 使用双指针技巧，先让一个指针领先 n 步，然后两个指针同步移动，直到领先的指针到达链表末尾，从而定位并删除倒数第 n 个节点。

2. **简洁的中文实现思路描述：** 
   - 创建一个哑节点（dummy node）并将其指向链表头部，以便处理边界情况。
   - 初始化两个指针（slow 和 fast），都指向哑节点。
   - 先让 fast 指针移动 n 步，这样 fast 和 slow 之间的距离就是 n。
   - 然后同时移动 slow 和 fast，直到 fast 到达链表末尾。
   - 此时，slow 的下一个节点就是需要删除的节点，调整 slow 的 next 指针跳过该节点。
   - 返回哑节点的 next 作为新的链表头。

3. **总结AC版本所有的通用解决方式/逻辑的中文伪代码：**

```plaintext
创建哑节点 dummy 并指向链表头
初始化 slow 和 fast 指针指向 dummy
让 fast 指针先移动 n 步
同时移动 slow 和 fast，直到 fast 到达链表末尾
此时 slow 的下一个节点就是要删除的节点
调整 slow 的 next 指针跳过该节点
返回 dummy 的 next 作为新的链表头
```

4. **时间复杂度和空间复杂度：**

- 时间复杂度：$O(L)$，其中 $L$ 是链表的长度，因为我们最多遍历链表两次。
- 空间复杂度：$O(1)$，因为我们只使用了常数个额外指针。