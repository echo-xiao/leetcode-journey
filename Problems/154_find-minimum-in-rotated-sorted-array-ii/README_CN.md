# 154. 寻找旋转排序数组中的最小值 II

**难度**: Hard | **标签**: `Array` `Binary Search`

## 题目描述

已知一个长度为 <code>n</code> 的数组，预先按照升序排列，经由 <code>1</code> 到 <code>n</code> 次 <strong>旋转</strong> 后，得到输入数组。例如，原数组 <code>nums = [0,1,4,4,5,6,7]</code> 在变化后可能得到：
<ul>
	<li>若旋转 <code>4</code> 次，则可以得到 <code>[4,5,6,7,0,1,4]</code></li>
	<li>若旋转 <code>7</code> 次，则可以得到 <code>[0,1,4,4,5,6,7]</code></li>
</ul>

<p>注意，数组 <code>[a[0], a[1], a[2], ..., a[n-1]]</code> <strong>旋转一次</strong> 的结果为数组 <code>[a[n-1], a[0], a[1], a[2], ..., a[n-2]]</code> 。</p>

<p>给你一个可能存在 <strong>重复</strong> 元素值的数组 <code>nums</code> ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 <strong>最小元素</strong> 。</p>

<p>你必须尽可能减少整个过程的操作步骤。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,5]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,2,2,0,1]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
	<li><code>-5000 &lt;= nums[i] &lt;= 5000</code></li>
	<li><code>nums</code> 原来是一个升序排序的数组，并进行了 <code>1</code> 至 <code>n</code> 次旋转</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>这道题与 <a href="https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/description/">寻找旋转排序数组中的最小值</a> 类似，但 <code>nums</code> 可能包含重复元素。允许重复会影响算法的时间复杂度吗？会如何影响，为什么？</p>


---
## 解题思路与复盘

1. 一句话直击本质：使用二分查找法，通过比较中间元素与右端元素的大小关系，逐步缩小搜索范围，找到旋转排序数组中的最小值。

2. 综合思路：
   - **二分查找法**：所有版本都采用了二分查找的思想，通过比较中间元素与右端元素的大小关系来决定搜索范围的缩小方式。
   - **处理重复元素**：在处理重复元素时，采用了不同的策略，如直接缩小右边界或左边界。
   - **迭代法**：所有版本均使用迭代法实现，没有递归版本。

3. 全量伪代码：
   ```plaintext
   初始化 left 为 0，right 为数组长度减 1
   当 left 小于 right 时，重复以下步骤：
       计算 mid 为 left 和 right 的中间位置
       如果 nums[mid] 大于 nums[right]：
           最小值在 mid+1 到 right 之间，更新 left 为 mid + 1
       否则如果 nums[mid] 小于 nums[right]：
           最小值在 left 到 mid 之间，更新 right 为 mid
       否则：
           缩小搜索范围，right 减 1（或 left 加 1）
   返回 nums[left] 作为最小值
   ```

4. 复杂度：
   - 时间复杂度：所有版本的时间复杂度为 $O(\log n)$，但在最坏情况下（如存在大量重复元素），可能退化为 $O(n)$。
   - 空间复杂度：所有版本的空间复杂度为 $O(1)$，因为只使用了常数级别的额外空间。