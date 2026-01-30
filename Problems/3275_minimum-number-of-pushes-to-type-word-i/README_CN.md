# 3275. 输入单词需要的最少按键次数 I

**难度**: Easy | **标签**: `Math` `String` `Greedy`

## 题目描述

<p>给你一个字符串 <code>word</code>，由 <strong>不同 </strong>小写英文字母组成。</p>

<p>电话键盘上的按键与 <strong>不同 </strong>小写英文字母集合相映射，可以通过按压按键来组成单词。例如，按键 <code>2</code> 对应 <code>["a","b","c"]</code>，我们需要按一次键来输入 <code>"a"</code>，按两次键来输入 <code>"b"</code>，按三次键来输入 <code>"c"</code><em>。</em></p>

<p>现在允许你将编号为 <code>2</code> 到 <code>9</code> 的按键重新映射到 <strong>不同 </strong>字母集合。每个按键可以映射到<strong> 任意数量 </strong>的字母，但每个字母 <strong>必须</strong> <strong>恰好</strong> 映射到 <strong>一个 </strong>按键上。你需要找到输入字符串 <code>word</code> 所需的<strong> 最少 </strong>按键次数。</p>

<p>返回重新映射按键后输入 <code>word</code> 所需的 <strong>最少 </strong>按键次数。</p>

<p>下面给出了一种电话键盘上字母到按键的映射作为示例。注意 <code>1</code>，<code>*</code>，<code>#</code> 和 <code>0</code> <strong>不</strong> 对应任何字母。</p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/26/keypaddesc.png" style="width: 329px; height: 313px;" />
<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/26/keypadv1e1.png" style="width: 329px; height: 313px;" />
<pre>
<strong>输入：</strong>word = "abcde"
<strong>输出：</strong>5
<strong>解释：</strong>图片中给出的重新映射方案的输入成本最小。
"a" -&gt; 在按键 2 上按一次
"b" -&gt; 在按键 3 上按一次
"c" -&gt; 在按键 4 上按一次
"d" -&gt; 在按键 5 上按一次
"e" -&gt; 在按键 6 上按一次
总成本为 1 + 1 + 1 + 1 + 1 = 5 。
可以证明不存在其他成本更低的映射方案。
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/26/keypadv1e2.png" style="width: 329px; height: 313px;" />
<pre>
<strong>输入：</strong>word = "xycdefghij"
<strong>输出：</strong>12
<strong>解释：</strong>图片中给出的重新映射方案的输入成本最小。
"x" -&gt; 在按键 2 上按一次
"y" -&gt; 在按键 2 上按两次
"c" -&gt; 在按键 3 上按一次
"d" -&gt; 在按键 3 上按两次
"e" -&gt; 在按键 4 上按一次
"f" -&gt; 在按键 5 上按一次
"g" -&gt; 在按键 6 上按一次
"h" -&gt; 在按键 7 上按一次
"i" -&gt; 在按键 8 上按一次
"j" -&gt; 在按键 9 上按一次
总成本为 1 + 2 + 1 + 2 + 1 + 1 + 1 + 1 + 1 + 1 = 12 。
可以证明不存在其他成本更低的映射方案。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 26</code></li>
	<li><code>word</code> 仅由小写英文字母组成。</li>
	<li><code>word</code> 中的所有字母互不相同。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是将输入单词按每组最多8个字符分段，计算每段字符的按键次数，随着段数增加，按键次数呈线性递增。

2. 综合思路：
   - 迭代法：通过循环迭代，逐步减少剩余字符数，每次处理最多8个字符，并累加按键次数。
   - 条件判断法：通过条件判断，直接根据字符长度范围计算按键次数，适用于字符长度在特定范围内的情况。

3. 全量伪代码：
   - 迭代法：
     ```
     初始化字符总数 n
     初始化总按键次数 ttl 为 0
     初始化当前段按键代价 cost 为 1
     当 n 大于 0 时：
         计算当前段字符数 slot 为 n 和 8 的最小值
         将 slot 乘以 cost 加到 ttl
         从 n 中减去 slot
         将 cost 增加 1
     返回 ttl
     ```
   - 条件判断法：
     ```
     初始化字符总数 n
     如果 n 小于等于 8：
         返回 n
     否则如果 n 大于 8 且小于等于 16：
         返回 8 + (n-8) * 2
     否则如果 n 大于 16 且小于等于 24：
         返回 8 + 8 * 2 + (n-16) * 3
     否则：
         返回 8 + 8 * 2 + 8 * 3 + (n-24) * 4
     ```

4. 复杂度：
   - 时间复杂度：$O(1)$，因为无论是迭代法还是条件判断法，计算次数与输入长度无关，最多进行常数次操作。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外变量。