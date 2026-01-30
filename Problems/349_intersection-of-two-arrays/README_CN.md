# 349. 两个数组的交集

**难度**: Easy | **标签**: `Array` `Hash Table` `Two Pointers` `Binary Search` `Sorting`

## 题目描述

<p>给定两个数组&nbsp;<code>nums1</code>&nbsp;和&nbsp;<code>nums2</code> ，返回 <em>它们的 <span data-keyword="array-intersection">交集</span></em>&nbsp;。输出结果中的每个元素一定是 <strong>唯一</strong> 的。我们可以 <strong>不考虑输出结果的顺序</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,2,2,1], nums2 = [2,2]
<strong>输出：</strong>[2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [4,9,5], nums2 = [9,4,9,8,4]
<strong>输出：</strong>[9,4]
<strong>解释：</strong>[4,9] 也是可通过的
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过排序和二分查找或双指针遍历等方法，找出两个数组中的公共元素。

2. 综合思路：
   - **二分查找法**：将一个数组排序后，对另一个数组中的每个元素进行二分查找，判断其是否存在于第一个数组中。
   - **双指针法**：将两个数组排序后，使用双指针同时遍历两个数组，找到相同的元素。
   - **暴力法**：直接使用双重循环遍历两个数组，检查每个元素是否在另一个数组中。

3. 全量伪代码：
   - **二分查找法**：
     ```
     对 nums1 和 nums2 进行排序
     初始化结果集合 res
     对于 nums2 中的每个元素 target：
         在 nums1 中使用二分查找 target：
             如果找到，添加 target 到 res
     返回 res 的列表形式
     ```
   - **双指针法**：
     ```
     对 nums1 和 nums2 进行排序
     初始化指针 i 和 j 为 0
     初始化结果列表 nums
     当 i < len(nums1) 且 j < len(nums2) 时：
         如果 nums1[i] == nums2[j]：
             将 nums1[i] 添加到 nums
             i 和 j 都加 1
         否则如果 nums1[i] > nums2[j]：
             j 加 1
         否则：
             i 加 1
     返回 nums 的集合形式
     ```
   - **暴力法**：
     ```
     初始化结果集合 num
     对于 nums1 中的每个元素：
         对于 nums2 中的每个元素：
             如果两个元素相等且不在 num 中：
                 将元素添加到 num
     返回 num 的列表形式
     ```

4. 复杂度：
   - **二分查找法**：
     - 时间复杂度：$O(n \log n + m \log n)$，其中 $n$ 是 nums1 的长度，$m$ 是 nums2 的长度。
     - 空间复杂度：$O(n)$，用于存储结果集合。
   - **双指针法**：
     - 时间复杂度：$O(n \log n + m \log m)$，排序两个数组的时间复杂度。
     - 空间复杂度：$O(n)$，用于存储结果集合。
   - **暴力法**：
     - 时间复杂度：$O(n \times m)$，双重循环遍历两个数组。
     - 空间复杂度：$O(n)$，用于存储结果集合。