# 908. 链表的中间结点

**难度**: Easy | **标签**: `Linked List` `Two Pointers`

## 题目描述

<p>给你单链表的头结点 <code>head</code> ，请你找出并返回链表的中间结点。</p>

<p>如果有两个中间结点，则返回第二个中间结点。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg" style="width: 544px; height: 65px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,4,5]
<strong>输出：</strong>[3,4,5]
<strong>解释：</strong>链表只有一个中间结点，值为 3 。
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg" style="width: 664px; height: 65px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,4,5,6]
<strong>输出：</strong>[4,5,6]
<strong>解释：</strong>该链表有两个中间结点，值分别为 3 和 4 ，返回第二个结点。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表的结点数范围是 <code>[1, 100]</code></li>
	<li><code>1 &lt;= Node.val &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用快慢指针法，通过两个指针以不同速度遍历链表，最终慢指针指向链表的中间结点。

2. 综合思路：
   - 快慢指针法：使用两个指针 `slow` 和 `fast`，`slow` 每次移动一步，`fast` 每次移动两步，当 `fast` 到达链表末尾时，`slow` 正好位于链表的中间。
   - 计数法：遍历链表两次，第一次计算链表长度，第二次找到中间结点。
   - 数组法：将链表结点存入数组，然后直接访问数组的中间位置。

3. 全量伪代码：
   - 快慢指针法：
     ```
     初始化 slow 和 fast 指针都指向链表头部
     当 fast 不为空且 fast.next 不为空时，重复以下步骤：
         将 slow 移动到下一个结点
         将 fast 移动到下下个结点
     返回 slow 指针所指向的结点
     ```
   - 计数法：
     ```
     初始化长度为 0
     初始化指针指向链表头部
     遍历链表，计算链表长度
     计算中间位置为长度的一半
     重新初始化指针指向链表头部
     遍历链表直到到达中间位置
     返回当前指针所指向的结点
     ```
   - 数组法：
     ```
     初始化一个空数组
     初始化指针指向链表头部
     遍历链表，将每个结点存入数组
     计算中间位置为数组长度的一半
     返回数组中间位置的结点
     ```

4. 复杂度：
   - 快慢指针法：时间复杂度为 $O(n)$，空间复杂度为 $O(1)$。
   - 计数法：时间复杂度为 $O(n)$，空间复杂度为 $O(1)$。
   - 数组法：时间复杂度为 $O(n)$，空间复杂度为 $O(n)$。