# 1086. 除数博弈

**难度**: Easy | **标签**: `Math` `Dynamic Programming` `Brainteaser` `Game Theory`

## 题目描述

<p>爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。</p>

<p>最初，黑板上有一个数字&nbsp;<code>n</code>&nbsp;。在每个玩家的回合，玩家需要执行以下操作：</p>

<ul>
	<li>选出任一整数&nbsp;<code>x</code>，满足&nbsp;<code>0 &lt; x &lt; n</code>&nbsp;且&nbsp;<code>n % x == 0</code>&nbsp;。</li>
	<li>用 <code>n - x</code>&nbsp;替换黑板上的数字&nbsp;<code>n</code> 。</li>
</ul>

<p>如果玩家无法执行这些操作，就会输掉游戏。</p>

<p><em>只有在爱丽丝在游戏中取得胜利时才返回&nbsp;<code>true</code>&nbsp;。假设两个玩家都以最佳状态参与游戏。</em></p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>true
<strong>解释：</strong>爱丽丝选择 1，鲍勃无法进行操作。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>false
<strong>解释：</strong>爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是利用动态规划或数学归纳法判断当前数字是否能通过选择一个合适的除数使得对手处于必败状态。

2. 综合思路：
   - 递归+记忆化搜索：通过递归判断当前数字能否通过选择一个合适的除数使得对手处于必败状态，并使用字典缓存中间结果以避免重复计算。
   - 动态规划：使用一个布尔数组记录每个数字的胜负状态，逐步从小到大计算每个数字是否能使对手处于必败状态。
   - 数学归纳法：利用数学性质，直接判断数字是否为偶数，因为偶数总能通过选择1使得对手面对奇数，从而最终获胜。

3. 全量伪代码：
   - 递归+记忆化搜索：
     ```
     定义函数 canWin(k):
         如果 k 等于 1，返回 False
         如果 k 在 memo 中，返回 memo[k]
         对于 x 从 1 到 k//2:
             如果 k % x == 0 且 canWin(k-x) 为 False:
                 memo[k] = True
                 返回 True
         memo[k] = False
         返回 False

     定义函数 divisorGame(n):
         初始化 memo 为一个空字典
         返回 canWin(n)
     ```
   - 动态规划：
     ```
     定义函数 divisorGame(n):
         初始化 dp 为长度为 n+1 的布尔数组，所有元素为 False
         对于 i 从 2 到 n:
             对于 x 从 1 到 i//2:
                 如果 i % x == 0 且 dp[i-x] 为 False:
                     dp[i] = True
                     跳出循环
         返回 dp[n]
     ```
   - 数学归纳法：
     ```
     定义函数 divisorGame(n):
         返回 n 是否为偶数
     ```

4. 复杂度：
   - 递归+记忆化搜索：时间复杂度为 $O(n^2)$，空间复杂度为 $O(n)$。
   - 动态规划：时间复杂度为 $O(n^2)$，空间复杂度为 $O(n)$。
   - 数学归纳法：时间复杂度为 $O(1)$，空间复杂度为 $O(1)$。