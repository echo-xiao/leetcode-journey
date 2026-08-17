# 133. 克隆图 · 解题思路与伪代码

1. 一句话直击本质：克隆图的核心逻辑是通过深度优先搜索（DFS）或广度优先搜索（BFS）遍历图的每个节点，并使用哈希表记录已访问节点以避免重复克隆。

2. 综合思路：
   - **DFS 递归解法**：使用递归函数进行深度优先搜索，克隆每个节点并递归克隆其邻居，利用哈希表记录已克隆的节点。
   - **DFS 迭代解法**：使用栈进行迭代的深度优先搜索，类似递归解法，克隆节点并处理其邻居。
   - **BFS 迭代解法**：使用队列进行广度优先搜索，逐层克隆节点及其邻居，确保每个节点只被克隆一次。

3. 全量伪代码：
   - **DFS 递归解法伪代码**：
     ```
     函数 cloneGraph(node):
         如果 node 为空:
             返回 None
         初始化 visited 哈希表
         返回 dfs(node, visited)

     函数 dfs(curr, visited):
         如果 curr 在 visited 中:
             返回 visited[curr]
         克隆当前节点 curr，创建 cloneNode
         将 curr 映射到 cloneNode 在 visited 中
         对于 curr 的每个邻居 neighbor:
             克隆邻居并添加到 cloneNode 的邻居列表中
         返回 cloneNode
     ```

   - **DFS 迭代解法伪代码**：
     ```
     函数 cloneGraph(node):
         如果 node 为空:
             返回 None
         初始化 visited 哈希表
         初始化栈 stack 并将 node 入栈
         克隆 node 并存储在 visited 中
         当栈不为空:
             弹出栈顶元素 curr
             对于 curr 的每个邻居 neighbor:
                 如果 neighbor 不在 visited 中:
                     克隆 neighbor 并存储在 visited 中
                     将 neighbor 入栈
                 将克隆的 neighbor 添加到克隆的 curr 的邻居列表中
         返回克隆的起始节点
     ```

   - **BFS 迭代解法伪代码**：
     ```
     函数 cloneGraph(node):
         如果 node 为空:
             返回 None
         初始化 visited 哈希表
         初始化队列 queue 并将 node 入队
         克隆 node 并存储在 visited 中
         当队列不为空:
             弹出队首元素 curr
             对于 curr 的每个邻居 neighbor:
                 如果 neighbor 不在 visited 中:
                     克隆 neighbor 并存储在 visited 中
                     将 neighbor 入队
                 将克隆的 neighbor 添加到克隆的 curr 的邻居列表中
         返回克隆的起始节点
     ```

4. 复杂度：
   - 时间复杂度：所有版本的时间复杂度均为 $O(n)$，其中 $n$ 是图中节点的数量，因为每个节点和边都只被访问一次。
   - 空间复杂度：所有版本的空间复杂度均为 $O(n)$，用于存储已访问节点的哈希表和递归栈或迭代栈/队列。
