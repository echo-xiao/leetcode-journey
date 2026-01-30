# 3555. K 次乘运算后的最终数组 I

**难度**: Easy | **标签**: `Array` `Math` `Heap (Priority Queue)` `Simulation`

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;，一个整数&nbsp;<code>k</code>&nbsp;&nbsp;和一个整数&nbsp;<code>multiplier</code>&nbsp;。</p>

<p>你需要对 <code>nums</code>&nbsp;执行 <code>k</code>&nbsp;次操作，每次操作中：</p>

<ul>
	<li>找到 <code>nums</code>&nbsp;中的 <strong>最小</strong>&nbsp;值&nbsp;<code>x</code>&nbsp;，如果存在多个最小值，选择最 <strong>前面</strong>&nbsp;的一个。</li>
	<li>将 <code>x</code>&nbsp;替换为&nbsp;<code>x * multiplier</code>&nbsp;。</li>
</ul>

<p>请你返回执行完 <code>k</code>&nbsp;次乘运算之后，最终的 <code>nums</code>&nbsp;数组。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [2,1,3,5,6], k = 5, multiplier = 2</span></p>

<p><span class="example-io"><b>输出：</b>[8,4,6,5,6]</span></p>

<p><strong>解释：</strong></p>

<table>
	<tbody>
		<tr>
			<th>操作</th>
			<th>结果</th>
		</tr>
		<tr>
			<td>1 次操作后</td>
			<td>[2, 2, 3, 5, 6]</td>
		</tr>
		<tr>
			<td>2 次操作后</td>
			<td>[4, 2, 3, 5, 6]</td>
		</tr>
		<tr>
			<td>3 次操作后</td>
			<td>[4, 4, 3, 5, 6]</td>
		</tr>
		<tr>
			<td>4 次操作后</td>
			<td>[4, 4, 6, 5, 6]</td>
		</tr>
		<tr>
			<td>5 次操作后</td>
			<td>[8, 4, 6, 5, 6]</td>
		</tr>
	</tbody>
</table>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span>nums = [1,2], k = 3, multiplier = 4</p>

<p><span class="example-io"><b>输出：</b></span>[16,8]</p>

<p><strong>解释：</strong></p>

<table>
	<tbody>
		<tr>
			<th>操作</th>
			<th>结果</th>
		</tr>
		<tr>
			<td>1 次操作后</td>
			<td>[4, 2]</td>
		</tr>
		<tr>
			<td>2 次操作后</td>
			<td>[4, 8]</td>
		</tr>
		<tr>
			<td>3 次操作后</td>
			<td>[16, 8]</td>
		</tr>
	</tbody>
</table>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 10</code></li>
	<li><code>1 &lt;= multiplier &lt;= 5</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是使用最小堆来反复选择和更新数组中最小的元素，进行乘法操作以达到最终数组状态。

2. 综合思路：
   - 堆排序思路：利用最小堆（优先队列）来高效地找到当前数组中最小的元素，并对其进行乘法操作，重复此过程 K 次以得到最终数组。

3. 全量伪代码：
   - 初始化一个最小堆。
   - 遍历输入数组，将每个元素及其索引作为元组插入最小堆。
   - 重复 K 次以下操作：
     - 从最小堆中弹出最小元素。
     - 将该元素乘以给定的乘数。
     - 将更新后的元素及其索引重新插入最小堆。
   - 初始化一个与输入数组大小相同的结果数组。
   - 遍历最小堆，将每个元素放回其原始索引位置。
   - 返回结果数组。

4. 复杂度：
   - 时间复杂度：$O(n \log n + k \log n)$，其中 $n$ 是数组的长度，$k$ 是乘法操作的次数。初始化堆的时间复杂度为 $O(n \log n)$，每次堆操作（弹出和插入）的时间复杂度为 $O(\log n)$，共进行 $k$ 次。
   - 空间复杂度：$O(n)$，用于存储最小堆和结果数组。