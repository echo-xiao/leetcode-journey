# 653. 两数之和 IV - 输入二叉搜索树

**难度**: Easy | **标签**: `Hash Table` `Two Pointers` `Tree` `Depth-First Search` `Breadth-First Search` `Binary Search Tree` `Binary Tree`

## 题目描述

<p>给定一个二叉搜索树 <code>root</code> 和一个目标结果 <code>k</code>，如果二叉搜索树中存在两个元素且它们的和等于给定的目标结果，则返回 <code>true</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg" style="height: 229px; width: 400px;" />
<pre>
<strong>输入:</strong> root = [5,3,6,2,4,null,7], k = 9
<strong>输出:</strong> true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg" style="height: 229px; width: 400px;" />
<pre>
<strong>输入:</strong> root = [5,3,6,2,4,null,7], k = 28
<strong>输出:</strong> false
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li>二叉树的节点个数的范围是&nbsp;&nbsp;<code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>4</sup>&nbsp;&lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li>题目数据保证，输入的 <code>root</code> 是一棵 <strong>有效</strong> 的二叉搜索树</li>
	<li><code>-10<sup>5</sup>&nbsp;&lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：利用集合存储已访问节点值，通过递归遍历二叉搜索树，检查是否存在两个节点值之和等于目标值。

2. 综合思路：
   - 递归遍历：通过递归的方式遍历二叉搜索树，使用集合存储已访问节点的值。在遍历过程中，检查当前节点的值与集合中某个值之和是否等于目标值。
   - 迭代遍历（未在提供的代码中出现，但作为可能的解法）：可以使用栈或队列进行迭代遍历，逻辑与递归类似，使用集合存储已访问节点的值。

3. 全量伪代码：
   - 递归遍历：
     ```
     定义函数 findTarget(root, k):
         初始化一个空集合 res
         返回 traverse(root, k, res)

     定义函数 traverse(node, k, res):
         如果节点 node 为空，返回 False
         如果 (k - node.val) 在集合 res 中，返回 True
         否则，将 node.val 添加到集合 res
         递归调用 traverse(node.left, k, res) 并存储结果到 left
         递归调用 traverse(node.right, k, res) 并存储结果到 right
         返回 left 或 right
     ```
   - 迭代遍历（伪代码，未在提供代码中出现）：
     ```
     定义函数 findTarget(root, k):
         初始化一个空集合 res
         初始化一个栈 stack 并将 root 入栈
         当栈不为空时：
             弹出栈顶节点 node
             如果 (k - node.val) 在集合 res 中，返回 True
             否则，将 node.val 添加到集合 res
             如果 node.right 不为空，将 node.right 入栈
             如果 node.left 不为空，将 node.left 入栈
         返回 False
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉搜索树的节点数，因为每个节点都需要访问一次。
   - 空间复杂度：$O(n)$，在最坏情况下，集合 res 需要存储所有节点的值。