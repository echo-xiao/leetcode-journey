# 399. 除法求值

**难度**: Medium | **标签**: `Array` `String` `Depth-First Search` `Breadth-First Search` `Union-Find` `Graph Theory` `Shortest Path`

## 题目描述

<p>给你一个变量对数组 <code>equations</code> 和一个实数值数组 <code>values</code> 作为已知条件，其中 <code>equations[i] = [A<sub>i</sub>, B<sub>i</sub>]</code> 和 <code>values[i]</code> 共同表示等式 <code>A<sub>i</sub> / B<sub>i</sub> = values[i]</code> 。每个 <code>A<sub>i</sub></code> 或 <code>B<sub>i</sub></code> 是一个表示单个变量的字符串。</p>

<p>另有一些以数组 <code>queries</code> 表示的问题，其中 <code>queries[j] = [C<sub>j</sub>, D<sub>j</sub>]</code> 表示第 <code>j</code> 个问题，请你根据已知条件找出 <code>C<sub>j</sub> / D<sub>j</sub> = ?</code> 的结果作为答案。</p>

<p>返回 <strong>所有问题的答案</strong> 。如果存在某个无法确定的答案，则用 <code>-1.0</code> 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 <code>-1.0</code> 替代这个答案。</p>

<p><strong>注意：</strong>输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。</p>

<p><strong>注意：</strong>未在等式列表中出现的变量是未定义的，因此无法确定它们的答案。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
<strong>输出：</strong>[6.00000,0.50000,-1.00000,1.00000,-1.00000]
<strong>解释：</strong>
条件：<em>a / b = 2.0</em>, <em>b / c = 3.0</em>
问题：<em>a / c = ?</em>, <em>b / a = ?</em>, <em>a / e = ?</em>, <em>a / a = ?</em>, <em>x / x = ?</em>
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
注意：x 是未定义的 =&gt; -1.0</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
<strong>输出：</strong>[3.75000,0.40000,5.00000,0.20000]
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
<strong>输出：</strong>[0.50000,2.00000,-1.00000,-1.00000]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= equations.length &lt;= 20</code></li>
	<li><code>equations[i].length == 2</code></li>
	<li><code>1 &lt;= A<sub>i</sub>.length, B<sub>i</sub>.length &lt;= 5</code></li>
	<li><code>values.length == equations.length</code></li>
	<li><code>0.0 &lt; values[i] &lt;= 20.0</code></li>
	<li><code>1 &lt;= queries.length &lt;= 20</code></li>
	<li><code>queries[i].length == 2</code></li>
	<li><code>1 &lt;= C<sub>j</sub>.length, D<sub>j</sub>.length &lt;= 5</code></li>
	<li><code>A<sub>i</sub>, B<sub>i</sub>, C<sub>j</sub>, D<sub>j</sub></code> 由小写英文字母与数字组成</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：**
   - 使用图的遍历（DFS/BFS）或并查集来求解变量间的比值关系。

2. **综合思路：**
   - **并查集解法：** 使用并查集（Union-Find）来维护变量之间的连通性和比值关系，通过路径压缩和按秩合并来优化查询效率。
   - **图的遍历解法：** 将变量和比值关系构建成图结构，通过深度优先搜索（DFS）或广度优先搜索（BFS）来查找从起点到终点的路径，并计算路径上的比值乘积。

3. **全量伪代码：**

   - **并查集解法：**
     ```
     初始化 parent 和 weight 字典
     对于每个方程 (u, v) 和对应的值 val:
         执行 union 操作，将 u 和 v 连接，更新 parent 和 weight
     对于每个查询 (u, v):
         如果 u 或 v 不在 parent 中，返回 -1.0
         否则，找到 u 和 v 的根 rootU 和 rootV
         如果 rootU 和 rootV 不同，返回 -1.0
         否则，返回 weight[u] / weight[v]
     
     函数 find(i):
         如果 i 不在 parent 中，初始化 parent[i] 为 i 和 weight[i] 为 1.0
         如果 parent[i] 是 i 自身，返回 i
         否则，递归查找 parent[i] 的根，并更新 parent[i] 和 weight[i]
     
     函数 union(i, j, value):
         找到 i 和 j 的根 rooti 和 rootj
         如果 rooti 和 rootj 不同，连接 rooti 到 rootj，并更新 weight[rooti]
     ```

   - **DFS 解法：**
     ```
     初始化 graph 为默认字典
     对于每个方程 (u, v) 和对应的值 val:
         在 graph 中添加边 u -> v 和 v -> u，权重分别为 val 和 1/val
     对于每个查询 (start, end):
         如果 start 或 end 不在 graph 中，返回 -1.0
         否则，执行 DFS 查找从 start 到 end 的路径，计算路径上的权重乘积
     
     函数 dfs(curr, target, visited, graph):
         如果 curr 是 target，返回 1.0
         将 curr 标记为已访问
         对于 curr 的每个邻居 (neighbor, weight):
             如果 neighbor 未访问，递归调用 dfs
             如果找到有效路径，返回 weight * 递归结果
         返回 -1.0
     ```

   - **BFS 解法：**
     ```
     初始化 graph 为默认字典
     对于每个方程 (u, v) 和对应的值 val:
         在 graph 中添加边 u -> v 和 v -> u，权重分别为 val 和 1/val
     对于每个查询 (start, end):
         如果 start 或 end 不在 graph 中，返回 -1.0
         否则，执行 BFS 查找从 start 到 end 的路径，计算路径上的权重乘积
     
     使用队列初始化 BFS，起始点为 (start, 1.0)
     当队列不为空时:
         弹出队列头部 (curr, currProduct)
         如果 curr 是 end，返回 currProduct
         将 curr 标记为已访问
         对于 curr 的每个邻居 (neighbor, weight):
             如果 neighbor 未访问，将 (neighbor, currProduct * weight) 入队
     如果未找到路径，返回 -1.0
     ```

4. **复杂度：**

   - **并查集解法：**
     - 时间复杂度：$O((E + Q) \cdot \alpha(N))$，其中 $E$ 是方程数量，$Q$ 是查询数量，$N$ 是变量数量，$\alpha$ 是阿克曼函数的反函数。
     - 空间复杂度：$O(N)$，用于存储 parent 和 weight。

   - **DFS/BFS 解法：**
     - 时间复杂度：$O(E + Q \cdot (V + E))$，其中 $V$ 是变量数量，$E$ 是边数量。
     - 空间复杂度：$O(V + E)$，用于存储图结构和访问状态。