# 153. 寻找旋转排序数组中的最小值

**难度**: Medium | **标签**: `Array` `Binary Search`

## 题目描述

已知一个长度为 <code>n</code> 的数组，预先按照升序排列，经由 <code>1</code> 到 <code>n</code> 次 <strong>旋转</strong> 后，得到输入数组。例如，原数组 <code>nums = [0,1,2,4,5,6,7]</code> 在变化后可能得到：
<ul>
	<li>若旋转 <code>4</code> 次，则可以得到 <code>[4,5,6,7,0,1,2]</code></li>
	<li>若旋转 <code>7</code> 次，则可以得到 <code>[0,1,2,4,5,6,7]</code></li>
</ul>

<p>注意，数组 <code>[a[0], a[1], a[2], ..., a[n-1]]</code> <strong>旋转一次</strong> 的结果为数组 <code>[a[n-1], a[0], a[1], a[2], ..., a[n-2]]</code> 。</p>

<p>给你一个元素值 <strong>互不相同</strong> 的数组 <code>nums</code> ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 <strong>最小元素</strong> 。</p>

<p>你必须设计一个时间复杂度为&nbsp;<code>O(log n)</code> 的算法解决此问题。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,4,5,1,2]
<strong>输出：</strong>1
<strong>解释：</strong>原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,5,6,7,0,1,2]
<strong>输出：</strong>0
<strong>解释：</strong>原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [11,13,15,17]
<strong>输出：</strong>11
<strong>解释：</strong>原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
	<li><code>-5000 &lt;= nums[i] &lt;= 5000</code></li>
	<li><code>nums</code> 中的所有整数 <strong>互不相同</strong></li>
	<li><code>nums</code> 原来是一个升序排序的数组，并进行了 <code>1</code> 至 <code>n</code> 次旋转</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：利用二分查找，通过比较中间元素与边界元素的大小关系，逐步缩小搜索范围，找到旋转排序数组中的最小值。

2. 综合思路：
   - 二分查找法：所有版本都使用了二分查找的思想，通过比较中间元素与边界元素的大小，判断最小值所在的区间。
   - 处理重复元素：部分版本（如版本1）考虑了数组中可能存在重复元素的情况，通过调整边界来处理。

3. 全量伪代码：
   ```plaintext
   初始化 left 为 0，right 为数组长度减 1
   当 left 小于等于 right 时：
       计算 mid 为 left 和 right 的中间索引
       如果 nums[mid] 小于 nums[right]：
           right 更新为 mid
       否则如果 nums[mid] 大于 nums[right]：
           left 更新为 mid + 1
       否则：
           如果考虑重复元素的情况，right 减 1
           否则直接返回 nums[mid]
   返回 nums[left] 作为最小值
   ```

4. 复杂度：
   - 时间复杂度：$O(\log n)$，因为每次操作都将搜索范围缩小一半。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外变量。