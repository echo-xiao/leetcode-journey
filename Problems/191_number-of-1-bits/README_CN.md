# 191. 位1的个数

**难度**: Easy | **标签**: `Divide and Conquer` `Bit Manipulation`

## 题目描述

<p>给定一个正整数 <code>n</code>，编写一个函数，获取一个正整数的二进制形式并返回其二进制表达式中 <span data-keyword="set-bit">设置位</span> 的个数（也被称为<a href="https://baike.baidu.com/item/%E6%B1%89%E6%98%8E%E9%87%8D%E9%87%8F" target="_blank">汉明重量</a>）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 11
<strong>输出：</strong>3
<strong>解释：</strong>输入的二进制串 <code><strong>1011</strong>&nbsp;中，共有 3 个设置位。</code>
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 128
<strong>输出：</strong>1
<strong>解释：</strong>输入的二进制串 <strong>10000000</strong>&nbsp;中，共有 1 个设置位。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 2147483645
<strong>输出：</strong>30
<strong>解释：</strong>输入的二进制串 <strong>1111111111111111111111111111101</strong> 中，共有 30 个设置位。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<ul>
</ul>

<p>&nbsp;</p>

<p><strong>进阶</strong>：</p>

<ul>
	<li>如果多次调用这个函数，你将如何优化你的算法？</li>
</ul>


---
## 解题思路与复盘

### 一句话直击本质
通过逐位检查整数的二进制表示来统计其中的1的个数。

### 综合思路
1. **逐位检查法**：通过不断将整数除以2，检查每一位是否为1，直到整数为0。
2. **位操作法**：利用位操作（如与操作）来快速消除最低有效位的1。
3. **内置函数法**：使用语言内置的函数直接计算二进制表示中1的个数（如Python的`bin()`和`count()`组合）。

### 全量伪代码
1. **逐位检查法**：
   ```plaintext
   初始化计数器 cnt 为 0
   当 n 大于 0 时重复以下步骤：
       如果 n 的最低位为 1（n % 2 == 1）：
           将 cnt 加 1
       将 n 右移一位（n = n // 2）
   返回 cnt
   ```

2. **位操作法**：
   ```plaintext
   初始化计数器 cnt 为 0
   当 n 不等于 0 时重复以下步骤：
       将 cnt 加 1
       将 n 与 (n - 1) 进行按位与操作（n = n & (n - 1)）
   返回 cnt
   ```

3. **内置函数法**：
   ```plaintext
   将 n 转换为二进制字符串
   统计二进制字符串中字符 '1' 的个数
   返回计数结果
   ```

### 复杂度
- **逐位检查法**：时间复杂度为 $O(\log n)$，空间复杂度为 $O(1)$。
- **位操作法**：时间复杂度为 $O(k)$，其中 $k$ 是二进制表示中1的个数，空间复杂度为 $O(1)$。
- **内置函数法**：时间复杂度为 $O(\log n)$，空间复杂度为 $O(\log n)$（取决于语言实现）。