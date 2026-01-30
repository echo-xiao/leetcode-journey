# 792. 二分查找

**难度**: Easy | **标签**: `Array` `Binary Search`

## 题目描述

<p>给定一个&nbsp;<code>n</code>&nbsp;个元素有序的（升序）整型数组&nbsp;<code>nums</code> 和一个目标值&nbsp;<code>target</code> &nbsp;，写一个函数搜索&nbsp;<code>nums</code>&nbsp;中的 <code>target</code>，如果&nbsp;<code>target</code> 存在返回下标，否则返回 <code>-1</code>。</p>

<p>你必须编写一个具有 <code>O(log n)</code> 时间复杂度的算法。</p>

<p><br />
<strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> <code>nums</code> = [-1,0,3,5,9,12], <code>target</code> = 9
<strong>输出:</strong> 4
<strong>解释:</strong> 9 出现在 <code>nums</code> 中并且下标为 4
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> <code>nums</code> = [-1,0,3,5,9,12], <code>target</code> = 2
<strong>输出:</strong> -1
<strong>解释:</strong> 2 不存在 <code>nums</code> 中因此返回 -1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>你可以假设 <code>nums</code>&nbsp;中的所有元素是不重复的。</li>
	<li><code>n</code>&nbsp;将在&nbsp;<code>[1, 10000]</code>之间。</li>
	<li><code>nums</code>&nbsp;的每个元素都将在&nbsp;<code>[-9999, 9999]</code>之间。</li>
</ol>


---
## 解题思路与复盘

1. 一句话直击本质：
   - 二分查找的核心逻辑是通过不断将搜索范围缩小一半来高效地查找有序数组中的目标元素。

2. 综合思路：
   - 递归解法：通过递归函数不断缩小搜索范围，直到找到目标元素或搜索范围为空。
   - 迭代解法：使用循环来调整搜索范围的边界，直到找到目标元素或搜索范围为空。

3. 全量伪代码：
   - 递归版本：
     ```
     函数 search(nums, target):
         返回 helper(nums, target, 0, len(nums) - 1)

     函数 helper(nums, target, left, right):
         如果 left > right:
             返回 -1
         mid = left + (right - left) // 2
         如果 nums[mid] == target:
             返回 mid
         否则如果 nums[mid] > target:
             返回 helper(nums, target, left, mid - 1)
         否则:
             返回 helper(nums, target, mid + 1, right)
     ```

   - 迭代版本：
     ```
     函数 search(nums, target):
         left = 0
         right = len(nums) - 1
         当 left <= right 时:
             mid = left + (right - left) // 2
             如果 nums[mid] == target:
                 返回 mid
             否则如果 nums[mid] > target:
                 right = mid - 1
             否则:
                 left = mid + 1
         返回 -1
     ```

4. 复杂度：
   - 时间复杂度：$O(\log n)$，因为每次操作将搜索范围缩小一半。
   - 空间复杂度：递归版本为 $O(\log n)$（由于递归栈），迭代版本为 $O(1)$。