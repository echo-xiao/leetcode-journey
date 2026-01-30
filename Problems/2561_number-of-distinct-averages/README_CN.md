# 2561. 不同的平均值数目

**难度**: Easy | **标签**: `Array` `Hash Table` `Two Pointers` `Sorting`

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始长度为 <strong>偶数</strong>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>只要&nbsp;<code>nums</code> <strong>不是</strong>&nbsp;空数组，你就重复执行以下步骤：</p>

<ul>
	<li>找到&nbsp;<code>nums</code>&nbsp;中的最小值，并删除它。</li>
	<li>找到&nbsp;<code>nums</code>&nbsp;中的最大值，并删除它。</li>
	<li>计算删除两数的平均值。</li>
</ul>

<p>两数 <code>a</code>&nbsp;和 <code>b</code>&nbsp;的 <strong>平均值</strong>&nbsp;为&nbsp;<code>(a + b) / 2</code>&nbsp;。</p>

<ul>
	<li>比方说，<code>2</code>&nbsp;和&nbsp;<code>3</code>&nbsp;的平均值是&nbsp;<code>(2 + 3) / 2 = 2.5</code>&nbsp;。</li>
</ul>

<p>返回上述过程能得到的 <strong>不同</strong>&nbsp;平均值的数目。</p>

<p><strong>注意</strong>&nbsp;，如果最小值或者最大值有重复元素，可以删除任意一个。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [4,1,4,0,3,5]
<b>输出：</b>2
<strong>解释：</strong>
1. 删除 0 和 5 ，平均值是 (0 + 5) / 2 = 2.5 ，现在 nums = [4,1,4,3] 。
2. 删除 1 和 4 ，平均值是 (1 + 4) / 2 = 2.5 ，现在 nums = [4,3] 。
3. 删除 3 和 4 ，平均值是 (3 + 4) / 2 = 3.5 。
2.5 ，2.5 和 3.5 之中总共有 2 个不同的数，我们返回 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [1,100]
<b>输出：</b>1
<strong>解释：</strong>
删除 1 和 100 后只有一个平均值，所以我们返回 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>nums.length</code>&nbsp;是偶数。</li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过排序和双指针方法计算数组中不同的平均值数目。

2. 综合思路：
   - 排序与双指针：首先对数组进行排序，然后使用双指针分别从数组的两端向中间移动，计算每对元素的平均值，并将其存入集合中以确保唯一性，最后返回集合的大小。

3. 全量伪代码：
   ```
   定义函数 distinctAverages(nums):
       对 nums 进行排序
       初始化一个空集合 my_set
       初始化指针 i 为 0，指针 j 为 nums 的最后一个索引
       当 i 小于 j 时:
           取 nums[i] 为 min_num
           取 nums[j] 为 max_num
           计算 min_num 和 max_num 的平均值 avg_num
           将 avg_num 添加到 my_set 中
           将 i 增加 1
           将 j 减少 1
       返回 my_set 的大小
   ```

4. 复杂度：
   - 时间复杂度：$O(n \log n)$，其中 $n$ 是数组的长度，因为排序操作是最耗时的部分。
   - 空间复杂度：$O(n)$，用于存储集合中的平均值。