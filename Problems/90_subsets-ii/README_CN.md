# 90. 子集 II

**难度**: Medium | **标签**: `Array` `Backtracking` `Bit Manipulation`

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，其中可能包含重复元素，请你返回该数组所有可能的 <span data-keyword="subset">子集</span>（幂集）。</p>

<p>解集 <strong>不能</strong> 包含重复的子集。返回的解集中，子集可以按 <strong>任意顺序</strong> 排列。</p>

<div class="original__bRMd">
<div>
<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,2]
<strong>输出：</strong>[[],[1],[1,2],[1,2,2],[2],[2,2]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0]
<strong>输出：</strong>[[],[0]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
</ul>
</div>
</div>


---
## 解题思路与复盘

1. 一句话直击本质：
   - 通过深度优先搜索（DFS）结合剪枝策略，生成所有可能的子集，同时避免重复子集的生成。

2. 综合思路：
   - 递归与DFS：使用递归的深度优先搜索方法，遍历每个元素，构建子集。在递归过程中，通过排序和跳过重复元素来避免生成重复的子集。
   - 迭代与BFS：虽然在提供的代码集中没有迭代与广度优先搜索（BFS）的实现，但另一种可能的解法是使用迭代的方法，通过逐步扩展已有子集来生成新的子集，并在每次扩展时检查重复。

3. 全量伪代码：
   ```plaintext
   函数 subsetsWithDup(输入数组 nums):
       初始化结果列表 res 为 []
       初始化路径列表 path 为 []
       对 nums 进行排序
       调用 dfs(nums, 0, path, res)
       返回 res

   函数 dfs(输入数组 nums, 当前索引 idx, 当前路径 path, 结果列表 res):
       将当前路径 path 的副本添加到结果列表 res 中
       从当前索引 idx 开始遍历 nums:
           如果当前索引 i 大于 idx 且 nums[i] 等于 nums[i-1]，则跳过当前循环
           将 nums[i] 添加到当前路径 path
           递归调用 dfs(nums, i+1, path, res)
           从当前路径 path 中移除最后一个元素（回溯）
   ```

4. 复杂度：
   - 时间复杂度：$O(2^n \cdot n)$，其中 $n$ 是输入数组的长度。排序的时间复杂度为 $O(n \log n)$，而生成所有子集的复杂度为 $O(2^n)$，每个子集的生成需要 $O(n)$ 的时间。
   - 空间复杂度：$O(n)$，主要用于递归调用栈和存储临时路径。