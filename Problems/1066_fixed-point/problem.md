# 1066. 不动点 · 题目

**难度**: Easy | **标签**: `Array` `Binary Search`

## 题目描述

<p>给定一个由不同整数构成的数组 <code>arr</code>，其中 <code>arr</code> 是按<strong>升序</strong>排序的，返回满足 <code>arr[i] == i</code> 的最小索引 <code>i</code>。如果没有这样的索引，返回 <code>-1</code>。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> arr = [-10,-5,0,3,7]
<strong>输出:</strong> 3
<strong>解释:</strong> 对于给定的数组，<code>arr[0] = -10, arr[1] = -5, arr[2] = 0, arr[3] = 3</code>，因此输出为 3。</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> arr = [0,2,5,8,17]
<strong>输出:</strong> 0
<strong>解释:</strong> <code>arr[0] = 0</code>，因此输出为 0。</pre>

<p><strong class="example">示例 3:</strong></p>

<pre>
<strong>输入:</strong> arr = [-10,-5,3,4,7,9]
<strong>输出:</strong> -1
<strong>解释:</strong> 没有这样的 <code>i</code> 使得 <code>arr[i] == i</code>，因此输出为 -1。</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt; 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>后续问题:</strong> <code>O(n)</code> 的解法非常简单。我们能做得更好吗？
