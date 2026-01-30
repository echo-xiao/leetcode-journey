# 2585. 删除每行中的最大值

**难度**: Easy | **标签**: `Array` `Sorting` `Heap (Priority Queue)` `Matrix` `Simulation`

## 题目描述

<p>给你一个 <code>m x n</code> 大小的矩阵 <code>grid</code> ，由若干正整数组成。</p>

<p>执行下述操作，直到 <code>grid</code> 变为空矩阵：</p>

<ul>
	<li>从每一行删除值最大的元素。如果存在多个这样的值，删除其中任何一个。</li>
	<li>将删除元素中的最大值与答案相加。</li>
</ul>

<p><strong>注意</strong> 每执行一次操作，矩阵中列的数据就会减 1 。</p>

<p>返回执行上述操作后的答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/10/19/q1ex1.jpg" style="width: 600px; height: 135px;" /></p>

<pre>
<strong>输入：</strong>grid = [[1,2,4],[3,3,1]]
<strong>输出：</strong>8
<strong>解释：</strong>上图展示在每一步中需要移除的值。
- 在第一步操作中，从第一行删除 4 ，从第二行删除 3（注意，有两个单元格中的值为 3 ，我们可以删除任一）。在答案上加 4 。
- 在第二步操作中，从第一行删除 2 ，从第二行删除 3 。在答案上加 3 。
- 在第三步操作中，从第一行删除 1 ，从第二行删除 1 。在答案上加 1 。
最终，答案 = 4 + 3 + 1 = 8 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/10/19/q1ex2.jpg" style="width: 83px; height: 83px;" /></p>

<pre>
<strong>输入：</strong>grid = [[10]]
<strong>输出：</strong>10
<strong>解释：</strong>上图展示在每一步中需要移除的值。
- 在第一步操作中，从第一行删除 10 。在答案上加 10 。
最终，答案 = 10 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质**：通过使用最大堆结构逐行删除每行的最大值，并在每列中选择最大的删除值累加得到结果。

2. **综合思路**：
   - **最大堆方法**：使用最大堆（通过 Python 的 `heapq` 实现最小堆的负值技巧）来存储每行的元素，逐行删除最大值，并在每列中选择最大的删除值进行累加。
   - **直接排序方法**（未在代码集中出现，但作为一种可能的解法）：直接对每行进行排序，逐行删除最大值，然后在每列中选择最大的删除值进行累加。

3. **全量伪代码**：
   - 初始化一个空列表 `arr` 用于存储每行的最大堆。
   - 初始化一个变量 `ttl` 为 0，用于累加结果。
   - 对于每一行：
     - 初始化一个空的最大堆 `maxHeap`。
     - 将该行的每个元素的负值插入 `maxHeap`。
     - 将 `maxHeap` 添加到 `arr` 中。
   - 对于每列：
     - 初始化一个空列表 `deleted`。
     - 对于每一行：
       - 从该行的堆中弹出最大值（负值转换为正值）。
       - 将该最大值添加到 `deleted` 中。
     - 找到 `deleted` 中的最大值 `res`。
     - 将 `res` 累加到 `ttl`。
   - 返回 `ttl`。

4. **复杂度**：
   - 时间复杂度：$O(m \cdot n \cdot \log n)$，其中 $m$ 是行数，$n$ 是列数。每行的元素需要插入堆中，且每列需要从堆中弹出元素。
   - 空间复杂度：$O(m \cdot n)$，用于存储每行的堆。