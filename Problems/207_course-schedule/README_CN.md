# 207. 课程表

**难度**: Medium | **标签**: `Depth-First Search` `Breadth-First Search` `Graph Theory` `Topological Sort`

## 题目描述

<p>你这个学期必须选修 <code>numCourses</code> 门课程，记为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>numCourses - 1</code> 。</p>

<p>在选修某些课程之前需要一些先修课程。 先修课程按数组&nbsp;<code>prerequisites</code> 给出，其中&nbsp;<code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> ，表示如果要学习课程&nbsp;<code>a<sub>i</sub></code> 则 <strong>必须</strong> 先学习课程&nbsp; <code>b<sub>i</sub></code><sub> </sub>。</p>

<ul>
	<li>例如，先修课程对&nbsp;<code>[0, 1]</code> 表示：想要学习课程 <code>0</code> ，你需要先完成课程 <code>1</code> 。</li>
</ul>

<p>请你判断是否可能完成所有课程的学习？如果可以，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>numCourses = 2, prerequisites = [[1,0]]
<strong>输出：</strong>true
<strong>解释：</strong>总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>numCourses = 2, prerequisites = [[1,0],[0,1]]
<strong>输出：</strong>false
<strong>解释：</strong>总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= numCourses &lt;= 2000</code></li>
	<li><code>0 &lt;= prerequisites.length &lt;= 5000</code></li>
	<li><code>prerequisites[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; numCourses</code></li>
	<li><code>prerequisites[i]</code> 中的所有课程对 <strong>互不相同</strong></li>
</ul>


---
## 解题思路与复盘

### 一句话直击本质
判断课程表是否可以完成的核心在于检测有向图中是否存在环。

### 综合思路
1. **BFS（广度优先搜索）+ 拓扑排序**：
   - **逻辑**：通过计算每个节点的入度，使用队列进行拓扑排序，逐步移除入度为零的节点，最终判断是否能移除所有节点。
   - **实现**：版本 1 至版本 5 都采用了这种方法。
   
2. **DFS（深度优先搜索）+ 环检测**：
   - **逻辑**：使用深度优先搜索检测图中是否存在环，通过标记节点的访问状态（未访问、访问中、已访问）来判断。
   - **实现**：版本 6 至版本 8 采用了这种方法。

### 全量伪代码
#### BFS + 拓扑排序
```plaintext
初始化入度表和邻接表
对于每个先修关系 (cur, pre):
    在邻接表中添加边 pre -> cur
    增加 cur 的入度

初始化队列，将所有入度为 0 的节点入队
初始化已访问节点计数为 0

当队列不为空时:
    从队列中取出一个节点 u
    增加已访问节点计数
    对于 u 的每个邻接节点 v:
        减少 v 的入度
        如果 v 的入度为 0，将 v 入队

如果已访问节点计数等于课程总数:
    返回 True
否则:
    返回 False
```

#### DFS + 环检测
```plaintext
初始化邻接表
对于每个先修关系 (cur, pre):
    在邻接表中添加边 cur -> pre

初始化标记数组 flags，所有元素初始化为 0

定义递归函数 dfs(u):
    如果 flags[u] 为 1，返回 False
    如果 flags[u] 为 2，返回 True

    将 flags[u] 标记为 1
    对于 u 的每个邻接节点 v:
        如果 dfs(v) 返回 False，返回 False

    将 flags[u] 标记为 2
    返回 True

对于每个课程 i:
    如果 dfs(i) 返回 False，返回 False

返回 True
```

### 复杂度
- **时间复杂度**：对于两种方法，时间复杂度均为 $O(V + E)$，其中 $V$ 是课程数，$E$ 是先修关系数。
- **空间复杂度**：对于两种方法，空间复杂度均为 $O(V + E)$，用于存储邻接表和其他辅助数据结构。