# 340. 至多包含 K 个不同字符的最长子串 · 题目

**难度**: Medium | **标签**: `Hash Table` `String` `Sliding Window`

## 题目描述

<p>给定一个字符串 <code>s</code> 和一个整数 <code>k</code>，返回 <em>包含至多</em> <code>k</code> <em><strong>不同</strong> 字符</em> 的 <em>最长</em><span data-keyword="substring-nonempty"><em>子串</em></span><em> 的长度</em>。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> s = &quot;eceba&quot;, k = 2
<strong>输出:</strong> 3
<strong>解释:</strong> 该子串为 &quot;ece&quot;，长度为 3。</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> s = &quot;aa&quot;, k = 1
<strong>输出:</strong> 2
<strong>解释:</strong> 该子串为 &quot;aa&quot;，长度为 2。
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= k &lt;= 50</code></li>
</ul>
