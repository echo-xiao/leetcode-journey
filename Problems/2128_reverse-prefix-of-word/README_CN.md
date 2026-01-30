# 2128. 反转单词前缀

**难度**: Easy | **标签**: `Two Pointers` `String` `Stack`

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的字符串 <code>word</code> 和一个字符 <code>ch</code> 。找出 <code>ch</code> 第一次出现的下标 <code>i</code> ，<strong>反转 </strong><code>word</code> 中从下标 <code>0</code> 开始、直到下标 <code>i</code> 结束（含下标 <code>i</code> ）的那段字符。如果 <code>word</code> 中不存在字符 <code>ch</code> ，则无需进行任何操作。</p>

<ul>
	<li>例如，如果 <code>word = "abcdefd"</code> 且 <code>ch = 'd'</code>&nbsp;，那么你应该 <strong>反转</strong> 从下标 0 开始、直到下标 <code>3</code> 结束（含下标 <code>3</code> ）。结果字符串将会是 <code>"<em><strong>dcba</strong></em>efd"</code> 。</li>
</ul>

<p>返回 <strong>结果字符串</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>word = "<em><strong>abcd</strong></em>efd", ch = 'd'
<strong>输出：</strong>"<em><strong>dcba</strong></em>efd"
<strong>解释：</strong>"d" 第一次出现在下标 3 。 
反转从下标 0 到下标 3（含下标 3）的这段字符，结果字符串是 "dcbaefd" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>word = "<em><strong>xyxz</strong></em>xe", ch = 'z'
<strong>输出：</strong>"<em><strong>zxyx</strong></em>xe"
<strong>解释：</strong>"z" 第一次也是唯一一次出现是在下标 3 。
反转从下标 0 到下标 3（含下标 3）的这段字符，结果字符串是 "zxyxxe" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>word = "abcd", ch = 'z'
<strong>输出：</strong>"abcd"
<strong>解释：</strong>"z" 不存在于 word 中。
无需执行反转操作，结果字符串是 "abcd" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 250</code></li>
	<li><code>word</code> 由小写英文字母组成</li>
	<li><code>ch</code> 是一个小写英文字母</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是找到目标字符在字符串中的位置，然后反转从字符串开头到该位置的子字符串。

2. 综合思路：
   - 迭代法：通过迭代找到目标字符的位置，然后使用栈数据结构来反转从字符串开头到该位置的子字符串。
   - 直接切片法（未在提供的代码中出现，但常见于此类问题）：直接使用字符串切片和反转操作来实现相同的功能。

3. 全量伪代码：
   - 迭代法：
     ```
     初始化一个空栈
     尝试在字符串中找到目标字符的位置
     如果找不到目标字符，返回原字符串
     否则，遍历从字符串开头到目标字符位置的子字符串，将每个字符压入栈中
     初始化一个结果列表
     当栈不为空时，将栈顶元素弹出并添加到结果列表中
     将结果列表转换为字符串，并连接上从目标字符位置之后的子字符串
     返回最终字符串
     ```
   - 直接切片法（假设存在）：
     ```
     尝试在字符串中找到目标字符的位置
     如果找不到目标字符，返回原字符串
     否则，使用字符串切片和反转操作反转从字符串开头到目标字符位置的子字符串
     将反转后的子字符串与目标字符位置之后的子字符串连接
     返回最终字符串
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度，因为在最坏情况下需要遍历整个字符串来找到目标字符的位置。
   - 空间复杂度：$O(n)$，因为使用了栈来存储子字符串的字符。