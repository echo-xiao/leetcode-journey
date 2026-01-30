# 107. 二叉树的层序遍历 II

**难度**: Medium | **标签**: `Tree` `Breadth-First Search` `Binary Tree`

## 题目描述

<p>给你二叉树的根节点 <code>root</code> ，返回其节点值 <strong>自底向上的层序遍历</strong> 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>输入：</strong>root = [3,9,20,null,null,15,7]
<strong>输出：</strong>[[15,7],[9,20],[3]]
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

1. 一句话直击本质：该算法的核心逻辑是通过广度优先搜索（BFS）遍历二叉树的每一层，并将结果逆序输出。

2. 综合思路：
   - 迭代法（BFS）：使用队列（如 `collections.deque`）进行广度优先搜索，逐层遍历二叉树，将每层节点值存储在列表中，最后将结果列表逆序输出。
   - 递归法（DFS）：可以通过递归的深度优先搜索来实现，但在给定的代码集中未出现这种实现。

3. 全量伪代码：
   - 迭代法（BFS）：
     ```
     如果根节点为空，返回空列表
     初始化队列 q，包含根节点
     初始化结果列表 ans
     当队列 q 不为空时：
         初始化当前层节点值列表 vals
         对于队列 q 中的每个节点：
             从队列中弹出节点
             将节点值加入当前层节点值列表 vals
             如果节点有左子节点，将左子节点加入队列 q
             如果节点有右子节点，将右子节点加入队列 q
         将当前层节点值列表 vals 加入结果列表 ans
     返回结果列表 ans 的逆序
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点被访问一次。
   - 空间复杂度：$O(n)$，用于存储结果列表和队列中的节点。