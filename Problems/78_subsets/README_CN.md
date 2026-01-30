# 78. 子集

**难度**: Medium | **标签**: `Array` `Backtracking` `Bit Manipulation`

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code> ，数组中的元素 <strong>互不相同</strong> 。返回该数组所有可能的<span data-keyword="subset">子集</span>（幂集）。</p>

<p>解集 <strong>不能</strong> 包含重复的子集。你可以按 <strong>任意顺序</strong> 返回解集。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
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
	<li><code>nums</code> 中的所有元素 <strong>互不相同</strong></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用深度优先搜索（DFS）递归地构建所有可能的子集。

2. 综合思路：
   - 递归 DFS：所有版本都使用递归的深度优先搜索方法来生成子集。通过递归调用，逐步构建子集，并在每一步将当前路径（子集）添加到结果集中。
   - 迭代与 BFS：虽然在给定的代码集中没有出现，但另一种常见方法是使用迭代或广度优先搜索（BFS）来生成子集。这种方法通常通过逐步扩展当前子集来实现。

3. 全量伪代码：
   ```plaintext
   定义函数 subsets(nums):
       初始化结果集 res 为一个空列表
       初始化路径 path 为一个空列表
       调用递归函数 dfs(nums, 0, res, path)
       返回结果集 res

   定义递归函数 dfs(nums, start, res, path):
       将当前路径 path 的副本添加到结果集 res 中

       如果 start 大于等于 nums 的长度:
           返回

       对于从 start 到 nums 长度的每一个索引 i:
           将 nums[i] 添加到路径 path 中
           递归调用 dfs(nums, i+1, res, path)
           从路径 path 中移除最后一个元素（回溯）
   ```

4. 复杂度：
   - 时间复杂度：$O(2^n \cdot n)$，其中 $n$ 是输入数组的长度。每个元素都有两种选择（在子集中或不在子集中），因此有 $2^n$ 个子集，每个子集的生成需要 $O(n)$ 的时间。
   - 空间复杂度：$O(n)$，用于递归调用栈和存储临时路径。