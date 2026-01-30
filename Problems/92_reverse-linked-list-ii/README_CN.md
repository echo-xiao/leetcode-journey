# 92. 反转链表 II

**难度**: Medium | **标签**: `Linked List`

## 题目描述

给你单链表的头指针 <code>head</code> 和两个整数 <code>left</code> 和 <code>right</code> ，其中 <code>left <= right</code> 。请你反转从位置 <code>left</code> 到位置 <code>right</code> 的链表节点，返回 <strong>反转后的链表</strong> 。
<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,4,5], left = 2, right = 4
<strong>输出：</strong>[1,4,3,2,5]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>head = [5], left = 1, right = 1
<strong>输出：</strong>[5]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中节点数目为 <code>n</code></li>
	<li><code>1 <= n <= 500</code></li>
	<li><code>-500 <= Node.val <= 500</code></li>
	<li><code>1 <= left <= right <= n</code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong> 你可以使用一趟扫描完成反转吗？</p>


---
## 解题思路与复盘

1. **一句话直击本质**：通过调整链表节点的指针，局部反转链表的指定区间。

2. **综合思路**：
   - **迭代法**：通过遍历链表找到反转区间的起始节点，然后逐步调整节点指针以反转该区间。
   - **分段法**：将链表分为三个部分：左段、反转段、右段，反转中间段后再拼接回去。

3. **全量伪代码**：

   - **迭代法**：
     ```
     初始化虚拟头节点 dummy 指向 head
     初始化 prev 指向 dummy
     遍历链表直到 prev 到达 left 之前的节点
     初始化 curr 指向 prev 的下一个节点
     对于从 left 到 right 的每个节点：
         保存 curr 的下一个节点为 nxt
         将 curr 的 next 指向 nxt 的下一个节点
         将 nxt 的 next 指向 prev 的下一个节点
         将 prev 的 next 指向 nxt
     返回 dummy 的下一个节点
     ```

   - **分段法**：
     ```
     初始化三个虚拟头节点 leftDummy, middleDummy, rightDummy
     初始化三个尾指针 leftTail, middleTail, rightTail 分别指向这三个虚拟头节点
     初始化计数器 cnt 为 1
     初始化 curr 指向 head
     遍历链表：
         保存 curr 的下一个节点为 tmp
         将 curr 的 next 置为 None
         如果 cnt 小于 left，将 curr 添加到 leftTail 后面
         如果 cnt 在 left 和 right 之间，将 curr 添加到 middleTail 后面
         如果 cnt 大于 right，将 curr 添加到 rightTail 后面
         更新 cnt 和 curr
     反转 middleDummy 的下一个节点
     将 leftTail 的 next 指向反转后的中间段头节点
     如果 middleDummy 的下一个节点不为空，将 middleDummy 的下一个节点的 next 指向 rightDummy 的下一个节点
     否则，将 leftTail 的 next 指向 rightDummy 的下一个节点
     返回 leftDummy 的下一个节点
     ```

4. **复杂度**：
   - 时间复杂度：$O(n)$，其中 $n$ 是链表的长度，因为我们需要遍历链表一次。
   - 空间复杂度：$O(1)$，因为我们只使用了常数个额外指针。