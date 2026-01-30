# 413. 等差数列划分

**难度**: Medium | **标签**: `Array` `Dynamic Programming` `Sliding Window`

## 题目描述

<p>如果一个数列 <strong>至少有三个元素</strong> ，并且任意两个相邻元素之差相同，则称该数列为等差数列。</p>

<ul>
	<li>例如，<code>[1,3,5,7,9]</code>、<code>[7,7,7,7]</code> 和 <code>[3,-1,-5,-9]</code> 都是等差数列。</li>
</ul>

<div class="original__bRMd">
<div>
<p>给你一个整数数组 <code>nums</code> ，返回数组 <code>nums</code> 中所有为等差数组的 <strong>子数组</strong> 个数。</p>

<p><strong>子数组</strong> 是数组中的一个连续序列。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>3
<strong>解释：</strong>nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1]
<strong>输出：</strong>0
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 5000</code></li>
	<li><code>-1000 <= nums[i] <= 1000</code></li>
</ul>
</div>
</div>


---
## 解题思路与复盘

1. 一句话直击本质：通过滑动窗口维护一个子数组，检查其是否为等差数列，并在满足条件时累加结果。

2. 综合思路：
   - 滑动窗口：通过两个指针（left 和 right）来维护一个动态窗口，检查窗口内的子数组是否为等差数列，并在满足条件时更新结果。
   - 递归/迭代：虽然当前代码没有递归实现，但可以通过递归来检查每个子数组是否为等差数列。
   - 动态规划：另一种常见解法是使用动态规划，记录以每个元素结尾的等差数列的数量。

3. 全量伪代码：
   - 滑动窗口：
     ```
     初始化窗口指针 left 和 right 为 0
     初始化结果计数器 ttl 为 0
     初始化临时数组 res 为空
     当 right 小于数组长度时：
         将 nums[right] 加入 res
         增加 right
         当 res 长度大于等于 3 且不是等差数列时：
             删除 res 的第一个元素
             增加 left
         如果 res 长度大于等于 3：
             将 res 的长度减去 2 加到 ttl
     返回 ttl
     ```
   - 检查等差数列：
     ```
     函数 calcDiff(nums):
         初始化标志 tag 为 True
         计算初始差 diff 为 nums[1] - nums[0]
         对于 i 从 0 到 len(nums) - 2：
             如果 nums[i+1] - nums[i] 不等于 diff：
                 设置 tag 为 False
                 跳出循环
         返回 tag
     ```

4. 复杂度：
   - 时间复杂度：$O(n^2)$，因为在最坏情况下，内层循环会遍历整个窗口。
   - 空间复杂度：$O(n)$，用于存储滑动窗口内的元素。