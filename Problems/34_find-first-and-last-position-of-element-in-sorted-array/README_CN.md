# 34. 在排序数组中查找元素的第一个和最后一个位置

**难度**: Medium | **标签**: `Array` `Binary Search`

## 题目描述

<p>给你一个按照非递减顺序排列的整数数组 <code>nums</code>，和一个目标值 <code>target</code>。请你找出给定目标值在数组中的开始位置和结束位置。</p>

<p>如果数组中不存在目标值 <code>target</code>，返回&nbsp;<code>[-1, -1]</code>。</p>

<p>你必须设计并实现时间复杂度为&nbsp;<code>O(log n)</code>&nbsp;的算法解决此问题。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [<code>5,7,7,8,8,10]</code>, target = 8
<strong>输出：</strong>[3,4]</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>nums = [<code>5,7,7,8,8,10]</code>, target = 6
<strong>输出：</strong>[-1,-1]</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [], target = 0
<strong>输出：</strong>[-1,-1]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= nums[i]&nbsp;&lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code>&nbsp;是一个非递减数组</li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= target&nbsp;&lt;= 10<sup>9</sup></code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：**  
   使用二分查找分别找到目标值在排序数组中的第一个和最后一个位置。

2. **综合思路：**  
   - **分开查找左右边界：**  
     通过两个独立的二分查找函数分别查找目标值的左边界和右边界。每个函数根据查找到的中间值调整左右指针，直到找到边界。
   - **合并查找左右边界：**  
     使用一个函数，通过一个标志位来决定查找左边界还是右边界。根据标志位调整指针方向，找到目标值的边界。

3. **全量伪代码：**

   - **查找左边界：**
     ```
     函数 leftBound(数组 nums, 整数 target):
         初始化 left 为 0, right 为 数组长度 - 1
         当 left 小于等于 right 时:
             计算 mid 为 left 和 right 的中间位置
             如果 nums[mid] 等于 target:
                 将 right 移动到 mid - 1
             否则如果 nums[mid] 小于 target:
                 将 left 移动到 mid + 1
             否则:
                 将 right 移动到 mid - 1
         如果 left 超出数组边界或 nums[left] 不等于 target:
             返回 -1
         返回 left
     ```

   - **查找右边界：**
     ```
     函数 rightBound(数组 nums, 整数 target):
         初始化 left 为 0, right 为 数组长度 - 1
         当 left 小于等于 right 时:
             计算 mid 为 left 和 right 的中间位置
             如果 nums[mid] 等于 target:
                 将 left 移动到 mid + 1
             否则如果 nums[mid] 小于 target:
                 将 left 移动到 mid + 1
             否则:
                 将 right 移动到 mid - 1
         如果 right 超出数组边界或 nums[right] 不等于 target:
             返回 -1
         返回 right
     ```

   - **合并查找边界：**
     ```
     函数 findBound(数组 nums, 整数 target, 布尔 isFirst):
         初始化 left 为 0, right 为 数组长度 - 1
         初始化 candidate 为 -1
         当 left 小于等于 right 时:
             计算 mid 为 left 和 right 的中间位置
             如果 nums[mid] 等于 target:
                 将 candidate 设为 mid
                 如果 isFirst 为真:
                     将 right 移动到 mid - 1
                 否则:
                     将 left 移动到 mid + 1
             否则如果 nums[mid] 小于 target:
                 将 left 移动到 mid + 1
             否则:
                 将 right 移动到 mid - 1
         返回 candidate
     ```

4. **复杂度：**  
   - **时间复杂度：** $O(\log n)$，因为每次查找都是通过二分查找进行的。
   - **空间复杂度：** $O(1)$，因为只使用了常数级别的额外空间。