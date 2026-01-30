# 147. 对链表进行插入排序

**难度**: Medium | **标签**: `Linked List` `Sorting`

## 题目描述

<p>给定单个链表的头<meta charset="UTF-8" />&nbsp;<code>head</code>&nbsp;，使用 <strong>插入排序</strong> 对链表进行排序，并返回&nbsp;<em>排序后链表的头</em>&nbsp;。</p>

<p><strong>插入排序</strong>&nbsp;算法的步骤:</p>

<ol>
	<li>插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。</li>
	<li>每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。</li>
	<li>重复直到所有输入数据插入完为止。</li>
</ol>

<p>下面是插入排序算法的一个图形示例。部分排序的列表(黑色)最初只包含列表中的第一个元素。每次迭代时，从输入数据中删除一个元素(红色)，并就地插入已排序的列表中。</p>

<p>对链表进行插入排序。</p>

<p><img alt="" src="https://pic.leetcode.cn/1724130387-qxfMwx-Insertion-sort-example-300px.gif" /></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1724130414-QbPAjl-image.png" /></p>

<pre>
<strong>输入:</strong> head = [4,2,1,3]
<strong>输出:</strong> [1,2,3,4]</pre>

<p><strong>示例&nbsp;2：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1724130432-zoOvdI-image.png" /></p>

<pre>
<strong>输入:</strong> head = [-1,5,3,4,0]
<strong>输出:</strong> [-1,0,3,4,5]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<p><meta charset="UTF-8" /></p>

<ul>
	<li>列表中的节点数在&nbsp;<code>[1, 5000]</code>范围内</li>
	<li><code>-5000 &lt;= Node.val &lt;= 5000</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 插入排序通过逐个遍历链表节点，将每个节点插入到已排序部分的正确位置。

2. **综合思路：**
   - **迭代法：** 所有版本均采用迭代法，通过一个虚拟头节点 `dummy` 来简化插入操作，遍历链表并在已排序部分找到合适位置插入当前节点。
   - **不同处理方式：** 版本 1 通过维护一个 `lastSorted` 指针来优化部分情况，而其他版本直接在每次迭代中从 `dummy` 开始寻找插入位置。

3. **全量伪代码：**
   - 初始化一个虚拟头节点 `dummy`，其 `next` 指向 `head`。
   - 设置 `curr` 指针指向链表的第一个节点。
   - **迭代遍历链表：**
     - 保存 `curr.next` 到 `nxt`。
     - 初始化 `prev` 指针指向 `dummy`。
     - **寻找插入位置：**
       - 当 `prev.next` 存在且 `prev.next.val` 小于 `curr.val` 时，移动 `prev` 到 `prev.next`。
     - 将 `curr` 插入到 `prev` 和 `prev.next` 之间。
     - 更新 `curr` 为 `nxt`。
   - 返回 `dummy.next` 作为排序后的链表头。

4. **复杂度：**
   - **时间复杂度：** $O(n^2)$，其中 $n$ 是链表的节点数。每个节点在最坏情况下需要遍历已排序部分的所有节点。
   - **空间复杂度：** $O(1)$，只使用了常数个额外指针。