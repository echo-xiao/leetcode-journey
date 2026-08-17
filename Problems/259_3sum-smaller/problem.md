# 259. 较小的三数之和 · 题目

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
