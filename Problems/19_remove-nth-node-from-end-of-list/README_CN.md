# 19. 删除链表的倒数第 N 个结点

**难度**: Medium | **标签**: `Linked List` `Two Pointers`

**归类**: 1. 滑动窗口与双指针 > Linked List

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

1. 一句话直击本质：使用双指针法，先让一个指针先行 n 步，然后两个指针同步前进，直到先行指针到达链表末尾，后行指针即指向待删除节点的前一个节点。

2. 综合思路：
   - 双指针法（迭代）：通过设置两个指针，一个指针先行 n 步，然后两个指针同步前进，直到先行指针到达链表末尾，后行指针即指向待删除节点的前一个节点。
   - 递归法：通过递归遍历链表，记录节点的倒数位置，当到达倒数第 n 个节点时，进行删除操作。（此方法未在提供的代码集中出现，但也是常见解法）

3. 全量伪代码：
   - 双指针法：
     ```
     初始化一个虚拟节点 dummy，指向链表头节点
     初始化两个指针 slow 和 fast，均指向 dummy
     让 fast 指针先移动 n 步
     当 fast 的下一个节点不为空时，slow 和 fast 同时向前移动一步
     slow 的下一个节点即为待删除节点，将 slow 的下一个节点指向其下下个节点
     返回 dummy 的下一个节点作为新的链表头
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是链表的长度，因为需要遍历链表一次。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外指针。