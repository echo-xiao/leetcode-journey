# 2582. 两个城市间路径的最小分数

**难度**: Medium | **标签**: `Depth-First Search` `Breadth-First Search` `Union-Find` `Graph Theory`

**归类**: 11. 链表、树与回溯 > Depth-First Search

## 题目描述

<p>给你一个正整数&nbsp;<code>n</code>&nbsp;，表示总共有&nbsp;<code>n</code>&nbsp;个城市，城市从&nbsp;<code>1</code>&nbsp;到&nbsp;<code>n</code>&nbsp;编号。给你一个二维数组&nbsp;<code>roads</code>&nbsp;，其中&nbsp;<code>roads[i] = [a<sub>i</sub>, b<sub>i</sub>, distance<sub>i</sub>]</code>&nbsp;表示城市&nbsp;<code>a<sub>i</sub></code> 和&nbsp;<code>b<sub>i</sub></code>&nbsp;之间有一条 <strong>双向</strong>&nbsp;道路，道路距离为&nbsp;<code>distance<sub>i</sub></code>&nbsp;。城市构成的图不一定是连通的。</p>

<p>两个城市之间一条路径的 <strong>分数</strong>&nbsp;定义为这条路径中道路的 <strong>最小</strong>&nbsp;距离。</p>

<p><span class="text-only" data-eleid="20" style="white-space: pre;">返回城市</span><span class="text-only text-font-italic" data-eleid="21" style="white-space: pre;"> </span><code><span class="text-only" data-eleid="22" style="white-space: pre;">1</span></code><span class="text-only text-font-italic" data-eleid="23" style="white-space: pre;"> </span><span class="text-only" data-eleid="24" style="white-space: pre;">和城市</span><span class="text-only text-font-italic" data-eleid="25" style="white-space: pre;"> </span><span class="text-only" data-eleid="26" style="white-space: pre;"><code>n</code> 之间的所有路径的 </span><strong><span class="text-only" data-eleid="27" style="white-space: pre;">最小</span></strong><span class="text-only" data-eleid="28" style="white-space: pre;"> 分数。</span></p>

<p><b>注意：</b></p>

<ul>
	<li>一条路径指的是两个城市之间的道路序列。</li>
	<li>一条路径可以 <strong>多次</strong> 包含同一条道路，你也可以沿着路径多次到达城市 <code>1</code>&nbsp;和城市 <code>n</code>&nbsp;。</li>
	<li>测试数据保证城市 <code>1</code>&nbsp;和城市<code>n</code>&nbsp;之间 <strong>至少</strong>&nbsp;有一条路径。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/10/12/graph11.png" style="width: 190px; height: 231px;" /></p>

<pre>
<b>输入：</b>n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
<b>输出：</b>5
<b>解释：</b>城市 1 到城市 4 的路径中，分数最小的一条为：1 -&gt; 2 -&gt; 4 。这条路径的分数是 min(9,5) = 5 。
不存在分数更小的路径。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/10/12/graph22.png" style="width: 190px; height: 231px;" /></p>

<pre>
<b>输入：</b>n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
<b>输出：</b>2
<b>解释：</b>城市 1 到城市 4 分数最小的路径是：1 -&gt; 2 -&gt; 1 -&gt; 3 -&gt; 4 。这条路径的分数是 min(2,2,4,7) = 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= roads.length &lt;= 10<sup>5</sup></code></li>
	<li><code>roads[i].length == 3</code></li>
	<li><code>1 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li><code>1 &lt;= distance<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
	<li>不会有重复的边。</li>
	<li>城市 <code>1</code>&nbsp;和城市 <code>n</code>&nbsp;之间至少有一条路径。</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：**  
   该算法的核心逻辑是通过图的遍历（DFS、BFS或并查集）来找到从城市 1 开始的所有路径中最小的边权值。

2. **综合思路：**  
   - **并查集（Union-Find）：**  
     通过并查集结构，将所有城市连接成一个集合，并在合并过程中记录每个集合的最小边权值。最终返回城市 1 所在集合的最小边权值。
   - **深度优先搜索（DFS）：**  
     使用递归的方式从城市 1 开始遍历所有可达城市，记录遍历过程中遇到的最小边权值。
   - **广度优先搜索（BFS）：**  
     使用队列从城市 1 开始逐层遍历所有可达城市，记录遍历过程中遇到的最小边权值。

3. **全量伪代码：**

   - **并查集（Union-Find）伪代码：**
     ```
     初始化 parent 数组，表示每个城市的父节点
     初始化 min_score 数组，记录每个集合的最小边权值
     对于每条道路 (u, v, w):
         合并 u 和 v，更新 min_score
     找到城市 1 的根节点
     返回城市 1 所在集合的最小边权值
     ```

   - **深度优先搜索（DFS）伪代码：**
     ```
     初始化邻接表 adj
     初始化全局变量 res 为正无穷
     初始化 visited 集合
     定义递归函数 dfs(node):
         如果 node 已访问，返回
         标记 node 为已访问
         对于 node 的每个邻居 v 和边权 w:
             更新 res 为 min(res, w)
             递归调用 dfs(v)
     从城市 1 开始调用 dfs
     返回 res
     ```

   - **广度优先搜索（BFS）伪代码：**
     ```
     初始化邻接表 adj
     初始化队列 queue，初始包含城市 1
     初始化 visited 集合，初始包含城市 1
     初始化 res 为正无穷
     当队列不为空时:
         弹出队列头部元素 u
         对于 u 的每个邻居 v 和边权 w:
             更新 res 为 min(res, w)
             如果 v 未访问:
                 标记 v 为已访问
                 将 v 加入队列
     返回 res
     ```

4. **复杂度：**

   - **并查集（Union-Find）时间复杂度：** $O(m \cdot \alpha(n))$，其中 $m$ 是道路的数量，$\alpha$ 是阿克曼函数的反函数。
   - **并查集（Union-Find）空间复杂度：** $O(n)$，用于存储 parent 和 min_score 数组。

   - **深度优先搜索（DFS）时间复杂度：** $O(n + m)$，其中 $n$ 是城市数量，$m$ 是道路数量。
   - **深度优先搜索（DFS）空间复杂度：** $O(n)$，用于递归栈和 visited 集合。

   - **广度优先搜索（BFS）时间复杂度：** $O(n + m)$，其中 $n$ 是城市数量，$m$ 是道路数量。
   - **广度优先搜索（BFS）空间复杂度：** $O(n)$，用于队列和 visited 集合。