# 2634. 最小公共值

**难度**: Easy | **标签**: `Array` `Hash Table` `Two Pointers` `Binary Search`

## 题目描述

<p>给你两个整数数组&nbsp;<code>nums1</code> 和&nbsp;<code>nums2</code>&nbsp;，它们已经按非降序排序，请你返回两个数组的 <strong>最小公共整数</strong>&nbsp;。如果两个数组&nbsp;<code>nums1</code> 和&nbsp;<code>nums2</code>&nbsp;没有公共整数，请你返回&nbsp;<code>-1</code>&nbsp;。</p>

<p>如果一个整数在两个数组中都 <strong>至少出现一次</strong>&nbsp;，那么这个整数是数组&nbsp;<code>nums1</code> 和&nbsp;<code>nums2</code>&nbsp;<strong>公共</strong>&nbsp;的。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums1 = [1,2,3], nums2 = [2,4]
<b>输出：</b>2
<b>解释：</b>两个数组的最小公共元素是 2 ，所以我们返回 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums1 = [1,2,3,6], nums2 = [2,3,4,5]
<b>输出：</b>2
<b>解释：</b>两个数组中的公共元素是 2 和 3 ，2 是较小值，所以返回 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums1[i], nums2[j] &lt;= 10<sup>9</sup></code></li>
	<li><code>nums1</code> 和&nbsp;<code>nums2</code>&nbsp;都是 <strong>非降序</strong>&nbsp;的。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：核心逻辑是通过双指针或二分查找在两个有序数组中寻找最小的公共元素。

2. 综合思路：
   - 双指针法：同时遍历两个有序数组，比较当前元素，若相等则返回该元素，否则移动较小元素的指针。
   - 二分查找法：对其中一个数组的每个元素，在另一个数组中进行二分查找，找到相同元素则更新最小公共值。

3. 全量伪代码：
   - 双指针法：
     ```
     初始化指针 i 和 j 为 0
     当 i 和 j 都在各自数组的范围内时：
         如果 nums1[i] 等于 nums2[j]：
             返回 nums1[i]
         否则如果 nums1[i] 大于 nums2[j]：
             增加 j
         否则：
             增加 i
     返回 -1
     ```
   - 二分查找法：
     ```
     初始化 min_res 为正无穷
     对于 nums2 中的每个元素 target：
         初始化 left 为 0，right 为 nums1 的长度减 1
         初始化 res 为正无穷
         当 left 小于等于 right 时：
             计算 mid 为 left 和 right 的中间索引
             如果 nums1[mid] 等于 target：
                 将 res 更新为 nums1[mid]
                 跳出循环
             否则如果 nums1[mid] 大于 target：
                 将 right 更新为 mid 减 1
             否则：
                 将 left 更新为 mid 加 1
         将 min_res 更新为 min(res, min_res)
     如果 min_res 仍为正无穷：
         返回 -1
     否则：
         返回 min_res
     ```

4. 复杂度：
   - 双指针法的时间复杂度为 $O(n + m)$，空间复杂度为 $O(1)$，其中 $n$ 和 $m$ 分别是两个数组的长度。
   - 二分查找法的时间复杂度为 $O(m \log n)$，空间复杂度为 $O(1)$，其中 $m$ 是较短数组的长度，$n$ 是较长数组的长度。