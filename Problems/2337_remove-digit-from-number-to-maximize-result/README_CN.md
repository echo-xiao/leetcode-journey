# 2337. 移除指定数字得到的最大结果

**难度**: Easy | **标签**: `String` `Greedy` `Enumeration`

## 题目描述

<p>给你一个表示某个正整数的字符串 <code>number</code> 和一个字符 <code>digit</code> 。</p>

<p>从 <code>number</code> 中 <strong>恰好</strong> 移除 <strong>一个</strong> 等于&nbsp;<code>digit</code> 的字符后，找出并返回按 <strong>十进制</strong> 表示 <strong>最大</strong> 的结果字符串。生成的测试用例满足 <code>digit</code> 在 <code>number</code> 中出现至少一次。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>number = "123", digit = '3'
<strong>输出：</strong>"12"
<strong>解释：</strong>"123" 中只有一个 '3' ，在移除 '3' 之后，结果为 "12" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>number = "1231", digit = '1'
<strong>输出：</strong>"231"
<strong>解释：</strong>可以移除第一个 '1' 得到 "231" 或者移除第二个 '1' 得到 "123" 。
由于 231 &gt; 123 ，返回 "231" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>number = "551", digit = '5'
<strong>输出：</strong>"51"
<strong>解释：</strong>可以从 "551" 中移除第一个或者第二个 '5' 。
两种方案的结果都是 "51" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= number.length &lt;= 100</code></li>
	<li><code>number</code> 由数字 <code>'1'</code> 到 <code>'9'</code> 组成</li>
	<li><code>digit</code> 是 <code>'1'</code> 到 <code>'9'</code> 中的一个数字</li>
	<li><code>digit</code> 在 <code>number</code> 中出现至少一次</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过遍历字符串，移除每个出现的指定数字，生成多个可能结果，并返回其中的最大值。

2. 综合思路：
   - 迭代法：遍历字符串的每个字符，若字符等于指定数字，则移除该字符并记录结果，最后返回所有结果中的最大值。
   - 由于提供的代码版本逻辑相同，未涉及其他解法（如递归、DFS、BFS等）。

3. 全量伪代码：
   ```
   定义函数 removeDigit，输入为字符串 number 和字符 digit
       初始化空列表 res 用于存储可能的结果
       对于 number 中的每个字符及其索引 i：
           如果字符等于 digit：
               从 number 中移除索引 i 处的字符，生成新的字符串
               将新的字符串添加到 res 列表中
       返回 res 列表中的最大字符串
   ```

4. 复杂度：
   - 时间复杂度：$O(n^2)$，其中 $n$ 是字符串 number 的长度。对于每个字符的移除操作，生成新字符串的时间复杂度为 $O(n)$。
   - 空间复杂度：$O(n^2)$，因为可能会存储多达 $n$ 个长度为 $n-1$ 的字符串。