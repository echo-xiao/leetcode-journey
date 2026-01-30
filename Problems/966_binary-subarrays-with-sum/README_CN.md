# 966. 和相同的二元子数组

**难度**: Medium | **标签**: `Array` `Hash Table` `Sliding Window` `Prefix Sum`

## 题目描述

<p>给你一个二元数组 <code>nums</code> ，和一个整数 <code>goal</code> ，请你统计并返回有多少个和为 <code>goal</code> 的<strong> 非空</strong> 子数组。</p>

<p><strong>子数组</strong> 是数组的一段连续部分。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,0,1,0,1], goal = 2
<strong>输出：</strong>4
<strong>解释：</strong>
有 4 个满足题目要求的子数组：[1,0,1]、[1,0,1,0]、[0,1,0,1]、[1,0,1]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,0,0,0,0], goal = 0
<strong>输出：</strong>15
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 3 * 10<sup>4</sup></code></li>
	<li><code>nums[i]</code> 不是 <code>0</code> 就是 <code>1</code></li>
	<li><code>0 <= goal <= nums.length</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过滑动窗口计算最多为 `goal` 和 `goal-1` 的子数组数量，利用差值得到和为 `goal` 的子数组数量。

2. 综合思路：
   - 滑动窗口：使用滑动窗口方法计算最多为 `goal` 和 `goal-1` 的子数组数量，然后通过两者的差值得到和为 `goal` 的子数组数量。这种方法通过维护一个窗口来动态调整子数组的和。
   - 前缀和与哈希表：另一种常见的解法是使用前缀和与哈希表来记录前缀和出现的次数，通过计算当前前缀和与目标和的差值来确定符合条件的子数组数量。

3. 全量伪代码：
   - 滑动窗口方法：
     ```
     定义函数 numSubarraysWithSum(nums, goal):
         返回 atMost(nums, goal) - atMost(nums, goal - 1)

     定义函数 atMost(nums, k):
         如果 k < 0，返回 0
         初始化 left, right, res, cnt 为 0
         当 right 小于 nums 的长度时:
             将 nums[right] 加到 res
             将 right 加 1
             当 res 大于 k 时:
                 从 res 中减去 nums[left]
                 将 left 加 1
             将 (right - left) 加到 cnt
         返回 cnt
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是数组 `nums` 的长度，因为每个元素最多被访问两次。
   - 空间复杂度：$O(1)$，因为只使用了固定数量的额外空间。