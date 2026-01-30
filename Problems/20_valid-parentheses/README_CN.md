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

1. **一句话直击本质**：通过栈结构匹配括号的开闭关系，确保每个闭括号都能正确匹配到最近的开括号。

2. **综合思路**：
   - **迭代法**：使用栈数据结构遍历字符串，遇到开括号时将其对应的闭括号或开括号本身压入栈中，遇到闭括号时检查栈顶元素是否匹配，匹配则弹出栈顶元素，否则返回 `False`。
   - **数据结构**：所有实现均使用栈（`stack`）来管理括号的匹配过程。

3. **全量伪代码**：
   ```plaintext
   初始化一个空栈
   定义括号匹配规则（如：'(': ')', '{': '}', '[': ']' 或反向）
   
   对于字符串中的每个字符：
       如果字符是开括号：
           将对应的闭括号或开括号本身压入栈
       如果字符是闭括号：
           如果栈为空：
               返回 False
           弹出栈顶元素
           如果栈顶元素与当前闭括号不匹配：
               返回 False
   
   如果栈为空：
       返回 True
   否则：
       返回 False
   ```

4. **复杂度**：
   - 时间复杂度：$\mathcal{O}(n)$，其中 $n$ 是字符串的长度，因为每个字符最多被压入和弹出栈一次。
   - 空间复杂度：$\mathcal{O}(n)$，在最坏情况下，栈可能需要存储所有的开括号。