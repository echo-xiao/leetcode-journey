# 1737. 括号的最大嵌套深度

**难度**: Easy | **标签**: `String` `Stack`

## 题目描述

<p>给定 <strong>有效括号字符串</strong> <code>s</code>，返回 <code>s</code> 的 <strong>嵌套深度</strong>。嵌套深度是嵌套括号的 <strong>最大</strong> 数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>s = "(1+(2*3)+((<strong>8</strong>)/4))+1"</p>

<p><strong>输出：</strong>3</p>

<p><strong>解释：</strong>数字 8 在嵌套的 3 层括号中。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>s = "(1)+((2))+(((<strong>3</strong>)))"</p>

<p><strong>输出：</strong>3</p>

<p><strong>解释：</strong>数字 3 在嵌套的 3 层括号中。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "()(())((()()))"</span></p>

<p><strong>输出：</strong><span class="example-io">3</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 由数字 <code>0-9</code> 和字符 <code>'+'</code>、<code>'-'</code>、<code>'*'</code>、<code>'/'</code>、<code>'('</code>、<code>')'</code> 组成</li>
	<li>题目数据保证括号字符串&nbsp;<code>s</code> 是 <strong>有效的括号字符串</strong></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过遍历字符串并使用栈记录当前括号嵌套层数，实时更新最大嵌套深度。

2. 综合思路：
   - **栈方法**：遍历字符串，遇到左括号时入栈，遇到右括号时出栈，栈的最大深度即为括号的最大嵌套深度。
   - **计数器方法**：使用一个计数器代替栈，遇到左括号时计数器加一，遇到右括号时计数器减一，计数器的最大值即为最大嵌套深度。

3. 全量伪代码：
   - **栈方法伪代码**：
     ```
     初始化一个空栈
     初始化最大深度为0
     对于字符串中的每个字符：
         如果字符是左括号：
             将字符入栈
         如果字符是右括号：
             从栈中弹出一个元素
         更新最大深度为当前栈的大小和最大深度中的较大值
     返回最大深度
     ```
   - **计数器方法伪代码**：
     ```
     初始化计数器为0
     初始化最大深度为0
     对于字符串中的每个字符：
         如果字符是左括号：
             计数器加一
             更新最大深度为计数器和最大深度中的较大值
         如果字符是右括号：
             计数器减一
     返回最大深度
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度，因为每个字符只被遍历一次。
   - 空间复杂度：$O(n)$，在栈方法中，最坏情况下栈的大小可能达到字符串长度的一半。对于计数器方法，空间复杂度为 $O(1)$。