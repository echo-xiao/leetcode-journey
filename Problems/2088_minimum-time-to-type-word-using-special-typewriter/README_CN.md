# 2088. 使用特殊打字机键入单词的最少时间

**难度**: Easy | **标签**: `String` `Greedy`

## 题目描述

<p>有一个特殊打字机，它由一个 <strong>圆盘</strong> 和一个 <strong>指针</strong>&nbsp;组成， 圆盘上标有小写英文字母&nbsp;<code>'a'</code> 到&nbsp;<code>'z'</code>。<strong>只有</strong>&nbsp;当指针指向某个字母时，它才能被键入。指针 <strong>初始时</strong>&nbsp;指向字符 <code>'a'</code>&nbsp;。</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/31/chart.jpg" style="width: 530px; height: 410px;" />
<p>每一秒钟，你可以执行以下操作之一：</p>

<ul>
	<li>将指针 <strong>顺时针</strong>&nbsp;或者 <b>逆时针</b>&nbsp;移动一个字符。</li>
	<li>键入指针 <strong>当前</strong>&nbsp;指向的字符。</li>
</ul>

<p>给你一个字符串&nbsp;<code>word</code>&nbsp;，请你返回键入&nbsp;<code>word</code>&nbsp;所表示单词的 <b>最少</b>&nbsp;秒数&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>word = "abc"
<b>输出：</b>5
<strong>解释：
</strong>单词按如下操作键入：
- 花 1 秒键入字符 'a' in 1 ，因为指针初始指向 'a' ，故不需移动指针。
- 花 1 秒将指针顺时针移到 'b' 。
- 花 1 秒键入字符 'b' 。
- 花 1 秒将指针顺时针移到 'c' 。
- 花 1 秒键入字符 'c' 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>word = "bza"
<b>输出：</b>7
<strong>解释：
</strong>单词按如下操作键入：
- 花 1 秒将指针顺时针移到 'b' 。
- 花 1 秒键入字符 'b' 。
- 花 2 秒将指针逆时针移到 'z' 。
- 花 1 秒键入字符 'z' 。
- 花 1 秒将指针顺时针移到 'a' 。
- 花 1 秒键入字符 'a' 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>word = "zjpc"
<b>输出：</b>34
<strong>解释：</strong>
单词按如下操作键入：
- 花 1 秒将指针逆时针移到 'z' 。
- 花 1 秒键入字符 'z' 。
- 花 10 秒将指针顺时针移到 'j' 。
- 花 1 秒键入字符 'j' 。
- 花 6 秒将指针顺时针移到 'p' 。
- 花 1 秒键入字符 'p' 。
- 花 13 秒将指针逆时针移到 'c' 。
- 花 1 秒键入字符 'c' 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 100</code></li>
	<li><code>word</code>&nbsp;只包含小写英文字母。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是计算从当前字符到目标字符的最短旋转距离，并累加每次移动和输入的时间。

2. 综合思路：
   - 迭代法：通过遍历目标字符串中的每个字符，计算从当前字符到目标字符的最短旋转距离，更新当前位置，并累加时间。
   - 不同实现方式：一种使用字符在字母表中的索引来计算距离，另一种直接使用 ASCII 值来计算距离。

3. 全量伪代码：
   ```plaintext
   初始化结果时间 res 为 0
   初始化当前字符 curr 为 'a'
   定义字母表 alpha 为 "abcdefghijklmnopqrstuvwxyz"

   对于目标单词 word 中的每个字符 w：
       计算当前字符 curr 在字母表中的位置 pos2
       计算目标字符 w 在字母表中的位置 pos1
       计算顺时针距离 dis1 为 |pos1 - pos2|
       计算逆时针距离 dis2 为 |26 - dis1|
       选择最小的距离 disf 为 min(dis1, dis2) + 1
       将 disf 累加到结果时间 res
       更新当前字符 curr 为 w

   返回结果时间 res
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是目标单词的长度，因为需要遍历每个字符。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外变量。