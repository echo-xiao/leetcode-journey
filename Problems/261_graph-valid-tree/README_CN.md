# 261. 以图判树

**难度**: Medium | **标签**: `Depth-First Search` `Breadth-First Search` `Union-Find` `Graph Theory`

## 题目描述

None

---
## 解题思路与复盘

1. 一句话直击本质：判断一个无向图是否为树的核心逻辑是检查图是否连通且无环，即边数为节点数减一，并通过遍历确认所有节点可达。

2. 综合思路：
   - **DFS 递归**：使用深度优先搜索递归遍历图，标记访问过的节点，最终检查所有节点是否都被访问。
   - **DFS 迭代**：使用栈实现深度优先搜索，类似递归方法，遍历图并检查连通性。
   - **BFS 迭代**：使用队列实现广度优先搜索，遍历图并检查所有节点是否可达。
   - **数据结构**：使用列表或集合来记录访问状态，列表用于布尔标记，集合用于存储已访问节点。

3. 全量伪代码：
   ```plaintext
   方法 validTree(n, edges):
       如果 边的数量 != n-1:
           返回 False

       初始化 邻接表 adj 为每个节点的空列表
       对于 每条边 (u, v) 在 edges 中:
           将 v 添加到 adj[u]
           将 u 添加到 adj[v]

       初始化 访问标记 visited 为大小为 n 的布尔列表或集合

       方法 DFS(curr, adj, visited):
           如果 curr 已访问:
               返回
           标记 curr 为已访问
           对于 curr 的每个邻居 neighbor:
               如果 neighbor 未访问:
                   递归调用 DFS(neighbor, adj, visited)

       方法 BFS(adj, visited):
           初始化 队列 queue 并将节点 0 入队
           标记节点 0 为已访问
           当 queue 非空:
               出队 curr
               对于 curr 的每个邻居 neighbor:
                   如果 neighbor 未访问:
                       标记 neighbor 为已访问
                       入队 neighbor

       选择 DFS 或 BFS 方法:
           DFS(0, adj, visited) 或 BFS(adj, visited)

       返回 所有节点是否都已访问
   ```

4. 复杂度：
   - 时间复杂度：$O(n + m)$，其中 $n$ 是节点数，$m$ 是边数，因为需要遍历所有节点和边。
   - 空间复杂度：$O(n)$，用于存储邻接表和访问标记。