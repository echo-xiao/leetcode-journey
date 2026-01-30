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

1. 一句话直击本质：使用滑动窗口和集合来动态维护当前无重复字符的子串，并在遍历过程中更新最大长度。

2. 综合思路：
   - 滑动窗口：通过两个指针（left 和 right）来维护一个窗口，窗口内的字符是当前无重复字符的子串。当发现重复字符时，移动左指针以缩小窗口，直到窗口内无重复字符。
   - 数据结构：使用列表和集合来存储当前窗口内的字符，列表用于顺序存储字符，集合用于快速判断是否有重复。

3. 全量伪代码：
   ```
   定义函数 lengthOfLongestSubstring，输入为字符串 s
       将字符串 s 转换为字符数组 string
       初始化变量 size 为 string 的长度
       初始化两个指针 left 和 right 为 0
       初始化空列表 res 用于存储当前窗口的字符
       初始化变量 maxLen 为 0，用于存储最大无重复子串长度

       当 right 小于 size 时，执行以下循环：
           将 string[right] 添加到 res 列表中
           将 right 指针右移一位

           当 res 列表中存在重复字符时，执行以下循环：
               删除 res 列表的第一个元素
               将 left 指针右移一位

           更新 maxLen 为 max(maxLen, right - left)

       返回 maxLen
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度。每个字符最多被访问两次（一次通过 right 指针，一次通过 left 指针）。
   - 空间复杂度：$O(n)$，在最坏情况下，列表 res 可能存储所有字符。