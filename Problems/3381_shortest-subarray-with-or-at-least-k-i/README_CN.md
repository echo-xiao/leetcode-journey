# 3381. 或值至少 K 的最短子数组 I

**难度**: Easy | **标签**: `Array` `Bit Manipulation` `Sliding Window`

## 题目描述

<p>给你一个 <strong>非负</strong>&nbsp;整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。</p>

<p>如果一个数组中所有元素的按位或运算 <code>OR</code>&nbsp;的值 <strong>至少</strong>&nbsp;为 <code>k</code>&nbsp;，那么我们称这个数组是 <strong>特别的</strong>&nbsp;。</p>

<p>请你返回&nbsp;<code>nums</code>&nbsp;中&nbsp;<strong>最短特别非空</strong>&nbsp;<span data-keyword="subarray-nonempty">子数组</span>的长度，如果特别子数组不存在，那么返回 <code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,3], k = 2</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>

<p><strong>解释：</strong></p>

<p>子数组&nbsp;<code>[3]</code>&nbsp;的按位&nbsp;<code>OR</code> 值为&nbsp;<code>3</code>&nbsp;，所以我们返回 <code>1</code>&nbsp;。</p>

<p>注意，<code>[2]</code> 也是一个特别子数组。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [2,1,8], k = 10</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><strong>解释：</strong></p>

<p>子数组&nbsp;<code>[2,1,8]</code> 的按位&nbsp;<code>OR</code>&nbsp;值为 <code>11</code>&nbsp;，所以我们返回 <code>3</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2], k = 0</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>

<p><b>解释：</b></p>

<p>子数组&nbsp;<code>[1]</code>&nbsp;的按位&nbsp;<code>OR</code>&nbsp;值为&nbsp;<code>1</code>&nbsp;，所以我们返回&nbsp;<code>1</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 50</code></li>
	<li><code>0 &lt;= k &lt; 64</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：利用滑动窗口或双重循环，计算子数组的或值，寻找满足条件的最短子数组。

2. 综合思路：
   - **双重循环**：版本 1、3 和 4 使用双重循环遍历所有可能的子数组，计算其或值，并在满足条件时更新最短长度。
   - **滑动窗口**：版本 2 使用滑动窗口和位计数数组优化计算过程，通过调整窗口来动态维护或值，减少不必要的计算。

3. 全量伪代码：
   - **双重循环方法**：
     ```
     初始化最小长度为无穷大
     对于每个起始位置 l 从 0 到数组长度：
         初始化当前或值为 0
         对于每个结束位置 r 从 l 到数组长度：
             更新当前或值为或上 nums[r]
             如果当前或值大于等于 k：
                 更新最小长度为当前子数组长度
                 跳出内层循环
     如果最小长度仍为无穷大，返回 -1，否则返回最小长度
     ```
   - **滑动窗口方法**：
     ```
     初始化最小长度为无穷大
     初始化位计数数组为 0
     对于每个结束位置 r 从 0 到数组长度：
         更新位计数数组
         计算当前窗口的或值
         当当前或值大于等于 k 且 l <= r：
             更新最小长度为当前窗口长度
             更新位计数数组以移除 nums[l] 的影响
             计算新的或值
             增加 l
     如果最小长度仍为无穷大，返回 -1，否则返回最小长度
     ```

4. 复杂度：
   - **双重循环方法**：时间复杂度为 $O(n^2)$，空间复杂度为 $O(1)$。
   - **滑动窗口方法**：时间复杂度为 $O(n \cdot m)$，其中 $m$ 是整数的位数（通常为常数 32），空间复杂度为 $O(m)$。