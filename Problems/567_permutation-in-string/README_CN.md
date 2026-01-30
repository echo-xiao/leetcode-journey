# 567. 字符串的排列

**难度**: Medium | **标签**: `Hash Table` `Two Pointers` `String` `Sliding Window`

## 题目描述

<p>给你两个字符串&nbsp;<code>s1</code>&nbsp;和&nbsp;<code>s2</code> ，写一个函数来判断 <code>s2</code> 是否包含 <code>s1</code><strong>&nbsp;</strong>的 <span data-keyword="permutation-string">排列</span>。如果是，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>换句话说，<code>s1</code> 的排列之一是 <code>s2</code> 的 <strong>子串</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s1 = "ab" s2 = "eidbaooo"
<strong>输出：</strong>true
<strong>解释：</strong>s2 包含 s1 的排列之一 ("ba").
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s1= "ab" s2 = "eidboaoo"
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s1</code> 和 <code>s2</code> 仅包含小写字母</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法通过滑动窗口和哈希表统计字符频次，动态比较两个字符串的字符频次以判断排列关系。

2. 综合思路：
   - 滑动窗口：利用两个哈希表分别记录目标字符串 `s1` 和当前窗口内 `s2` 的字符频次，通过移动窗口边界调整窗口大小，并在每次调整后比较两个哈希表是否相等。
   - 频次比较：在滑动窗口的过程中，实时更新窗口内的字符频次，并在窗口大小等于 `s1` 长度时进行频次比较。

3. 全量伪代码：
   ```
   定义函数 checkInclusion(s1, s2):
       初始化 s1Count 和 s2Count 为两个空字典
       
       对于 s1 中的每个字符 char:
           将 char 的计数加一到 s1Count 中

       初始化 left 和 right 为 0

       当 right 小于 s2 的长度时:
           将 s2[right] 的计数加一到 s2Count 中
           将 right 增加 1

           当 right - left 大于 s1 的长度时:
               将 s2[left] 的计数减一
               如果 s2[left] 的计数为 0:
                   从 s2Count 中删除 s2[left]
               将 left 增加 1

           如果 s1Count 等于 s2Count:
               返回 True

       返回 False
   ```

4. 复杂度：
   - 时间复杂度：$O(n + m)$，其中 $n$ 是 `s1` 的长度，$m$ 是 `s2` 的长度。初始化 `s1Count` 需要 $O(n)$，滑动窗口遍历 `s2` 需要 $O(m)$。
   - 空间复杂度：$O(1)$，因为哈希表的大小最多为字符集大小（常数级别）。