# 240. 搜索二维矩阵 II

**难度**: Medium | **标签**: `Array` `Binary Search` `Divide and Conquer` `Matrix`

## 题目描述

<p>编写一个高效的算法来搜索&nbsp;<code><em>m</em>&nbsp;x&nbsp;<em>n</em></code>&nbsp;矩阵 <code>matrix</code> 中的一个目标值 <code>target</code> 。该矩阵具有以下特性：</p>

<ul>
	<li>每行的元素从左到右升序排列。</li>
	<li>每列的元素从上到下升序排列。</li>
</ul>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>
<img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/11/25/searchgrid2.jpg" />
<pre>
<b>输入：</b>matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
<b>输出：</b>true
</pre>

<p><b>示例 2：</b></p>
<img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/11/25/searchgrid.jpg" />
<pre>
<b>输入：</b>matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
<b>输出：</b>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= n, m &lt;= 300</code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= matrix[i][j] &lt;= 10<sup>9</sup></code></li>
	<li>每行的所有元素从左到右升序排列</li>
	<li>每列的所有元素从上到下升序排列</li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：**  
   利用矩阵的排序特性，从矩阵的某个角落开始逐步缩小搜索范围，直到找到目标值或确定目标值不存在。

2. **综合思路：**  
   - **从右上角或左下角开始的线性搜索：**  
     通过从矩阵的右上角或左下角开始，根据当前元素与目标值的比较结果，决定向左或向下（或向右或向上）移动，从而逐步缩小搜索范围。
   - **逐行二分搜索：**  
     对每一行进行二分搜索，利用行内元素的有序性快速定位目标值。

3. **全量伪代码：**

   - **从右上角开始的线性搜索：**
     ```
     初始化 row 为 0，col 为矩阵列数减 1
     当 row 小于矩阵行数且 col 大于等于 0 时重复：
         如果 matrix[row][col] 等于 target，返回 True
         如果 matrix[row][col] 大于 target，col 减 1
         否则，row 加 1
     返回 False
     ```

   - **从左下角开始的线性搜索：**
     ```
     初始化 row 为矩阵行数减 1，col 为 0
     当 row 大于等于 0 且 col 小于矩阵列数时重复：
         如果 matrix[row][col] 等于 target，返回 True
         如果 matrix[row][col] 大于 target，row 减 1
         否则，col 加 1
     返回 False
     ```

   - **逐行二分搜索：**
     ```
     对于每一行 row 从 0 到矩阵行数减 1：
         初始化 left 为 0，right 为矩阵列数减 1
         当 left 小于等于 right 时重复：
             计算 mid 为 left 和 right 的中间索引
             如果 matrix[row][mid] 等于 target，返回 True
             如果 matrix[row][mid] 小于 target，left 设为 mid 加 1
             否则，right 设为 mid 减 1
     返回 False
     ```

4. **复杂度：**

   - **从右上角或左下角开始的线性搜索：**  
     时间复杂度：$O(m + n)$，其中 $m$ 是矩阵的行数，$n$ 是矩阵的列数。  
     空间复杂度：$O(1)$。

   - **逐行二分搜索：**  
     时间复杂度：$O(m \log n)$，其中 $m$ 是矩阵的行数，$n$ 是矩阵的列数。  
     空间复杂度：$O(1)$。