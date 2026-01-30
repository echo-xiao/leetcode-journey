# 2714. 左右元素和的差值

**难度**: Easy | **标签**: `Array` `Prefix Sum`

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的长度为&nbsp;<code>n</code>&nbsp;的整数数组 <code>nums</code>。</p>

<p>定义两个数组&nbsp;<code>leftSum</code>&nbsp;和&nbsp;<code>rightSum</code>，其中：</p>

<ul>
	<li><code>leftSum[i]</code> 是数组 <code>nums</code> 中下标 <code>i</code> 左侧元素之和。如果不存在对应的元素，<code>leftSum[i] = 0</code> 。</li>
	<li><code>rightSum[i]</code> 是数组 <code>nums</code> 中下标 <code>i</code> 右侧元素之和。如果不存在对应的元素，<code>rightSum[i] = 0</code> 。</li>
</ul>

<p>返回长度为&nbsp;<code>n</code> 数组 <code>answer</code>，其中 <code>answer[i] = |leftSum[i] - rightSum[i]|</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [10,4,8,3]
<strong>输出：</strong>[15,1,11,22]
<strong>解释：</strong>数组 leftSum 为 [0,10,14,22] 且数组 rightSum 为 [15,11,3,0] 。
数组 answer 为 [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1]
<strong>输出：</strong>[0]
<strong>解释：</strong>数组 leftSum 为 [0] 且数组 rightSum 为 [0] 。
数组 answer 为 [|0 - 0|] = [0] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过前缀和与后缀和分别计算每个元素左侧和右侧的和，然后求其绝对差值。

2. 综合思路：
   - 前缀和与后缀和：使用两个数组分别存储每个元素左侧的和与右侧的和，然后计算差值。
   - 迭代法：通过遍历数组两次，第一次计算前缀和，第二次计算后缀和，最后计算差值。

3. 全量伪代码：
   ```
   输入：nums 数组
   初始化：n 为 nums 的长度
   初始化：left 数组长度为 n+1，所有元素为 0
   初始化：right 数组长度为 n+1，所有元素为 0

   # 计算前缀和
   对于 i 从 1 到 n-1:
       left[i] = left[i-1] + nums[i-1]
   截取 left 数组的前 n 个元素

   # 计算后缀和
   对于 i 从 n-1 到 0:
       right[i] = right[i+1] + nums[i]
   截取 right 数组的从第 1 个元素开始的所有元素

   初始化：res 为空列表
   对于 i 从 0 到 n-1:
       计算 left[i] 和 right[i] 的绝对差值，并添加到 res 中

   返回 res
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，因为需要遍历数组三次。
   - 空间复杂度：$O(n)$，因为使用了两个额外的数组来存储前缀和与后缀和。