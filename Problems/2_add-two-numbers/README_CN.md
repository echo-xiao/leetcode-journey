# 2. 两数相加

**难度**: Medium | **标签**: `Linked List` `Math` `Recursion`

## 题目描述

<p>给你两个&nbsp;<strong>非空</strong> 的链表，表示两个非负的整数。它们每位数字都是按照&nbsp;<strong>逆序</strong>&nbsp;的方式存储的，并且每个节点只能存储&nbsp;<strong>一位</strong>&nbsp;数字。</p>

<p>请你将两个数相加，并以相同形式返回一个表示和的链表。</p>

<p>你可以假设除了数字 0 之外，这两个数都不会以 0&nbsp;开头。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/01/02/addtwonumber1.jpg" style="width: 483px; height: 342px;" />
<pre>
<strong>输入：</strong>l1 = [2,4,3], l2 = [5,6,4]
<strong>输出：</strong>[7,0,8]
<strong>解释：</strong>342 + 465 = 807.
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>l1 = [0], l2 = [0]
<strong>输出：</strong>[0]
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>输出：</strong>[8,9,9,9,0,0,0,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>每个链表中的节点数在范围 <code>[1, 100]</code> 内</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
	<li>题目数据保证列表表示的数字不含前导零</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质**：通过逐位相加两个链表的节点值，并处理进位，构建一个新的链表表示两个数的和。

2. **中文实现思路描述**：
   - 初始化一个哑节点 `dummy` 和一个指针 `curr` 指向它，同时初始化进位 `carry` 为0。
   - 遍历两个链表 `l1` 和 `l2`，直到它们都为空且没有进位。
   - 在每次迭代中，获取当前节点的值（若节点为空则为0），计算当前位的总和 `ttl`，并更新进位 `carry`。
   - 创建一个新节点保存当前位的结果，并将其连接到结果链表中。
   - 移动指针到下一个节点。
   - 返回哑节点的下一个节点作为结果链表的头。

3. **通用解决方式/逻辑的中文伪代码**：
   ```plaintext
   初始化哑节点 dummy 和指针 curr 指向 dummy
   初始化进位 carry 为 0

   当 l1 不为空 或 l2 不为空 或 carry 不为 0 时：
       如果 l1 不为空，则 v1 = l1 的值，否则 v1 = 0
       如果 l2 不为空，则 v2 = l2 的值，否则 v2 = 0

       计算总和 ttl = v1 + v2 + carry
       更新进位 carry = ttl // 10
       计算当前位的值 val = ttl % 10

       创建新节点保存 val，并连接到 curr 的下一个节点
       移动 curr 到下一个节点

       如果 l1 不为空，则移动 l1 到下一个节点
       如果 l2 不为空，则移动 l2 到下一个节点

   返回 dummy 的下一个节点
   ```

4. **时间复杂度和空间复杂度**：
   - 时间复杂度：$O(\max(m, n))$，其中 $m$ 和 $n$ 分别是链表 `l1` 和 `l2` 的长度，因为我们需要遍历两个链表的每个节点。
   - 空间复杂度：$O(\max(m, n))$，因为结果链表的长度最多为较长的输入链表长度加1（如果有进位）。