# 1079. 从根到叶的二进制数之和

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Binary Tree`

## 题目描述

<p>给出一棵二叉树，其上每个结点的值都是&nbsp;<code>0</code>&nbsp;或&nbsp;<code>1</code>&nbsp;。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。</p>

<ul>
	<li>例如，如果路径为&nbsp;<code>0 -&gt; 1 -&gt; 1 -&gt; 0 -&gt; 1</code>，那么它表示二进制数&nbsp;<code>01101</code>，也就是&nbsp;<code>13</code>&nbsp;。</li>
</ul>

<p>对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。</p>

<p>返回这些数字之和。题目数据保证答案是一个 <strong>32 位 </strong>整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/04/04/sum-of-root-to-leaf-binary-numbers.png" />
<pre>
<strong>输入：</strong>root = [1,0,1,0,1,0,1]
<strong>输出：</strong>22
<strong>解释：</strong>(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = [0]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中的节点数在&nbsp;<code>[1, 1000]</code>&nbsp;范围内</li>
	<li><code>Node.val</code>&nbsp;仅为 <code>0</code> 或 <code>1</code>&nbsp;</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过深度优先搜索（DFS）遍历二叉树，从根到叶节点构建二进制数并累加其值。

2. **综合思路：**
   - **递归 DFS：** 使用递归的深度优先搜索遍历树，从根到叶节点构建二进制数。每到达一个叶节点时，将该路径的二进制数值累加到总和中。
   - **迭代 DFS：** 虽然在提供的代码中没有迭代实现，但可以通过显式栈模拟递归过程来实现迭代 DFS。
   - **BFS：** 虽然未在代码中体现，但广度优先搜索（BFS）也可以用于此问题，通过队列逐层遍历树并构建二进制数。

3. **全量伪代码：**

   - **递归 DFS 版本 1：**
     ```
     定义函数 sumRootToLeaf(root):
         初始化总和 res 为 0
         调用辅助函数 traverse(node, ttl) 从根节点开始遍历
         返回 res

     定义辅助函数 traverse(node, ttl):
         如果节点为空，返回
         更新 ttl 为 (ttl * 2) + node.val
         如果节点是叶节点，将 ttl 加到 res
         递归调用 traverse(node.left, ttl)
         递归调用 traverse(node.right, ttl)
     ```

   - **递归 DFS 版本 2：**
     ```
     定义函数 sumRootToLeaf(root):
         如果根节点为空，返回 0
         返回 dfs(root, 0)

     定义辅助函数 dfs(node, ttl):
         如果节点为空，返回 0
         更新 ttl 为 (ttl * 2) + node.val
         如果节点是叶节点，返回 ttl
         计算左子树和右子树的和
         返回左子树和右子树的和之和
     ```

4. **复杂度：**

   - **时间复杂度：** $O(n)$，其中 $n$ 是二叉树中的节点数，因为每个节点都被访问一次。
   - **空间复杂度：** $O(h)$，其中 $h$ 是树的高度，递归调用栈的深度等于树的高度。对于平衡树，$h = \log n$；对于不平衡树，$h = n$。