# 40. 组合总和 II

**难度**: Medium | **标签**: `Array` `Backtracking`

## 题目描述

<p>给定一个候选人编号的集合&nbsp;<code>candidates</code>&nbsp;和一个目标数&nbsp;<code>target</code>&nbsp;，找出&nbsp;<code>candidates</code>&nbsp;中所有可以使数字和为&nbsp;<code>target</code>&nbsp;的组合。</p>

<p><code>candidates</code>&nbsp;中的每个数字在每个组合中只能使用&nbsp;<strong>一次</strong>&nbsp;。</p>

<p><strong>注意：</strong>解集不能包含重复的组合。&nbsp;</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong> candidates =&nbsp;<code>[10,1,2,7,6,1,5]</code>, target =&nbsp;<code>8</code>,
<strong>输出:</strong>
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> candidates =&nbsp;[2,5,2,1,2], target =&nbsp;5,
<strong>输出:</strong>
[
[1,2,2],
[5]
]</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;candidates.length &lt;= 100</code></li>
	<li><code>1 &lt;=&nbsp;candidates[i] &lt;= 50</code></li>
	<li><code>1 &lt;= target &lt;= 30</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法通过深度优先搜索（DFS）结合剪枝策略，避免重复组合以找到所有和为目标值的唯一组合。

2. 综合思路：
   - **递归与DFS**：使用递归的深度优先搜索方法遍历所有可能的组合路径，结合排序和剪枝策略避免重复组合。
   - **剪枝策略**：在递归过程中，通过排序后的数组和索引判断，跳过重复元素以减少不必要的计算。

3. 全量伪代码：
   ```plaintext
   定义函数 combinationSum2(candidates, target):
       初始化结果列表 res
       初始化路径列表 path
       对 candidates 进行排序
       调用 dfs(candidates, target, 0, path, res)
       返回 res

   定义函数 dfs(candidates, target, begin, path, res):
       如果 target 等于 0:
           将 path 的副本添加到 res 中
           返回

       如果 target 小于 0:
           返回

       对于从 begin 到 candidates 长度的每个索引 idx:
           令 c 为 candidates[idx]

           如果 idx 大于 begin 且 candidates[idx] 等于 candidates[idx-1]:
               跳过当前循环

           将 c 添加到 path
           调用 dfs(candidates, target-c, idx+1, path, res)
           从 path 中移除最后一个元素
   ```

4. 复杂度：
   - 时间复杂度：$O(2^n)$，其中 $n$ 是候选数组的长度。由于每个元素可以选择或不选择，组合数量在最坏情况下为指数级。
   - 空间复杂度：$O(n)$，主要用于递归调用栈和存储临时路径。