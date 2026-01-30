# 3. 无重复字符的最长子串

**难度**: Medium | **标签**: `Hash Table` `String` `Sliding Window`

## 题目描述

<p>给定一个字符串 <code>s</code> ，请你找出其中不含有重复字符的&nbsp;<strong>最长 <span data-keyword="substring-nonempty">子串</span></strong><strong>&nbsp;</strong>的长度。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入: </strong>s = "abcabcbb"
<strong>输出: </strong>3 
<strong>解释:</strong> 因为无重复字符的最长子串是 <code>"abc"</code>，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: </strong>s = "bbbbb"
<strong>输出: </strong>1
<strong>解释: </strong>因为无重复字符的最长子串是 <code>"b"</code>，所以其长度为 1。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入: </strong>s = "pwwkew"
<strong>输出: </strong>3
<strong>解释: </strong>因为无重复字符的最长子串是&nbsp;<code>"wke"</code>，所以其长度为 3。
&nbsp;    请注意，你的答案必须是 <strong>子串 </strong>的长度，<code>"pwke"</code>&nbsp;是一个<em>子序列，</em>不是子串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code>&nbsp;由英文字母、数字、符号和空格组成</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用滑动窗口和哈希集合来动态维护一个无重复字符的子串，并在遍历过程中更新最长子串的长度。

2. 简洁的中文实现思路描述：
   - 使用两个指针（左指针和右指针）来表示当前窗口的左右边界。
   - 右指针逐步向右移动，将字符加入当前窗口。
   - 如果窗口内出现重复字符，移动左指针缩小窗口，直到窗口内无重复字符。
   - 在每次调整窗口后，更新记录的最长无重复字符子串的长度。

3. 总结AC版本所有的通用解决方式/逻辑的中文伪代码：
   ```
   初始化左指针left为0，右指针right为0，最大长度maxLen为0，和一个空的哈希集合seen。
   当右指针小于字符串长度时：
       如果字符s[right]不在seen中：
           将s[right]加入seen。
           更新maxLen为当前窗口长度（right - left + 1）的最大值。
           将右指针向右移动。
       否则：
           从seen中移除s[left]，并将左指针向右移动。
   返回maxLen。
   ```

4. 时间复杂度和空间复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度。每个字符最多被访问两次（一次通过右指针，一次通过左指针）。
   - 空间复杂度：$O(min(m, n))$，其中 $m$ 是字符集的大小，$n$ 是字符串的长度。哈希集合seen最多存储不重复的字符。