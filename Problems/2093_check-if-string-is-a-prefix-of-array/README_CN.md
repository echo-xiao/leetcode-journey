# 2093. 检查字符串是否为数组前缀

**难度**: Easy | **标签**: `Array` `Two Pointers` `String`

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个字符串数组 <code>words</code> ，请你判断 <code>s</code> 是否为 <code>words</code> 的 <strong>前缀字符串</strong> 。</p>

<p>字符串 <code>s</code> 要成为 <code>words</code> 的 <strong>前缀字符串</strong> ，需要满足：<code>s</code> 可以由 <code>words</code> 中的前 <code>k</code>（<code>k</code> 为 <strong>正数</strong> ）个字符串按顺序相连得到，且 <code>k</code> 不超过 <code>words.length</code> 。</p>

<p>如果 <code>s</code> 是 <code>words</code> 的 <strong>前缀字符串</strong> ，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "iloveleetcode", words = ["i","love","leetcode","apples"]
<strong>输出：</strong>true
<strong>解释：</strong>
s 可以由 "i"、"love" 和 "leetcode" 相连得到。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "iloveleetcode", words = ["apples","i","love","leetcode"]
<strong>输出：</strong>false
<strong>解释：</strong>
数组的前缀相连无法得到 s 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 20</code></li>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>words[i]</code> 和 <code>s</code> 仅由小写英文字母组成</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过逐步累加数组中的字符串并与目标字符串进行比较，以检查目标字符串是否为数组前缀。

2. 综合思路：
   - 迭代累加：所有版本都采用了迭代的方式，通过逐步累加数组中的字符串元素，检查累加结果是否与目标字符串相等。
   - 直接比较：在每次累加后，直接比较累加结果与目标字符串，若相等则返回 `True`，否则继续累加直到数组结束。

3. 全量伪代码：
   ```
   初始化累加字符串为空
   对于数组中的每个字符串：
       将当前字符串累加到累加字符串中
       如果累加字符串等于目标字符串：
           返回 True
   返回 False
   ```

4. 复杂度：
   - 时间复杂度：$O(n \cdot m)$，其中 $n$ 是数组中字符串的数量，$m$ 是字符串的平均长度，因为每次累加操作需要遍历累加字符串。
   - 空间复杂度：$O(m \cdot n)$，因为累加字符串可能会包含数组中所有字符串的总长度。