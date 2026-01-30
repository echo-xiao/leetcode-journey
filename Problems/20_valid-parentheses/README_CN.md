# 20. 有效的括号

**难度**: Easy | **标签**: `String` `Stack`

## 题目描述

<p>给定一个只包括 <code>'('</code>，<code>')'</code>，<code>'{'</code>，<code>'}'</code>，<code>'['</code>，<code>']'</code>&nbsp;的字符串 <code>s</code> ，判断字符串是否有效。</p>

<p>有效字符串需满足：</p>

<ol>
	<li>左括号必须用相同类型的右括号闭合。</li>
	<li>左括号必须以正确的顺序闭合。</li>
	<li>每个右括号都有一个对应的相同类型的左括号。</li>
</ol>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "()"</span></p>

<p><span class="example-io"><b>输出：</b>true</span></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "()[]{}"</span></p>

<p><span class="example-io"><b>输出：</b>true</span></p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "(]"</span></p>

<p><span class="example-io"><b>输出：</b>false</span></p>
</div>

<p><strong class="example">示例 4：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "([])"</span></p>

<p><span class="example-io"><b>输出：</b>true</span></p>
</div>

<p><strong class="example">示例 5：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "([)]"</span></p>

<p><span class="example-io"><b>输出：</b>false</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> 仅由括号 <code>'()[]{}'</code> 组成</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 使用栈数据结构来匹配括号的开闭关系，确保每个闭括号都能正确匹配到最近的开括号。

2. **综合思路：**
   - **栈匹配法：** 通过遍历字符串，将开括号压入栈中，遇到闭括号时检查栈顶元素是否匹配，匹配则弹出栈顶元素，否则返回 `False`。最终栈为空则表示括号匹配有效。
   - **映射匹配法：** 使用字典映射每个闭括号到对应的开括号，遍历字符串时，遇到闭括号检查栈顶是否匹配，匹配则弹出栈顶元素，否则返回 `False`。

3. **全量伪代码：**

   - **栈匹配法：**
     ```
     初始化一个空栈 stack
     遍历字符串 s 中的每个字符 char
         如果 char 是开括号
             将 char 压入栈 stack
         否则如果 char 是闭括号
             如果栈为空，返回 False
             弹出栈顶元素 top
             如果 top 和 char 不匹配，返回 False
     如果栈为空，返回 True，否则返回 False
     ```

   - **映射匹配法：**
     ```
     初始化一个字典 mapp 映射闭括号到开括号
     初始化一个空栈 stack
     遍历字符串 s 中的每个字符 char
         如果 char 是闭括号
             如果栈为空，返回 False
             弹出栈顶元素 top
             如果 mapp[char] 不等于 top，返回 False
         否则将 char 压入栈 stack
     如果栈为空，返回 True，否则返回 False
     ```

4. **复杂度：**

   - **时间复杂度：** $O(n)$，其中 $n$ 是字符串的长度，因为每个字符最多被压入和弹出栈一次。
   - **空间复杂度：** $O(n)$，在最坏情况下，栈可能需要存储所有的开括号。