# 404. 左叶子之和

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`

## 题目描述

<p>给定二叉树的根节点&nbsp;<code>root</code>&nbsp;，返回所有左叶子之和。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/04/08/leftsum-tree.jpg" /></p>

<pre>
<strong>输入:</strong> root = [3,9,20,null,null,15,7] 
<strong>输出:</strong> 24 
<strong>解释:</strong> 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> root = [1]
<strong>输出:</strong> 0
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li>节点数在&nbsp;<code>[1, 1000]</code>&nbsp;范围内</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过递归遍历二叉树，识别并累加所有左叶子节点的值。

2. **综合思路：**
   - **递归方法：** 使用递归遍历二叉树，判断每个节点是否为左叶子节点，如果是则累加其值。递归过程中需要传递父节点信息以判断当前节点是否为左子节点。
   - **递归分治法：** 直接在递归过程中判断当前节点的左子节点是否为叶子节点，如果是则累加其值，同时递归计算左右子树的左叶子之和。

3. **全量伪代码：**

   - **递归遍历法：**
     ```
     定义函数 sumOfLeftLeaves(root):
         如果 root 为空，返回 0
         初始化结果 res 为 0
         调用辅助函数 traverse(node, prev) 传入 root 和 None
         返回 res

     定义辅助函数 traverse(node, prev):
         如果 node 为空，返回
         判断 node 是否为叶子节点
         判断 node 是否为左子节点
         如果 node 是左叶子节点，累加 node.val 到 res
         递归调用 traverse(node.left, node)
         递归调用 traverse(node.right, node)
     ```

   - **递归分治法：**
     ```
     定义函数 sumOfLeftLeaves(root):
         如果 root 为空，返回 0
         初始化 leftVal 为 0
         如果 root.left 存在且是叶子节点，设置 leftVal 为 root.left.val
         计算左子树的左叶子之和 leftSum = sumOfLeftLeaves(root.left)
         计算右子树的左叶子之和 rightSum = sumOfLeftLeaves(root.right)
         返回 leftVal + leftSum + rightSum
     ```

4. **复杂度：**
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树中的节点数，因为每个节点都被访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是二叉树的高度，递归调用栈的深度取决于树的高度。