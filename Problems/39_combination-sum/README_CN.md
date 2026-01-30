# 39. 组合总和

**难度**: Medium | **标签**: `Array` `Backtracking`

## 题目描述

<p>给你一个 <strong>无重复元素</strong> 的整数数组&nbsp;<code>candidates</code> 和一个目标整数&nbsp;<code>target</code>&nbsp;，找出&nbsp;<code>candidates</code>&nbsp;中可以使数字和为目标数&nbsp;<code>target</code> 的 所有<em>&nbsp;</em><strong>不同组合</strong> ，并以列表形式返回。你可以按 <strong>任意顺序</strong> 返回这些组合。</p>

<p><code>candidates</code> 中的 <strong>同一个</strong> 数字可以 <strong>无限制重复被选取</strong> 。如果至少一个数字的被选数量不同，则两种组合是不同的。&nbsp;</p>

<p>对于给定的输入，保证和为&nbsp;<code>target</code> 的不同组合数少于 <code>150</code> 个。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>candidates = [2,3,6,7], target = 7
<strong>输出：</strong>[[2,2,3],[7]]
<strong>解释：</strong>
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入: </strong>candidates = [2,3,5], target = 8
<strong>输出: </strong>[[2,2,2,2],[2,3,3],[3,5]]</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入: </strong>candidates = [2], target = 1
<strong>输出: </strong>[]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= candidates.length &lt;= 30</code></li>
	<li><code>2 &lt;= candidates[i] &lt;= 40</code></li>
	<li><code>candidates</code> 的所有元素 <strong>互不相同</strong></li>
	<li><code>1 &lt;= target &lt;= 40</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用深度优先搜索（DFS）遍历所有可能的组合，寻找和为目标值的组合。

2. 综合思路：
   - 递归与DFS：所有版本都使用递归和深度优先搜索（DFS）来解决问题。通过递归调用，探索每个候选数的可能组合，并在每次递归中减去当前选择的数值，直到找到一个和为目标值的组合。
   - 数据结构：使用列表来存储当前路径和结果集。路径用于记录当前组合，结果集用于存储所有满足条件的组合。

3. 全量伪代码：
   ```
   定义函数 combinationSum(candidates, target):
       初始化结果集 res 为一个空列表
       初始化路径 path 为一个空列表
       调用 dfs(candidates, target, 0, path, res)
       返回结果集 res

   定义函数 dfs(candidates, target, start, path, res):
       如果 target 等于 0:
           将路径的副本添加到结果集 res 中
           返回

       如果 target 小于 0:
           返回

       对于从 start 到 candidates 长度的每个索引 i:
           获取当前候选数 c 为 candidates[i]
           将 c 添加到路径 path 中
           递归调用 dfs(candidates, target-c, i, path, res)
           从路径 path 中移除最后一个元素
   ```

4. 复杂度：
   - 时间复杂度：$O(N^{T/M+1})$，其中 $N$ 是候选数的数量，$T$ 是目标值，$M$ 是候选数中的最小值。复杂度来源于递归树的深度和每层的分支数。
   - 空间复杂度：$O(T/M)$，用于存储递归调用栈和路径。