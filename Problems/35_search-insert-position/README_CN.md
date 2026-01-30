# 35. 搜索插入位置

**难度**: Easy | **标签**: `Array` `Binary Search`

## 题目描述

<p>给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。</p>

<p>请必须使用时间复杂度为 <code>O(log n)</code> 的算法。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,3,5,6], target = 5
<strong>输出:</strong> 2
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,3,5,6], target = 2
<strong>输出:</strong> 1
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,3,5,6], target = 7
<strong>输出:</strong> 4
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> 为&nbsp;<strong>无重复元素&nbsp;</strong>的&nbsp;<strong>升序&nbsp;</strong>排列数组</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是利用二分查找法在有序数组中快速找到目标值的位置或插入位置。

2. 综合思路：
   - 递归法：通过递归调用实现二分查找，逐步缩小搜索范围，直到找到目标值或确定插入位置。
   - 迭代法：使用循环实现二分查找，通过调整左右边界来缩小搜索范围，直到找到目标值或确定插入位置。
   - 递归与迭代的区别在于递归方法可能会导致额外的栈空间使用，而迭代方法则在空间上更为高效。

3. 全量伪代码：
   - 递归法：
     ```
     函数 searchInsert(nums, target):
         如果 nums 为空:
             返回 0
         中间索引 m = 数组长度的一半
         如果 nums[m] 等于 target:
             返回 m
         否则如果 nums[m] 大于 target:
             返回 searchInsert(nums 的前半部分, target)
         否则:
             返回 searchInsert(nums 的后半部分, target) 加上 m+1
     ```
   - 递归法（优化版，传递索引）：
     ```
     函数 searchHelper(nums, target, left, right):
         如果 left 大于 right:
             返回 left
         中间索引 mid = left + (right - left + 1) // 2
         如果 nums[mid] 等于 target:
             返回 mid
         否则如果 nums[mid] 大于 target:
             返回 searchHelper(nums, target, left, mid-1)
         否则:
             返回 searchHelper(nums, target, mid+1, right)
     ```
   - 迭代法：
     ```
     函数 searchInsert(nums, target):
         初始化 l = 0, r = len(nums) - 1
         当 l 小于等于 r 时:
             计算中间索引 m = l + (r - l) // 2
             如果 nums[m] 等于 target:
                 返回 m
             否则如果 nums[m] 大于 target:
                 r = m - 1
             否则:
                 l = m + 1
         返回 l
     ```

4. 复杂度：
   - 时间复杂度：所有版本的时间复杂度均为 $O(\log n)$，因为二分查找每次将搜索范围缩小一半。
   - 空间复杂度：
     - 递归法（版本 1 和版本 2）：由于递归调用栈的存在，空间复杂度为 $O(\log n)$。
     - 迭代法（版本 3 和版本 4）：由于没有递归调用，空间复杂度为 $O(1)$。