# 1430. 找到一个数字的 K 美丽值

**难度**: Easy | **标签**: `Math` `String` `Sliding Window`

## 题目描述

<p>一个整数 <code>num</code>&nbsp;的&nbsp;<strong>k&nbsp;</strong>美丽值定义为&nbsp;<code>num</code>&nbsp;中符合以下条件的&nbsp;<strong>子字符串</strong>&nbsp;数目：</p>

<ul>
	<li>子字符串长度为&nbsp;<code>k</code>&nbsp;。</li>
	<li>子字符串能整除 <code>num</code> 。</li>
</ul>

<p>给你整数&nbsp;<code>num</code> 和&nbsp;<code>k</code>&nbsp;，请你返回<em>&nbsp;</em><code>num</code>&nbsp;的 k 美丽值。</p>

<p>注意：</p>

<ul>
	<li>允许有&nbsp;<strong>前缀</strong>&nbsp;<strong>0</strong>&nbsp;。</li>
	<li><code>0</code>&nbsp;不能整除任何值。</li>
</ul>

<p>一个 <strong>子字符串</strong>&nbsp;是一个字符串里的连续一段字符序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>num = 240, k = 2
<b>输出：</b>2
<b>解释：</b>以下是 num 里长度为 k 的子字符串：
- "<em><strong>24</strong></em>0" 中的 "24" ：24 能整除 240 。
- "2<em><strong>40</strong></em>" 中的 "40" ：40 能整除 240 。
所以，k 美丽值为 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>num = 430043, k = 2
<b>输出：</b>2
<b>解释：</b>以下是 num 里长度为 k 的子字符串：
- "<em><strong>43</strong></em>0043" 中的 "43" ：43 能整除 430043 。
- "4<em><strong>30</strong></em>043" 中的 "30" ：30 不能整除 430043 。
- "43<em><strong>00</strong></em>43" 中的 "00" ：0 不能整除 430043 。
- "430<em><strong>04</strong></em>3" 中的 "04" ：4 不能整除 430043 。
- "4300<em><strong>43</strong></em>" 中的 "43" ：43 能整除 430043 。
所以，k 美丽值为 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= num.length</code>&nbsp;（将&nbsp;<code>num</code>&nbsp;视为字符串）</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过滑动窗口遍历数字的所有长度为 \( k \) 的子串，判断其是否为原数字的因子。

2. 综合思路：
   - **迭代法**：使用一个固定大小的滑动窗口在字符串表示的数字上滑动，逐个检查每个长度为 \( k \) 的子串是否为原数字的因子。

3. 全量伪代码：
   ```plaintext
   定义函数 divisorSubstrings(数字 num, 整数 k):
       将数字 num 转换为字符串
       初始化计数器 cnt 为 0
       计算字符串长度 n

       对于 i 从 0 到 n-k（包括 n-k）:
           取子串 sub 为从位置 i 开始长度为 k 的子串
           如果 sub 转换为整数后不为 0 且 num 能被 sub 整除:
               计数器 cnt 增加 1

       返回计数器 cnt
   ```

4. 复杂度：
   - 时间复杂度：$O(n \cdot k)$，其中 \( n \) 是数字的位数，因为我们需要遍历每个可能的子串，并且每次检查子串是否为因子需要常数时间。
   - 空间复杂度：$O(1)$，除了输入和输出外，使用的额外空间是常数级别的。