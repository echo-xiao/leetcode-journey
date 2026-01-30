# 2154. 转换字符串的最少操作次数

**难度**: Easy | **标签**: `String` `Greedy`

## 题目描述

<p>给你一个字符串 <code>s</code> ，由 <code>n</code> 个字符组成，每个字符不是 <code>'X'</code> 就是 <code>'O'</code> 。</p>

<p>一次<strong> 操作</strong> 定义为从 <code>s</code> 中选出 <strong>三个连续字符 </strong>并将选中的每个字符都转换为 <code>'O'</code> 。注意，如果字符已经是 <code>'O'</code> ，只需要保持 <strong>不变</strong> 。</p>

<p>返回将 <code>s</code> 中所有字符均转换为 <code>'O'</code> 需要执行的&nbsp;<strong>最少</strong>&nbsp;操作次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "XXX"
<strong>输出：</strong>1
<strong>解释：<em>XXX</em></strong> -&gt; OOO
一次操作，选中全部 3 个字符，并将它们转换为 <code>'O' 。</code>
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "XXOX"
<strong>输出：</strong>2
<strong>解释：<em>XXO</em></strong>X -&gt; O<em><strong>OOX</strong></em> -&gt; OOOO
第一次操作，选择前 3 个字符，并将这些字符转换为 <code>'O'</code> 。
然后，选中后 3 个字符，并执行转换。最终得到的字符串全由字符 <code>'O'</code> 组成。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "OOOO"
<strong>输出：</strong>0
<strong>解释：</strong>s 中不存在需要转换的 <code>'X' 。</code>
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code> 为 <code>'X'</code> 或 <code>'O'</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过遍历字符串，每遇到一个 'X' 就跳过接下来的两个字符，并增加操作计数，以此来计算最少操作次数。

2. 综合思路：
   - 迭代法：遍历字符串，使用一个计数器记录操作次数，当遇到 'X' 时，跳过接下来的两个字符，因为一次操作可以将连续的三个字符转换为 'O'。
   - 递归法：虽然题目中没有递归实现，但可以通过递归方式模拟同样的逻辑，即每次遇到 'X' 时，递归处理剩余的字符串。

3. 全量伪代码：
   ```
   定义函数 minimumMoves(s: 字符串) -> 整数:
       初始化 cnt 为 0
       初始化 i 为 0
       当 i 小于 s 的长度时:
           如果 s[i] 等于 'X':
               将 i 增加 3
               将 cnt 增加 1
           否则:
               将 i 增加 1
       返回 cnt
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串的长度，因为我们需要遍历整个字符串一次。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外的变量。