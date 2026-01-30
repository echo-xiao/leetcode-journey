# 350. 两个数组的交集 II

**难度**: Easy | **标签**: `Array` `Hash Table` `Two Pointers` `Binary Search` `Sorting`

## 题目描述

<p>给你两个整数数组&nbsp;<code>nums1</code> 和 <code>nums2</code> ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,2,2,1], nums2 = [2,2]
<strong>输出：</strong>[2,2]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入：</strong>nums1 = [4,9,5], nums2 = [9,4,9,8,4]
<strong>输出：</strong>[4,9]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>

<p><strong><strong>进阶</strong>：</strong></p>

<ul>
	<li>如果给定的数组已经排好序呢？你将如何优化你的算法？</li>
	<li>如果&nbsp;<code>nums1</code><em>&nbsp;</em>的大小比&nbsp;<code>nums2</code> 小，哪种方法更优？</li>
	<li>如果&nbsp;<code>nums2</code><em>&nbsp;</em>的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过排序和双指针遍历两个数组，找到所有相同的元素。

2. 综合思路：
   - 排序 + 双指针：首先对两个数组进行排序，然后使用双指针同时遍历两个数组，找到相同的元素并加入结果集。
   - 哈希表：使用哈希表记录一个数组中每个元素的出现次数，然后遍历另一个数组，找到相同的元素并减少哈希表中的计数。

3. 全量伪代码：
   - 排序 + 双指针：
     ```
     对 nums1 和 nums2 进行排序
     初始化指针 i 和 j 为 0
     初始化结果数组 result 为 []
     当 i < nums1 的长度 且 j < nums2 的长度 时：
         如果 nums1[i] == nums2[j]：
             将 nums1[i] 添加到 result
             i 和 j 都增加 1
         否则如果 nums1[i] > nums2[j]：
             j 增加 1
         否则：
             i 增加 1
     返回 result
     ```

4. 复杂度：
   - 时间复杂度：$O(n \log n + m \log m)$，其中 $n$ 和 $m$ 分别是 nums1 和 nums2 的长度，因为需要对两个数组进行排序。
   - 空间复杂度：$O(1)$，如果不考虑结果数组的空间，因为只使用了常数级别的额外空间。