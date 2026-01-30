# 323. 无向图中连通分量的数目

**难度**: Medium | **标签**: `Depth-First Search` `Breadth-First Search` `Union-Find` `Graph Theory`

## 题目描述

None

---
## 解题思路与复盘

1. 一句话直击本质：通过并查集或图遍历（DFS/BFS）来识别无向图中的连通分量。

2. 综合思路：
   - 并查集（Union-Find）：利用并查集数据结构，通过合并操作来减少连通分量的数量，最终返回连通分量的数量。
   - 深度优先搜索（DFS）：使用递归或栈来遍历图，标记访问过的节点，统计连通分量的数量。
   - 广度优先搜索（BFS）：使用队列来遍历图，标记访问过的节点，统计连通分量的数量。

3. 全量伪代码：
   - 并查集（Union-Find）：
     ```
     初始化 parent 数组为每个节点自身
     初始化连通分量计数为 n
     对于每条边 (u, v):
         找到 u 和 v 的根节点 root_u 和 root_v
         如果 root_u != root_v:
             将 root_u 挂在 root_v 下
             连通分量计数减 1
     返回连通分量计数
     ```

   - 深度优先搜索（DFS）：
     ```
     初始化邻接表 adj
     初始化 visited 数组为 False
     初始化连通分量计数为 0
     对于每个节点 i:
         如果 i 未被访问:
             连通分量计数加 1
             调用 DFS(i)
     返回连通分量计数

     DFS(curr):
         标记 curr 为已访问
         对于 curr 的每个邻居 neighbor:
             如果 neighbor 未被访问:
                 调用 DFS(neighbor)
     ```

   - 广度优先搜索（BFS）：
     ```
     初始化邻接表 adj
     初始化 visited 数组为 False
     初始化连通分量计数为 0
     对于每个节点 i:
         如果 i 未被访问:
             连通分量计数加 1
             初始化队列 queue 并将 i 入队
             标记 i 为已访问
             当队列不为空:
                 出队 curr
                 对于 curr 的每个邻居 neighbor:
                     如果 neighbor 未被访问:
                         标记 neighbor 为已访问
                         将 neighbor 入队
     返回连通分量计数
     ```

4. 复杂度：
   - 并查集（Union-Find）：
     - 时间复杂度：$O(n + m \cdot \alpha(n))$，其中 $m$ 是边的数量，$\alpha$ 是阿克曼函数的反函数。
     - 空间复杂度：$O(n)$。
   
   - 深度优先搜索（DFS）和广度优先搜索（BFS）：
     - 时间复杂度：$O(n + m)$。
     - 空间复杂度：$O(n + m)$。