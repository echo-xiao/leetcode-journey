# 409. 最长回文串

**难度**: Easy | **标签**: `Hash Table` `String` `Greedy`

## 题目描述

<p>给定一个包含大写字母和小写字母的字符串<meta charset="UTF-8" />&nbsp;<code>s</code>&nbsp;，返回&nbsp;<em>通过这些字母构造成的 <strong>最长的 <span data-keyword="palindrome-string">回文串</span></strong></em>&nbsp;的长度。</p>

<p>在构造过程中，请注意 <strong>区分大小写</strong> 。比如&nbsp;<code>"Aa"</code>&nbsp;不能当做一个回文字符串。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1: </strong></p>

<pre>
<strong>输入:</strong>s = "abccccdd"
<strong>输出:</strong>7
<strong>解释:</strong>
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong>s = "a"
<strong>输出:</strong>1
<strong>解释：</strong>可以构造的最长回文串是"a"，它的长度是 1。
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code>&nbsp;只由小写 <strong>和/或</strong> 大写英文字母组成</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过统计字符出现次数，计算可以构成的最长回文串长度，其中允许一个字符出现奇数次。

2. 综合思路：
   - 哈希表计数法：遍历字符串，使用哈希表记录每个字符的出现次数，然后根据字符出现次数的奇偶性计算最长回文串长度。

3. 全量伪代码：
   ```
   定义函数 longestPalindrome(s: 字符串) -> 整数:
       初始化字典 dic 为一个空字典
       对于字符串 s 中的每个字符 i:
           如果 i 在字典 dic 中:
               将 dic[i] 的值加 1
           否则:
               将 dic[i] 设为 1
       
       初始化整数 res 为 0
       初始化布尔变量 hasOdd 为 False
       对于字典 dic 中的每个键值对 (val, cnt):
           如果 cnt 是偶数:
               将 cnt 加到 res 上
           否则:
               将 (cnt - 1) 加到 res 上
               将 hasOdd 设为 True
       
       如果 hasOdd 为 True:
           返回 res + 1
       否则:
           返回 res
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度，因为我们需要遍历字符串并统计字符出现次数。
   - 空间复杂度：$O(1)$，因为字母表的大小是固定的（假设只包含英文字母），所以字典的大小是有限的。