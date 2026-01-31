# 20. 有效的括号

**难度**: Easy | **标签**: `String` `Stack`

**归类**: 8. 常用数据结构 > String

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

1. **一句话直击本质：** 使用栈数据结构来匹配括号的开闭关系，确保每个闭括号都能正确匹配到其对应的开括号。

2. **综合思路：**
   - **迭代法（使用栈）：** 遍历字符串中的每个字符，遇到开括号时将其对应的闭括号或自身压入栈中，遇到闭括号时检查栈顶元素是否匹配，若匹配则弹出栈顶元素，否则返回 `False`；最后检查栈是否为空以确定括号是否完全匹配。
   - **映射法（使用字典和栈）：** 使用字典存储括号的对应关系，遍历字符串时，若字符为闭括号则检查栈顶元素是否为其对应的开括号，若匹配则弹出栈顶元素，否则返回 `False`；若字符为开括号则压入栈中，最后检查栈是否为空。

3. **全量伪代码：**

   - **版本 1 伪代码：**
     ```
     初始化空栈 stack
     初始化字典 mapp 存储开闭括号对应关系
     对于字符串 s 中的每个字符 char:
         如果 char 是开括号:
             将对应的闭括号压入栈 stack
         否则:
             如果栈不为空且栈顶元素等于 char:
                 弹出栈顶元素
             否则:
                 返回 False
     如果栈为空:
         返回 True
     否则:
         返回 False
     ```

   - **版本 2 和 3 伪代码：**
     ```
     初始化空栈 stack
     对于字符串 s 中的每个字符 i:
         如果 i 是开括号:
             将 i 压入栈 stack
         否则如果 i 是闭括号:
             如果栈为空:
                 返回 False
             如果栈顶元素与 i 匹配:
                 弹出栈顶元素
             否则:
                 返回 False
     如果栈为空:
         返回 True
     否则:
         返回 False
     ```

   - **版本 4 伪代码：**
     ```
     初始化字典 mapp 存储闭括号到开括号的对应关系
     初始化空栈 stack
     对于字符串 s 中的每个字符 char:
         如果 char 是闭括号:
             如果栈为空或栈顶元素不匹配:
                 返回 False
             弹出栈顶元素
         否则:
             将 char 压入栈 stack
     如果栈为空:
         返回 True
     否则:
         返回 False
     ```

4. **复杂度：**
   - **时间复杂度：** $O(n)$，其中 $n$ 是字符串的长度，因为每个字符最多被压入和弹出栈一次。
   - **空间复杂度：** $O(n)$，在最坏情况下（例如所有字符都是开括号）栈可能需要存储所有字符。