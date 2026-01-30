# 96. 不同的二叉搜索树

**难度**: Medium | **标签**: `Math` `Dynamic Programming` `Tree` `Binary Search Tree` `Binary Tree`

## 题目描述

<p>给你一个整数 <code>n</code> ，求恰由 <code>n</code> 个节点组成且节点值从 <code>1</code> 到 <code>n</code> 互不相同的 <strong>二叉搜索树</strong> 有多少种？返回满足题意的二叉搜索树的种数。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg" style="width: 600px; height: 148px;" />
<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>5
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 19</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是利用动态规划或记忆化递归计算卡特兰数，以求解不同的二叉搜索树的数量。

2. 综合思路：
   - 递归与记忆化：通过递归计算每个子问题的解，并使用字典或缓存装饰器来存储已经计算过的结果，以避免重复计算。
   - 动态规划：虽然在提供的代码中没有直接实现，但可以通过迭代的方式构建一个数组来存储每个子问题的解，从而避免递归调用。

3. 全量伪代码：
   - 递归与记忆化版本：
     ```
     定义函数 numTrees(n):
         如果 n <= 1:
             返回 1
         初始化 res 为 0
         对于 i 从 1 到 n:
             计算左子树数量 leftSide = numTrees(i-1)
             计算右子树数量 rightSide = numTrees(n-i)
             累加 res += leftSide * rightSide
         返回 res
     ```
   - 记忆化递归版本（带缓存）：
     ```
     定义函数 numTrees(n) 带缓存:
         如果 n <= 1:
             返回 1
         初始化 res 为 0
         对于 i 从 1 到 n:
             计算左子树数量 leftSide = numTrees(i-1)
             计算右子树数量 rightSide = numTrees(n-i)
             累加 res += leftSide * rightSide
         返回 res
     ```
   - 动态规划版本（未提供，但可以推导）：
     ```
     定义函数 numTrees(n):
         初始化 dp 数组，长度为 n+1，dp[0] = 1, dp[1] = 1
         对于 i 从 2 到 n:
             初始化 dp[i] 为 0
             对于 j 从 1 到 i:
                 dp[i] += dp[j-1] * dp[i-j]
         返回 dp[n]
     ```

4. 复杂度：
   - 时间复杂度：递归与记忆化版本的时间复杂度为 $O(n^2)$，因为每个子问题最多需要计算 $n$ 次。
   - 空间复杂度：递归与记忆化版本的空间复杂度为 $O(n)$，用于存储中间结果。