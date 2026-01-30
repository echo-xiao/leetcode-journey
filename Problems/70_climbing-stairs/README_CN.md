# 70. 爬楼梯

**难度**: Easy | **标签**: `Math` `Dynamic Programming` `Memoization`

## 题目描述

<p>假设你正在爬楼梯。需要 <code>n</code>&nbsp;阶你才能到达楼顶。</p>

<p>每次你可以爬 <code>1</code> 或 <code>2</code> 个台阶。你有多少种不同的方法可以爬到楼顶呢？</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>2
<strong>解释：</strong>有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>3
<strong>解释：</strong>有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 45</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是利用动态规划，通过记忆化递归的方法计算到达第 n 阶的方法数。

2. 综合思路：
   - **递归 + 记忆化**：通过递归计算每一阶楼梯的走法数，并使用一个数组来存储已经计算过的结果，避免重复计算，从而提高效率。
   - **迭代**：虽然在提供的代码中没有迭代版本，但通常也可以通过迭代的方式从底向上计算每一阶楼梯的走法数，避免递归的栈开销。

3. 全量伪代码：
   - **递归 + 记忆化**：
     ```
     定义函数 climbStairs(n)
         初始化 dp 数组，长度为 n+1，所有元素初始化为 -1
         返回 climbSteps(n)

     定义函数 climbSteps(n)
         如果 n 等于 1，返回 1
         如果 n 等于 2，返回 2
         如果 dp[n] 不等于 -1，返回 dp[n]
         计算 step1 为 climbSteps(n-1)
         计算 step2 为 climbSteps(n-2)
         将 dp[n] 赋值为 step1 + step2
         返回 dp[n]
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，因为每个台阶的结果只计算一次。
   - 空间复杂度：$O(n)$，用于存储每个台阶的结果。