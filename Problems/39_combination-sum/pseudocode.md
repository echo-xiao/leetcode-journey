# 39. 组合总和 · 解题思路与伪代码

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
