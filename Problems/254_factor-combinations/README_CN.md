# 254. 因子的组合

**难度**: Medium | **标签**: `Backtracking`

## 题目描述

None

---
## 解题思路与复盘

1. 一句话直击本质：使用深度优先搜索（DFS）从小到大枚举因子，递归地构建因子组合。

2. 综合思路：
   - 递归 DFS：所有版本都采用了递归的深度优先搜索方法，从2开始尝试所有可能的因子，若能整除则递归地继续寻找因子组合。
   - 版本 1、2、3：使用for循环遍历可能的因子，并在找到因子后递归调用自身。
   - 版本 4：使用while循环替代for循环，但逻辑上与前几个版本相同。

3. 全量伪代码：
   ```plaintext
   定义函数 getFactors(n):
       初始化结果列表 res
       初始化路径列表 path
       调用 dfs(n, 2, path, res)
       返回 res

   定义函数 dfs(target, start, path, res):
       对于 i 从 start 到 sqrt(target) 的整数:
           如果 target 可以被 i 整除:
               将 path + [i, target // i] 添加到 res
               将 i 添加到 path
               递归调用 dfs(target // i, i, path, res)
               从 path 移除 i
   ```

4. 复杂度：
   - 时间复杂度：$O(n^{\log n})$，因为每个因子组合的生成涉及递归调用，且每次递归调用的深度与因子数量相关。
   - 空间复杂度：$O(\log n)$，主要由递归调用栈的深度决定，最坏情况下递归深度为 $\log n$。