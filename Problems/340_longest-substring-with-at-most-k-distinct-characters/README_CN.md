# 340. 至多包含 K 个不同字符的最长子串

**难度**: Medium | **标签**: `Hash Table` `String` `Sliding Window`

## 题目描述

<p>给定一个字符串 <code>s</code> 和一个整数 <code>k</code>，返回 <em>包含至多</em> <code>k</code> <em><strong>不同</strong> 字符</em> 的 <em>最长</em><span data-keyword="substring-nonempty"><em>子串</em></span><em> 的长度</em>。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> s = &quot;eceba&quot;, k = 2
<strong>输出:</strong> 3
<strong>解释:</strong> 该子串为 &quot;ece&quot;，长度为 3。</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> s = &quot;aa&quot;, k = 1
<strong>输出:</strong> 2
<strong>解释:</strong> 该子串为 &quot;aa&quot;，长度为 2。
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= k &lt;= 50</code></li>
</ul>

---
## 解题思路与复盘

1. 一句话直击本质：使用滑动窗口和集合来动态维护一个包含至多 K 个不同字符的子串，并在遍历过程中更新最长子串的长度。

2. 综合思路：
   - 滑动窗口：通过两个指针（left 和 right）定义一个窗口，右指针不断向右扩展窗口，左指针根据窗口内不同字符的数量进行收缩，以保证窗口内最多包含 K 个不同字符。
   - 数据结构：使用集合来判断当前窗口内的不同字符数量。

3. 全量伪代码：
   ```
   定义函数 lengthOfLongestSubstringKDistinct(s, k)
       将字符串 s 转换为字符数组 string
       初始化字符串长度 size
       初始化左指针 left 为 0
       初始化右指针 right 为 0
       初始化最大长度 maxLen 为 0
       初始化结果数组 res 为空

       当右指针 right 小于 size 时
           将 string[right] 添加到 res
           右指针 right 增加 1

           当 res 中不同字符的数量大于 k 时
               删除 res 中的第一个元素
               左指针 left 增加 1

           更新 maxLen 为 max(maxLen, right - left)

       返回 maxLen
   ```

4. 复杂度：
   - 时间复杂度：$O(n \cdot k)$，其中 $n$ 是字符串的长度，$k$ 是不同字符的最大数量。最坏情况下，每次更新窗口时需要计算集合的大小。
   - 空间复杂度：$O(n)$，用于存储当前窗口内的字符。