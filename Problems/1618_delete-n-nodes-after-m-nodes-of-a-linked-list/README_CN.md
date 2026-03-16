# 1618. 删除链表 M 个节点之后的 N 个节点

**难度**: Easy | **标签**: `Linked List`

## 题目描述

<p>给定一个链表的 <code>head</code> 和两个整数 <code>m</code> 和 <code>n</code>。</p>

<p>遍历链表并以以下方式删除一些节点：</p>

<ul>
	<li>从头节点开始作为当前节点。</li>
	<li>保留从当前节点开始的前 <code>m</code> 个节点。</li>
	<li>删除接下来的 <code>n</code> 个节点。</li>
	<li>重复步骤 2 和 3，直到到达链表的末尾。</li>
</ul>

<p>返回 <em>删除提到的节点后修改过的链表的头节点</em>。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/06/06/sample_1_1848.png" style="width: 600px; height: 95px;" />
<pre>
<strong>输入:</strong> head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3
<strong>输出:</strong> [1,2,6,7,11,12]
<strong>解释:</strong> 从链表的头节点开始保留前 (m = 2) 个节点 (1 -&gt;2) 显示为黑色节点。
删除接下来的 (n = 3) 个节点 (3 -&gt; 4 -&gt; 5) 显示为红色节点。
继续相同的过程，直到到达链表的尾部。
返回删除节点后的链表头节点。
</pre>

<p><strong class="example">示例 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/06/06/sample_2_1848.png" style="width: 600px; height: 123px;" />
<pre>
<strong>输入:</strong> head = [1,2,3,4,5,6,7,8,9,10,11], m = 1, n = 3
<strong>输出:</strong> [1,5,9]
<strong>解释:</strong> 返回删除节点后的链表头节点。
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li>链表中的节点数在 <code>[1, 10<sup>4</sup>]</code> 范围内。</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= m, n &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>后续问题:</strong> 你能通过原地修改链表来解决这个问题吗？</p>

---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过迭代遍历链表，保留 M 个节点后跳过 N 个节点，调整链表指针以删除不需要的节点。

2. 综合思路：
   - 迭代法：通过两个指针 `slow` 和 `fast`，`slow` 用于遍历并保留 M 个节点，`fast` 用于跳过 N 个节点，然后调整 `slow` 的 `next` 指针以删除节点。
   - 递归法：可以通过递归的方式实现相同的逻辑，递归地处理链表的每一段，保留 M 个节点后跳过 N 个节点。

3. 全量伪代码：
   - 迭代法：
     ```
     初始化虚拟节点 dummy，指向链表头部
     初始化当前节点 curr 指向 dummy
     当 curr 不为空时，重复以下步骤：
         初始化 slow 指向 curr
         遍历 M 个节点：
             如果 slow 为空，跳出循环
             slow 移动到下一个节点
         如果 slow 为空，跳出循环
         初始化 fast 指向 slow 的下一个节点
         遍历 N 个节点：
             如果 fast 为空，跳出循环
             fast 移动到下一个节点
         将 slow 的 next 指针指向 fast
         更新 curr 为 slow
     返回链表头部
     ```
   - 递归法（伪代码示例）：
     ```
     定义递归函数 deleteNodesRecursively(head, m, n)
         如果 head 为空，返回 head
         初始化 curr 指向 head
         遍历 M 个节点：
             如果 curr 为空，返回 head
             curr 移动到下一个节点
         初始化 temp 指向 curr 的下一个节点
         遍历 N 个节点：
             如果 temp 为空，跳出循环
             temp 移动到下一个节点
         将 curr 的 next 指针指向 deleteNodesRecursively(temp, m, n)
         返回 head
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是链表的节点数，因为每个节点最多被访问一次。
   - 空间复杂度：$O(1)$，因为使用了常数级别的额外空间。对于递归实现，空间复杂度为 $O(n)$，因为递归调用栈的深度与链表长度成正比。