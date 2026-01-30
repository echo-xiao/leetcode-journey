# 2816. 字典序最小回文串

**难度**: Easy | **标签**: `Two Pointers` `String` `Greedy`

## 题目描述

<p>给你一个由 <strong>小写英文字母</strong> 组成的字符串 <code>s</code> ，你可以对其执行一些操作。在一步操作中，你可以用其他小写英文字母 <strong>替换</strong>&nbsp; <code>s</code> 中的一个字符。</p>

<p>请你执行 <strong>尽可能少的操作</strong> ，使 <code>s</code> 变成一个 <strong>回文串</strong> 。如果执行 <strong>最少</strong> 操作次数的方案不止一种，则只需选取 <strong>字典序最小</strong> 的方案。</p>

<p>对于两个长度相同的字符串 <code>a</code> 和 <code>b</code> ，在 <code>a</code> 和 <code>b</code> 出现不同的第一个位置，如果该位置上 <code>a</code> 中对应字母比 <code>b</code> 中对应字母在字母表中出现顺序更早，则认为 <code>a</code> 的字典序比 <code>b</code> 的字典序要小。</p>

<p>返回最终的回文字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "egcfe"
<strong>输出：</strong>"efcfe"
<strong>解释：</strong>将 "egcfe" 变成回文字符串的最小操作次数为 1 ，修改 1 次得到的字典序最小回文字符串是 "efcfe"，只需将 'g' 改为 'f' 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abcd"
<strong>输出：</strong>"abba"
<strong>解释：</strong>将 "abcd" 变成回文字符串的最小操作次数为 2 ，修改 2 次得到的字典序最小回文字符串是 "abba" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "seven"
<strong>输出：</strong>"neven"
<strong>解释：</strong>将 "seven" 变成回文字符串的最小操作次数为 1 ，修改 1 次得到的字典序最小回文字符串是 "neven" 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过双指针从两端向中间遍历字符串，将不相等的字符替换为字典序较小的字符，以构造字典序最小的回文串。

2. 综合思路：
   - 双指针法：使用两个指针分别从字符串的两端向中间移动，比较对应位置的字符，将较大的字符替换为较小的字符，确保最终字符串是回文且字典序最小。

3. 全量伪代码：
   ```
   定义函数 makeSmallestPalindrome，输入为字符串 s
       将字符串 s 转换为字符列表 string
       初始化左指针 i 为 0
       初始化右指针 j 为字符串长度减 1
       
       当 i 小于 j 时，重复以下步骤：
           如果 string[i] 的字典序小于 string[j]
               将 string[j] 替换为 string[i]
           否则如果 string[i] 的字典序大于 string[j]
               将 string[i] 替换为 string[j]
           将左指针 i 增加 1
           将右指针 j 减少 1
       
       将字符列表 string 转换回字符串并返回
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度，因为每个字符最多被访问一次。
   - 空间复杂度：$O(n)$，用于存储字符列表的空间。