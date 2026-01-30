# 744. 网络延迟时间

**难度**: Medium | **标签**: `Depth-First Search` `Breadth-First Search` `Graph Theory` `Heap (Priority Queue)` `Shortest Path`

## 题目描述

<p>有 <code>n</code> 个网络节点，标记为&nbsp;<code>1</code>&nbsp;到 <code>n</code>。</p>

<p>给你一个列表&nbsp;<code>times</code>，表示信号经过 <strong>有向</strong> 边的传递时间。&nbsp;<code>times[i] = (u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>)</code>，其中&nbsp;<code>u<sub>i</sub></code>&nbsp;是源节点，<code>v<sub>i</sub></code>&nbsp;是目标节点， <code>w<sub>i</sub></code>&nbsp;是一个信号从源节点传递到目标节点的时间。</p>

<p>现在，从某个节点&nbsp;<code>K</code>&nbsp;发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回&nbsp;<code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png" style="height: 220px; width: 200px;" /></p>

<pre>
<strong>输入：</strong>times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>times = [[1,2,1]], n = 2, k = 1
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>times = [[1,2,1]], n = 2, k = 2
<strong>输出：</strong>-1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= times.length &lt;= 6000</code></li>
	<li><code>times[i].length == 3</code></li>
	<li><code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li><code>0 &lt;= w<sub>i</sub> &lt;= 100</code></li>
	<li>所有 <code>(u<sub>i</sub>, v<sub>i</sub>)</code> 对都 <strong>互不相同</strong>（即，不含重复边）</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过不同的图遍历和最短路径算法（如DFS、BFS、Dijkstra、Floyd-Warshall）计算从起始节点到所有其他节点的最短路径，并返回最长的最短路径。

2. 综合思路：
   - **DFS（深度优先搜索）**：通过递归遍历节点，更新节点的最短路径，利用贪心策略优先访问边权小的路径以增加剪枝机会。
   - **BFS（广度优先搜索，SPFA变体）**：使用队列进行节点的层次遍历，逐步更新节点的最短路径。
   - **Dijkstra算法**：
     - **朴素Dijkstra**：使用数组记录最短路径，逐步选择未访问节点中距离最小的节点进行更新。
     - **堆优化Dijkstra**：使用优先队列（最小堆）加速选择当前最短路径节点的过程。
   - **Floyd-Warshall算法**：通过动态规划的方式，逐步更新所有节点对之间的最短路径，适合处理密集图。

3. 全量伪代码：
   - **DFS伪代码**：
     ```
     初始化图的邻接表
     初始化最短距离数组为无穷大
     定义DFS函数(node, current_time):
         如果current_time >= dist[node]，则返回
         更新dist[node]为current_time
         对于每个邻居节点，递归调用DFS
     调用DFS从起始节点开始
     返回最短距离数组的最大值
     ```
   - **BFS（SPFA变体）伪代码**：
     ```
     初始化图的邻接表
     初始化最短距离数组为无穷大
     将起始节点的距离设为0并加入队列
     当队列不为空时：
         弹出队列头节点
         对于每个邻居节点：
             如果通过当前节点的路径更短，更新距离并将邻居节点加入队列
     返回最短距离数组的最大值
     ```
   - **朴素Dijkstra伪代码**：
     ```
     初始化图的邻接矩阵
     初始化最短距离数组为无穷大
     初始化访问数组为False
     将起始节点的距离设为0
     对于每个节点：
         选择未访问节点中距离最小的节点
         标记该节点为已访问
         更新该节点的邻居节点的距离
     返回最短距离数组的最大值
     ```
   - **堆优化Dijkstra伪代码**：
     ```
     初始化图的邻接表
     初始化优先队列并将起始节点加入队列
     初始化最短距离字典
     当优先队列不为空时：
         弹出队列中距离最小的节点
         如果该节点已处理，跳过
         记录该节点的最短距离
         对于每个邻居节点：
             如果邻居节点未处理，将其加入队列
     返回最短距离字典的最大值
     ```
   - **Floyd-Warshall伪代码**：
     ```
     初始化距离矩阵为无穷大
     将自身到自身的距离设为0
     根据输入更新距离矩阵
     对于每个中转节点：
         对于每个起点：
             对于每个终点：
                 更新起点到终点的最短距离
     返回起始节点到其他节点的最大距离
     ```

4. 复杂度：
   - **DFS**：时间复杂度 $O(V + E)$，空间复杂度 $O(V)$。
   - **BFS（SPFA变体）**：时间复杂度 $O(V + E)$，空间复杂度 $O(V)$。
   - **朴素Dijkstra**：时间复杂度 $O(V^2)$，空间复杂度 $O(V^2)$。
   - **堆优化Dijkstra**：时间复杂度 $O((V + E) \log V)$，空间复杂度 $O(V + E)$。
   - **Floyd-Warshall**：时间复杂度 $O(V^3)$，空间复杂度 $O(V^2)$。