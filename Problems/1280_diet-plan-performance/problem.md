# 1280. 健身计划评估 · 题目

**难度**: Easy | **标签**: `Array` `Sliding Window`

## 题目描述

<p>一个节食者在第 <code>i</code> 天消耗了 <code>calories[i]</code> 卡路里。</p>

<p>给定一个整数 <code>k</code>，对于<strong>每个</strong>连续的 <code>k</code> 天的序列（<code>calories[i], calories[i+1], ..., calories[i+k-1]</code>，对于所有 <code>0 &lt;= i &lt;= n-k</code>），他们关注 <em>T</em>，即在这 <code>k</code> 天的序列中消耗的总卡路里（<code>calories[i] + calories[i+1] + ... + calories[i+k-1]</code>）：</p>

<ul>
	<li>如果 <code>T &lt; lower</code>，他们在饮食上表现不佳，失去 1 分；</li>
	<li>如果 <code>T &gt; upper</code>，他们在饮食上表现良好，获得 1 分；</li>
	<li>否则，他们表现正常，积分没有变化。</li>
</ul>

<p>最初，节食者的积分为零。返回节食者在饮食 <code>calories.length</code> 天后的总积分。</p>

<p>请注意，总积分可能为负数。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3
<strong>输出:</strong> 0
<strong>解释</strong>: 由于 k = 1，我们分别考虑数组的每个元素，并将其与 lower 和 upper 进行比较。
calories[0] 和 calories[1] 小于 lower，因此失去 2 分。
calories[3] 和 calories[4] 大于 upper，因此获得 2 分。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> calories = [3,2], k = 2, lower = 0, upper = 1
<strong>输出:</strong> 1
<strong>解释</strong>: 由于 k = 2，我们考虑长度为 2 的子数组。
calories[0] + calories[1] &gt; upper，因此获得 1 分。
</pre>

<p><strong class="example">示例 3:</strong></p>

<pre>
<strong>输入:</strong> calories = [6,5,0,0], k = 2, lower = 1, upper = 5
<strong>输出:</strong> 0
<strong>解释</strong>:
calories[0] + calories[1] &gt; upper，因此获得 1 分。
lower &lt;= calories[1] + calories[2] &lt;= upper，因此积分没有变化。
calories[2] + calories[3] &lt; lower，因此失去 1 分。
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= calories.length &lt;= 10^5</code></li>
	<li><code>0 &lt;= calories[i] &lt;= 20000</code></li>
	<li><code>0 &lt;= lower &lt;= upper</code></li>
</ul>
