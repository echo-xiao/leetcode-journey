# 3543. 统计满足 K 约束的子字符串数量 I

**难度**: Easy | **标签**: `String` `Sliding Window`

## 题目描述

<p>给你一个 <strong>二进制</strong> 字符串 <code>s</code> 和一个整数 <code>k</code>。</p>

<p>如果一个 <strong>二进制字符串</strong> 满足以下任一条件，则认为该字符串满足 <strong>k 约束</strong>：</p>

<ul>
	<li>字符串中 <code>0</code> 的数量最多为 <code>k</code>。</li>
	<li>字符串中 <code>1</code> 的数量最多为 <code>k</code>。</li>
</ul>

<p>返回一个整数，表示 <code>s</code> 的所有满足 <strong>k 约束 </strong>的<span data-keyword="substring-nonempty">子字符串</span>的数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "10101", k = 1</span></p>

<p><strong>输出：</strong><span class="example-io">12</span></p>

<p><strong>解释：</strong></p>

<p><code>s</code> 的所有子字符串中，除了 <code>"1010"</code>、<code>"10101"</code> 和 <code>"0101"</code> 外，其余子字符串都满足 k 约束。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "1010101", k = 2</span></p>

<p><strong>输出：</strong><span class="example-io">25</span></p>

<p><strong>解释：</strong></p>

<p><code>s</code> 的所有子字符串中，除了长度大于 5 的子字符串外，其余子字符串都满足 k 约束。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "11111", k = 1</span></p>

<p><strong>输出：</strong><span class="example-io">15</span></p>

<p><strong>解释：</strong></p>

<p><code>s</code> 的所有子字符串都满足 k 约束。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 50</code></li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
	<li><code>s[i]</code> 是 <code>'0'</code> 或 <code>'1'</code>。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用滑动窗口记录子字符串中字符出现次数，当窗口内字符数量满足条件时，计算满足条件的子字符串数量。

2. 综合思路：
   - 滑动窗口：通过左右指针维护一个动态窗口，窗口内记录字符出现次数，当窗口内字符数量满足条件时，计算满足条件的子字符串数量。
   - 该题目主要使用滑动窗口技术，没有其他显著的解法如递归或迭代、DFS与BFS等。

3. 全量伪代码：
   ```
   初始化计数器 cnt 为 0
   初始化一个字典 seen 用于记录字符 '0' 和 '1' 的出现次数
   初始化左指针 l 为 0

   遍历字符串 s 的每个字符，右指针 r 从 0 到 len(s) - 1：
       如果字符 s[r] 不在 seen 中，则将其加入 seen 并初始化为 1
       否则，将 seen 中对应字符的计数加 1

       当 seen 中 '0' 和 '1' 的计数都大于 k 时：
           将 seen 中 s[l] 对应的计数减 1
           左指针 l 向右移动一位

       将 r - l + 1 加到计数器 cnt 中

   返回计数器 cnt 的值
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，因为每个字符最多被左右指针访问一次。
   - 空间复杂度：$O(1)$，因为使用的额外空间与输入字符串的长度无关，仅用于存储固定数量的字符计数。