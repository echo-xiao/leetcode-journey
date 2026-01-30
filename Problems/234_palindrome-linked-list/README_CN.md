# 234. 回文链表

**难度**: Easy | **标签**: `Linked List` `Two Pointers` `Stack` `Recursion`

## 题目描述

<p>给你一个单链表的头节点 <code>head</code> ，请你判断该链表是否为<span data-keyword="palindrome-sequence">回文链表</span>。如果是，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg" style="width: 422px; height: 62px;" />
<pre>
<strong>输入：</strong>head = [1,2,2,1]
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg" style="width: 182px; height: 62px;" />
<pre>
<strong>输入：</strong>head = [1,2]
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中节点数目在范围<code>[1, 10<sup>5</sup>]</code> 内</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你能否用&nbsp;<code>O(n)</code> 时间复杂度和 <code>O(1)</code> 空间复杂度解决此题？</p>


---
## 解题思路与复盘

1. **一句话直击本质：**  
   利用栈或快慢指针法判断链表是否为回文，通过比较链表前半部分和后半部分的值。

2. **综合思路：**  
   - **栈方法：** 遍历链表，将所有节点值压入栈中，然后再次遍历链表，逐个弹出栈顶元素与当前节点值比较，若不相等则返回 `False`，否则返回 `True`。
   - **快慢指针法：** 使用快慢指针找到链表中点，将链表后半部分反转，然后比较前半部分和反转后的后半部分是否相等。

3. **全量伪代码：**

   - **栈方法：**
     ```
     初始化一个空栈
     当前节点指向链表头部
     遍历链表，将每个节点的值压入栈中
     当前节点重新指向链表头部
     遍历链表，弹出栈顶元素与当前节点值比较
       如果不相等，返回 False
     如果遍历结束，返回 True
     ```

   - **快慢指针法：**
     ```
     如果链表为空，返回 False
     如果链表只有一个节点，返回 True
     初始化慢指针和快指针指向链表头部
     初始化前慢指针为空
     使用快慢指针找到链表中点
     如果链表节点数为奇数，慢指针向前移动一位
     反转链表后半部分
     比较链表前半部分和反转后的后半部分
       如果不相等，返回 False
     如果比较结束，返回 True
     ```

4. **复杂度：**

   - **栈方法：**  
     时间复杂度：$O(n)$  
     空间复杂度：$O(n)$  

   - **快慢指针法：**  
     时间复杂度：$O(n)$  
     空间复杂度：$O(1)$  