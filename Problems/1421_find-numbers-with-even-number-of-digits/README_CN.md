# 1421. 统计位数为偶数的数字

**难度**: Easy | **标签**: `Array` `Math`

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>，请你返回其中包含&nbsp;<strong>偶数</strong>&nbsp;个数位的数字的个数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [12,345,2,6,7896]
<strong>输出：</strong>2
<strong>解释：
</strong>12 是 2 位数字（位数为偶数）&nbsp;
345 是 3 位数字（位数为奇数）&nbsp;&nbsp;
2 是 1 位数字（位数为奇数）&nbsp;
6 是 1 位数字 位数为奇数）&nbsp;
7896 是 4 位数字（位数为偶数）&nbsp;&nbsp;
因此只有 12 和 7896 是位数为偶数的数字
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [555,901,482,1771]
<strong>输出：</strong>1 
<strong>解释： </strong>
只有 1771 是位数为偶数的数字。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：算法的核心逻辑是通过将数字转换为字符串来计算其位数，并统计位数为偶数的数字个数。

2. 综合思路：
   - 迭代法：遍历数组中的每个数字，将其转换为字符串以计算位数，并检查位数是否为偶数。
   - 生成器表达式：使用生成器表达式在一行代码中完成上述逻辑，直接返回符合条件的数字个数。

3. 全量伪代码：
   ```
   定义函数 findNumbers(nums)
       初始化计数器 cnt 为 0
       对于 nums 中的每个数字 n
           将 n 转换为字符串
           如果字符串长度是偶数
               增加计数器 cnt
       返回计数器 cnt

   或者

   定义函数 findNumbers(nums)
       返回生成器表达式的结果：
           对于 nums 中的每个数字 n
               如果 n 转换为字符串后的长度是偶数
                   计为 1
               否则
                   计为 0
           求和生成器表达式的结果
   ```

4. 复杂度：
   - 时间复杂度：$O(n \cdot m)$，其中 $n$ 是数组的长度，$m$ 是数字转换为字符串后的平均长度。
   - 空间复杂度：$O(1)$，不考虑输入和输出的存储空间。