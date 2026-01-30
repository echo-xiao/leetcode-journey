# 1873. 最长的美好子字符串

**难度**: Easy | **标签**: `Hash Table` `String` `Divide and Conquer` `Bit Manipulation` `Sliding Window`

## 题目描述

<p>当一个字符串 <code>s</code> 包含的每一种字母的大写和小写形式 <strong>同时</strong> 出现在 <code>s</code> 中，就称这个字符串 <code>s</code> 是 <strong>美好</strong> 字符串。比方说，<code>"abABB"</code> 是美好字符串，因为 <code>'A'</code> 和 <code>'a'</code> 同时出现了，且 <code>'B'</code> 和 <code>'b'</code> 也同时出现了。然而，<code>"abA"</code> 不是美好字符串因为 <code>'b'</code> 出现了，而 <code>'B'</code> 没有出现。</p>

<p>给你一个字符串 <code>s</code> ，请你返回 <code>s</code> 最长的 <strong>美好子字符串</strong> 。如果有多个答案，请你返回 <strong>最早</strong> 出现的一个。如果不存在美好子字符串，请你返回一个空字符串。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "YazaAay"
<b>输出：</b>"aAa"
<strong>解释：</strong>"aAa" 是一个美好字符串，因为这个子串中仅含一种字母，其小写形式 'a' 和大写形式 'A' 也同时出现了。
"aAa" 是最长的美好子字符串。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "Bb"
<b>输出：</b>"Bb"
<b>解释：</b>"Bb" 是美好字符串，因为 'B' 和 'b' 都出现了。整个字符串也是原字符串的子字符串。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>s = "c"
<b>输出：</b>""
<b>解释：</b>没有美好子字符串。</pre>

<p><strong>示例 4：</strong></p>

<pre>
<b>输入：</b>s = "dDzeE"
<b>输出：</b>"dD"
<strong>解释：</strong>"dD" 和 "eE" 都是最长美好子字符串。
由于有多个美好子字符串，返回 "dD" ，因为它出现得最早。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 100</code></li>
	<li><code>s</code> 只包含大写和小写英文字母。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过递归或滑动窗口方法，寻找满足条件的最长子字符串，其中每个字母的大小写形式都存在。

2. 综合思路：
   - 递归方法（版本 1 和 3）：通过递归分治的方式，检查字符串中每个字符的大小写是否都存在，如果不满足条件，则将字符串分为左右两部分，递归求解最长的美好子字符串。
   - 滑动窗口方法（版本 2）：使用滑动窗口和哈希表记录字符的大小写出现情况，动态调整窗口以找到满足条件的最长子字符串。

3. 全量伪代码：
   - 递归方法：
     ```
     定义函数 longestNiceSubstring(s):
         如果字符串长度小于 2，返回空字符串
         初始化集合 seen 记录字符串中所有字符
         遍历字符串中的每个字符:
             如果字符的大小写形式不同时存在于 seen 中:
                 递归求解左半部分的最长美好子字符串
                 递归求解右半部分的最长美好子字符串
                 返回较长的子字符串
         返回整个字符串
     ```
   - 滑动窗口方法：
     ```
     定义函数 longestNiceSubstring(s):
         初始化 max_res 为空字符串
         遍历可能的字符种类数 k 从 1 到 26:
             初始化哈希表 seen 记录字符的大小写出现情况
             初始化 left 和 matched 为 0
             遍历字符串中的每个字符，作为右边界:
                 更新 seen 中当前字符的大小写出现情况
                 如果当前字符的大小写都出现，增加 matched
                 当 seen 中字符种类数大于 k 时:
                     更新 left 指针，减少左边界字符的大小写出现情况
                     如果左边界字符的大小写不再都出现，减少 matched
                     如果左边界字符的大小写都为 0，删除该字符
                 如果 matched 和 seen 的字符种类数都等于 k:
                     更新 max_res 为当前窗口的子字符串
         返回 max_res
     ```

4. 复杂度：
   - 递归方法的时间复杂度为 $O(n^2)$，空间复杂度为 $O(n)$，其中 $n$ 是字符串的长度。
   - 滑动窗口方法的时间复杂度为 $O(n \cdot 26)$，即 $O(n)$，空间复杂度为 $O(1)$，因为哈希表的大小最多为 26。