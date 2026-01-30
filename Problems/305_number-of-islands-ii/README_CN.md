# 305. 岛屿数量 II

**难度**: Hard | **标签**: `Array` `Hash Table` `Union-Find`

## 题目描述

None

---
## 解题思路与复盘

1. 一句话直击本质：该算法使用并查集（Union-Find）数据结构来动态管理和合并岛屿，从而高效地计算每次添加陆地后的岛屿数量。

2. 综合思路：
   - 并查集（Union-Find）：使用并查集数据结构来管理每个陆地的连通性，通过路径压缩和按秩合并来优化查询和合并操作的效率。
   - 其他可能解法（未在提供的代码中出现）：可以使用DFS或BFS来遍历和标记岛屿，但这些方法在动态添加陆地的情况下效率较低。

3. 全量伪代码：
   ```plaintext
   初始化并查集 parent 数组，大小为 m * n，初始值为自身索引
   初始化 isLand 数组，大小为 m * n，初始值为 False
   初始化岛屿计数器 cnt 为 0
   初始化结果列表 res

   对于每个位置 (r, c) 在 positions 中：
       计算该位置的索引 idx = r * n + c
       如果该位置已经是陆地：
           将当前岛屿数量 cnt 添加到结果列表 res
           继续下一个位置

       将该位置标记为陆地 isLand[idx] = True
       增加岛屿计数器 cnt

       对于每个方向 (dr, dc) 在 [(0, 1), (0, -1), (1, 0), (-1, 0)] 中：
           计算新位置 (nr, nc) = (r + dr, c + dc)
           计算新位置的索引 nidx = nr * n + nc
           如果新位置在边界内且是陆地：
               合并当前索引 idx 和新索引 nidx

       将当前岛屿数量 cnt 添加到结果列表 res

   返回结果列表 res

   函数 find(i):
       如果 parent[i] 不是 i：
           递归查找 parent[i] 的根，并路径压缩
       返回根节点

   函数 union(i, j):
       找到 i 和 j 的根节点 rooti 和 rootj
       如果 rooti 和 rootj 不同：
           将 rooti 的父节点设为 rootj
           减少岛屿计数器 cnt
   ```

4. 复杂度：
   - 时间复杂度：$O(k \cdot \alpha(m \cdot n))$，其中 $k$ 是 positions 的长度，$\alpha$ 是反阿克曼函数，表示并查集操作的均摊时间复杂度。
   - 空间复杂度：$O(m \cdot n)$，用于存储并查集的父节点数组和陆地标记数组。