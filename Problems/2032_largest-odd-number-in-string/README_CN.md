# 2032. 字符串中的最大奇数

**难度**: Easy | **标签**: `Math` `String` `Greedy`

## 题目描述

<p>给你一个字符串 <code>num</code> ，表示一个大整数。请你在字符串 <code>num</code> 的所有 <strong>非空子字符串</strong> 中找出 <strong>值最大的奇数</strong> ，并以字符串形式返回。如果不存在奇数，则返回一个空字符串<em> </em><code>""</code><em> </em>。</p>

<p><strong>子字符串</strong> 是字符串中的一个连续的字符序列。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>num = "52"
<strong>输出：</strong>"5"
<strong>解释：</strong>非空子字符串仅有 "5"、"2" 和 "52" 。"5" 是其中唯一的奇数。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>num = "4206"
<strong>输出：</strong>""
<strong>解释：</strong>在 "4206" 中不存在奇数。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>num = "35427"
<strong>输出：</strong>"35427"
<strong>解释：</strong>"35427" 本身就是一个奇数。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= num.length <= 10<sup>5</sup></code></li>
	<li><code>num</code> 仅由数字组成且不含前导零</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：从字符串末尾向前遍历，找到第一个奇数并返回从开头到该位置的子字符串。

2. 综合思路：
   - 迭代法：从字符串的末尾向前遍历，找到第一个奇数位置，返回从开头到该位置的子字符串。
   - 递归法：虽然在这个问题中不常用，但可以通过递归从末尾向前检查每个字符是否为奇数，找到第一个奇数后返回结果。

3. 全量伪代码：
   - 迭代法：
     ```
     定义函数 largestOddNumber(num)
         从字符串 num 的末尾向前遍历每个字符 i
             如果 num[i] 是奇数
                 返回 num 从开头到 i 的子字符串
         返回空字符串
     ```
   - 递归法（假设实现）：
     ```
     定义递归函数 findLargestOdd(num, index)
         如果 index 小于 0
             返回空字符串
         如果 num[index] 是奇数
             返回 num 从开头到 index 的子字符串
         否则
             调用 findLargestOdd(num, index - 1)
     
     定义函数 largestOddNumber(num)
         返回 findLargestOdd(num, len(num) - 1)
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度，因为在最坏情况下需要遍历整个字符串。
   - 空间复杂度：$O(1)$，因为只使用了常数额外空间。