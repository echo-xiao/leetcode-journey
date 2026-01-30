# 3691. 使每一列严格递增的最少操作次数

**难度**: Easy | **标签**: `Array` `Greedy` `Matrix`

## 题目描述

<p>给你一个由&nbsp;<b>非负&nbsp;</b>整数组成的 <code>m x n</code> 矩阵 <code>grid</code>。</p>

<p>在一次操作中，你可以将任意元素 <code>grid[i][j]</code> 的值增加 1。</p>

<p>返回使 <code>grid</code> 的所有列&nbsp;<strong>严格递增&nbsp;</strong>所需的&nbsp;<strong>最少&nbsp;</strong>操作次数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">grid = [[3,2],[1,3],[3,4],[0,1]]</span></p>

<p><strong>输出:</strong> <span class="example-io">15</span></p>

<p><strong>解释:</strong></p>

<ul>
	<li>为了让第 <code>0</code>&nbsp;列严格递增，可以对 <code>grid[1][0]</code> 执行 3 次操作，对 <code>grid[2][0]</code> 执行 2 次操作，对 <code>grid[3][0]</code> 执行 6 次操作。</li>
	<li>为了让第 <code>1</code>&nbsp;列严格递增，可以对 <code>grid[3][1]</code> 执行 4 次操作。</li>
</ul>
<img alt="" src="https://assets.leetcode.com/uploads/2024/11/10/firstexample.png" style="width: 200px; height: 347px;" /></div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">grid = [[3,2,1],[2,1,0],[1,2,3]]</span></p>

<p><strong>输出:</strong> <span class="example-io">12</span></p>

<p><strong>解释:</strong></p>

<ul>
	<li>为了让第 <code>0</code>&nbsp;列严格递增，可以对 <code>grid[1][0]</code> 执行 2 次操作，对 <code>grid[2][0]</code> 执行 4 次操作。</li>
	<li>为了让第 <code>1</code>&nbsp;列严格递增，可以对 <code>grid[1][1]</code> 执行 2 次操作，对 <code>grid[2][1]</code> 执行 2 次操作。</li>
	<li>为了让第 <code>2</code>&nbsp;列严格递增，可以对 <code>grid[1][2]</code> 执行 2 次操作。</li>
</ul>
<img alt="" src="https://assets.leetcode.com/uploads/2024/11/10/secondexample.png" style="width: 300px; height: 257px;" /></div>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>0 &lt;= grid[i][j] &lt; 2500</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过逐列检查并调整每列元素，使其严格递增，计算所需的最小操作次数。

2. 综合思路：
   - 迭代法：遍历每一列，将列中的元素提取为一维数组，然后通过线性扫描调整数组元素，使其严格递增，记录所需的调整次数。

3. 全量伪代码：
   ```
   定义函数 minimumOperations(grid):
       初始化总操作次数 ttl 为 0
       获取行数 rows 和列数 cols
       
       如果行数为 0:
           返回 0
       
       对于每一列 j 从 0 到 cols-1:
           初始化一个空数组 arr
           对于每一行 i 从 0 到 rows-1:
               将 grid[i][j] 添加到 arr 中
           计算调整 arr 为严格递增所需的操作次数 cal
           将 cal 添加到 ttl 中
       
       返回 ttl

   定义函数 cntOperation(nums):
       初始化操作次数 cnt 为 0
       对于每个元素 i 从 1 到 len(nums)-1:
           如果 nums[i-1] >= nums[i]:
               计算目标值 target 为 nums[i-1] + 1
               计算需要增加的值 needed 为 target - nums[i]
               增加 cnt 的值为 needed
               将 nums[i] 更新为 target
       返回 cnt
   ```

4. 复杂度：
   - 时间复杂度：$O(n \times m)$，其中 $n$ 是行数，$m$ 是列数，因为需要遍历每个元素。
   - 空间复杂度：$O(n)$，用于存储每列的元素。