# 874. 比较含退格的字符串

**难度**: Easy | **标签**: `Two Pointers` `String` `Stack` `Simulation`

## 题目描述

<p>给定 <code>s</code> 和 <code>t</code> 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 <code>true</code> 。<code>#</code> 代表退格字符。</p>

<p><strong>注意：</strong>如果对空文本输入退格字符，文本继续为空。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "ab#c", t = "ad#c"
<strong>输出：</strong>true
<strong>解释：</strong>s 和 t 都会变成 "ac"。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "ab##", t = "c#d#"
<strong>输出：</strong>true
<strong>解释：</strong>s 和 t 都会变成 ""。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "a#c", t = "b"
<strong>输出：</strong>false
<strong>解释：</strong>s 会变成 "c"，但 t 仍然是 "b"。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 200</code></li>
	<li><code>s</code> 和 <code>t</code> 只含有小写字母以及字符 <code>'#'</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>你可以用 <code>O(n)</code> 的时间复杂度和 <code>O(1)</code> 的空间复杂度解决该问题吗？</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过模拟退格操作构建最终字符串并比较。

2. **综合思路：**
   - **栈模拟法：** 使用栈数据结构模拟字符串的退格操作，逐字符处理，遇到退格符则弹出栈顶元素，最终比较两个栈的内容。
   - **双指针法（未在提供代码中出现，但常见于此类问题）：** 从后向前遍历字符串，跳过退格符影响的字符，直接比较有效字符。

3. **全量伪代码：**

   - **栈模拟法：**
     ```
     定义函数 backspaceCompare(s, t):
         返回 buildStack(s) 是否等于 buildStack(t)

     定义函数 buildStack(nums):
         初始化空栈 stack
         对于 nums 中的每个字符 n:
             如果 n 不是 '#':
                 将 n 压入栈 stack
             否则如果栈 stack 不为空:
                 弹出栈顶元素
         返回栈 stack
     ```

   - **双指针法（伪代码示例）：**
     ```
     定义函数 backspaceCompare(s, t):
         初始化指针 i 为 s 的末尾
         初始化指针 j 为 t 的末尾
         当 i 和 j 都大于等于 0 时:
             初始化 skipS 和 skipT 为 0
             当 i 大于等于 0:
                 如果 s[i] 是 '#':
                     增加 skipS
                     减少 i
                 否则如果 skipS 大于 0:
                     减少 skipS
                     减少 i
                 否则:
                     退出循环
             当 j 大于等于 0:
                 如果 t[j] 是 '#':
                     增加 skipT
                     减少 j
                 否则如果 skipT 大于 0:
                     减少 skipT
                     减少 j
                 否则:
                     退出循环
             如果 i 和 j 都大于等于 0 且 s[i] 不等于 t[j]:
                 返回 False
             如果 i 大于等于 0 或 j 大于等于 0:
                 返回 False
         返回 True
     ```

4. **复杂度：**
   - **时间复杂度：** $O(n + m)$，其中 $n$ 和 $m$ 分别是字符串 $s$ 和 $t$ 的长度，因为每个字符最多被处理一次。
   - **空间复杂度：** $O(n + m)$，在栈模拟法中，最坏情况下栈需要存储所有字符。