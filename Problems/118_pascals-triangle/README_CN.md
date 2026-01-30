# 118. 杨辉三角

**难度**: Easy | **标签**: `Array` `Dynamic Programming`

## 题目描述

<p>给定一个非负整数&nbsp;<em><code>numRows</code>，</em>生成「杨辉三角」的前&nbsp;<em><code>numRows</code>&nbsp;</em>行。</p>

<p>在<strong>「杨辉三角」</strong>中，每个数是它左上方和右上方的数的和。</p>

<p><img alt="" src="https://pic.leetcode.cn/1626927345-DZmfxB-PascalTriangleAnimated2.gif" /></p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> numRows = 5
<strong>输出:</strong> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> numRows = 1
<strong>输出:</strong> [[1]]
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= numRows &lt;= 30</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：杨辉三角的生成依赖于前一行的元素之和来构建当前行的中间元素，首尾元素始终为1。

2. 综合思路：
   - 迭代法：通过迭代从第一行开始逐行构建杨辉三角，每一行的中间元素通过前一行的相邻元素之和计算得出。
   - 递归法：通过递归调用生成前 n-1 行的杨辉三角，然后基于最后一行构建第 n 行。

3. 全量伪代码：
   - 迭代法：
     ```
     初始化结果数组 arr 为 [[1]]
     对于从 1 到 numRows-1 的每一个 i：
         取出 arr 的最后一行 lastRow
         初始化新行 newRow 为 [1]
         对于从 0 到 lastRow 的长度减去 2 的每一个 j：
             将 lastRow[j] + lastRow[j+1] 添加到 newRow
         将 1 添加到 newRow
         将 newRow 添加到 arr
     返回 arr
     ```
   - 递归法：
     ```
     如果 numRows 等于 1，返回 [[1]]
     如果 numRows 等于 2，返回 [[1], [1, 1]]
     调用递归函数生成前 numRows-1 行的杨辉三角 preProb
     基于 preProb 的最后一行生成新行 subProb
     将 subProb 添加到 preProb
     返回 preProb

     定义函数 subProb(lastRow):
         初始化新行 newRow 为 [1]
         对于从 0 到 lastRow 的长度减去 2 的每一个 idx：
             将 lastRow[idx] + lastRow[idx+1] 添加到 newRow
         将 1 添加到 newRow
         返回 newRow
     ```

4. 复杂度：
   - 时间复杂度：$O(n^2)$，其中 $n$ 是行数，因为每一行的生成需要遍历前一行的所有元素。
   - 空间复杂度：$O(n^2)$，因为需要存储整个杨辉三角的所有行。