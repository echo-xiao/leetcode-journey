# 187. 重复的DNA序列

**难度**: Medium | **标签**: `Hash Table` `String` `Bit Manipulation` `Sliding Window` `Rolling Hash` `Hash Function`

## 题目描述

<p><strong>DNA序列</strong>&nbsp;由一系列核苷酸组成，缩写为<meta charset="UTF-8" />&nbsp;<code>'A'</code>,&nbsp;<code>'C'</code>,&nbsp;<code>'G'</code>&nbsp;和<meta charset="UTF-8" />&nbsp;<code>'T'</code>.。</p>

<ul>
	<li>例如，<meta charset="UTF-8" /><code>"ACGAATTCCG"</code>&nbsp;是一个 <strong>DNA序列</strong> 。</li>
</ul>

<p>在研究 <strong>DNA</strong> 时，识别 DNA 中的重复序列非常有用。</p>

<p>给定一个表示 <strong>DNA序列</strong> 的字符串 <code>s</code> ，返回所有在 DNA 分子中出现不止一次的&nbsp;<strong>长度为&nbsp;<code>10</code></strong>&nbsp;的序列(子字符串)。你可以按 <strong>任意顺序</strong> 返回答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
<strong>输出：</strong>["AAAAACCCCC","CCCCCAAAAA"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "AAAAAAAAAAAAA"
<strong>输出：</strong>["AAAAAAAAAA"]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code><code>==</code><code>'A'</code>、<code>'C'</code>、<code>'G'</code>&nbsp;or&nbsp;<code>'T'</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：利用滑动窗口和哈希表记录DNA序列的出现次数，找出所有重复出现的长度为10的子串。

2. 综合思路：
   - 滑动窗口与哈希表：通过滑动窗口遍历字符串的每个长度为10的子串，并使用哈希表记录每个子串的出现次数，当某个子串出现次数超过一次时，将其加入结果列表。

3. 全量伪代码：
   ```
   定义函数 findRepeatedDnaSequences(s: 字符串) -> 列表:
       将字符串 s 转换为 string
       获取 string 的长度 size
       初始化右指针 right 为 10
       初始化结果列表 ans 为 []
       初始化字典 dic 为 {}

       如果 size 小于 10:
           返回空列表

       当 right 小于等于 size 时:
           获取当前子串 res 为 string 从 right-10 到 right 的子串
           如果 res 不在 dic 中:
               将 res 加入 dic，值为 1
           否则:
               如果 dic 中 res 的值为 1:
                   将 res 加入结果列表 ans
               将 dic 中 res 的值加 1
           将 right 加 1

       返回结果列表 ans
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度，因为每个长度为10的子串都被遍历一次。
   - 空间复杂度：$O(n)$，用于存储哈希表中所有可能的子串。