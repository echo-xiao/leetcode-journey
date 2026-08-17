# 1083. 小于 K 的两数之和 · 题目

**难度**: Easy | **标签**: `Array` `Two Pointers` `Binary Search` `Sorting`

## 题目描述

<p>给定一个整数数组 <code>nums</code> 和一个整数 <code>k</code>，返回最大 <code>sum</code>，使得存在 <code>i &lt; j</code> 使得 <code>nums[i] + nums[j] = sum</code> 且 <code>sum &lt; k</code>。如果不存在满足该条件的 <code>i</code> 和 <code>j</code>，则返回 <code>-1</code>。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [34,23,1,24,75,33,54,8], k = 60
<strong>输出:</strong> 58
<strong>解释: </strong>我们可以使用 34 和 24 来得到 58，且小于 60。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [10,20,30], k = 15
<strong>输出:</strong> -1
<strong>解释: </strong>在这种情况下，不可能得到小于 15 的配对和。
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= 2000</code></li>
</ul>
