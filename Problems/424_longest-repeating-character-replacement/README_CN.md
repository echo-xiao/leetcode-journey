# 424. 替换后的最长重复字符

**难度**: Medium | **标签**: `Hash Table` `String` `Sliding Window`

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个整数 <code>k</code> 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 <code>k</code> 次。</p>

<p>在执行上述操作后，返回 <em>包含相同字母的最长子字符串的长度。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "ABAB", k = 2
<strong>输出：</strong>4
<strong>解释：</strong>用两个'A'替换为两个'B',反之亦然。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "AABABBA", k = 1
<strong>输出：</strong>4
<strong>解释：</strong>
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。
可能存在其他的方法来得到同样的结果。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 仅由大写英文字母组成</li>
	<li><code>0 &lt;= k &lt;= s.length</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用滑动窗口维护一个窗口内字符的频率表，通过调整窗口边界确保窗口内最多有 $k$ 个字符可以被替换以形成最长的重复字符子串。

2. 综合思路：
   - 滑动窗口：通过双指针（left 和 right）来定义窗口的左右边界，动态调整窗口大小以满足条件。
   - 频率计数：使用字典记录当前窗口内每个字符的出现次数，维护窗口内最多出现的字符数。
   - 窗口调整：当窗口内非最多字符的数量超过 $k$ 时，调整左边界以缩小窗口。

3. 全量伪代码：
   ```
   初始化字典 dic 用于记录字符频率
   初始化 maxCount 为 0，表示窗口内某字符的最大频率
   初始化左右指针 right 和 left 为 0
   初始化结果列表 res 用于存储当前窗口的字符
   初始化 maxLen 为 0，表示最长重复字符子串的长度

   当 right 小于字符串长度时：
       获取当前字符 char
       将 char 添加到 res 列表
       
       如果 char 不在字典 dic 中：
           将 char 添加到 dic，频率设为 1
       否则：
           增加 char 在 dic 中的频率

       更新 maxCount 为 dic 中 char 的频率和 maxCount 的最大值
       将 right 指针右移一位

       当 res 列表长度减去 maxCount 大于 k 时：
           减少 res 列表中第一个字符在 dic 中的频率
           从 res 列表中删除第一个字符
           将 left 指针右移一位

       更新 maxLen 为 maxLen 和 (right - left) 的最大值

   返回 maxLen
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度，因为每个字符最多被访问两次（一次被加入窗口，一次被移出窗口）。
   - 空间复杂度：$O(1)$，因为字典的大小最多为常数级别（字符集大小有限）。