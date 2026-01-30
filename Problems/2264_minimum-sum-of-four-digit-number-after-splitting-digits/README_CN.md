# 2264. 拆分数位后四位数字的最小和

**难度**: Easy | **标签**: `Math` `Greedy` `Sorting`

## 题目描述

<p>给你一个四位&nbsp;<strong>正</strong>&nbsp;整数&nbsp;<code>num</code>&nbsp;。请你使用 <code>num</code>&nbsp;中的 <strong>数位</strong> ，将&nbsp;<code>num</code>&nbsp;拆成两个新的整数&nbsp;<code>new1</code>&nbsp;和&nbsp;<code>new2</code>&nbsp;。<code>new1</code> 和&nbsp;<code>new2</code>&nbsp;中可以有&nbsp;<strong>前导 0</strong>&nbsp;，且&nbsp;<code>num</code>&nbsp;中 <strong>所有</strong>&nbsp;数位都必须使用。</p>

<ul>
	<li>比方说，给你&nbsp;<code>num = 2932</code>&nbsp;，你拥有的数位包括：两个&nbsp;<code>2</code>&nbsp;，一个&nbsp;<code>9</code>&nbsp;和一个&nbsp;<code>3</code>&nbsp;。一些可能的&nbsp;<code>[new1, new2]</code>&nbsp;数对为&nbsp;<code>[22, 93]</code>，<code>[23, 92]</code>，<code>[223, 9]</code> 和&nbsp;<code>[2, 329]</code>&nbsp;。</li>
</ul>

<p>请你返回可以得到的&nbsp;<code>new1</code>&nbsp;和 <code>new2</code>&nbsp;的 <strong>最小</strong>&nbsp;和。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>num = 2932
<b>输出：</b>52
<b>解释：</b>可行的 [new1, new2] 数对为 [29, 23] ，[223, 9] 等等。
最小和为数对 [29, 23] 的和：29 + 23 = 52 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>num = 4009
<b>输出：</b>13
<b>解释：</b>可行的 [new1, new2] 数对为 [0, 49] ，[490, 0] 等等。
最小和为数对 [4, 9] 的和：4 + 9 = 13 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1000 &lt;= num &lt;= 9999</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过对四位数字进行排序后，构造两个最小的两位数以获得最小和。

2. 综合思路：
   - 排序法：将四位数字拆分并排序，然后通过组合最小的两位数来求和。
   - 由于题目简单，通常只需一种直接的排序和组合方法即可解决问题。

3. 全量伪代码：
   ```
   定义函数 minimumSum(num):
       将 num 转换为字符串并拆分为字符列表 nums
       对 nums 进行排序
       将 nums 中的最小两个数字组合成一个两位数 num1
       将 nums 中的次小两个数字组合成另一个两位数 num2
       返回 num1 和 num2 的和
   ```

4. 复杂度：
   - 时间复杂度：$O(1)$，因为输入的数字固定为四位数，排序和组合操作都是常数时间。
   - 空间复杂度：$O(1)$，因为使用的额外空间不随输入大小变化。