# 3447. 清除数字

**难度**: Easy | **标签**: `String` `Stack` `Simulation`

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;。</p>

<p>你的任务是重复以下操作删除 <strong>所有</strong>&nbsp;数字字符：</p>

<ul>
	<li>删除 <strong>第一个数字字符</strong>&nbsp;以及它左边 <strong>最近</strong>&nbsp;的 <strong>非数字</strong>&nbsp;字符。</li>
</ul>

<p>请你返回删除所有数字字符以后剩下的字符串。</p>

<p><strong>注意</strong>，该操作不能对左侧没有任何非数字字符的数字执行。</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "abc"</span></p>

<p><span class="example-io"><b>输出：</b>"abc"</span></p>

<p><strong>解释：</strong></p>

<p>字符串中没有数字。<!-- notionvc: ff07e34f-b1d6-41fb-9f83-5d0ba3c1ecde --></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "cb34"</span></p>

<p><span class="example-io"><b>输出：</b>""</span></p>

<p><b>解释：</b></p>

<p>一开始，我们对&nbsp;<code>s[2]</code>&nbsp;执行操作，<code>s</code>&nbsp;变为&nbsp;<code>"c4"</code>&nbsp;。</p>

<p>然后对&nbsp;<code>s[1]</code>&nbsp;执行操作，<code>s</code>&nbsp;变为&nbsp;<code>""</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母和数字字符。</li>
	<li>输入保证所有数字都可以按以上操作被删除。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：利用栈结构遍历字符串，遇到字母入栈，遇到数字则出栈，从而实现清除数字对应数量的字母。

2. 综合思路：
   - 迭代法：通过遍历字符串，使用栈来处理字母和数字的逻辑。字母入栈，数字则尝试从栈中弹出元素。
   - 递归法：虽然当前代码集中没有递归实现，但可以设想递归地处理字符串，遇到字母递归地加入结果，遇到数字则递归地从结果中移除元素。

3. 全量伪代码：
   ```
   方法 clearDigits(输入字符串 s):
       初始化一个空栈 stack

       对于字符串 s 中的每个字符 element:
           如果 element 是字母:
               将 element 压入栈 stack
           否则如果 element 是数字:
               如果栈 stack 不为空:
                   从栈 stack 弹出一个元素

       返回通过连接栈 stack 中所有元素形成的字符串
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度，因为每个字符只被处理一次。
   - 空间复杂度：$O(n)$，在最坏情况下，栈可能需要存储所有的字母字符。