# 444. 序列重建 · 题目

**难度**: Medium | **标签**: `Array` `Graph Theory` `Topological Sort`

## 题目描述

<p>给定一个长度为 <code>n</code> 的整数数组 <code>nums</code>，其中 <code>nums</code> 是范围 <code>[1, n]</code> 内整数的一个排列。还给定一个二维整数数组 <code>sequences</code>，其中 <code>sequences[i]</code> 是 <code>nums</code> 的一个子序列。</p>

<p>检查 <code>nums</code> 是否是唯一的最短 <strong>超序列</strong>。最短的 <strong>超序列</strong> 是一个 <strong>长度最短</strong> 的序列，并且包含所有 <code>sequences[i]</code> 作为子序列。对于给定的数组 <code>sequences</code>，可能存在多个有效的 <strong>超序列</strong>。</p>

<ul>
	<li>例如，对于 <code>sequences = [[1,2],[1,3]]</code>，存在两个最短的 <strong>超序列</strong>，<code>[1,2,3]</code> 和 <code>[1,3,2]</code>。</li>
	<li>而对于 <code>sequences = [[1,2],[1,3],[1,2,3]]</code>，唯一的最短 <strong>超序列</strong> 是 <code>[1,2,3]</code>。<code>[1,2,3,4]</code> 是一个可能的超序列，但不是最短的。</li>
</ul>

<p>如果 <code>nums</code> 是 <code>sequences</code> 的唯一最短 <strong>超序列</strong>，则返回 <code>true</code><em>，否则返回 </em><code>false</code>.</p>

<p>一个 <strong>子序列</strong> 是一个可以通过删除某些或不删除任何元素而不改变剩余元素顺序从另一个序列中派生出的序列。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,2,3], sequences = [[1,2],[1,3]]
<strong>输出:</strong> false
<strong>解释:</strong> 存在两个可能的超序列: [1,2,3] 和 [1,3,2]。
序列 [1,2] 是两个序列的子序列: [<strong><u>1</u></strong>,<strong><u>2</u></strong>,3] 和 [<strong><u>1</u></strong>,3,<strong><u>2</u></strong>]。
序列 [1,3] 是两个序列的子序列: [<strong><u>1</u></strong>,2,<strong><u>3</u></strong>] 和 [<strong><u>1</u></strong>,<strong><u>3</u></strong>,2]。
由于 nums 不是唯一的最短超序列，因此返回 false。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,2,3], sequences = [[1,2]]
<strong>输出:</strong> false
<strong>解释:</strong> 最短的超序列是 [1,2]。
序列 [1,2] 是它的子序列: [<strong><u>1</u></strong>,<strong><u>2</u></strong>]。
由于 nums 不是最短超序列，因此返回 false。
</pre>

<p><strong class="example">示例 3:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]
<strong>输出:</strong> true
<strong>解释:</strong> 最短的超序列是 [1,2,3]。
序列 [1,2] 是它的子序列: [<strong><u>1</u></strong>,<strong><u>2</u></strong>,3]。
序列 [1,3] 是它的子序列: [<strong><u>1</u></strong>,2,<strong><u>3</u></strong>]。
序列 [2,3] 是它的子序列: [1,<strong><u>2</u></strong>,<strong><u>3</u></strong>]。
由于 nums 是唯一的最短超序列，因此返回 true。
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> 是范围 <code>[1, n]</code> 内所有整数的一个排列。</li>
	<li><code>1 &lt;= sequences.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= sequences[i].length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= sum(sequences[i].length) &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= sequences[i][j] &lt;= n</code></li>
	<li>所有的 <code>sequences</code> 数组都是 <strong>唯一</strong> 的。</li>
	<li><code>sequences[i]</code> 是 <code>nums</code> 的一个子序列。</li>
</ul>
