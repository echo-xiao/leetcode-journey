# 259. 较小的三数之和

**难度**: Medium | **标签**: `Array` `Two Pointers` `Binary Search` `Sorting`

## 题目描述

<p>给定一个包含 <code>n</code> 个整数的数组 <code>nums</code> 和一个整数 <code>target</code>，找到满足条件 <code>nums[i] + nums[j] + nums[k] &lt; target</code> 的索引三元组 <code>i</code>，<code>j</code>，<code>k</code>，使得 <code>0 &lt;= i &lt; j &lt; k &lt; n</code>。</p>
<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [-2,0,1,3], target = 2
<strong>输出:</strong> 2
<strong>解释:</strong> 因为有两个三元组的和小于 2:
[-2,0,1]
[-2,0,3]
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [], target = 0
<strong>输出:</strong> 0
</pre>

<p><strong class="example">示例 3:</strong></p>

<pre>
<strong>输入:</strong> nums = [0], target = 0
<strong>输出:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>0 &lt;= n &lt;= 3500</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>-100 &lt;= target &lt;= 100</code></li>
	<li>输入生成的结果保证小于或等于 10<sup>9</sup>。</li>
</ul>

---
## 解题思路与复盘

1. 一句话直击本质：通过排序和双指针技术，遍历数组并计算满足条件的三元组数量。

2. 综合思路：
   - 排序 + 双指针：首先对数组进行排序，然后固定一个数，使用双指针在剩余数组中寻找满足条件的两数之和。

3. 全量伪代码：
   ```
   函数 threeSumSmaller(数组 nums, 整数 target):
       对 nums 进行排序
       初始化计数器 res 为 0
       对于 i 从 0 到 len(nums) - 2:
           计算 targetSum = target - nums[i]
           初始化双指针 j = i + 1, k = len(nums) - 1
           当 j < k 时:
               如果 nums[j] + nums[k] >= targetSum:
                   将 k 左移一位
               否则:
                   将 res 增加 (k - j)
                   将 j 右移一位
       返回 res
   ```

4. 复杂度：
   - 时间复杂度：$O(n^2)$，其中 $n$ 是数组的长度，因为排序需要 $O(n \log n)$，而双指针遍历需要 $O(n^2)$。
   - 空间复杂度：$O(1)$，因为除了输入和输出外，算法只使用了常数空间。