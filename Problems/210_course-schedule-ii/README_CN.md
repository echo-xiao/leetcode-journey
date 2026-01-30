# 210. 课程表 II

**难度**: Medium | **标签**: `Depth-First Search` `Breadth-First Search` `Graph Theory` `Topological Sort`

## 题目描述

<p>现在你总共有 <code>numCourses</code> 门课需要选，记为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>numCourses - 1</code>。给你一个数组&nbsp;<code>prerequisites</code> ，其中 <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> ，表示在选修课程 <code>a<sub>i</sub></code> 前 <strong>必须</strong> 先选修&nbsp;<code>b<sub>i</sub></code> 。</p>

<ul>
	<li>例如，想要学习课程 <code>0</code> ，你需要先完成课程&nbsp;<code>1</code> ，我们用一个匹配来表示：<code>[0,1]</code> 。</li>
</ul>

<p>返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 <strong>任意一种</strong> 就可以了。如果不可能完成所有课程，返回 <strong>一个空数组</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>numCourses = 2, prerequisites = [[1,0]]
<strong>输出：</strong>[0,1]
<strong>解释：</strong>总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 <code>[0,1] 。</code>
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
<strong>输出：</strong>[0,2,1,3]
<strong>解释：</strong>总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
因此，一个正确的课程顺序是&nbsp;<code>[0,1,2,3]</code> 。另一个正确的排序是&nbsp;<code>[0,2,1,3]</code> 。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>numCourses = 1, prerequisites = []
<strong>输出：</strong>[0]
</pre>

<p>&nbsp;</p>
<strong>提示：</strong>

<ul>
	<li><code>1 &lt;= numCourses &lt;= 2000</code></li>
	<li><code>0 &lt;= prerequisites.length &lt;= numCourses * (numCourses - 1)</code></li>
	<li><code>prerequisites[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; numCourses</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>所有<code>[a<sub>i</sub>, b<sub>i</sub>]</code> <strong>互不相同</strong></li>
</ul>


---
## 解题思路与复盘

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