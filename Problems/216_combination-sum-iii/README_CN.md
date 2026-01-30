# 216. 组合总和 III

**难度**: Medium | **标签**: `Array` `Backtracking`

## 题目描述

<p>找出所有相加之和为&nbsp;<code>n</code><em> </em>的&nbsp;<code>k</code><strong>&nbsp;</strong>个数的组合，且满足下列条件：</p>

<ul>
	<li>只使用数字1到9</li>
	<li>每个数字&nbsp;<strong>最多使用一次</strong>&nbsp;</li>
</ul>

<p>返回 <em>所有可能的有效组合的列表</em> 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> <em><strong>k</strong></em> = 3, <em><strong>n</strong></em> = 7
<strong>输出:</strong> [[1,2,4]]
<strong>解释:</strong>
1 + 2 + 4 = 7
没有其他符合的组合了。</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> <em><strong>k</strong></em> = 3, <em><strong>n</strong></em> = 9
<strong>输出:</strong> [[1,2,6], [1,3,5], [2,3,4]]
<strong>解释:
</strong>1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
没有其他符合的组合了。</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> k = 4, n = 1
<strong>输出:</strong> []
<strong>解释:</strong> 不存在有效的组合。
在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 &gt; 1，没有有效的组合。
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>2 &lt;= k &lt;= 9</code></li>
	<li><code>1 &lt;= n &lt;= 60</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用深度优先搜索（DFS）遍历所有可能的数字组合，确保组合长度为 \(k\) 且总和为 \(n\)。

2. 综合思路：
   - **递归与DFS**：所有实现均采用递归的深度优先搜索方法，通过递归函数逐步构建可能的数字组合，并在满足条件时将其加入结果集中。
   - **剪枝优化**：在循环中提前判断当前组合的和是否已经超过目标值 \(n\)，以此减少不必要的递归调用。

3. 全量伪代码：
   ```plaintext
   定义函数 combinationSum3(k, n):
       初始化结果列表 res
       初始化路径列表 path
       调用递归函数 dfs(k, n, 1, path, res)
       返回 res

   定义递归函数 dfs(k, n, start, path, res):
       如果路径长度等于 k 且路径和等于 n:
           将路径的副本加入结果列表 res
           返回

       对于从 start 到 9 的每个数字 num:
           如果路径和加上 num 大于 n:
               结束循环 (剪枝)
           
           将 num 加入路径
           递归调用 dfs(k, n, num+1, path, res)
           从路径中移除 num (回溯)
   ```

4. 复杂度：
   - 时间复杂度：$O(2^9)$，因为每个数字可以选择或不选择，最多有 9 个数字可供选择。
   - 空间复杂度：$O(k)$，用于存储递归调用栈和当前路径。