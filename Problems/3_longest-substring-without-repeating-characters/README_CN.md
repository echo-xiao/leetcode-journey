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

### 一句话直击本质
使用滑动窗口和哈希集合来动态维护一个无重复字符的子串，并在遍历过程中更新最长子串的长度。

### 综合思路
1. **滑动窗口法**：通过两个指针（左指针和右指针）构成一个窗口，右指针不断向右扩展窗口，左指针在出现重复字符时向右收缩窗口，确保窗口内的字符无重复。
2. **哈希集合**：利用集合的特性快速判断字符是否重复，并在重复时调整窗口。

### 全量伪代码
```plaintext
函数 lengthOfLongestSubstring(字符串 s):
    将字符串 s 转换为字符数组 string
    初始化 size 为 string 的长度
    初始化 左指针 left 和 右指针 right 为 0
    初始化 空列表 res 用于存储当前窗口的字符
    初始化 maxLen 为 0 用于记录最长子串长度

    当 right 小于 size 时，重复以下步骤:
        将 string[right] 添加到 res
        将 right 增加 1
        
        当 res 中的字符数目不等于 res 转换为集合后的大小时:
            删除 res 中的第一个元素
            将 left 增加 1
        
        更新 maxLen 为 max(maxLen, right - left)

    返回 maxLen
```

### 复杂度
- 时间复杂度: $O(n)$，其中 $n$ 是字符串的长度。每个字符在最坏情况下被访问两次（一次被右指针访问，一次被左指针移出）。
- 空间复杂度: $O(min(n, m))$，其中 $m$ 是字符集的大小。使用集合存储当前窗口的字符。