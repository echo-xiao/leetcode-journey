# 1468. 检查整数及其两倍数是否存在

**难度**: Easy | **标签**: `Array` `Hash Table` `Two Pointers` `Binary Search` `Sorting`

## 题目描述

<p>给你一个整数数组&nbsp;<code>arr</code>，请你检查是否存在两个整数&nbsp;<code>N</code> 和 <code>M</code>，满足&nbsp;<code>N</code>&nbsp;是&nbsp;<code>M</code>&nbsp;的两倍（即，<code>N = 2 * M</code>）。</p>

<p>更正式地，检查是否存在两个下标&nbsp;<code>i</code> 和 <code>j</code> 满足：</p>

<ul>
	<li><code>i != j</code></li>
	<li><code>0 &lt;= i, j &lt; arr.length</code></li>
	<li><code>arr[i] == 2 * arr[j]</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [10,2,5,3]
<strong>输出：</strong>true
<strong>解释：</strong>N<code> = 10</code> 是 M<code> = 5 的两倍</code>，即 <code>10 = 2 * 5 。</code>
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [7,1,14,11]
<strong>输出：</strong>true
<strong>解释：</strong>N<code> = 14</code> 是 M<code> = 7 的两倍</code>，即 <code>14 = 2 * 7 </code>。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [3,1,7,11]
<strong>输出：</strong>false
<strong>解释：</strong>在该情况下不存在 N 和 M 满足 N = 2 * M 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 500</code></li>
	<li><code>-10^3 &lt;= arr[i] &lt;= 10^3</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：利用哈希集合或双重循环检查数组中是否存在一个数是另一个数的两倍。

2. 综合思路：
   - 哈希集合法：遍历数组，使用哈希集合记录已访问的元素，检查当前元素的两倍或一半是否已存在于集合中。
   - 双重循环法：使用两层循环，逐对检查数组中的每一对元素，判断其中一个是否是另一个的两倍。

3. 全量伪代码：
   - 哈希集合法：
     ```
     初始化一个空集合 seen
     对于数组中的每个元素 num：
         如果 num 的两倍在 seen 中：
             返回 True
         如果 num 是偶数并且 num 的一半在 seen 中：
             返回 True
         将 num 添加到 seen 中
     返回 False
     ```
   - 双重循环法：
     ```
     对于数组中的每个元素 arr[i]：
         对于数组中的每个元素 arr[j]：
             如果 i 不等于 j 并且 arr[i] 是 arr[j] 的两倍：
                 返回 True
     返回 False
     ```

4. 复杂度：
   - 哈希集合法的时间复杂度为 $O(n)$，空间复杂度为 $O(n)$，其中 $n$ 是数组的长度。
   - 双重循环法的时间复杂度为 $O(n^2)$，空间复杂度为 $O(1)$。