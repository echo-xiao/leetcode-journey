# 487. 最大连续1的个数 II · 题目

**难度**: Medium | **标签**: `Array` `Dynamic Programming` `Sliding Window`

## 题目描述

<p>给定一个二进制数组 <code>nums</code>，如果你最多可以翻转一个 <code>0</code>，则返回 <em>数组中连续 <code>1</code> 的最大数量</em>。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,0,1,1,0]
<strong>输出:</strong> 4
<strong>解释:</strong> 
- 如果我们翻转第一个零，nums 变为 [1,1,1,1,0]，我们有 4 个连续的 1。
- 如果我们翻转第二个零，nums 变为 [1,0,1,1,1]，我们有 3 个连续的 1。
连续 1 的最大数量是 4。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,0,1,1,0,1]
<strong>输出:</strong> 4
<strong>解释:</strong> 
- 如果我们翻转第一个零，nums 变为 [1,1,1,1,0,1]，我们有 4 个连续的 1。
- 如果我们翻转第二个零，nums 变为 [1,0,1,1,1,1]，我们有 4 个连续的 1。
连续 1 的最大数量是 4。
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> 只能是 <code>0</code> 或 <code>1</code>。</li>
</ul>

<p>&nbsp;</p>
<p><strong>后续问题:</strong> 如果输入的数字是一个一个地以无限流的形式到达呢？换句话说，你不能存储所有来自流的数字，因为它们太大而无法在内存中保存。你能有效地解决这个问题吗？</p>
