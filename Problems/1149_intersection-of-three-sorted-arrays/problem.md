# 1149. 三个有序数组的交集 · 题目

**难度**: Easy | **标签**: `Array` `Hash Table` `Binary Search` `Counting`

## 题目描述

<p>给定三个整数数组 <code>arr1</code>、<code>arr2</code> 和 <code>arr3</code>&nbsp;<strong>按严格递增</strong> 的顺序排序，返回一个<strong>仅包含</strong>&nbsp;在<strong>所有</strong>三个数组中出现的整数的排序数组。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
<strong>输出:</strong> [1,5]
<strong>解释: </strong>只有 1 和 5 出现在三个数组中。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]
<strong>输出:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>1 &lt;= arr1.length, arr2.length, arr3.length &lt;= 1000</code></li>
	<li><code>1 &lt;= arr1[i], arr2[i], arr3[i] &lt;= 2000</code></li>
</ul>
