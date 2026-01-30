# 69. x 的平方根 

**难度**: Easy | **标签**: `Math` `Binary Search`

## 题目描述

<p>给你一个非负整数 <code>x</code> ，计算并返回&nbsp;<code>x</code>&nbsp;的 <strong>算术平方根</strong> 。</p>

<p>由于返回类型是整数，结果只保留 <strong>整数部分 </strong>，小数部分将被 <strong>舍去 。</strong></p>

<p><strong>注意：</strong>不允许使用任何内置指数函数和算符，例如 <code>pow(x, 0.5)</code> 或者 <code>x ** 0.5</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>x = 4
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>x = 8
<strong>输出：</strong>2
<strong>解释：</strong>8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：这些算法都通过二分查找或线性查找的方法来逼近并找到不超过给定数的最大整数平方根。

2. 综合思路：
   - 二分查找法（版本 1、2、3）：通过在可能的平方根范围内不断缩小搜索区间，快速逼近目标平方根。
   - 递归二分查找法（版本 3）：使用递归的方式实现二分查找，逻辑与迭代版本相同，但通过递归函数调用来实现。
   - 线性查找法（版本 4）：从0开始逐一尝试，直到找到第一个平方大于给定数的整数，然后返回前一个整数。

3. 全量伪代码：
   - 二分查找法（版本 1、2）：
     ```
     初始化 left 为 0 或 1，right 为 x，res 为 0
     当 left 小于等于 right 时：
         计算 mid 为 left 和 right 的中间值
         如果 mid 的平方等于 x，返回 mid
         如果 mid 的平方大于 x，right 设为 mid - 1
         如果 mid 的平方小于 x，res 设为 mid，left 设为 mid + 1
     返回 res
     ```
   - 递归二分查找法（版本 3）：
     ```
     定义递归函数 helper(x, left, right)
         如果 left 大于 right，返回 right
         计算 mid 为 left 和 right 的中间值
         如果 mid 的平方等于 x，返回 mid
         如果 mid 的平方大于 x，递归调用 helper(x, left, mid - 1)
         如果 mid 的平方小于 x，递归调用 helper(x, mid + 1, right)
     调用 helper(x, 0, x) 并返回结果
     ```
   - 线性查找法（版本 4）：
     ```
     初始化 i 为 0
     当 i 的平方小于等于 x 时：
         i 增加 1
     返回 i - 1
     ```

4. 复杂度：
   - 二分查找法（版本 1、2、3）的时间复杂度为 $O(\log x)$，空间复杂度为 $O(1)$（迭代版本）或 $O(\log x)$（递归版本）。
   - 线性查找法（版本 4）的时间复杂度为 $O(\sqrt{x})$，空间复杂度为 $O(1)$。