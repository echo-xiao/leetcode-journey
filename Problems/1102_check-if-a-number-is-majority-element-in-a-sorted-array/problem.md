# 1102. 检查一个数是否在数组中占绝大多数 · 题目

**难度**: Easy | **标签**: `Array` `Binary Search`

## 题目描述

<p>给定一个按非递减顺序排序的整数数组 <code>nums</code> 和一个整数 <code>target</code>，如果 <code>target</code> 是一个 <strong>多数</strong> 元素，则返回 <code>true</code>，否则返回 <code>false</code>。</p>

<p>数组 <code>nums</code> 中的 <strong>多数</strong> 元素是指在数组中出现次数超过 <code>nums.length / 2</code> 的元素。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [2,4,5,5,5,5,5,6,6], target = 5
<strong>输出:</strong> true
<strong>解释:</strong> 值 5 出现了 5 次，数组的长度为 9。
因此，5 是一个多数元素，因为 5 &gt; 9/2 为真。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [10,100,101,101], target = 101
<strong>输出:</strong> false
<strong>解释:</strong> 值 101 出现了 2 次，数组的长度为 4。
因此，101 不是一个多数元素，因为 2 &gt; 4/2 为假。
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i], target &lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code> 是按非递减顺序排序的。</li>
</ul>
