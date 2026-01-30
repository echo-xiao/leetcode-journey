# 2704. 替换一个数字后的最大差值

**难度**: Easy | **标签**: `Math` `Greedy`

## 题目描述

<p>给你一个整数&nbsp;<code>num</code>&nbsp;。你知道 Danny Mittal 会偷偷将 <code>0</code>&nbsp;到 <code>9</code>&nbsp;中的一个数字 <strong>替换</strong> 成另一个数字。</p>

<p>请你返回将 <code>num</code>&nbsp;中&nbsp;<strong>恰好一个</strong>&nbsp;数字进行替换后，得到的最大值和最小值的差为多少。</p>

<p><strong>注意：</strong></p>

<ul>
	<li>当 Danny 将一个数字 <code>d1</code> 替换成另一个数字 <code>d2</code> 时，Danny 需要将&nbsp;<code>num</code>&nbsp;中所有 <code>d1</code>&nbsp;都替换成&nbsp;<code>d2</code>&nbsp;。</li>
	<li>Danny 可以将一个数字替换成它自己，也就是说&nbsp;<code>num</code>&nbsp;可以不变。</li>
	<li>Danny 可以将数字分别替换成两个不同的数字分别得到最大值和最小值。</li>
	<li>替换后得到的数字可以包含前导 0 。</li>
	<li>Danny Mittal 获得周赛 326 前 10 名，让我们恭喜他。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>num = 11891
<b>输出：</b>99009
<b>解释：</b>
为了得到最大值，我们将数字 1 替换成数字 9 ，得到 99899 。
为了得到最小值，我们将数字 1 替换成数字 0 ，得到 890 。
两个数字的差值为 99009 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>num = 90
<b>输出：</b>99
<strong>解释：</strong>
可以得到的最大值是 99（将 0 替换成 9），最小值是 0（将 9 替换成 0）。
所以我们得到 99 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 10<sup>8</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过替换数字字符串中的第一个非目标数字（非'9'或非'0'）为目标数字（'9'或'0'），计算最大和最小可能值的差。

2. 综合思路：
   - **字符串替换法**：将数字转换为字符串，找到第一个非'9'的字符替换为'9'以获得最大值，找到第一个非'0'的字符替换为'0'以获得最小值。
   - **列表操作法**：将数字转换为字符列表，类似地进行替换操作，通过列表操作实现字符串替换的效果。

3. 全量伪代码：
   ```plaintext
   函数 minMaxDifference(输入数字 num):
       将 num 转换为字符串 s
       
       # 计算最大值
       初始化 target 为 ''
       对于字符串 s 中的每个字符 char:
           如果 char 不是 '9':
               将 target 设为 char
               跳出循环
       如果 target 不为空:
           将 s 中的 target 替换为 '9' 得到 maxS
       否则:
           maxS = s

       # 计算最小值
       初始化 target 为 ''
       对于字符串 s 中的每个字符 char:
           如果 char 不是 '0':
               将 target 设为 char
               跳出循环
       如果 target 不为空:
           将 s 中的 target 替换为 '0' 得到 minS
       否则:
           minS = s

       返回 int(maxS) - int(minS)
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是数字转换为字符串后的长度，因为需要遍历字符串两次。
   - 空间复杂度：$O(n)$，用于存储字符串的副本。