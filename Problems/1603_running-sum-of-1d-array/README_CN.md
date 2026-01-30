# 1603. 一维数组的动态和

**难度**: Easy | **标签**: `Array` `Prefix Sum`

## 题目描述

<p>给你一个数组 <code>nums</code> 。数组「动态和」的计算公式为：<code>runningSum[i] = sum(nums[0]&hellip;nums[i])</code> 。</p>

<p>请返回 <code>nums</code> 的动态和。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>[1,3,6,10]
<strong>解释：</strong>动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,1,1,1,1]
<strong>输出：</strong>[1,2,3,4,5]
<strong>解释：</strong>动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [3,1,2,10,1]
<strong>输出：</strong>[3,4,6,16,17]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-10^6&nbsp;&lt;= nums[i] &lt;=&nbsp;10^6</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过累加前缀和的方式计算一维数组的动态和。

2. 综合思路：
   - 迭代法：使用一个额外的数组来存储累加的结果，通过遍历原数组逐步累加得到动态和。
   - 原地修改法（未在提供的代码中出现，但常见）：直接在原数组上进行累加修改，避免使用额外空间。

3. 全量伪代码：
   - 迭代法：
     ```
     定义函数 runningSum(nums):
         令 n 为 nums 的长度
         初始化 arr 为长度为 n+1 的数组，所有元素为 0
         对于 i 从 0 到 n-1:
             arr[i+1] = arr[i] + nums[i]
         返回 arr 从索引 1 开始的子数组
     ```
   - 原地修改法（假设存在）：
     ```
     定义函数 runningSum(nums):
         对于 i 从 1 到 len(nums)-1:
             nums[i] = nums[i] + nums[i-1]
         返回 nums
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，因为需要遍历整个数组一次。
   - 空间复杂度：$O(n)$，因为使用了一个额外的数组来存储结果。对于原地修改法，空间复杂度为 $O(1)$。