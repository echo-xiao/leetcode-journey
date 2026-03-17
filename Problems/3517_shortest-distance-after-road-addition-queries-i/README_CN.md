# 3517. 新增道路查询后的最短距离 I

**难度**: Medium | **标签**: `Array` `Breadth-First Search` `Graph Theory`

**归类**: 11. 链表、树与回溯 > Array

## 题目描述

<p>给你一个整数 <code>n</code> 和一个二维整数数组 <code>queries</code>。</p>

<p>有 <code>n</code> 个城市，编号从 <code>0</code> 到 <code>n - 1</code>。初始时，每个城市 <code>i</code> 都有一条<strong>单向</strong>道路通往城市 <code>i + 1</code>（ <code>0 &lt;= i &lt; n - 1</code>）。</p>

<p><code>queries[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> 表示新建一条从城市 <code>u<sub>i</sub></code> 到城市 <code>v<sub>i</sub></code> 的<strong>单向</strong>道路。每次查询后，你需要找到从城市 <code>0</code> 到城市 <code>n - 1</code> 的<strong>最短路径</strong>的<strong>长度</strong>。</p>

<p>返回一个数组 <code>answer</code>，对于范围 <code>[0, queries.length - 1]</code> 中的每个 <code>i</code>，<code>answer[i]</code> 是处理完<strong>前</strong> <code>i + 1</code> 个查询后，从城市 <code>0</code> 到城市 <code>n - 1</code> 的最短路径的<em>长度</em>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 5, queries = [[2, 4], [0, 2], [0, 4]]</span></p>

<p><strong>输出：</strong> <span class="example-io">[3, 2, 1]</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/28/image8.jpg" style="width: 350px; height: 60px;" /></p>

<p>新增一条从 2 到 4 的道路后，从 0 到 4 的最短路径长度为 3。</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/28/image9.jpg" style="width: 350px; height: 60px;" /></p>

<p>新增一条从 0 到 2 的道路后，从 0 到 4 的最短路径长度为 2。</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/28/image10.jpg" style="width: 350px; height: 96px;" /></p>

<p>新增一条从 0 到 4 的道路后，从 0 到 4 的最短路径长度为 1。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 4, queries = [[0, 3], [0, 2]]</span></p>

<p><strong>输出：</strong> <span class="example-io">[1, 1]</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/28/image11.jpg" style="width: 300px; height: 70px;" /></p>

<p>新增一条从 0 到 3 的道路后，从 0 到 3 的最短路径长度为 1。</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/28/image12.jpg" style="width: 300px; height: 70px;" /></p>

<p>新增一条从 0 到 2 的道路后，从 0 到 3 的最短路径长度仍为 1。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 500</code></li>
	<li><code>1 &lt;= queries.length &lt;= 500</code></li>
	<li><code>queries[i].length == 2</code></li>
	<li><code>0 &lt;= queries[i][0] &lt; queries[i][1] &lt; n</code></li>
	<li><code>1 &lt; queries[i][1] - queries[i][0]</code></li>
	<li>查询中没有重复的道路。</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：**  
   使用广度优先搜索（BFS）在每次查询后动态更新图结构并计算从起点到终点的最短路径。

2. **综合思路：**  
   - **广度优先搜索（BFS）：**  
     该算法使用 BFS 来处理每个查询后的图结构，确保在每次新增道路后能够快速找到从起点到终点的最短路径。BFS 是一种逐层遍历的搜索算法，适合用于寻找无权图中的最短路径。
   - **图的动态更新：**  
     每次查询会新增一条边，算法通过更新邻接表来动态调整图结构，然后重新计算最短路径。

3. **全量伪代码：**

   ```plaintext
   初始化邻接表 adj 为一个包含 n 个空列表的列表
   对于每个从 0 到 n-2 的节点 i：
       将 i+1 添加到 adj[i] 中

   初始化结果列表 res 为一个空列表
   对于每个查询 (u, v)：
       将 v 添加到 adj[u] 中

       初始化队列 queue 并将 (0, 0) 入队，表示从节点 0 开始，当前深度为 0
       初始化访问列表 visited 为一个长度为 n 的布尔列表，所有值为 False
       将 visited[0] 设置为 True

       当队列 queue 不为空时：
           弹出队列中的第一个元素 (curr, depth)
           如果 curr 等于 n-1：
               将 depth 添加到结果列表 res 中
               跳出循环

           对于 curr 的每个邻居 neighbor：
               如果 neighbor 未被访问：
                   将 visited[neighbor] 设置为 True
                   将 (neighbor, depth+1) 入队

   返回结果列表 res
   ```

4. **复杂度：**

   - **时间复杂度：**  
     每次查询都需要进行一次 BFS，最坏情况下需要遍历整个图，因此时间复杂度为 $O(q \cdot (n + m))$，其中 $q$ 是查询次数，$n$ 是节点数，$m$ 是边数。
   
   - **空间复杂度：**  
     主要由邻接表和队列占用，空间复杂度为 $O(n + m)$。