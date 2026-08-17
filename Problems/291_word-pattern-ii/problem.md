# 291. 单词规律 II · 题目

**难度**: Medium | **标签**: `Hash Table` `String` `Backtracking`

## 题目描述

<p>给定一个 <code>pattern</code> 和一个字符串 <code>s</code>，如果 <code>s</code><em> <strong>与</strong> </em><code>pattern</code><em> 匹配，返回 </em><code>true</code>。</p>

<p>一个字符串 <code>s</code> <b>匹配</b> 一个 <code>pattern</code>，如果存在某种<strong>双射映射</strong>将单个字符映射到<strong>非空</strong>字符串，使得如果将 <code>pattern</code> 中的每个字符替换为它所映射的字符串，则得到的字符串为 <code>s</code>。<strong>双射映射</strong>意味着没有两个字符映射到相同的字符串，并且没有字符映射到两个不同的字符串。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> pattern = &quot;abab&quot;, s = &quot;redblueredblue&quot;
<strong>输出:</strong> true
<strong>解释:</strong> 一种可能的映射如下：
&#39;a&#39; -&gt; &quot;red&quot;
&#39;b&#39; -&gt; &quot;blue&quot;</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> pattern = &quot;aaaa&quot;, s = &quot;asdasdasdasd&quot;
<strong>输出:</strong> true
<strong>解释:</strong> 一种可能的映射如下：
&#39;a&#39; -&gt; &quot;asd&quot;
</pre>

<p><strong class="example">示例 3:</strong></p>

<pre>
<strong>输入:</strong> pattern = &quot;aabb&quot;, s = &quot;xyzabcxzyabc&quot;
<strong>输出:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>1 &lt;= pattern.length, s.length &lt;= 20</code></li>
	<li><code>pattern</code> 和 <code>s</code> 仅由小写英文字母组成。</li>
</ul>
