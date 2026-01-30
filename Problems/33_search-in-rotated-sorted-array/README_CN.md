# 33. 搜索旋转排序数组

**难度**: Medium | **标签**: `Array` `Binary Search`

## 题目描述

<p>整数数组 <code>nums</code> 按升序排列，数组中的值 <strong>互不相同</strong> 。</p>

<p>在传递给函数之前，<code>nums</code> 在预先未知的某个下标 <code>k</code>（<code>0 &lt;= k &lt; nums.length</code>）上进行了 <strong>向左旋转</strong>，使数组变为 <code>[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]</code>（下标 <strong>从 0 开始</strong> 计数）。例如， <code>[0,1,2,4,5,6,7]</code> 下标&nbsp;<code>3</code>&nbsp;上向左旋转后可能变为&nbsp;<code>[4,5,6,7,0,1,2]</code> 。</p>

<p>给你 <strong>旋转后</strong> 的数组 <code>nums</code> 和一个整数 <code>target</code> ，如果 <code>nums</code> 中存在这个目标值 <code>target</code> ，则返回它的下标，否则返回&nbsp;<code>-1</code>&nbsp;。</p>

<p>你必须设计一个时间复杂度为 <code>O(log n)</code> 的算法解决此问题。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,5,6,7,0,1,2], target = 0
<strong>输出：</strong>4
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,5,6,7,0,1,2], target = 3
<strong>输出：</strong>-1</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1], target = 0
<strong>输出：</strong>-1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> 中的每个值都 <strong>独一无二</strong></li>
	<li>题目数据保证 <code>nums</code> 在预先未知的某个下标上进行了旋转</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：利用二分查找法，通过判断中点与边界值的关系来确定目标值所在的有序区间。

2. 综合思路：
   - **版本 1 和 2**：先通过二分查找找到旋转数组的旋转点（即最小值位置），然后在确定的有序区间内再次使用二分查找寻找目标值。
   - **版本 3 和 4**：类似于版本 1 和 2，但在寻找旋转点时，直接通过比较中点与末尾元素的关系来确定旋转点。
   - **版本 5 到 9**：直接在一次二分查找过程中，通过判断中点与左右边界的关系来确定目标值所在的有序区间，并在该区间内继续二分查找。

3. 全量伪代码：
   - **寻找旋转点的二分查找**：
     ```
     定义函数 findPivotIndex(nums):
         初始化 left 为 0, right 为 len(nums) - 1
         当 left <= right 时:
             计算 mid 为 left + (right - left) // 2
             如果 nums[mid] > nums[right]:
                 left = mid + 1
             否则:
                 right = mid - 1
         返回 left
     ```
   - **在有序区间内进行二分查找**：
     ```
     定义函数 binarySearch(nums, left, right, target):
         当 left <= right 时:
             计算 mid 为 left + (right - left) // 2
             如果 nums[mid] == target:
                 返回 mid
             如果 nums[mid] < target:
                 left = mid + 1
             否则:
                 right = mid - 1
         返回 -1
     ```
   - **直接在旋转数组中进行二分查找**：
     ```
     定义函数 search(nums, target):
         初始化 left 为 0, right 为 len(nums) - 1
         当 left <= right 时:
             计算 mid 为 left + (right - left) // 2
             如果 nums[mid] == target:
                 返回 mid
             如果 nums[left] <= nums[mid]:
                 如果 nums[left] <= target < nums[mid]:
                     right = mid - 1
                 否则:
                     left = mid + 1
             否则:
                 如果 nums[mid] < target <= nums[right]:
                     left = mid + 1
                 否则:
                     right = mid - 1
         返回 -1
     ```

4. 复杂度：
   - 时间复杂度：$O(\log n)$，因为每次操作都将搜索空间减半。
   - 空间复杂度：$O(1)$，因为只使用了常数级别的额外空间。