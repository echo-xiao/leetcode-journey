# 162. 寻找峰值

**难度**: Medium | **标签**: `Array` `Binary Search`

## 题目描述

<p>峰值元素是指其值严格大于左右相邻值的元素。</p>

<p>给你一个整数数组&nbsp;<code>nums</code>，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 <strong>任何一个峰值</strong> 所在位置即可。</p>

<p>你可以假设&nbsp;<code>nums[-1] = nums[n] = -∞</code> 。</p>

<p>你必须实现时间复杂度为 <code>O(log n)</code><em> </em>的算法来解决此问题。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = <code>[1,2,3,1]</code>
<strong>输出：</strong>2
<strong>解释：</strong>3 是峰值元素，你的函数应该返回其索引 2。</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>nums = <code>[</code>1,2,1,3,5,6,4]
<strong>输出：</strong>1 或 5 
<strong>解释：</strong>你的函数可以返回索引 1，其峰值元素为 2；
&nbsp;    或者返回索引 5， 其峰值元素为 6。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li>对于所有有效的 <code>i</code> 都有 <code>nums[i] != nums[i + 1]</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是利用二分查找法，通过比较中点与其右邻元素的大小，逐步缩小搜索区间，最终找到一个峰值元素。

2. 综合思路：
   - 二分查找法：两种实现版本都采用了二分查找的思路，通过比较中点与其右邻元素的大小，决定是向左还是向右缩小搜索区间，直到找到一个峰值。
   - 递归与迭代：虽然题目中提供的代码都是迭代实现，但二分查找也可以用递归方式实现。
   - 不同数据结构：该问题主要处理数组，不涉及其他复杂数据结构。

3. 全量伪代码：
   ```plaintext
   初始化 left 为 0，right 为数组长度减 1
   当 left 小于 right 时，重复以下步骤：
       计算 mid 为 left 和 right 的中间索引
       如果 nums[mid] 大于等于 nums[mid+1]，则说明峰值在左侧或 mid 处，更新 right 为 mid
       否则，说明峰值在右侧，更新 left 为 mid + 1
   返回 left 作为峰值索引
   ```

4. 复杂度：
   - 时间复杂度：$O(\log n)$，因为每次迭代将搜索区间缩小一半。
   - 空间复杂度：$O(1)$，因为只使用了常数级别的额外空间。