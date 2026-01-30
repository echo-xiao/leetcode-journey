# 2231. 找出数组中的第一个回文字符串

**难度**: Easy | **标签**: `Array` `Two Pointers` `String`

## 题目描述

<p>给你一个字符串数组 <code>words</code> ，找出并返回数组中的 <strong>第一个回文字符串</strong> 。如果不存在满足要求的字符串，返回一个 <strong>空字符串</strong><em> </em><code>""</code> 。</p>

<p><strong>回文字符串</strong> 的定义为：如果一个字符串正着读和反着读一样，那么该字符串就是一个 <strong>回文字符串</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>words = ["abc","car","ada","racecar","cool"]
<strong>输出：</strong>"ada"
<strong>解释：</strong>第一个回文字符串是 "ada" 。
注意，"racecar" 也是回文字符串，但它不是第一个。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>words = ["notapalindrome","racecar"]
<strong>输出：</strong>"racecar"
<strong>解释：</strong>第一个也是唯一一个回文字符串是 "racecar" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>words = ["def","ghi"]
<strong>输出：</strong>""
<strong>解释：</strong>不存在回文字符串，所以返回一个空字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> 仅由小写英文字母组成</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：遍历数组中的每个字符串，逐字符比较其首尾字符以判断是否为回文。

2. 综合思路：
   - 迭代法：通过遍历每个字符串并使用双指针法（即从字符串两端向中间移动指针）来判断字符串是否为回文。
   - 递归法：虽然在给定的代码集中没有递归实现，但可以通过递归方式检查字符串的首尾字符是否相等来判断回文。
   - 不同数据结构：在给定的代码中，使用的是列表和字符串的基本操作，没有使用复杂的数据结构。

3. 全量伪代码：
   ```
   定义函数 firstPalindrome(words):
       对于每个字符串 word 在 words 中:
           初始化 left 指针为 0
           初始化 right 指针为 word 的长度减 1
           初始化 is_palindromic 为 True
           
           当 left 小于 right 时:
               如果 word[left] 不等于 word[right]:
                   将 is_palindromic 设为 False
                   跳出循环
               否则:
                   将 left 增加 1
                   将 right 减少 1
           
           如果 is_palindromic 为 True:
               返回 word
       
       返回空字符串 ""
   ```

4. 复杂度：
   - 时间复杂度：$O(n \cdot m)$，其中 $n$ 是数组中字符串的数量，$m$ 是字符串的平均长度。
   - 空间复杂度：$O(1)$，因为只使用了常数级别的额外空间。