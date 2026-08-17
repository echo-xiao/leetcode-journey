# 294. 翻转游戏 II · 题目

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
