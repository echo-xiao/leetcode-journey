# 367. 有效的完全平方数

**难度**: Easy | **标签**: `Math` `Binary Search`

## 题目描述

<p>给你一个正整数 <code>num</code> 。如果 <code>num</code> 是一个完全平方数，则返回 <code>true</code> ，否则返回 <code>false</code> 。</p>

<p><strong>完全平方数</strong> 是一个可以写成某个整数的平方的整数。换句话说，它可以写成某个整数和自身的乘积。</p>

<p>不能使用任何内置的库函数，如&nbsp; <code>sqrt</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>num = 16
<strong>输出：</strong>true
<strong>解释：</strong>返回 true ，因为 4 * 4 = 16 且 4 是一个整数。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>num = 14
<strong>输出：</strong>false
<strong>解释：</strong>返回 false ，因为 3.742 * 3.742 = 14 但 3.742 不是一个整数。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用二分查找算法在 1 到 num 的范围内寻找一个整数，使其平方等于 num。

2. 综合思路：
   - 递归二分查找：通过递归方式实现二分查找，逐步缩小搜索范围，直到找到平方等于 num 的整数或确定不存在。
   - 迭代二分查找：通过迭代方式实现二分查找，逐步调整左右边界，直到找到平方等于 num 的整数或确定不存在。

3. 全量伪代码：
   - 递归二分查找：
     ```
     函数 isPerfectSquare(num):
         返回 helper(num, 1, num)

     函数 helper(num, left, right):
         如果 left > right:
             返回 False

         mid = left + (right - left) // 2

         如果 mid * mid == num:
             返回 True
         否则如果 mid * mid > num:
             返回 helper(num, left, mid - 1)
         否则:
             返回 helper(num, mid + 1, right)
     ```

   - 迭代二分查找：
     ```
     函数 isPerfectSquare(num):
         初始化 left = 1, right = num

         当 left <= right 时:
             mid = left + (right - left) // 2

             如果 mid * mid == num:
                 返回 True
             否则如果 mid * mid > num:
                 right = mid - 1
             否则:
                 left = mid + 1

         返回 False
     ```

4. 复杂度：
   - 时间复杂度：$O(\log n)$，因为二分查找每次将搜索范围缩小一半。
   - 空间复杂度：递归版本为 $O(\log n)$（递归调用栈），迭代版本为 $O(1)$。