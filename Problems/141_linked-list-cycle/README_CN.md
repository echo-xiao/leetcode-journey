# 141. 环形链表

**难度**: Easy | **标签**: `Hash Table` `Linked List` `Two Pointers`

## 题目描述

<p>给你一个链表的头节点 <code>head</code> ，判断链表中是否有环。</p>

<p>如果链表中有某个节点，可以通过连续跟踪 <code>next</code> 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 <code>pos</code> 来表示链表尾连接到链表中的位置（索引从 0 开始）。<strong>注意：<code>pos</code> 不作为参数进行传递&nbsp;</strong>。仅仅是为了标识链表的实际情况。</p>

<p><em>如果链表中存在环</em>&nbsp;，则返回 <code>true</code> 。 否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png" /></p>

<pre>
<strong>输入：</strong>head = [3,2,0,-4], pos = 1
<strong>输出：</strong>true
<strong>解释：</strong>链表中有一个环，其尾部连接到第二个节点。
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png" /></p>

<pre>
<strong>输入：</strong>head = [1,2], pos = 0
<strong>输出：</strong>true
<strong>解释：</strong>链表中有一个环，其尾部连接到第一个节点。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png" /></p>

<pre>
<strong>输入：</strong>head = [1], pos = -1
<strong>输出：</strong>false
<strong>解释：</strong>链表中没有环。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中节点的数目范围是 <code>[0, 10<sup>4</sup>]</code></li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li><code>pos</code> 为 <code>-1</code> 或者链表中的一个 <strong>有效索引</strong> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你能用 <code>O(1)</code>（即，常量）内存解决此问题吗？</p>


---
## 解题思路与复盘

1. 一句话直击本质：
   - 使用快慢指针遍历链表，若存在环则快慢指针必定相遇。

2. 综合思路：
   - 快慢指针法：使用两个指针（快指针和慢指针）同时遍历链表，快指针每次移动两步，慢指针每次移动一步。如果链表中存在环，快指针和慢指针最终会在环内相遇。
   - 哈希表法（未在提供的代码中出现，但常见于此类问题）：遍历链表的同时将每个节点存入哈希表，如果遇到已经存在于哈希表中的节点，则说明存在环。

3. 全量伪代码：
   - 快慢指针法：
     ```
     定义两个指针 slow 和 fast，初始都指向链表头部
     当 fast 和 fast.next 都不为空时，执行以下循环：
         将 slow 移动到下一个节点
         将 fast 移动到下两个节点
         如果 slow 和 fast 相遇，返回 True
     循环结束后，返回 False
     ```
   - 哈希表法（未在提供的代码中出现，但常见于此类问题）：
     ```
     初始化一个空的哈希表
     定义一个指针 current 指向链表头部
     当 current 不为空时，执行以下循环：
         如果 current 在哈希表中，返回 True
         将 current 加入哈希表
         将 current 移动到下一个节点
     循环结束后，返回 False
     ```

4. 复杂度：
   - 时间复杂度：快慢指针法的时间复杂度为 $O(n)$，其中 $n$ 是链表的节点数，因为每个节点最多被访问两次。
   - 空间复杂度：快慢指针法的空间复杂度为 $O(1)$，因为只使用了固定数量的指针。
   - 哈希表法的时间复杂度为 $O(n)$，空间复杂度为 $O(n)$，因为需要存储每个访问过的节点。