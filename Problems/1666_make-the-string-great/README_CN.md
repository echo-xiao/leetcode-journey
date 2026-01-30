# 1666. 整理字符串

**难度**: Easy | **标签**: `String` `Stack`

## 题目描述

<p>给你一个由大小写英文字母组成的字符串 <code>s</code> 。</p>

<p>一个整理好的字符串中，两个相邻字符 <code>s[i]</code> 和 <code>s[i+1]</code>，其中 <code>0<= i <= s.length-2</code> ，要满足如下条件:</p>

<ul>
	<li>若 <code>s[i]</code> 是小写字符，则 <code>s[i+1]</code> 不可以是相同的大写字符。</li>
	<li>若 <code>s[i]</code> 是大写字符，则 <code>s[i+1]</code> 不可以是相同的小写字符。</li>
</ul>

<p>请你将字符串整理好，每次你都可以从字符串中选出满足上述条件的 <strong>两个相邻</strong> 字符并删除，直到字符串整理好为止。</p>

<p>请返回整理好的 <strong>字符串</strong> 。题目保证在给出的约束条件下，测试样例对应的答案是唯一的。</p>

<p><strong>注意：</strong>空字符串也属于整理好的字符串，尽管其中没有任何字符。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "leEeetcode"
<strong>输出：</strong>"leetcode"
<strong>解释：</strong>无论你第一次选的是 i = 1 还是 i = 2，都会使 "leEeetcode" 缩减为 "leetcode" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abBAcC"
<strong>输出：</strong>""
<strong>解释：</strong>存在多种不同情况，但所有的情况都会导致相同的结果。例如：
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "s"
<strong>输出：</strong>"s"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 100</code></li>
	<li><code>s</code> 只包含小写和大写英文字母</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用栈来逐步消除相邻的大小写异同字符对，最终返回整理后的字符串。

2. 综合思路：在所有给定的版本中，均采用了迭代的方式，并使用栈作为数据结构来实现字符串的整理。具体步骤如下：
   - 遍历字符串中的每个字符。
   - 使用栈来存储字符，如果栈顶字符与当前字符大小写相同但字符不同，则从栈中弹出栈顶字符。
   - 否则，将当前字符压入栈中。
   - 最终，栈中剩余的字符即为整理后的字符串。

3. 全量伪代码：
   ```
   定义函数 makeGood(s: 字符串) -> 字符串：
       初始化一个空栈 stack
       对于字符串 s 中的每个字符 char：
           如果栈不为空：
               获取栈顶字符 peek
               如果 peek 的小写形式等于 char 的小写形式且 peek 不等于 char：
                   从栈中弹出栈顶字符
               否则：
                   将 char 压入栈
           否则：
               将 char 压入栈
       将栈中的字符连接成字符串并返回
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度，因为每个字符最多被压入和弹出栈一次。
   - 空间复杂度：$O(n)$，因为在最坏情况下，栈可能会存储所有字符。