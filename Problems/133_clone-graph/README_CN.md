# 133. 克隆图

**难度**: Medium | **标签**: `Hash Table` `Depth-First Search` `Breadth-First Search` `Graph Theory`

## 题目描述

<p>给你无向&nbsp;<strong><a href="https://baike.baidu.com/item/连通图/6460995?fr=aladdin" target="_blank">连通</a>&nbsp;</strong>图中一个节点的引用，请你返回该图的&nbsp;<a href="https://baike.baidu.com/item/深拷贝/22785317?fr=aladdin" target="_blank"><strong>深拷贝</strong></a>（克隆）。</p>

<p>图中的每个节点都包含它的值 <code>val</code>（<code>int</code>） 和其邻居的列表（<code>list[Node]</code>）。</p>

<pre>
class Node {
    public int val;
    public List&lt;Node&gt; neighbors;
}</pre>

<p>&nbsp;</p>

<p><strong>测试用例格式：</strong></p>

<p>简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（<code>val = 1</code>），第二个节点值为 2（<code>val = 2</code>），以此类推。该图在测试用例中使用邻接列表表示。</p>

<p><strong>邻接列表</strong> 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。</p>

<p>给定节点将始终是图中的第一个节点（值为 1）。你必须将&nbsp;<strong>给定节点的拷贝&nbsp;</strong>作为对克隆图的引用返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/01/133_clone_graph_question.png" style="height: 500px; width: 500px;" /></p>

<pre>
<strong>输入：</strong>adjList = [[2,4],[1,3],[2,4],[1,3]]
<strong>输出：</strong>[[2,4],[1,3],[2,4],[1,3]]
<strong>解释：
</strong>图中有 4 个节点。
节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
节点 4 的值是 4，它有两个邻居：节点 1 和 3 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/01/graph.png" style="height: 148px; width: 163px;" /></p>

<pre>
<strong>输入：</strong>adjList = [[]]
<strong>输出：</strong>[[]]
<strong>解释：</strong>输入包含一个空列表。该图仅仅只有一个值为 1 的节点，它没有任何邻居。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>adjList = []
<strong>输出：</strong>[]
<strong>解释：</strong>这个图是空的，它不含任何节点。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>这张图中的节点数在 <code>[0, 100]</code>&nbsp;之间。</li>
	<li><code>1 &lt;= Node.val &lt;= 100</code></li>
	<li>每个节点值&nbsp;<code>Node.val</code> 都是唯一的，</li>
	<li>图中没有重复的边，也没有自环。</li>
	<li>图是连通图，你可以从给定节点访问到所有节点。</li>
</ul>


---
## 解题思路与复盘

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