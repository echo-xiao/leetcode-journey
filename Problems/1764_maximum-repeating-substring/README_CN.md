# 1764. 最大重复子字符串

**难度**: Easy | **标签**: `String` `Dynamic Programming` `String Matching`

## 题目描述

<p>给你一个字符串 <code>sequence</code> ，如果字符串 <code>word</code> 连续重复 <code>k</code> 次形成的字符串是 <code>sequence</code> 的一个子字符串，那么单词 <code>word</code> 的 <strong>重复值为 <code>k</code></strong><strong> </strong>。单词 <code>word</code> 的 <strong>最</strong><strong>大重复值</strong> 是单词 <code>word</code> 在 <code>sequence</code> 中最大的重复值。如果 <code>word</code> 不是 <code>sequence</code> 的子串，那么重复值 <code>k</code> 为 <code>0</code> 。</p>

<p>给你一个字符串 <code>sequence</code> 和 <code>word</code> ，请你返回 <strong>最大重复值 <code>k</code> </strong>。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>sequence = "ababc", word = "ab"
<b>输出：</b>2
<strong>解释：</strong>"abab" 是 "<strong>abab</strong>c" 的子字符串。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>sequence = "ababc", word = "ba"
<b>输出：</b>1
<strong>解释：</strong>"ba" 是 "a<strong>ba</strong>bc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>sequence = "ababc", word = "ac"
<b>输出：</b>0
<strong>解释：</strong>"ac" 不是 "ababc" 的子字符串。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= sequence.length <= 100</code></li>
	<li><code>1 <= word.length <= 100</code></li>
	<li><code>sequence</code> 和 <code>word</code> 都只包含小写英文字母。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过滑动窗口或递归方式，逐个检查子字符串是否与目标字符串匹配，并记录最大匹配次数。

2. 综合思路：
   - 递归解法：使用递归和记忆化搜索，从字符串的每个位置开始，递归地检查以该位置结尾的子字符串是否与目标字符串匹配，并记录匹配次数。
   - 迭代解法：使用双指针（滑动窗口）方法，从字符串的每个位置开始，逐个检查子字符串是否与目标字符串匹配，并记录最大匹配次数。

3. 全量伪代码：
   - 递归解法：
     ```
     定义函数 maxRepeating(sequence, word):
         初始化 n 为 sequence 的长度
         初始化 m 为 word 的长度
         初始化 memo 为一个空字典
         初始化 maxk 为 0

         对于 i 从 0 到 n-1:
             更新 maxk 为 max(maxk, 调用 recursion(i))

         返回 maxk

     定义递归函数 recursion(i):
         如果 i 小于 m-1:
             返回 0

         如果 i 在 memo 中:
             返回 memo[i]

         取 curr 为 sequence 从 i-m+1 到 i+1 的子字符串

         如果 curr 等于 word:
             结果 res 为 1 + 调用 recursion(i-m)
         否则:
             结果 res 为 0

         将 res 存入 memo[i]
         返回 res
     ```

   - 迭代解法：
     ```
     定义函数 maxRepeating(sequence, word):
         初始化 n 为 sequence 的长度
         初始化 m 为 word 的长度
         初始化 k 为 0

         初始化 left 为 0

         当 left 小于 n 时:
             初始化 curr 为 0
             初始化 right 为 left

             当 right + m 小于等于 n 时:
                 如果 sequence 从 right 到 right+m 的子字符串等于 word:
                     curr 增加 1
                     right 增加 m
                 否则:
                     退出循环

             更新 k 为 max(k, curr)
             left 增加 1

         返回 k
     ```

4. 复杂度：
   - 递归解法：
     - 时间复杂度：$O(n)$，因为每个位置最多被访问一次，且使用了记忆化。
     - 空间复杂度：$O(n)$，用于存储递归调用栈和记忆化字典。
   - 迭代解法：
     - 时间复杂度：$O(n \cdot m)$，因为每个起始位置最多需要检查 $m$ 个字符。
     - 空间复杂度：$O(1)$，只使用了常数级别的额外空间。