# 2800. 删除子串后的字符串最小长度

**难度**: Easy | **标签**: `String` `Stack` `Simulation`

## 题目描述

<p>给你一个仅由 <strong>大写</strong> 英文字符组成的字符串 <code>s</code> 。</p>

<p>你可以对此字符串执行一些操作，在每一步操作中，你可以从 <code>s</code> 中删除 <strong>任一个</strong> <code>"AB"</code> 或 <code>"CD"</code> 子字符串。</p>

<p>通过执行操作，删除所有&nbsp;<code>"AB"</code> 和 <code>"CD"</code> 子串，返回可获得的最终字符串的 <strong>最小</strong> 可能长度。</p>

<p><strong>注意</strong>，删除子串后，重新连接出的字符串可能会产生新的&nbsp;<code>"AB"</code> 或 <code>"CD"</code> 子串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "ABFCACDB"
<strong>输出：</strong>2
<strong>解释：</strong>你可以执行下述操作：
- 从 "<em><strong>AB</strong></em>FCACDB" 中删除子串 "AB"，得到 s = "FCACDB" 。
- 从 "FCA<em><strong>CD</strong></em>B" 中删除子串 "CD"，得到 s = "FCAB" 。
- 从 "FC<strong><em>AB</em></strong>" 中删除子串 "AB"，得到 s = "FC" 。
最终字符串的长度为 2 。
可以证明 2 是可获得的最小长度。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "ACBBD"
<strong>输出：</strong>5
<strong>解释：</strong>无法执行操作，字符串长度不变。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 仅由大写英文字母组成</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用栈来消除满足条件的相邻字符对，从而得到删除子串后的最小字符串长度。

2. 综合思路：
   - 栈方法：遍历字符串，使用栈来存储字符，当遇到特定的相邻字符对（如 'AB' 或 'CD'）时，弹出栈顶元素以模拟删除操作。

3. 全量伪代码：
   ```plaintext
   定义函数 minLength(s: 字符串) -> 整数:
       初始化一个空栈 stack

       对于字符串 s 中的每个字符 char:
           如果栈不为空:
               获取栈顶元素 top
               如果 top 和 char 形成 'AB' 或 'CD':
                   弹出栈顶元素
               否则:
                   将 char 压入栈
           否则:
               将 char 压入栈

       返回栈的长度作为结果
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度，因为每个字符最多只会被压入和弹出栈一次。
   - 空间复杂度：$O(n)$，在最坏情况下，栈可能会存储所有字符。