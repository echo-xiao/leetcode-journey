# 3349. 每个字符最多出现两次的最长子字符串

**难度**: Easy | **标签**: `Hash Table` `String` `Sliding Window`

## 题目描述

<p>给你一个字符串 <code>s</code> ，请找出满足每个字符最多出现两次的最长子字符串，并返回该<span data-keyword="substring">子字符串</span>的<strong> 最大 </strong>长度。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "bcbbbcba"</span></p>

<p><strong>输出：</strong> <span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<p>以下子字符串长度为 4，并且每个字符最多出现两次：<code>"bcbb<u>bcba</u>"</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "aaaa"</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>以下子字符串长度为 2，并且每个字符最多出现两次：<code>"<u>aa</u>aa"</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul><!-- 字符串 s 的长度在 2 到 100 之间 -->
	<li><code>2 &lt;= s.length &lt;= 100</code></li>
	<!-- 字符串 s 仅包含小写英文字母 -->
	<li><code>s</code> 仅由小写英文字母组成。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用滑动窗口和哈希表来记录字符出现次数，动态调整窗口以确保每个字符最多出现两次。

2. 综合思路：
   - 滑动窗口：通过左右指针（`l` 和 `r`）构建一个动态窗口，遍历字符串时调整窗口大小以满足条件。
   - 哈希表：使用哈希表记录当前窗口内每个字符的出现次数，当某字符出现次数超过两次时，移动左指针缩小窗口。

3. 全量伪代码：
   ```
   初始化左指针 l 为 0
   初始化最大长度 max_length 为 0
   初始化哈希表 seen 为空

   遍历字符串 s 的每个字符，索引为 r：
       如果字符 s[r] 不在哈希表 seen 中：
           将 s[r] 加入哈希表 seen，值为 1
       否则：
           将 seen 中 s[r] 的值加 1

       当 seen 中 s[r] 的值大于 2 时：
           将 seen 中 s[l] 的值减 1
           左指针 l 向右移动一位

       计算当前窗口长度 length 为 r - l + 1
       更新 max_length 为 length 和 max_length 中的较大值

   返回 max_length
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度，因为每个字符在最坏情况下被访问常数次。
   - 空间复杂度：$O(1)$，因为哈希表的大小最多为常数级（字符集大小有限）。