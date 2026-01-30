# 392. 判断子序列

**难度**: Easy | **标签**: `Two Pointers` `String` `Dynamic Programming`

## 题目描述

<p>给定字符串 <strong>s</strong> 和 <strong>t</strong> ，判断 <strong>s</strong> 是否为 <strong>t</strong> 的子序列。</p>

<p>字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，<code>"ace"</code>是<code>"abcde"</code>的一个子序列，而<code>"aec"</code>不是）。</p>

<p><strong>进阶：</strong></p>

<p>如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？</p>

<p><strong>致谢：</strong></p>

<p>特别感谢<strong> </strong><a href="https://leetcode.com/pbrother/">@pbrother </a>添加此问题并且创建所有测试用例。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "abc", t = "ahbgdc"
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "axc", t = "ahbgdc"
<strong>输出：</strong>false
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= s.length <= 100</code></li>
	<li><code>0 <= t.length <= 10^4</code></li>
	<li>两个字符串都只由小写字符组成。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：判断子序列的核心逻辑是通过双指针遍历或动态规划来验证字符串 `s` 的所有字符是否按顺序出现在字符串 `t` 中。

2. 综合思路：
   - **双指针法**：使用两个指针分别遍历字符串 `s` 和 `t`，如果当前字符匹配则移动 `s` 的指针，始终移动 `t` 的指针，最终判断 `s` 的指针是否遍历完。
   - **动态规划法**：构建一个二维数组 `dp`，其中 `dp[i][j]` 表示 `s` 的前 `i` 个字符和 `t` 的前 `j` 个字符的最长公共子序列长度，最后判断 `dp[m][n]` 是否等于 `s` 的长度。

3. 全量伪代码：
   - **双指针法**：
     ```
     初始化 i = 0, j = 0
     当 i < len(s) 且 j < len(t) 时循环：
         如果 s[i] == t[j]：
             增加 i
         增加 j
     返回 i == len(s)
     ```
   - **动态规划法**：
     ```
     初始化 m = len(s), n = len(t)
     创建二维数组 dp 大小为 (m+1) x (n+1)，所有元素初始化为 0
     对于 i 从 1 到 m：
         对于 j 从 1 到 n：
             如果 s[i-1] == t[j-1]：
                 dp[i][j] = dp[i-1][j-1] + 1
             否则：
                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
     返回 dp[m][n] == m
     ```

4. 复杂度：
   - **双指针法**：
     - 时间复杂度：$O(n)$，其中 $n$ 是字符串 `t` 的长度，因为每个字符最多访问一次。
     - 空间复杂度：$O(1)$，因为只使用了常数级别的额外空间。
   - **动态规划法**：
     - 时间复杂度：$O(m \times n)$，其中 $m$ 和 $n$ 分别是字符串 `s` 和 `t` 的长度，因为需要填充一个 $m \times n$ 的表。
     - 空间复杂度：$O(m \times n)$，因为需要存储一个 $m \times n$ 的二维数组。