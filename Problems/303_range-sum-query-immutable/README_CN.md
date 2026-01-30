# 303. 区域和检索 - 数组不可变

**难度**: Easy | **标签**: `Array` `Design` `Prefix Sum`

## 题目描述

<p>给定一个整数数组 &nbsp;<code>nums</code>，处理以下类型的多个查询:</p>

<ol>
	<li>计算索引&nbsp;<code>left</code>&nbsp;和&nbsp;<code>right</code>&nbsp;（包含 <code>left</code> 和 <code>right</code>）之间的 <code>nums</code> 元素的 <strong>和</strong> ，其中&nbsp;<code>left &lt;= right</code></li>
</ol>

<p>实现 <code>NumArray</code> 类：</p>

<ul>
	<li><code>NumArray(int[] nums)</code> 使用数组 <code>nums</code> 初始化对象</li>
	<li><code>int sumRange(int left, int right)</code> 返回数组 <code>nums</code>&nbsp;中索引&nbsp;<code>left</code>&nbsp;和&nbsp;<code>right</code>&nbsp;之间的元素的 <strong>总和</strong> ，包含&nbsp;<code>left</code>&nbsp;和&nbsp;<code>right</code>&nbsp;两点（也就是&nbsp;<code>nums[left] + nums[left + 1] + ... + nums[right]</code>&nbsp;)</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
<strong>输出：
</strong>[null, 1, -1, -3]

<strong>解释：</strong>
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup>&nbsp;&lt;= nums[i] &lt;=&nbsp;10<sup>5</sup></code></li>
	<li><code>0 &lt;= left&nbsp;&lt;= right&nbsp;&lt; nums.length</code></li>
	<li>最多调用 <code>10<sup>4</sup></code> 次 <code>sumRange</code><strong> </strong>方法</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质**：通过构建前缀和数组，使得区间和查询能够在常数时间内完成。

2. **综合思路**：在所有版本中，唯一的解法是使用前缀和数组。初始化时计算前缀和数组，查询时通过前缀和数组快速计算区间和。

3. **全量伪代码**：
   - 初始化逻辑：
     - 创建一个长度为 `n+1` 的数组 `curr`，其中 `n` 是输入数组 `nums` 的长度。
     - 初始化 `curr[0]` 为 0。
     - 遍历 `nums` 数组，对于每个索引 `i`，计算 `curr[i+1] = curr[i] + nums[i]`。
   - 查询逻辑：
     - 对于给定的区间 `[left, right]`，返回 `curr[right+1] - curr[left]`。

4. **复杂度**：
   - 时间复杂度：初始化时为 $O(n)$，查询时为 $O(1)$。
   - 空间复杂度：$O(n)$，用于存储前缀和数组。