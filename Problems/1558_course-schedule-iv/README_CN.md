# 1558. 课程表 IV

**难度**: Medium | **标签**: `Depth-First Search` `Breadth-First Search` `Graph Theory` `Topological Sort`

**归类**: 6. 图论算法 > Depth-First Search

## 题目描述

<p>你总共需要上<meta charset="UTF-8" />&nbsp;<code>numCourses</code>&nbsp;门课，课程编号依次为 <code>0</code>&nbsp;到&nbsp;<code>numCourses-1</code>&nbsp;。你会得到一个数组&nbsp;<code>prerequisite</code> ，其中<meta charset="UTF-8" />&nbsp;<code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;表示如果你想选<meta charset="UTF-8" />&nbsp;<code>b<sub>i</sub></code> 课程，你<strong> 必须</strong> 先选<meta charset="UTF-8" />&nbsp;<code>a<sub>i</sub></code>&nbsp;课程。</p>

<ul>
	<li>有的课会有直接的先修课程，比如如果想上课程 <code>1</code>&nbsp;，你必须先上课程 <code>0</code>&nbsp;，那么会以 <code>[0,1]</code>&nbsp;数对的形式给出先修课程数对。</li>
</ul>

<p>先决条件也可以是 <strong>间接</strong> 的。如果课程 <code>a</code> 是课程 <code>b</code> 的先决条件，课程 <code>b</code> 是课程 <code>c</code> 的先决条件，那么课程 <code>a</code> 就是课程 <code>c</code> 的先决条件。</p>

<p>你也得到一个数组<meta charset="UTF-8" />&nbsp;<code>queries</code>&nbsp;，其中<meta charset="UTF-8" />&nbsp;<code>queries[j] = [u<sub>j</sub>, v<sub>j</sub>]</code>。对于第 <code>j</code> 个查询，您应该回答课程<meta charset="UTF-8" />&nbsp;<code>u<sub>j</sub></code>&nbsp;是否是课程<meta charset="UTF-8" />&nbsp;<code>v<sub>j</sub></code>&nbsp;的先决条件。</p>

<p>返回一个布尔数组 <code>answer</code> ，其中 <code>answer[j]</code> 是第 <code>j</code> 个查询的答案。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/courses4-1-graph.jpg" /></p>

<pre>
<strong>输入：</strong>numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
<strong>输出：</strong>[false,true]
<strong>解释：</strong>[1, 0] 数对表示在你上课程 0 之前必须先上课程 1。
课程 0 不是课程 1 的先修课程，但课程 1 是课程 0 的先修课程。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
<strong>输出：</strong>[false,false]
<strong>解释：</strong>没有先修课程对，所以每门课程之间是独立的。
</pre>

<p><strong class="example">示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/courses4-3-graph.jpg" /></p>

<pre>
<strong>输入：</strong>numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
<strong>输出：</strong>[true,true]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<p><meta charset="UTF-8" /></p>

<ul>
	<li><code>2 &lt;= numCourses &lt;= 100</code></li>
	<li><code>0 &lt;= prerequisites.length &lt;= (numCourses * (numCourses - 1) / 2)</code></li>
	<li><code>prerequisites[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub>&nbsp;&lt;= numCourses - 1</code></li>
	<li><code>a<sub>i</sub>&nbsp;!= b<sub>i</sub></code></li>
	<li>每一对<meta charset="UTF-8" />&nbsp;<code>[a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;都 <strong>不同</strong></li>
	<li>先修课程图中没有环。</li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub>&nbsp;&lt;= numCourses - 1</code></li>
	<li><code>u<sub>i</sub>&nbsp;!= v<sub>i</sub></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过图的遍历或传递闭包算法，判断课程之间的先修关系。

2. 综合思路：
   - **拓扑排序 + BFS**：使用拓扑排序结合广度优先搜索（BFS）来逐层更新课程的先修关系。
   - **深度优先搜索（DFS）**：通过深度优先搜索遍历图，记录每个课程的先修关系。
   - **动态规划 + 传递闭包（Floyd-Warshall）**：使用传递闭包算法更新所有课程对之间的可达性。

3. 全量伪代码：
   - **拓扑排序 + BFS**：
     ```
     初始化入度数组和邻接表
     初始化每个课程的先修课程集合
     将入度为0的课程加入队列
     当队列不为空时：
         弹出队列中的课程
         对于该课程的每个后继课程：
             更新后继课程的先修课程集合
             减少后继课程的入度
             如果后继课程的入度为0，将其加入队列
     对于每个查询，检查查询的课程对是否存在先修关系
     ```
   - **DFS**：
     ```
     初始化邻接表
     初始化先修关系矩阵为False
     对于每个课程，进行DFS：
         对于当前课程的每个邻居：
             如果邻居不是先修课程，标记为True
             递归DFS邻居
     对于每个查询，返回先修关系矩阵的值
     ```
   - **动态规划 + 传递闭包**：
     ```
     初始化先修关系矩阵为False
     对于每个先修关系，标记矩阵对应位置为True
     对于每个中间课程：
         对于每对课程(i, j)：
             如果课程i通过中间课程可以到达课程j，标记为True
     对于每个查询，返回先修关系矩阵的值
     ```

4. 复杂度：
   - **拓扑排序 + BFS**：
     - 时间复杂度：$O(n + m)$，其中 $n$ 是课程数量，$m$ 是先修关系数量。
     - 空间复杂度：$O(n^2)$，用于存储先修关系集合。
   - **DFS**：
     - 时间复杂度：$O(n^2)$，每个课程进行DFS遍历。
     - 空间复杂度：$O(n^2)$，用于存储先修关系矩阵。
   - **动态规划 + 传递闭包**：
     - 时间复杂度：$O(n^3)$，三重循环更新传递闭包。
     - 空间复杂度：$O(n^2)$，用于存储先修关系矩阵。