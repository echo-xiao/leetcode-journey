# 1236. 第 N 个泰波那契数

**难度**: Easy | **标签**: `Math` `Dynamic Programming` `Memoization`

## 题目描述

<p>泰波那契序列&nbsp;T<sub>n</sub>&nbsp;定义如下：&nbsp;</p>

<p>T<sub>0</sub> = 0, T<sub>1</sub> = 1, T<sub>2</sub> = 1, 且在 n &gt;= 0&nbsp;的条件下 T<sub>n+3</sub> = T<sub>n</sub> + T<sub>n+1</sub> + T<sub>n+2</sub></p>

<p>给你整数&nbsp;<code>n</code>，请返回第 n 个泰波那契数&nbsp;T<sub>n </sub>的值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 4
<strong>输出：</strong>4
<strong>解释：</strong>
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 25
<strong>输出：</strong>1389537
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 37</code></li>
	<li>答案保证是一个 32 位整数，即&nbsp;<code>answer &lt;= 2^31 - 1</code>。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法通过递归结合记忆化搜索（动态规划）来计算第 N 个泰波那契数，以避免重复计算。

2. 综合思路：
   - 递归与记忆化搜索：使用递归函数计算泰波那契数，并通过一个数组存储已经计算过的结果，以减少重复计算。
   - 迭代：可以通过迭代的方式，从底向上计算每个泰波那契数，逐步累积到第 N 个。

3. 全量伪代码：
   - 递归与记忆化搜索：
     ```
     定义函数 tribonacci(n):
         初始化数组 dp 长度为 n+1，所有元素为 -1
         返回 递归函数 recursion(n)

     定义递归函数 recursion(n):
         如果 n 等于 0:
             返回 0
         如果 n 等于 1 或 n 等于 2:
             返回 1
         如果 dp[n] 不等于 -1:
             返回 dp[n]
         dp[n] = recursion(n-1) + recursion(n-2) + recursion(n-3)
         返回 dp[n]
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，因为每个泰波那契数只计算一次。
   - 空间复杂度：$O(n)$，用于存储中间结果的数组。