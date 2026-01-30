# 1411. 二进制链表转整数

**难度**: Easy | **标签**: `Linked List` `Math`

## 题目描述

<p>给你一个单链表的引用结点&nbsp;<code>head</code>。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。</p>

<p>请你返回该链表所表示数字的 <strong>十进制值</strong> 。</p>

<p><strong>最高位</strong> 在链表的头部。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/12/15/graph-1.png" style="height: 108px; width: 426px;" /></p>

<pre>
<strong>输入：</strong>head = [1,0,1]
<strong>输出：</strong>5
<strong>解释：</strong>二进制数 (101) 转化为十进制数 (5)
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>head = [0]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表不为空。</li>
	<li>链表的结点总数不超过&nbsp;<code>30</code>。</li>
	<li>每个结点的值不是&nbsp;<code>0</code> 就是 <code>1</code>。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过遍历链表，将每个节点的二进制位按顺序累加到一个整数中。

2. 综合思路：
   - 迭代法：遍历链表，从头到尾依次处理每个节点的值，将其视为二进制数的一位，使用位运算或乘法累加到最终的整数结果中。

3. 全量伪代码：
   ```
   定义函数 getDecimalValue(head):
       初始化 total_value 为 0
       初始化 curr 为 head

       当 curr 不为空时:
           将 total_value 左移一位（或 total_value 乘以 2）
           将 curr.val 加到 total_value 上
           将 curr 移动到下一个节点

       返回 total_value
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是链表的长度，因为需要遍历整个链表。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外变量。