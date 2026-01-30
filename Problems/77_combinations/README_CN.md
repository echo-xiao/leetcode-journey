# 77. 组合

**难度**: Medium | **标签**: `Backtracking`

## 题目描述

<p>给定两个整数 <code>n</code> 和 <code>k</code>，返回范围 <code>[1, n]</code> 中所有可能的 <code>k</code> 个数的组合。</p>

<p>你可以按 <strong>任何顺序</strong> 返回答案。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 4, k = 2
<strong>输出：</strong>
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1, k = 1
<strong>输出：</strong>[[1]]</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 20</code></li>
	<li><code>1 <= k <= n</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 该算法的核心逻辑是通过深度优先搜索（DFS）递归地构建所有可能的组合，当组合长度达到目标长度时将其加入结果集。

2. **综合思路：**
   - **递归与DFS：** 所有版本都使用了递归和深度优先搜索（DFS）来生成组合。通过递归调用，逐步构建组合，直到达到所需的长度。
   - **起始点控制：** 版本 2、3 和 4 使用了一个起始点参数来控制递归的范围，从而避免重复组合的生成。
   - **剪枝优化：** 版本 2 和 4 通过调整循环的结束条件进行剪枝，减少不必要的递归调用。

3. **全量伪代码：**

   ```plaintext
   定义函数 combine(n, k):
       初始化结果列表 res 为 []
       初始化路径列表 path 为 []
       调用 dfs(n, k, 1, path, res)
       返回 res

   定义函数 dfs(n, k, start, path, res):
       如果路径长度等于 k:
           将路径的副本加入结果列表 res
           返回

       对于 num 从 start 到 n 的某个上限:
           将 num 加入路径
           递归调用 dfs(n, k, num+1, path, res)
           从路径中移除 num

   版本 1 特殊逻辑:
       循环从 n 到 k-len(path)-1 递减

   版本 2 和 4 特殊逻辑:
       循环从 start 到 n-(k-len(path))+2

   版本 3 特殊逻辑:
       循环从 start 到 n+1
   ```

4. **复杂度：**

   - **时间复杂度：** $O(\binom{n}{k})$，因为算法需要生成所有可能的组合。
   - **空间复杂度：** $O(k)$，用于存储当前路径的递归调用栈。