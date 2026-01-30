# 438. 找到字符串中所有字母异位词

**难度**: Medium | **标签**: `Hash Table` `String` `Sliding Window`

## 题目描述

<p>给定两个字符串&nbsp;<code>s</code>&nbsp;和 <code>p</code>，找到&nbsp;<code>s</code><strong>&nbsp;</strong>中所有&nbsp;<code>p</code><strong>&nbsp;</strong>的&nbsp;<strong><span data-keyword="anagram">异位词</span>&nbsp;</strong>的子串，返回这些子串的起始索引。不考虑答案输出的顺序。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入: </strong>s = "cbaebabacd", p = "abc"
<strong>输出: </strong>[0,6]
<strong>解释:</strong>
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
</pre>

<p><strong>&nbsp;示例 2:</strong></p>

<pre>
<strong>输入: </strong>s = "abab", p = "ab"
<strong>输出: </strong>[0,1,2]
<strong>解释:</strong>
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, p.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s</code>&nbsp;和&nbsp;<code>p</code>&nbsp;仅包含小写字母</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：利用滑动窗口和字符频率计数来判断当前窗口是否为目标字符串的字母异位词。

2. 综合思路：
   - 滑动窗口：两个版本都使用滑动窗口的方法，通过维护一个窗口内的字符频率计数来判断窗口内的字符串是否为目标字符串的字母异位词。
   - 字符频率计数：通过字典来记录目标字符串和当前窗口内的字符频率，比较这两个频率字典来判断是否为字母异位词。

3. 全量伪代码：
   ```plaintext
   初始化目标字符串的字符频率字典 pCount
   初始化当前窗口的字符频率字典 sCount
   初始化结果列表 res
   初始化左右指针 left 和 right 为 0

   遍历目标字符串 p 中的每个字符，更新 pCount 中的频率

   当 right 小于字符串 s 的长度时，执行以下步骤：
       获取当前字符 c = s[right]
       将 c 的频率在 sCount 中增加
       将 right 指针右移

       当窗口大小大于或等于目标字符串长度时，执行以下步骤：
           如果 pCount 和 sCount 相等，记录当前左指针位置 left 到结果列表 res
           获取窗口左端字符 l = s[left]
           将 l 的频率在 sCount 中减少
           如果 l 的频率为 0，从 sCount 中删除 l
           将 left 指针右移

   返回结果列表 res
   ```

4. 复杂度：
   - 时间复杂度：$O(n + m)$，其中 $n$ 是字符串 $s$ 的长度，$m$ 是字符串 $p$ 的长度。初始化频率字典需要 $O(m)$，滑动窗口遍历字符串 $s$ 需要 $O(n)$。
   - 空间复杂度：$O(1)$，因为字符频率字典的大小是固定的，最多包含 26 个字母。