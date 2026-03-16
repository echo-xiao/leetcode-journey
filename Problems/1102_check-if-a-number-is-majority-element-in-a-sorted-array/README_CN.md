# 1102. 检查一个数是否在数组中占绝大多数

**难度**: Easy | **标签**: `Array` `Binary Search`

## 题目描述

<p>给定一个按非递减顺序排序的整数数组 <code>nums</code> 和一个整数 <code>target</code>，如果 <code>target</code> 是一个 <strong>多数</strong> 元素，则返回 <code>true</code>，否则返回 <code>false</code>。</p>

<p>数组 <code>nums</code> 中的 <strong>多数</strong> 元素是指在数组中出现次数超过 <code>nums.length / 2</code> 的元素。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [2,4,5,5,5,5,5,6,6], target = 5
<strong>输出:</strong> true
<strong>解释:</strong> 值 5 出现了 5 次，数组的长度为 9。
因此，5 是一个多数元素，因为 5 &gt; 9/2 为真。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [10,100,101,101], target = 101
<strong>输出:</strong> false
<strong>解释:</strong> 值 101 出现了 2 次，数组的长度为 4。
因此，101 不是一个多数元素，因为 2 &gt; 4/2 为假。
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i], target &lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code> 是按非递减顺序排序的。</li>
</ul>

---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过线性扫描或二分查找找到目标元素的出现次数，并判断其是否超过数组长度的一半。

2. 综合思路：
   - **线性扫描法**：直接遍历数组，统计目标元素的出现次数，然后判断其是否超过数组长度的一半。
   - **二分查找法**：首先通过线性扫描找到目标元素的第一个出现位置，然后使用递归或迭代的二分查找找到最后一个出现位置，计算目标元素的总出现次数并判断其是否超过数组长度的一半。

3. 全量伪代码：
   - **线性扫描法**：
     ```
     初始化计数器 cnt 为 0
     对于数组中的每个元素：
         如果元素等于目标值：
             增加计数器 cnt
     如果 cnt 大于数组长度的一半：
         返回 True
     否则：
         返回 False
     ```
   - **二分查找法**：
     ```
     初始化 first 为 -1
     遍历数组找到目标值的第一个出现位置 first
     如果 first 为 -1：
         返回 False
     初始化 left 为 first，right 为数组长度减一
     使用递归或迭代的二分查找找到目标值的最后一个出现位置 last
     计算目标值的出现次数 dis = last - first + 1
     如果 dis 大于数组长度的一半：
         返回 True
     否则：
         返回 False
     ```

4. 复杂度：
   - **线性扫描法**：
     - 时间复杂度：$O(n)$
     - 空间复杂度：$O(1)$
   - **二分查找法**：
     - 时间复杂度：$O(\log n)$（假设数组是有序的，二分查找才有意义）
     - 空间复杂度：$O(1)$（迭代版本）或 $O(\log n)$（递归版本，考虑递归栈空间）