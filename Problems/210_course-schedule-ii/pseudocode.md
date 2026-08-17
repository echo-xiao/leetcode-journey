# 210. 课程表 II · 解题思路与伪代码

1. 一句话直击本质：该算法的核心逻辑是通过拓扑排序（DFS或BFS）检测有向图中的环并确定课程的学习顺序。

2. 综合思路：
   - **DFS（深度优先搜索）**：使用递归或显式栈来遍历图，检测环并记录拓扑排序，利用三种状态（未访问、正在访问、已完成）来避免重复访问和检测环。
   - **BFS（广度优先搜索）**：通过入度数组和队列来实现拓扑排序，逐步减少节点的入度，入度为零的节点入队，直到所有节点被访问或检测到环。

3. 全量伪代码：
   - **DFS 递归实现**：
     ```
     初始化邻接表 adj 和状态数组 states
     对于每个课程 i：
         如果 states[i] 为未访问：
             如果 dfs(i) 返回 False：
                 返回空数组
     返回结果 res 的逆序

     函数 dfs(u):
         如果 states[u] 为已完成：
             返回 True
         如果 states[u] 为正在访问：
             返回 False
         将 states[u] 标记为正在访问
         对于邻居 v in adj[u]:
             如果 dfs(v) 返回 False：
                 返回 False
         将 states[u] 标记为已完成
         将 u 添加到 res
         返回 True
     ```

   - **DFS 显式栈实现**：
     ```
     初始化邻接表 adj 和访问标记 visited
     对于每个课程 i：
         如果 visited[i] 为未访问：
             初始化栈 stack，存储 (i, 0)
             当 stack 不为空：
                 弹出 (u, state)：
                 如果 state 为 0：
                     如果 visited[u] 为正在访问：
                         返回空数组
                     如果 visited[u] 为已完成：
                         继续
                     将 visited[u] 标记为正在访问
                     将 (u, 1) 压入栈
                     对于邻居 v in adj[u]:
                         如果 visited[v] 为未访问：
                             将 (v, 0) 压入栈
                         如果 visited[v] 为正在访问：
                             返回空数组
                 否则：
                     如果 visited[u] 不为已完成：
                         将 visited[u] 标记为已完成
                         将 u 添加到 res
     返回 res 的逆序，如果 res 长度等于课程总数，否则返回空数组
     ```

   - **BFS 实现**：
     ```
     初始化入度数组 indegree 和邻接表 adj
     对于每个先修关系 (cur, pre)：
         将 cur 添加到 adj[pre]
         增加 indegree[cur]
     初始化队列 queue，包含所有入度为 0 的节点
     初始化结果数组 res
     当 queue 不为空：
         弹出节点 u
         将 u 添加到 res
         对于邻居 v in adj[u]:
             减少 indegree[v]
             如果 indegree[v] 为 0：
                 将 v 添加到 queue
     如果 res 长度等于课程总数：
         返回 res
     否则：
         返回空数组
     ```

4. 复杂度：
   - 时间复杂度：$O(V + E)$，其中 $V$ 是课程数，$E$ 是先修关系数。
   - 空间复杂度：$O(V + E)$，用于存储邻接表和其他辅助数据结构。
