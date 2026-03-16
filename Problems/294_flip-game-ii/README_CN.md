# 294. 翻转游戏 II

**难度**: Medium | **标签**: `Math` `Dynamic Programming` `Backtracking` `Memoization` `Game Theory`

## 题目描述

<p>你正在和你的朋友玩一个翻转游戏。</p>

<p>你被给定一个字符串 <code>currentState</code>，它只包含 <code>&#39;+&#39;</code> 和 <code>&#39;-&#39;</code>。你和你的朋友轮流将<strong>两个连续的</strong> <code>&quot;++&quot;</code> 翻转为 <code>&quot;--&quot;</code>。当某个人无法再进行移动时，游戏结束，因此另一个人将成为赢家。</p>

<p>如果起始玩家可以<strong>保证获胜</strong>，则返回 <code>true</code>，否则返回 <code>false</code>。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> currentState = &quot;++++&quot;
<strong>输出:</strong> true
<strong>解释:</strong> 起始玩家可以通过翻转中间的 &quot;++&quot; 使其变为 &quot;+--+&quot; 来保证获胜。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> currentState = &quot;+&quot;
<strong>输出:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>1 &lt;= currentState.length &lt;= 60</code></li>
	<li><code>currentState[i]</code> 要么是 <code>&#39;+&#39;</code> 要么是 <code>&#39;-&#39;</code>。</li>
	<li>不能有超过 20 个连续的 <code>&#39;+&#39;</code>。</li>
</ul>

<p>&nbsp;</p>
<strong>后续问题:</strong> 推导你的算法的运行时间复杂度。

---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过递归和记忆化搜索判断当前玩家是否能通过一次合法翻转操作使对手处于必败状态。

2. 综合思路：
   - 递归与记忆化搜索：通过递归遍历所有可能的翻转操作，并使用记忆化技术缓存已经计算过的状态结果，避免重复计算。
   - 纯递归：直接递归遍历所有可能的翻转操作，不使用记忆化技术，可能导致重复计算。

3. 全量伪代码：
   ```plaintext
   定义函数 canWin(currentState):
       初始化一个字典 memo 用于记忆化搜索

       定义递归函数 solve(s):
           如果 s 在 memo 中:
               返回 memo[s]

           遍历 s 中的每一个可能的翻转位置 i:
               如果 s[i:i+2] 是 "++":
                   生成新的状态 nxt = s[:i] + "--" + s[i+2:]
                   如果 solve(nxt) 返回 False:
                       记录 memo[s] = True
                       返回 True

           记录 memo[s] = False
           返回 False

       返回 solve(currentState)

   定义函数 canWin(currentState):
       遍历 currentState 中的每一个可能的翻转位置 i:
           如果 currentState[i:i+2] 是 "++":
               生成新的状态 nxt = currentState[:i] + "--" + currentState[i+2:]
               如果 canWin(nxt) 返回 False:
                   返回 True

       返回 False
   ```

4. 复杂度：
   - 时间复杂度：递归版本的时间复杂度为 $O(2^n)$，其中 $n$ 是字符串的长度，因为每个位置的翻转可能性是二叉树的分支。
   - 空间复杂度：使用记忆化搜索的版本空间复杂度为 $O(n)$，因为需要存储每个状态的计算结果。