# 1. 两数之和

**难度**: Easy | **标签**: `Array` `Hash Table`

**归类**: 8. 常用数据结构 > Array

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

1. 一句话直击本质：通过双重循环遍历数组，寻找两个数的和等于目标值。

2. 综合思路：
   - 暴力解法：使用双重循环遍历数组，检查每一对数的和是否等于目标值。
   - 哈希表解法（未在提供的代码中出现）：使用哈希表记录已访问的数及其索引，检查当前数与目标值的差是否在哈希表中。

3. 全量伪代码：
   - 暴力解法伪代码：
     ```
     定义函数 twoSum(数组 nums, 整数 target):
         对于 i 从 0 到 len(nums) - 2:
             对于 j 从 i + 1 到 len(nums) - 1:
                 如果 nums[i] + nums[j] 等于 target:
                     返回 [i, j]
     ```
   - 哈希表解法伪代码（未在代码集中出现，但常见于该问题的解法）：
     ```
     定义函数 twoSum(数组 nums, 整数 target):
         创建一个空的哈希表 hash_map
         对于 i 从 0 到 len(nums) - 1:
             计算差值 complement = target - nums[i]
             如果 complement 在 hash_map 中:
                 返回 [hash_map[complement], i]
             否则:
                 将 nums[i] 和 i 存入 hash_map
     ```

4. 复杂度：
   - 暴力解法时间复杂度：$O(n^2)$，空间复杂度：$O(1)$。
   - 哈希表解法时间复杂度：$O(n)$，空间复杂度：$O(n)$。