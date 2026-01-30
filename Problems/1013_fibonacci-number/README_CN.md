# 1013. 斐波那契数

**难度**: Easy | **标签**: `Math` `Dynamic Programming` `Recursion` `Memoization`

## 题目描述

<p><strong>斐波那契数</strong>&nbsp;（通常用&nbsp;<code>F(n)</code> 表示）形成的序列称为 <strong>斐波那契数列</strong> 。该数列由&nbsp;<code>0</code> 和 <code>1</code> 开始，后面的每一项数字都是前面两项数字的和。也就是：</p>

<pre>
F(0) = 0，F(1)&nbsp;= 1
F(n) = F(n - 1) + F(n - 2)，其中 n &gt; 1
</pre>

<p>给定&nbsp;<code>n</code> ，请计算 <code>F(n)</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>1
<strong>解释：</strong>F(2) = F(1) + F(0) = 1 + 0 = 1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>2
<strong>解释：</strong>F(3) = F(2) + F(1) = 1 + 1 = 2
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 4
<strong>输出：</strong>3
<strong>解释：</strong>F(4) = F(3) + F(2) = 2 + 1 = 3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 30</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：斐波那契数的计算可以通过递归调用自身来实现，其中使用记忆化技术可以优化递归的效率。

2. 综合思路：
   - 递归：直接递归调用自身来计算斐波那契数，适用于小规模问题，但效率较低。
   - 记忆化递归：在递归的基础上使用数组存储已经计算过的结果，避免重复计算，提高效率。

3. 全量伪代码：
   - 递归版本：
     ```
     函数 斐波那契(n):
         如果 n 等于 0:
             返回 0
         如果 n 等于 1:
             返回 1
         返回 斐波那契(n-1) + 斐波那契(n-2)
     ```
   - 记忆化递归版本：
     ```
     函数 斐波那契(n):
         初始化 dp 数组为长度 n+1，所有元素为 -1
         返回 递归计算(n)

     函数 递归计算(n):
         如果 n 等于 0:
             返回 0
         如果 n 等于 1:
             返回 1
         如果 dp[n] 不等于 -1:
             返回 dp[n]
         dp[n] = 递归计算(n-1) + 递归计算(n-2)
         返回 dp[n]
     ```

4. 复杂度：
   - 递归版本的时间复杂度为 $O(2^n)$，空间复杂度为 $O(n)$（递归栈的深度）。
   - 记忆化递归版本的时间复杂度为 $O(n)$，空间复杂度为 $O(n)$（用于存储计算结果的数组）。