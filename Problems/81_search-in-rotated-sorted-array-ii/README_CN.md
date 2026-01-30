# 81. 搜索旋转排序数组 II

**难度**: Medium | **标签**: `Array` `Binary Search`

## 题目描述

<p>已知存在一个按非降序排列的整数数组 <code>nums</code> ，数组中的值不必互不相同。</p>

<p>在传递给函数之前，<code>nums</code> 在预先未知的某个下标 <code>k</code>（<code>0 &lt;= k &lt; nums.length</code>）上进行了 <strong>旋转 </strong>，使数组变为 <code>[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]</code>（下标 <strong>从 0 开始</strong> 计数）。例如， <code>[0,1,2,4,4,4,5,6,6,7]</code> 在下标 <code>5</code> 处经旋转后可能变为 <code>[4,5,6,6,7,0,1,2,4,4]</code> 。</p>

<p>给你 <strong>旋转后</strong> 的数组 <code>nums</code> 和一个整数 <code>target</code> ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 <code>nums</code> 中存在这个目标值 <code>target</code> ，则返回 <code>true</code> ，否则返回 <code>false</code> 。</p>

<p>你必须尽可能减少整个操作步骤。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>nums = <code>[2,5,6,0,0,1,2]</code>, target = 0
<strong>输出：</strong>true
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>nums = <code>[2,5,6,0,0,1,2]</code>, target = 3
<strong>输出：</strong>false</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li>题目数据保证 <code>nums</code> 在预先未知的某个下标上进行了旋转</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>此题与&nbsp;<a href="https://leetcode.cn/problems/search-in-rotated-sorted-array/description/">搜索旋转排序数组</a>&nbsp;相似，但本题中的&nbsp;<code>nums</code>&nbsp; 可能包含 <strong>重复</strong> 元素。这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？</li>
</ul>

<p>&nbsp;</p>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过找到旋转点将数组分为两部分，然后在可能的部分进行二分查找，或者直接在旋转数组中进行调整后的二分查找。

2. **综合思路：**
   - **分段二分查找法：** 先通过二分法找到数组的旋转点（最小值），然后在旋转点的两侧分别进行标准的二分查找。
   - **调整后的二分查找法：** 直接在旋转数组上进行二分查找，通过判断中间值与左右边界的关系来调整搜索区间。

3. **全量伪代码：**

   - **分段二分查找法：**
     ```
     定义函数 search(nums, target):
         pivot = 找到旋转点(nums)
         在 [0, pivot-1] 区间进行二分查找(target)
         在 [pivot, len(nums)-1] 区间进行二分查找(target)
         返回是否找到 target

     定义函数 找到旋转点(nums):
         初始化 left = 0, right = len(nums) - 1
         当 left <= right 时:
             计算 mid = (left + right) // 2
             如果 nums[mid] > nums[right]:
                 left = mid + 1
             否则如果 nums[mid] < nums[right]:
                 right = mid
             否则:
                 如果 right > 0 且 nums[right] < nums[right - 1]:
                     返回 right
                 right -= 1
         返回 0

     定义函数 二分查找(nums, left, right, target):
         当 left <= right 时:
             计算 mid = (left + right) // 2
             如果 nums[mid] == target:
                 返回 True
             否则如果 nums[mid] < target:
                 left = mid + 1
             否则:
                 right = mid - 1
         返回 False
     ```

   - **调整后的二分查找法：**
     ```
     定义函数 search(nums, target):
         初始化 left = 0, right = len(nums) - 1
         当 left <= right 时:
             计算 mid = (left + right) // 2
             如果 nums[mid] == target:
                 返回 True
             如果 nums[left] == nums[mid]:
                 left += 1
             否则如果 nums[left] < nums[mid]:
                 如果 nums[left] <= target < nums[mid]:
                     right = mid - 1
                 否则:
                     left = mid + 1
             否则:
                 如果 nums[mid] < target <= nums[right]:
                     left = mid + 1
                 否则:
                     right = mid - 1
         返回 False
     ```

4. **复杂度：**
   - **时间复杂度：** $O(n)$，在最坏情况下，例如数组中有大量重复元素时，可能需要线性扫描。
   - **空间复杂度：** $O(1)$，只使用了常数级别的额外空间。