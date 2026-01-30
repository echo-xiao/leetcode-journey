# 143. 重排链表

**难度**: Medium | **标签**: `Linked List` `Two Pointers` `Stack` `Recursion`

## 题目描述

<p>给定一个单链表 <code>L</code><em> </em>的头节点 <code>head</code> ，单链表 <code>L</code> 表示为：</p>

<pre>
L<sub>0</sub> → L<sub>1</sub> → … → L<sub>n - 1</sub> → L<sub>n</sub>
</pre>

<p>请将其重新排列后变为：</p>

<pre>
L<sub>0</sub> → L<sub>n</sub> → L<sub>1</sub> → L<sub>n - 1</sub> → L<sub>2</sub> → L<sub>n - 2</sub> → …</pre>

<p>不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1626420311-PkUiGI-image.png" style="width: 240px; " /></p>

<pre>
<strong>输入：</strong>head = [1,2,3,4]
<strong>输出：</strong>[1,4,2,3]</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1626420320-YUiulT-image.png" style="width: 320px; " /></p>

<pre>
<strong>输入：</strong>head = [1,2,3,4,5]
<strong>输出：</strong>[1,5,2,4,3]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表的长度范围为 <code>[1, 5 * 10<sup>4</sup>]</code></li>
	<li><code>1 &lt;= node.val &lt;= 1000</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过快慢指针找到链表中点，将后半部分反转，然后合并前半部分和反转后的后半部分。

2. **综合思路：** 
   - **快慢指针 + 反转 + 合并：** 所有版本都采用了这种思路。首先使用快慢指针找到链表的中点，然后将链表的后半部分反转，最后将前半部分和反转后的后半部分交替合并。
   - **迭代实现：** 反转链表和合并链表的过程均通过迭代实现，没有使用递归或其他数据结构。

3. **全量伪代码：**
   ```plaintext
   函数 reorderList(链表头节点 head):
       如果 head 为空或只有一个节点:
           返回

       初始化快指针 fast 和慢指针 slow 指向 head

       // 使用快慢指针找到链表中点
       当 fast 和 fast.next 不为空:
           fast 移动两步
           slow 移动一步

       将 slow 的下一个节点作为后半部分的头节点 fast
       将 slow.next 置为 None 断开链表

       // 反转后半部分链表
       调用 reverse 函数反转 fast 链表

       // 合并前半部分和反转后的后半部分
       初始化 lst1 指向 head, lst2 指向反转后的链表头
       当 lst1 和 lst2 均不为空:
           保存 lst1.next 到 tmp1
           保存 lst2.next 到 tmp2

           将 lst1.next 指向 lst2
           将 lst2.next 指向 tmp1

           更新 lst1 为 tmp1
           更新 lst2 为 tmp2

   函数 reverse(链表头节点 head):
       初始化 prev 为 None, curr 为 head

       // 反转链表
       当 curr 不为空:
           保存 curr.next 到 tmp
           将 curr.next 指向 prev

           更新 prev 为 curr
           更新 curr 为 tmp

       返回 prev
   ```

4. **复杂度：**
   - **时间复杂度：** $O(n)$，其中 $n$ 是链表的节点数。找到中点、反转链表和合并链表均需要线性时间。
   - **空间复杂度：** $O(1)$，只使用了常数级别的额外空间。