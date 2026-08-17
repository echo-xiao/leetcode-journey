# 1847. 长度为 K 的最大子数组 · 题目

**难度**: Easy | **标签**: `Array` `Greedy`

## 题目描述

<p>如果数组 <code>A</code> 在某个数组 <code>B</code> 中更大，则在第一个索引 <code>i</code> 处满足 <code>A[i] != B[i]</code> 时，<code>A[i] &gt; B[i]</code>。</p>

<p>例如，考虑 <code>0</code> 索引：</p>

<ul>
	<li><code>[1,3,2,4] &gt; [1,2,2,4]</code>，因为在索引 <code>1</code> 处，<code>3 &gt; 2</code>。</li>
	<li><code>[1,4,4,4] &lt; [2,1,1,1]</code>，因为在索引 <code>0</code> 处，<code>1 &lt; 2</code>。</li>
</ul>

<p>子数组是数组的一个连续子序列。</p>

<p>给定一个包含<strong>不同</strong>整数的整数数组 <code>nums</code>，返回长度为 <code>k</code> 的 <strong>最大</strong> 子数组。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,4,5,2,3], k = 3
<strong>输出:</strong> [5,2,3]
<strong>解释:</strong> 大小为 3 的子数组有: [1,4,5], [4,5,2], 和 [5,2,3]。
其中，[5,2,3] 是最大的。</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,4,5,2,3], k = 4
<strong>输出:</strong> [4,5,2,3]
<strong>解释:</strong> 大小为 4 的子数组有: [1,4,5,2], 和 [4,5,2,3]。
其中，[4,5,2,3] 是最大的。</pre>

<p><strong class="example">示例 3:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,4,5,2,3], k = 1
<strong>输出:</strong> [5]
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li>所有 <code>nums</code> 的整数都是<strong>唯一</strong>的。</li>
</ul>

<p>&nbsp;</p>
<strong>后续问题:</strong> 如果 <code>nums</code> 中的整数不是不同的呢？</strong>
