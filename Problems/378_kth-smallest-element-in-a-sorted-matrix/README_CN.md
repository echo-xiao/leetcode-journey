# 378. 有序矩阵中第 K 小的元素

**难度**: Medium | **标签**: `Array` `Binary Search` `Sorting` `Heap (Priority Queue)` `Matrix`

## 题目描述

<p>给你一个&nbsp;<code>n x n</code><em>&nbsp;</em>矩阵&nbsp;<code>matrix</code> ，其中每行和每列元素均按升序排序，找到矩阵中第 <code>k</code> 小的元素。<br />
请注意，它是 <strong>排序后</strong> 的第 <code>k</code> 小元素，而不是第 <code>k</code> 个 <strong>不同</strong> 的元素。</p>

<p>你必须找到一个内存复杂度优于&nbsp;<code>O(n<sup>2</sup>)</code> 的解决方案。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
<strong>输出：</strong>13
<strong>解释：</strong>矩阵中的元素为 [1,5,9,10,11,12,13,<strong>13</strong>,15]，第 8 小元素是 13
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[-5]], k = 1
<strong>输出：</strong>-5
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>-10<sup>9</sup> &lt;= matrix[i][j] &lt;= 10<sup>9</sup></code></li>
	<li>题目数据 <strong>保证</strong> <code>matrix</code> 中的所有行和列都按 <strong>非递减顺序</strong> 排列</li>
	<li><code>1 &lt;= k &lt;= n<sup>2</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>你能否用一个恒定的内存(即 <code>O(1)</code> 内存复杂度)来解决这个问题?</li>
	<li>你能在 <code>O(n)</code> 的时间复杂度下解决这个问题吗?这个方法对于面试来说可能太超前了，但是你会发现阅读这篇文章（&nbsp;<a href="http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf" target="_blank">this paper</a>&nbsp;）很有趣。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：
   - 该算法的核心逻辑是利用二分查找结合计数方法，在有序矩阵中确定第 K 小的元素。

2. 综合思路：
   - 二分查找法：通过在矩阵的最小值和最大值之间进行二分查找，逐步缩小范围，利用计数函数确定当前中间值在矩阵中的排名，调整搜索区间，直到找到第 K 小的元素。

3. 全量伪代码：
   ```plaintext
   定义函数 kthSmallest(matrix, k):
       初始化 left 为矩阵的第一个元素
       初始化 right 为矩阵的最后一个元素

       当 left 小于 right 时:
           计算 mid 为 left 和 right 的中间值
           调用辅助函数 cntElement(matrix, mid) 或 countLessEqual(matrix, mid) 计算小于等于 mid 的元素个数 cnt

           如果 cnt 小于 k:
               更新 left 为 mid + 1
           否则:
               更新 right 为 mid

       返回 left

   定义辅助函数 cntElement(matrix, mid) 或 countLessEqual(matrix, mid):
       初始化 row 为矩阵的最后一行
       初始化 col 为矩阵的第一列
       初始化计数器 cnt 为 0

       当 row 大于等于 0 且 col 小于矩阵的列数时:
           如果 matrix[row][col] 小于等于 mid:
               将 cnt 增加 row + 1
               增加 col
           否则:
               减少 row

       返回 cnt
   ```

4. 复杂度：
   - 时间复杂度：$O(n \log (max - min))$，其中 $n$ 是矩阵的维度，$max$ 和 $min$ 分别是矩阵中的最大值和最小值。
   - 空间复杂度：$O(1)$，因为只使用了常数级别的额外空间。