# 1065. 子串能表示从 1 到 N 数字的二进制串

**难度**: Medium | **标签**: `Hash Table` `String` `Bit Manipulation` `Sliding Window`

## 题目描述

<p>给定一个二进制字符串&nbsp;<code>s</code>&nbsp;和一个正整数&nbsp;<code>n</code>，如果对于&nbsp;<code>[1, n]</code>&nbsp;范围内的每个整数，<em>其二进制表示都是&nbsp;<code>s</code> 的 <strong>子字符串</strong> ，就返回 <code>true</code>，否则返回 <code>false</code>&nbsp;</em>。</p>

<p><strong>子字符串</strong>&nbsp;是字符串中连续的字符序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "0110", n = 3
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "0110", n = 4
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code>&nbsp;不是&nbsp;<code>'0'</code>&nbsp;就是&nbsp;<code>'1'</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 该算法的核心逻辑是检查从 1 到 N 的每个数字的二进制表示是否都是给定字符串的子串。

2. **综合思路：**
   - **迭代法：** 通过迭代从 1 到 N 的所有数字，生成其二进制表示，并检查这些表示是否存在于给定字符串中。

3. **全量伪代码：**
   ```plaintext
   定义函数 queryString(s: 字符串, n: 整数) -> 布尔值:
       如果 n 大于 2000:
           返回 False
       
       初始化空列表 res
       对于 i 从 1 到 n（包括 n）:
           将 i 的二进制表示（去掉前缀 '0b'）添加到 res 中
       
       对于 res 中的每个元素 ele:
           如果 ele 不是 s 的子串:
               返回 False
       
       返回 True
   ```

4. **复杂度：**
   - 时间复杂度：$O(n \cdot m)$，其中 $n$ 是数字的范围，$m$ 是二进制字符串的平均长度。
   - 空间复杂度：$O(n \cdot m)$，用于存储从 1 到 N 的所有二进制字符串。