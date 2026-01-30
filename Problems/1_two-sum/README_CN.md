# 1. 两数之和

**难度**: Easy | **标签**: `Array` `Hash Table`

## 题目描述

<p>给定一个整数数组 <code>nums</code>&nbsp;和一个整数目标值 <code>target</code>，请你在该数组中找出 <strong>和为目标值 </strong><em><code>target</code></em>&nbsp; 的那&nbsp;<strong>两个</strong>&nbsp;整数，并返回它们的数组下标。</p>

<p>你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。</p>

<p>你可以按任意顺序返回答案。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,7,11,15], target = 9
<strong>输出：</strong>[0,1]
<strong>解释：</strong>因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,4], target = 6
<strong>输出：</strong>[1,2]
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,3], target = 6
<strong>输出：</strong>[0,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>只会存在一个有效答案</strong></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你可以想出一个时间复杂度小于 <code>O(n<sup>2</sup>)</code> 的算法吗？</p>


---
## 解题思路与复盘

1. 一句话直击本质：通过遍历数组中的每一对元素，寻找其和等于目标值的两个索引。

2. 综合思路：
   - 暴力枚举：直接使用双重循环遍历数组中的每一对元素，检查其和是否等于目标值。这种方法简单直接，但效率较低。
   - 哈希表：使用哈希表存储数组中每个元素的值及其索引，在遍历数组时检查目标值与当前元素的差是否已存在于哈希表中，从而在一次遍历中找到结果。

3. 全量伪代码：
   - 暴力枚举：
     ```
     对于数组中的每一个元素 i:
         对于数组中从 i+1 开始的每一个元素 j:
             如果 nums[i] + nums[j] 等于目标值:
                 返回 [i, j]
     ```
   - 哈希表：
     ```
     创建一个空的哈希表
     对于数组中的每一个元素 i:
         计算差值 diff = 目标值 - nums[i]
         如果差值 diff 存在于哈希表中:
             返回 [哈希表中 diff 的索引, i]
         否则，将 nums[i] 和其索引存入哈希表
     ```

4. 复杂度：
   - 暴力枚举的时间复杂度为 $O(n^2)$，空间复杂度为 $O(1)$。
   - 使用哈希表的时间复杂度为 $O(n)$，空间复杂度为 $O(n)$。