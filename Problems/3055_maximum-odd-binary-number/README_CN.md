# 3055. 最大二进制奇数

**难度**: Easy | **标签**: `Math` `String` `Greedy`

## 题目描述

<p>给你一个 <strong>二进制</strong> 字符串 <code>s</code> ，其中至少包含一个 <code>'1'</code> 。</p>

<p>你必须按某种方式 <strong>重新排列</strong> 字符串中的位，使得到的二进制数字是可以由该组合生成的 <strong>最大二进制奇数</strong> 。</p>

<p>以字符串形式，表示并返回可以由给定组合生成的最大二进制奇数。</p>

<p><strong>注意 </strong>返回的结果字符串 <strong>可以</strong> 含前导零。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "010"
<strong>输出：</strong>"001"
<strong>解释：</strong>因为字符串 s 中仅有一个 '1' ，其必须出现在最后一位上。所以答案是 "001" 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "0101"
<strong>输出：</strong>"1001"
<strong>解释：</strong>其中一个 '1' 必须出现在最后一位上。而由剩下的数字可以生产的最大数字是 "100" 。所以答案是 "1001" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 仅由 <code>'0'</code> 和 <code>'1'</code> 组成</li>
	<li><code>s</code> 中至少包含一个 <code>'1'</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过统计字符串中'1'的数量，将所有'1'尽量靠前排列，并确保最后一位为'1'以构成最大二进制奇数。

2. 综合思路：
   - 迭代法：遍历字符串统计'1'的数量，然后重新构造字符串，使得所有'1'尽量靠前，最后一位为'1'，其余位置为'0'。

3. 全量伪代码：
   ```
   定义函数 maximumOddBinaryNumber(s: 字符串) -> 字符串:
       将字符串 s 转换为字符列表 nums
       计算 nums 的长度 n
       初始化计数器 cnt 为 0
       对于 nums 中的每个字符 i:
           如果 i 是 '1':
               将 cnt 加 1
       将 nums 的最后一个元素设为 '1'
       计算剩余 '1' 的数量 rem 为 cnt - 1
       将 nums 的前 rem 个元素设为 '1'
       计算剩余位置 left 为 n - 1 - rem
       将 nums 中从 rem 到倒数第二个元素设为 '0'
       返回 nums 转换为字符串后的结果
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是输入字符串的长度，因为需要遍历字符串统计'1'的数量，并重新构造字符串。
   - 空间复杂度：$O(n)$，用于存储字符列表。