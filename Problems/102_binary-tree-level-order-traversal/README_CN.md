# 102. 二叉树的层序遍历

**难度**: Medium | **标签**: `Tree` `Breadth-First Search` `Binary Tree`

## 题目描述

<p>给你二叉树的根节点 <code>root</code> ，返回其节点值的 <strong>层序遍历</strong> 。 （即逐层地，从左到右访问所有节点）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>输入：</strong>root = [3,9,20,null,null,15,7]
<strong>输出：</strong>[[3],[9,20],[15,7]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = [1]
<strong>输出：</strong>[[1]]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = []
<strong>输出：</strong>[]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目在范围 <code>[0, 2000]</code> 内</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 使用广度优先搜索（BFS）遍历二叉树的每一层，将每层节点的值收集到一个列表中。

2. **综合思路：**
   - **迭代 BFS 解法：** 使用队列（通常是 `collections.deque`）来实现广度优先搜索，逐层遍历二叉树。每次从队列中取出当前层的所有节点，记录它们的值，并将它们的子节点加入队列以便处理下一层。
   - **递归 DFS 解法：** 虽然在给定的代码集中没有出现，但递归深度优先搜索（DFS）也可以用于层序遍历。通过递归函数传递当前层级信息，将节点值添加到相应的层级列表中。

3. **全量伪代码：**

   - **迭代 BFS 解法：**
     ```
     如果根节点为空，返回空列表
     初始化队列 q，将根节点加入队列
     初始化结果列表 res
     当队列 q 不为空时：
         获取当前队列的长度 size
         初始化当前层的值列表 level
         循环 size 次：
             从队列中弹出一个节点 node
             将 node 的值加入 level
             如果 node 有左子节点，将其加入队列
             如果 node 有右子节点，将其加入队列
         将 level 加入结果列表 res
     返回结果列表 res
     ```

   - **递归 DFS 解法（伪代码，未在代码集中出现）：**
     ```
     定义递归函数 dfs(node, level)
         如果 node 为空，返回
         如果 level 等于结果列表的长度，向结果列表添加一个新的空列表
         将 node 的值加入结果列表的第 level 层
         递归调用 dfs(node 的左子节点, level + 1)
         递归调用 dfs(node 的右子节点, level + 1)
     如果根节点为空，返回空列表
     初始化结果列表 res
     调用 dfs(根节点, 0)
     返回结果列表 res
     ```

4. **复杂度：**
   - **时间复杂度：** $O(n)$，其中 $n$ 是二叉树中的节点数，因为每个节点都被访问一次。
   - **空间复杂度：** $O(n)$，在最坏情况下（例如完全二叉树的最后一层），队列中可能会存储 $n/2$ 个节点。