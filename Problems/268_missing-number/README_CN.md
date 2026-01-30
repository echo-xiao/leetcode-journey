# 268. 丢失的数字

**难度**: Easy | **标签**: `Array` `Hash Table` `Math` `Binary Search` `Bit Manipulation` `Sorting`

## 题目描述

<p>给定一个包含 <code>[0, n]</code>&nbsp;中&nbsp;<code>n</code>&nbsp;个数的数组 <code>nums</code> ，找出 <code>[0, n]</code> 这个范围内没有出现在数组中的那个数。</p>

<ul>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>nums = [3,0,1]</p>

<p><strong>输出：</strong>2</p>

<p><b>解释：</b><code>n = 3</code>，因为有 3 个数字，所以所有的数字都在范围 <code>[0,3]</code> 内。2 是丢失的数字，因为它没有出现在 <code>nums</code> 中。</p>
</div>

<p><strong>示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>nums = [0,1]</p>

<p><strong>输出：</strong>2</p>

<p><b>解释：</b><code>n = 2</code>，因为有 2 个数字，所以所有的数字都在范围 <code>[0,2]</code> 内。2 是丢失的数字，因为它没有出现在 <code>nums</code> 中。</p>
</div>

<p><strong>示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>nums = [9,6,4,2,3,5,7,0,1]</p>

<p><strong>输出：</strong>8</p>

<p><b>解释：</b><code>n = 9</code>，因为有 9 个数字，所以所有的数字都在范围 <code>[0,9]</code> 内。8 是丢失的数字，因为它没有出现在 <code>nums</code> 中。</p>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= n</code></li>
	<li><code>nums</code> 中的所有数字都 <strong>独一无二</strong></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?</p>


---
## 解题思路与复盘

1. 一句话直击本质：利用排序后的数组，通过二分查找法找到第一个索引与元素不匹配的位置，即为丢失的数字。

2. 综合思路：
   - 递归二分查找：通过递归的方式实现二分查找，逐步缩小查找范围，直到找到丢失的数字。
   - 迭代二分查找：通过迭代的方式实现二分查找，使用循环来调整查找范围，最终找到丢失的数字。

3. 全量伪代码：
   - 递归二分查找：
     ```
     函数 missingNumber(nums):
         对 nums 进行排序
         返回 helper(nums, 0, len(nums) - 1)

     函数 helper(nums, left, right):
         如果 left > right:
             返回 left
         计算 mid = left + (right - left) // 2
         如果 nums[mid] == mid:
             返回 helper(nums, mid + 1, right)
         否则如果 nums[mid] > mid:
             返回 helper(nums, left, mid - 1)
     ```
   - 迭代二分查找：
     ```
     函数 missingNumber(nums):
         对 nums 进行排序
         初始化 left = 0, right = len(nums) - 1
         当 left <= right 时:
             计算 mid = left + (right - left) // 2
             如果 nums[mid] == mid:
                 更新 left = mid + 1
             否则如果 nums[mid] > mid:
                 更新 right = mid - 1
         返回 left
     ```

4. 复杂度：
   - 时间复杂度：$O(n \log n)$，由于需要对数组进行排序，排序的时间复杂度为 $O(n \log n)$，二分查找的时间复杂度为 $O(\log n)$，但排序是主要的时间消耗。
   - 空间复杂度：$O(1)$，不考虑排序所需的额外空间，递归版本的空间复杂度为 $O(\log n)$，因为递归调用栈的深度为 $O(\log n)$。