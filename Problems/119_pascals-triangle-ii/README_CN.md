# 119. 杨辉三角 II

**难度**: Easy | **标签**: `Array` `Dynamic Programming`

## 题目描述

<p>给定一个非负索引 <code>rowIndex</code>，返回「杨辉三角」的第 <code>rowIndex</code><em> </em>行。</p>

<p><small>在「杨辉三角」中，每个数是它左上方和右上方的数的和。</small></p>

<p><img alt="" src="https://pic.leetcode.cn/1626927345-DZmfxB-PascalTriangleAnimated2.gif" /></p>

<p> </p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> rowIndex = 3
<strong>输出:</strong> [1,3,3,1]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> rowIndex = 0
<strong>输出:</strong> [1]
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> rowIndex = 1
<strong>输出:</strong> [1,1]
</pre>

<p> </p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>0 <= rowIndex <= 33</code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong></p>

<p>你可以优化你的算法到 <code><em>O</em>(<i>rowIndex</i>)</code> 空间复杂度吗？</p>


---
## 解题思路与复盘

1. 一句话直击本质：该算法通过递归计算上一行的杨辉三角值，并利用其生成当前行。

2. 综合思路：
   - 递归解法：通过递归调用计算前一行的值，然后根据杨辉三角的性质生成当前行。
   - 迭代解法（未在代码集中出现）：可以通过迭代逐行计算，避免递归的额外开销。

3. 全量伪代码：
   - 递归解法：
     ```
     定义函数 getRow(rowIndex):
         如果 rowIndex 等于 0:
             返回 [1]
         如果 rowIndex 等于 1:
             返回 [1, 1]
         
         lastRow = 调用 getRow(rowIndex - 1)
         newRow = 调用 newRow(lastRow)
         
         返回 newRow

     定义函数 newRow(lastRow):
         初始化 newRow 为 [1]
         对于 idx 从 0 到 len(lastRow) - 2:
             计算 num = lastRow[idx] + lastRow[idx + 1]
             将 num 添加到 newRow
         将 1 添加到 newRow
         返回 newRow
     ```

4. 复杂度：
   - 时间复杂度：递归解法的时间复杂度为 $O(n^2)$，因为每一行的生成需要遍历上一行的所有元素。
   - 空间复杂度：递归解法的空间复杂度为 $O(n)$，主要由于递归调用栈的深度为 $n$。