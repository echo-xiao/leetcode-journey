# 400. 第 N 位数字

**难度**: Medium | **标签**: `Math` `Binary Search`

## 题目描述

<p>给你一个整数 <code>n</code> ，请你在无限的整数序列&nbsp;<code>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...]</code> 中找出并返回第&nbsp;<code>n</code><em> </em>位上的数字。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>3
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 11
<strong>输出：</strong>0
<strong>解释：</strong>第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 <strong>0 </strong>，它是 10 的一部分。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质**：通过逐步确定数字的位数范围，找到第 N 位数字所在的具体数字及其在数字中的位置。

2. **综合思路**：
   - **迭代法**：通过迭代逐步减少 N 的值，确定第 N 位数字所在的数字位数范围（如个位数、十位数、百位数等），然后计算出具体的数字和位置。

3. **全量伪代码**：
   ```plaintext
   初始化变量：length = 1, count = 9, start = 1
   当 n 大于 length * count 时：
       减去当前范围的数字总位数：n -= length * count
       增加数字位数：length += 1
       更新起始数字：start *= 10
       更新当前范围的数字个数：count *= 10
   计算目标数字：num = start + (n-1) // length
   计算目标数字中的索引：idx = (n-1) % length
   返回 num 的第 idx 位数字
   ```

4. **复杂度**：
   - 时间复杂度：$O(\log_{10} n)$，因为每次循环中，数字的位数增加一位，最多需要处理 $\log_{10} n$ 次。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外变量。