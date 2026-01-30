# 61. 旋转链表

**难度**: Medium | **标签**: `Linked List` `Two Pointers`

## 题目描述

<p>给你一个链表的头节点 <code>head</code> ，旋转链表，将链表每个节点向右移动&nbsp;<code>k</code><em>&nbsp;</em>个位置。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg" style="width: 450px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,4,5], k = 2
<strong>输出：</strong>[4,5,1,2,3]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg" style="width: 305px; height: 350px;" />
<pre>
<strong>输入：</strong>head = [0,1,2], k = 4
<strong>输出：</strong>[2,0,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中节点的数目在范围 <code>[0, 500]</code> 内</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li><code>0 &lt;= k &lt;= 2 * 10<sup>9</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：将链表首尾相连形成环，然后根据旋转步数计算新的断开点以形成新的链表头。

2. 综合思路：
   - **迭代法**：通过遍历链表计算长度，将链表首尾相连形成环，然后根据旋转步数计算新的断开点，最后断开环形成新的链表。

3. 全量伪代码：
   ```plaintext
   定义函数 rotateRight(head, k):
       如果链表为空或只有一个节点:
           返回 head

       初始化 curr 为 head
       初始化 cnt 为 1

       # 计算链表长度并将链表首尾相连
       当 curr.next 不为空:
           cnt 增加 1
           curr 移动到下一个节点
       将 curr.next 指向 head 形成环

       计算旋转步数 r 为 k 对 cnt 取模
       初始化 prev 为一个新的节点，其 next 指向 head
       计算新的断开点 l 为 cnt 减去 r

       # 移动到新的断开点
       当 l 大于 0:
           prev 移动到下一个节点
           head 移动到下一个节点
           l 减少 1

       将 prev.next 设为 None 断开环

       返回新的 head
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是链表的长度，因为需要遍历链表两次（一次计算长度，一次找到新的断开点）。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外空间。