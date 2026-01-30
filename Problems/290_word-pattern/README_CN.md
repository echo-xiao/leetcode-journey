# 290. 单词规律

**难度**: Easy | **标签**: `Hash Table` `String`

## 题目描述

<p>给定一种规律 <code>pattern</code>&nbsp;和一个字符串&nbsp;<code>s</code>&nbsp;，判断 <code>s</code>&nbsp;是否遵循相同的规律。</p>

<p>这里的&nbsp;<strong>遵循&nbsp;</strong>指完全匹配，例如，&nbsp;<code>pattern</code>&nbsp;里的每个字母和字符串&nbsp;<code>s</code><strong>&nbsp;</strong>中的每个非空单词之间存在着双向连接的对应规律。具体来说：</p>

<ul>
	<li><code>pattern</code>&nbsp;中的每个字母都 <strong>恰好</strong> 映射到 <code>s</code> 中的一个唯一单词。</li>
	<li><code>s</code> 中的每个唯一单词都 <strong>恰好</strong> 映射到&nbsp;<code>pattern</code> 中的一个字母。</li>
	<li>没有两个字母映射到同一个单词，也没有两个单词映射到同一个字母。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例1:</strong></p>

<pre>
<strong>输入:</strong> pattern = <code>"abba"</code>, s = <code>"dog cat cat dog"</code>
<strong>输出:</strong> true</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong>pattern = <code>"abba"</code>, s = <code>"dog cat cat fish"</code>
<strong>输出:</strong> false</pre>

<p><strong class="example">示例 3:</strong></p>

<pre>
<strong>输入:</strong> pattern = <code>"aaaa"</code>, s = <code>"dog cat cat dog"</code>
<strong>输出:</strong> false</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= pattern.length &lt;= 300</code></li>
	<li><code>pattern</code>&nbsp;只包含小写英文字母</li>
	<li><code>1 &lt;= s.length &lt;= 3000</code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母和&nbsp;<code>' '</code></li>
	<li><code>s</code>&nbsp;<strong>不包含</strong> 任何前导或尾随对空格</li>
	<li><code>s</code>&nbsp;中每个单词都被 <strong>单个空格 </strong>分隔</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用双向映射验证模式字符串和单词序列之间的一一对应关系。

2. 综合思路：
   - 双向映射：使用两个字典分别记录模式字符到单词的映射和单词到模式字符的映射，确保每个字符和单词之间的映射是唯一且一致的。

3. 全量伪代码：
   ```
   定义函数 wordPattern(pattern, s):
       将字符串 s 按空格分割成单词列表 words
       如果 pattern 的长度不等于 words 的长度:
           返回 False

       初始化两个空字典 charToStr 和 strToChar

       对于 pattern 和 words 中的每一对字符 c 和单词 w:
           如果 c 在 charToStr 中且 charToStr[c] 不等于 w:
               返回 False
           如果 w 在 strToChar 中且 strToChar[w] 不等于 c:
               返回 False

           将 c 映射到 w (charToStr[c] = w)
           将 w 映射到 c (strToChar[w] = c)

       返回 True
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串 $s$ 中单词的数量，因为我们需要遍历每个单词和对应的模式字符。
   - 空间复杂度：$O(m)$，其中 $m$ 是模式字符串和单词列表中不同字符和单词的数量，因为我们需要存储这些映射关系。