# 979. 增减字符串匹配

**难度**: Easy | **标签**: `Array` `Two Pointers` `String` `Greedy`

## 题目描述

<p>由范围 <code>[0,n]</code> 内所有整数组成的 <code>n + 1</code> 个整数的排列序列可以表示为长度为 <code>n</code> 的字符串 <code>s</code> ，其中:</p>

<ul>
	<li>如果&nbsp;<code>perm[i] &lt; perm[i + 1]</code>&nbsp;，那么&nbsp;<code>s[i] == 'I'</code>&nbsp;</li>
	<li>如果&nbsp;<code>perm[i] &gt; perm[i + 1]</code>&nbsp;，那么 <code>s[i] == 'D'</code>&nbsp;</li>
</ul>

<p>给定一个字符串 <code>s</code> ，重构排列&nbsp;<code>perm</code> 并返回它。如果有多个有效排列perm，则返回其中 <strong>任何一个</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "IDID"
<strong>输出：</strong>[0,4,1,3,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "III"
<strong>输出：</strong>[0,1,2,3]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "DDI"
<strong>输出：</strong>[3,2,0,1]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code><font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">s</span></span></font></font></code> 只包含字符&nbsp;<code>"I"</code>&nbsp;或&nbsp;<code>"D"</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：算法的核心逻辑是通过双指针法，根据字符串中的'I'和'D'分别从数组的两端选择合适的数字填入结果数组。

2. 综合思路：
   - 双指针法：所有版本都采用了双指针法，使用两个指针分别指向当前可用的最小值和最大值，根据字符串中的字符选择合适的值填入结果数组。
   - 版本 1 和 3：直接使用两个变量 `left` 和 `right` 来表示当前可用的最小值和最大值。
   - 版本 2：使用一个预先生成的列表 `lst` 来存储所有可能的数字，然后通过索引访问。

3. 全量伪代码：
   - 初始化一个空数组 `arr` 用于存储结果。
   - 初始化两个指针 `left` 和 `right`，分别指向 0 和字符串长度。
   - 对于字符串中的每个字符：
     - 如果字符是 'I'，将 `left` 指针指向的值加入 `arr`，然后将 `left` 增加 1。
     - 如果字符是 'D'，将 `right` 指针指向的值加入 `arr`，然后将 `right` 减少 1。
   - 将 `left` 指针指向的值加入 `arr`（此时 `left` 和 `right` 应该相等）。
   - 返回结果数组 `arr`。

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度，因为我们需要遍历字符串一次。
   - 空间复杂度：$O(n)$，因为结果数组 `arr` 的长度与字符串长度相同。