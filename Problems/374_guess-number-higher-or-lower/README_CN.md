# 374. 猜数字大小

**难度**: Easy | **标签**: `Binary Search` `Interactive`

## 题目描述

<p>我们正在玩猜数字游戏。猜数字游戏的规则如下：</p>

<p>我会从&nbsp;<code>1</code>&nbsp;到&nbsp;<code>n</code> 随机选择一个数字。 请你猜选出的是哪个数字。（我选的数字在整个游戏中保持不变）。</p>

<p>如果你猜错了，我会告诉你，我选出的数字比你猜测的数字大了还是小了。</p>

<p>你可以通过调用一个预先定义好的接口 <code>int guess(int num)</code> 来获取猜测结果，返回值一共有三种可能的情况：</p>

<ul>
	<li><code>-1</code>：你猜的数字比我选出的数字大 （即&nbsp;<code>num &gt; pick</code>）。</li>
	<li><code>1</code>：你猜的数字比我选出的数字小&nbsp;（即&nbsp;<code>num &lt;&nbsp;pick</code>）。</li>
	<li><code>0</code>：你猜的数字与我选出的数字相等。（即&nbsp;<code>num&nbsp;== pick</code>）。</li>
</ul>

<p>返回我选出的数字。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 10, pick = 6
<strong>输出：</strong>6
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1, pick = 1
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 2, pick = 1
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>1 &lt;= pick &lt;= n</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是使用二分查找法来有效地缩小搜索范围，直到找到目标数字。

2. 综合思路：
   - 递归解法：通过递归调用函数来实现二分查找，每次根据 `guess` 函数的返回值调整搜索范围。
   - 迭代解法：使用一个循环来实现二分查找，通过调整左右边界来逐步缩小搜索范围，直到找到目标数字。

3. 全量伪代码：
   - 递归解法伪代码：
     ```
     定义函数 guessNumber(n):
         返回 helper(n, 1, n)

     定义函数 helper(n, left, right):
         计算 mid 为 left 和 right 的中间值
         如果 guess(mid) 返回 0:
             返回 mid
         如果 guess(mid) 返回 -1:
             返回 helper(n, left, mid-1)
         如果 guess(mid) 返回 1:
             返回 helper(n, mid+1, right)
     ```

   - 迭代解法伪代码：
     ```
     定义函数 guessNumber(n):
         初始化 left 为 1, right 为 n
         当 left 小于等于 right 时:
             计算 mid 为 left 和 right 的中间值
             如果 guess(mid) 返回 0:
                 返回 mid
             如果 guess(mid) 返回 -1:
                 将 right 更新为 mid - 1
             如果 guess(mid) 返回 1:
                 将 left 更新为 mid + 1
     ```

4. 复杂度：
   - 时间复杂度：$O(\log n)$，因为每次查找都将搜索范围缩小一半。
   - 空间复杂度：
     - 递归解法：$O(\log n)$，由于递归调用栈的深度。
     - 迭代解法：$O(1)$，因为只使用了有限的额外变量。