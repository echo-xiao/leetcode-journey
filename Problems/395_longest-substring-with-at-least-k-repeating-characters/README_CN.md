# 395. 至少有 K 个重复字符的最长子串

**难度**: Medium | **标签**: `Hash Table` `String` `Divide and Conquer` `Sliding Window`

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个整数 <code>k</code> ，请你找出 <code>s</code> 中的最长子串，&nbsp;要求该子串中的每一字符出现次数都不少于 <code>k</code> 。返回这一子串的长度。</p>

<p data-pm-slice="1 1 []">如果不存在这样的子字符串，则返回 0。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "aaabb", k = 3
<strong>输出：</strong>3
<strong>解释：</strong>最长子串为 "aaa" ，其中 'a' 重复了 3 次。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "ababbc", k = 2
<strong>输出：</strong>5
<strong>解释：</strong>最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过递归分治法，将字符串按不满足条件的字符分割成子串，递归求解每个子串的最长符合条件的子串长度。

2. 综合思路：
   - 递归分治法：遍历字符串统计字符出现次数，若某字符出现次数小于 K，则以该字符为分隔符将字符串分割成多个子串，递归求解每个子串的最长符合条件的子串长度。
   - 迭代法（未在提供的代码集中出现，但作为可能的解法）：使用滑动窗口或双指针技术，动态调整窗口大小，统计窗口内字符出现次数，判断是否满足条件。

3. 全量伪代码：
   ```
   函数 longestSubstring(字符串 s, 整数 k):
       如果 s 的长度小于 k:
           返回 0

       创建一个空字典 dic

       对于字符串 s 中的每个字符 char:
           如果 char 不在 dic 中:
               将 char 加入 dic，初始值为 1
           否则:
               将 dic[char] 增加 1

       初始化 maxRes 为 0

       对于 dic 中的每个键值对 (key, val):
           如果 val 小于 k:
               将字符串 s 按照 key 分割成多个子串 subStrings

               初始化 maxRes 为 0
               对于每个子串 cut 在 subStrings 中:
                   递归调用 longestSubstring(cut, k) 得到结果 res
                   更新 maxRes 为 max(res, maxRes)
               返回 maxRes
       返回字符串 s 的长度
   ```

4. 复杂度：
   - 时间复杂度：$O(n^2)$，其中 $n$ 是字符串的长度。最坏情况下，每次递归调用都可能需要遍历整个字符串。
   - 空间复杂度：$O(n)$，递归调用栈的深度在最坏情况下可能达到字符串的长度。