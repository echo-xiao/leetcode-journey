# 2524. 与对应负数同时存在的最大正整数

**难度**: Easy | **标签**: `Array` `Hash Table` `Two Pointers` `Sorting`

## 题目描述

<p>给你一个 <strong>不包含</strong> 任何零的整数数组 <code>nums</code> ，找出自身与对应的负数都在数组中存在的最大正整数 <code>k</code> 。</p>

<p>返回正整数<em> </em><code>k</code> ，如果不存在这样的整数，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1,2,-3,3]
<strong>输出：</strong>3
<strong>解释：</strong>3 是数组中唯一一个满足题目要求的 k 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1,10,6,7,-7,1]
<strong>输出：</strong>7
<strong>解释：</strong>数组中存在 1 和 7 对应的负数，7 的值更大。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [-10,8,6,7,-2,-3]
<strong>输出：</strong>-1
<strong>解释：</strong>不存在满足题目要求的 k ，返回 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>nums[i] != 0</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：利用集合存储负数的相反数，通过遍历找到同时存在的最大正整数。

2. 综合思路：
   - 使用集合：将所有数的相反数存入集合中，然后遍历数组，检查每个数是否在集合中存在，更新最大值。
   - 其他可能的解法（未在代码集中出现）：可以使用排序和双指针的方法，先对数组排序，然后使用双指针从两端向中间查找。

3. 全量伪代码：
   ```plaintext
   函数 findMaxK(输入数组 nums):
       创建一个空集合 my_set
       初始化 max_num 为 -1

       对于 nums 中的每个元素 num:
           将 -num 添加到 my_set 中

       对于 nums 中的每个元素 num:
           如果 num 存在于 my_set 中:
               更新 max_num 为 num 和 max_num 中的较大值

       返回 max_num
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是数组的长度，因为我们需要遍历数组两次。
   - 空间复杂度：$O(n)$，因为我们使用了一个集合来存储数组元素的相反数。