# 724. 寻找数组的中心下标

**难度**: Easy | **标签**: `Array` `Prefix Sum`

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code> ，请计算数组的 <strong>中心下标 </strong>。</p>

<p>数组<strong> 中心下标</strong><strong> </strong>是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。</p>

<p>如果中心下标位于数组最左端，那么左侧数之和视为 <code>0</code> ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。</p>

<p>如果数组有多个中心下标，应该返回 <strong>最靠近左边</strong> 的那一个。如果数组不存在中心下标，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1, 7, 3, 6, 5, 6]
<strong>输出：</strong>3
<strong>解释：</strong>
中心下标是 3 。
左侧数之和 sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 ，
右侧数之和 sum = nums[4] + nums[5] = 5 + 6 = 11 ，二者相等。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1, 2, 3]
<strong>输出：</strong>-1
<strong>解释：</strong>
数组中不存在满足此条件的中心下标。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [2, 1, -1]
<strong>输出：</strong>0
<strong>解释：</strong>
中心下标是 0 。
左侧数之和 sum = 0 ，（下标 0 左侧不存在元素），
右侧数之和 sum = nums[1] + nums[2] = 1 + -1 = 0 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与主站 1991 题相同：<a href="https://leetcode.cn/problems/find-the-middle-index-in-array/" target="_blank">https://leetcode.cn/problems/find-the-middle-index-in-array/</a></p>


---
## 解题思路与复盘

1. 一句话直击本质：通过前缀和计算数组的中心下标，使得中心下标左侧和右侧的元素和相等。

2. 综合思路：
   - 前缀和法：计算每个位置的前缀和，然后通过比较左侧前缀和与右侧前缀和来确定中心下标。
   - 单次遍历法：先计算总和，然后在一次遍历中通过维护左侧和来判断中心下标。

3. 全量伪代码：
   - 前缀和法：
     ```
     初始化前缀和数组 curr，长度为 len(nums) + 1，初始值为 0
     对于每个索引 i 从 0 到 len(nums) - 1：
         计算 curr[i+1] 为 curr[i] 加上 nums[i]
     对于每个索引 j 从 0 到 len(nums) - 1：
         计算左侧和 left 为 curr[j]
         计算右侧和 right 为 curr[-1] 减去 curr[j+1]
         如果 left 等于 right：
             返回 j 作为中心下标
     返回 -1 表示没有找到中心下标
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是数组的长度，因为需要遍历数组两次。
   - 空间复杂度：$O(n)$，用于存储前缀和数组。