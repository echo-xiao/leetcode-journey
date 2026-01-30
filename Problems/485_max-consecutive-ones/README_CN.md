# 485. 最大连续 1 的个数

**难度**: Easy | **标签**: `Array`

## 题目描述

<p>给定一个二进制数组 <code>nums</code> ， 计算其中最大连续 <code>1</code> 的个数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,0,1,1,1]
<strong>输出：</strong>3
<strong>解释：</strong>开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<b>输入：</b>nums = [1,0,1,1,0,1]
<b>输出：</b>2
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code>&nbsp;不是&nbsp;<code>0</code>&nbsp;就是&nbsp;<code>1</code>.</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过遍历数组，使用计数器记录连续 1 的长度，并在遇到 0 时更新最大长度。

2. 综合思路：
   - 迭代法：遍历数组，使用一个计数器 `cnt` 来记录当前连续 1 的数量，当遇到 0 时，将 `cnt` 与当前最大值 `result` 比较并更新 `result`，然后重置 `cnt`。最后返回 `result` 和 `cnt` 的最大值。
   - 由于题目提供的代码版本逻辑完全相同，因此没有其他不同的解法。

3. 全量伪代码：
   ```
   初始化 result 为 0
   初始化 cnt 为 0
   对于数组中的每个元素 n：
       如果 n 等于 1：
           将 cnt 增加 1
       否则：
           将 result 更新为 result 和 cnt 中的较大值
           将 cnt 重置为 0
   返回 result 和 cnt 中的较大值
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是数组的长度，因为需要遍历整个数组一次。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外变量。