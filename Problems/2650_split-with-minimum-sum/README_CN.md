# 2650. 最小和分割

**难度**: Easy | **标签**: `Math` `Greedy` `Sorting`

## 题目描述

<p>给你一个正整数&nbsp;<code>num</code>&nbsp;，请你将它分割成两个非负整数&nbsp;<code>num1</code> 和&nbsp;<code>num2</code>&nbsp;，满足：</p>

<ul>
	<li><code>num1</code> 和&nbsp;<code>num2</code>&nbsp;直接连起来，得到&nbsp;<code>num</code>&nbsp;各数位的一个排列。

	<ul>
		<li>换句话说，<code>num1</code> 和&nbsp;<code>num2</code>&nbsp;中所有数字出现的次数之和等于&nbsp;<code>num</code>&nbsp;中所有数字出现的次数。</li>
	</ul>
	</li>
	<li><code>num1</code> 和&nbsp;<code>num2</code>&nbsp;可以包含前导 0 。</li>
</ul>

<p>请你返回&nbsp;<code>num1</code> 和 <code>num2</code>&nbsp;可以得到的和的 <strong>最小</strong> 值。</p>

<p><strong>注意：</strong></p>

<ul>
	<li><code>num</code>&nbsp;保证没有前导 0 。</li>
	<li><code>num1</code> 和&nbsp;<code>num2</code>&nbsp;中数位顺序可以与&nbsp;<code>num</code>&nbsp;中数位顺序不同。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>num = 4325
<b>输出：</b>59
<b>解释：</b>我们可以将 4325 分割成 <code>num1 </code>= 24 和 <code>num2 </code>= 35 ，和为 59 ，59 是最小和。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>num = 687
<b>输出：</b>75
<b>解释：</b>我们可以将 687 分割成 <code>num1</code> = 68 和 <code>num2 </code>= 7 ，和为最优值 75 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>10 &lt;= num &lt;= 10<sup>9</sup></code></li>
</ul>


---
## 解题思路与复盘

### 1. 一句话直击本质

通过将数字的各位按升序排列后，交替分配到两个数字中，以最小化它们的和。

### 2. 综合思路

该题目主要有以下解法：

- **贪心算法**：通过将数字的各位按升序排列后，交替分配到两个数字中，确保每个数字的位数尽可能小，从而使得两个数字的和最小化。

### 3. 全量伪代码

以下是该算法的中文伪代码：

```plaintext
函数 splitNum(输入数字 num):
    将 num 转换为字符串并分割为字符列表
    对字符列表进行升序排序

    初始化 num1 和 num2 为两个空列表

    对于字符列表中的每个字符 i:
        如果 num2 的长度大于 num1 的长度:
            将字符 i 添加到 num1
        否则:
            将字符 i 添加到 num2

    将 num1 和 num2 转换为字符串并连接，然后转换为整数
    返回 num1 和 num2 的和
```

### 4. 复杂度

- **时间复杂度**: 排序操作的时间复杂度为 $O(n \log n)$，其中 $n$ 是数字的位数。
- **空间复杂度**: 需要额外的空间来存储排序后的字符列表和两个数字，空间复杂度为 $O(n)$。