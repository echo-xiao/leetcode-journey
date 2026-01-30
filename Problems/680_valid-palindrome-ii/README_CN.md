# 680. 验证回文串 II

**难度**: Easy | **标签**: `Two Pointers` `String` `Greedy`

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>，<strong>最多</strong> 可以从中删除一个字符。</p>

<p>请你判断 <code>s</code> 是否能成为回文字符串：如果能，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "aba"
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abca"
<strong>输出：</strong>true
<strong>解释：</strong>你可以删除字符 'c' 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "abc"
<strong>输出：</strong>false</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 由小写英文字母组成</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过双指针遍历字符串，允许最多跳过一个字符来验证是否为回文。

2. 综合思路：
   - 双指针法：使用两个指针从字符串两端向中间移动，遇到不匹配时，尝试跳过左指针或右指针的字符进行回文验证。
   - 递归法：可以将双指针法中的跳过字符操作改为递归调用，验证去掉一个字符后的子串是否为回文。

3. 全量伪代码：
   ```plaintext
   函数 validPalindrome(字符串 s):
       初始化 left 为 0
       初始化 right 为 字符串长度减一
       当 left 小于 right 时:
           如果 s[left] 不等于 s[right]:
               调用 ifPalindrome 函数检查 s[left+1:right] 是否为回文，结果存入 leftCheck
               调用 ifPalindrome 函数检查 s[left:right-1] 是否为回文，结果存入 rightCheck
               返回 leftCheck 或 rightCheck
           left 增加 1
           right 减少 1
       返回 True

   函数 ifPalindrome(字符串 s, 整数 left, 整数 right):
       当 left 小于 right 时:
           如果 s[left] 等于 s[right]:
               left 增加 1
               right 减少 1
           否则:
               返回 False
       返回 True
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度。最坏情况下需要遍历整个字符串两次。
   - 空间复杂度：$O(1)$，只使用了常数级别的额外空间。