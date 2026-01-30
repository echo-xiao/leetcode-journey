# 106. 从中序与后序遍历序列构造二叉树

**难度**: Medium | **标签**: `Array` `Hash Table` `Divide and Conquer` `Tree` `Binary Tree`

## 题目描述

<p>给定两个整数数组 <code>inorder</code> 和 <code>postorder</code> ，其中 <code>inorder</code> 是二叉树的中序遍历， <code>postorder</code> 是同一棵树的后序遍历，请你构造并返回这颗&nbsp;<em>二叉树</em>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" />
<pre>
<b>输入：</b>inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
<b>输出：</b>[3,9,20,null,null,15,7]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<b>输入：</b>inorder = [-1], postorder = [-1]
<b>输出：</b>[-1]
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= inorder.length &lt;= 3000</code></li>
	<li><code>postorder.length == inorder.length</code></li>
	<li><code>-3000 &lt;= inorder[i], postorder[i] &lt;= 3000</code></li>
	<li><code>inorder</code>&nbsp;和&nbsp;<code>postorder</code>&nbsp;都由 <strong>不同</strong> 的值组成</li>
	<li><code>postorder</code>&nbsp;中每一个值都在&nbsp;<code>inorder</code>&nbsp;中</li>
	<li><code>inorder</code>&nbsp;<strong>保证</strong>是树的中序遍历</li>
	<li><code>postorder</code>&nbsp;<strong>保证</strong>是树的后序遍历</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：**  
   通过后序遍历的最后一个元素确定根节点，并利用中序遍历划分左右子树，递归构建二叉树。

2. **综合思路：**  
   所有版本都采用递归的方式来构建二叉树，核心思想是利用后序遍历的最后一个元素作为当前子树的根节点，然后在中序遍历中找到该根节点的位置，以此划分出左子树和右子树的中序遍历和后序遍历序列，递归构建左右子树。

3. **全量伪代码：**

   ```plaintext
   函数 buildTree(中序遍历序列, 后序遍历序列):
       如果中序遍历序列或后序遍历序列为空:
           返回 None

       根节点值 = 后序遍历序列的最后一个元素
       创建根节点

       在中序遍历序列中找到根节点值的位置

       左子树的中序遍历序列 = 中序遍历序列中根节点值左边的部分
       右子树的中序遍历序列 = 中序遍历序列中根节点值右边的部分

       左子树的后序遍历序列 = 后序遍历序列中前面与左子树中序遍历序列长度相同的部分
       右子树的后序遍历序列 = 后序遍历序列中去掉最后一个元素后的剩余部分

       递归构建左子树并连接到根节点的左子节点
       递归构建右子树并连接到根节点的右子节点

       返回根节点
   ```

4. **复杂度：**  
   时间复杂度：$O(n^2)$，因为对于每个节点都需要在中序遍历中查找其位置，最坏情况下需要 $O(n)$ 的时间。  
   空间复杂度：$O(n)$，用于递归栈的空间。