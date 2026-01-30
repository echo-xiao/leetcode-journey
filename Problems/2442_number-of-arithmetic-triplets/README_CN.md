# 2442. 等差三元组的数目

**难度**: Easy | **标签**: `Array` `Hash Table` `Two Pointers` `Enumeration`

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、<strong>严格递增</strong> 的整数数组 <code>nums</code> 和一个正整数 <code>diff</code> 。如果满足下述全部条件，则三元组 <code>(i, j, k)</code> 就是一个 <strong>等差三元组</strong> ：</p>

<ul>
	<li><code>i &lt; j &lt; k</code> ，</li>
	<li><code>nums[j] - nums[i] == diff</code> 且</li>
	<li><code>nums[k] - nums[j] == diff</code></li>
</ul>

<p>返回不同 <strong>等差三元组</strong> 的数目<em>。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1,4,6,7,10], diff = 3
<strong>输出：</strong>2
<strong>解释：</strong>
(1, 2, 4) 是等差三元组：7 - 4 == 3 且 4 - 1 == 3 。
(2, 4, 5) 是等差三元组：10 - 7 == 3 且 7 - 4 == 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,5,6,7,8,9], diff = 2
<strong>输出：</strong>2
<strong>解释：</strong>
(0, 2, 4) 是等差三元组：8 - 6 == 2 且 6 - 4 == 2 。
(1, 3, 5) 是等差三元组：9 - 7 == 2 且 7 - 5 == 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 200</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 200</code></li>
	<li><code>1 &lt;= diff &lt;= 50</code></li>
	<li><code>nums</code> <strong>严格</strong> 递增</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：所有算法的核心逻辑都是通过遍历数组寻找满足条件的等差三元组。

2. 综合思路：
   - **版本 1** 使用集合来快速判断某个数是否存在，通过两次遍历数组来寻找等差三元组。
   - **版本 2** 采用双指针法，通过三个指针分别指向三元组的三个元素，逐步寻找满足条件的组合。
   - **版本 3** 使用三重循环暴力枚举所有可能的三元组组合，检查是否满足等差条件。

3. 全量伪代码：
   - **版本 1 伪代码**：
     ```
     初始化一个空集合 my_set 和计数器 cnt
     遍历数组 nums，将每个元素加入 my_set
     再次遍历数组 nums，对于每个元素 a，计算 b = a + diff 和 c = a + 2 * diff
     如果 a, b, c 都在 my_set 中，计数器 cnt 增加 1
     返回 cnt
     ```
   - **版本 2 伪代码**：
     ```
     初始化变量 n 为数组长度，j 和 k 为指针，cnt 为计数器
     遍历数组 nums，i 从 0 到 n-2
       将 j 更新为 i+1 或 j 中的较大值
       移动 j 直到 nums[j] >= nums[i] + diff
       如果 j 超出范围或 nums[j] > nums[i] + diff，继续下一次循环
       将 k 更新为 j+1 或 k 中的较大值
       移动 k 直到 nums[k] >= nums[i] + 2 * diff
       如果 k 超出范围，退出循环
       如果 nums[k] == nums[j] + diff，计数器 cnt 增加 1
     返回 cnt
     ```
   - **版本 3 伪代码**：
     ```
     初始化计数器 res
     三重循环遍历数组 nums，i 从 0 到 n-3，j 从 i+1 到 n-2，k 从 j+1 到 n-1
       如果 nums[j] - nums[i] == diff 且 nums[k] - nums[j] == diff
         计数器 res 增加 1
     返回 res
     ```

4. 复杂度：
   - **版本 1** 时间复杂度为 $O(n)$，空间复杂度为 $O(n)$，因为使用了集合来存储数组元素。
   - **版本 2** 时间复杂度为 $O(n)$，空间复杂度为 $O(1)$，因为使用了双指针法。
   - **版本 3** 时间复杂度为 $O(n^3)$，空间复杂度为 $O(1)$，因为使用了三重循环暴力枚举。