# 1476. 统计有序矩阵中的负数

**难度**: Easy | **标签**: `Array` `Binary Search` `Matrix`

## 题目描述

<p>给你一个&nbsp;<code>m&nbsp;* n</code>&nbsp;的矩阵&nbsp;<code>grid</code>，矩阵中的元素无论是按行还是按列，都以非严格递减顺序排列。&nbsp;请你统计并返回&nbsp;<code>grid</code>&nbsp;中 <strong>负数</strong> 的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
<strong>输出：</strong>8
<strong>解释：</strong>矩阵中共有 8 个负数。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [[3,2],[1,0]]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>-100 &lt;= grid[i][j] &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你可以设计一个时间复杂度为 <code>O(n + m)</code> 的解决方案吗？</p>


---
## 解题思路与复盘

1. 一句话直击本质：利用二分查找或从矩阵的右下角开始遍历，快速定位每行或每列的第一个负数，从而统计负数的总数。

2. 综合思路：
   - **二分查找**：对于每一行，使用二分查找找到第一个负数的位置，然后计算该位置到行末的元素个数，这些元素都是负数。
   - **矩阵遍历**：从矩阵的右下角开始，向上或向左移动，逐行或逐列统计负数的数量。

3. 全量伪代码：
   - **二分查找方法**：
     ```
     初始化结果计数 res 为 0
     对于每一行 lst in grid:
         初始化 left 为 0, right 为 len(lst) - 1
         当 left <= right:
             计算 mid 为 left + (right - left) // 2
             如果 lst[mid] >= 0:
                 将 left 更新为 mid + 1
             否则:
                 将 right 更新为 mid - 1
         计算负数的数量为 len(lst) - left
         将负数数量加入 res
     返回 res
     ```
   - **矩阵遍历方法**：
     ```
     如果 grid 为空或 grid[0] 为空，返回 0
     初始化行数 m 和列数 n
     初始化 row 为 m - 1, col 为 0, 计数 count 为 0
     当 row >= 0 且 col < n:
         如果 grid[row][col] < 0:
             将 count 增加 n - col
             将 row 减 1
         否则:
             将 col 增加 1
     返回 count
     ```

4. 复杂度：
   - **二分查找方法**：
     - 时间复杂度：$O(m \log n)$，其中 $m$ 是矩阵的行数，$n$ 是矩阵的列数。
     - 空间复杂度：$O(1)$。
   - **矩阵遍历方法**：
     - 时间复杂度：$O(m + n)$，因为最多遍历 $m + n$ 个元素。
     - 空间复杂度：$O(1)$。