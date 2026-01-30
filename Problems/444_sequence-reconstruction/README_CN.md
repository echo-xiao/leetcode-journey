# 444. 序列重建

**难度**: Medium | **标签**: `Array` `Graph Theory` `Topological Sort`

## 题目描述

None

---
## 解题思路与复盘

1. 一句话直击本质：
   - 使用拓扑排序验证唯一序列重建，通过检查是否存在唯一的拓扑排序路径来判断给定序列是否可以被唯一重建。

2. 综合思路：
   - 拓扑排序（BFS）：利用入度数组和邻接表构建图，使用队列进行拓扑排序，确保每次只有一个节点可以被选择以保证唯一性。

3. 全量伪代码：
   ```plaintext
   初始化节点数量 n 为 nums 的长度
   创建一个大小为 n+1 的入度数组 indegree，初始值为 0
   创建一个大小为 n+1 的邻接表 adj，初始为空列表

   对于每个序列 seq 在 sequences 中：
       对于 seq 中的每对相邻元素 (u, v)：
           在 adj[u] 中添加 v
           增加 indegree[v] 的值

   初始化队列 queue，包含所有入度为 0 的节点

   初始化结果列表 res 为空

   当队列不为空时：
       如果队列中元素数量大于 1，返回 False
       弹出队列中的第一个元素 curr
       将 curr 添加到结果列表 res 中
       对于 curr 的每个邻居 neighbor：
           减少 indegree[neighbor] 的值
           如果 indegree[neighbor] 为 0，将 neighbor 添加到队列中

   返回 res 是否等于 nums
   ```

4. 复杂度：
   - 时间复杂度：$O(n + m)$，其中 $n$ 是 nums 的长度，$m$ 是 sequences 中所有序列的总长度。
   - 空间复杂度：$O(n + m)$，用于存储入度数组和邻接表。