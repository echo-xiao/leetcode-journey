# 1341. 分割平衡字符串

**难度**: Easy | **标签**: `String` `Greedy` `Counting`

## 题目描述

<p><strong>平衡字符串</strong> 中，<code>'L'</code> 和 <code>'R'</code> 字符的数量是相同的。</p>

<p>给你一个平衡字符串&nbsp;<code>s</code>，请你将它分割成尽可能多的子字符串，并满足：</p>

<ul>
	<li>每个子字符串都是平衡字符串。</li>
</ul>

<p>返回可以通过分割得到的平衡字符串的 <strong>最大数量</strong> <strong>。</strong></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "RLRRLLRLRL"
<strong>输出：</strong>4
<strong>解释：</strong>s 可以分割为 "RL"、"RRLL"、"RL"、"RL" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "RLRRRLLRLL"
<strong>输出：</strong>2
<strong>解释：</strong>s 可以分割为 "RL"、"RRRLLRLL"，每个子字符串中都包含相同数量的 'L' 和 'R' 。
注意，s 无法分割为 "RL"、"RR"、"RL"、"LR"、"LL" 因为第 2 个和第 5 个子字符串不是平衡字符串。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "LLLLRRRR"
<strong>输出：</strong>1
<strong>解释：</strong>s 只能保持原样 "LLLLRRRR" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i] = 'L' 或 'R'</code></li>
	<li><code>s</code> 是一个 <strong>平衡</strong> 字符串</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过遍历字符串并维护一个计数器，当计数器归零时，记录一次平衡字符串的分割。

2. 综合思路：
   - 迭代法：使用一个计数器遍历字符串，遇到字符 'R' 增加计数器，遇到字符 'L' 减少计数器，当计数器为零时，说明找到了一个平衡的子字符串，增加结果计数。
   - 该题目主要采用迭代法实现，没有递归或其他复杂的数据结构。

3. 全量伪代码：
   ```
   定义函数 balancedStringSplit(s: 字符串) -> 整数:
       初始化计数器 cnt 为 0
       初始化结果计数 res 为 0
       
       对于字符串 s 中的每个字符 i:
           如果字符 i 是 'R':
               计数器 cnt 增加 1
           否则如果字符 i 是 'L':
               计数器 cnt 减少 1
           
           如果计数器 cnt 为 0:
               结果计数 res 增加 1
       
       返回结果计数 res
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度，因为我们只需遍历字符串一次。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外的变量。