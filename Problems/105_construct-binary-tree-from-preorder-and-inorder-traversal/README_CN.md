# 105. 从前序与中序遍历序列构造二叉树

**难度**: Medium | **标签**: `Array` `Hash Table` `Divide and Conquer` `Tree` `Binary Tree`

## 题目描述

<p>给定两个整数数组&nbsp;<code>preorder</code> 和 <code>inorder</code>&nbsp;，其中&nbsp;<code>preorder</code> 是二叉树的<strong>先序遍历</strong>， <code>inorder</code>&nbsp;是同一棵树的<strong>中序遍历</strong>，请构造二叉树并返回其根节点。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" style="height: 302px; width: 277px;" />
<pre>
<strong>输入</strong><strong>:</strong> preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
<strong>输出:</strong> [3,9,20,null,null,15,7]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> preorder = [-1], inorder = [-1]
<strong>输出:</strong> [-1]
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= preorder.length &lt;= 3000</code></li>
	<li><code>inorder.length == preorder.length</code></li>
	<li><code>-3000 &lt;= preorder[i], inorder[i] &lt;= 3000</code></li>
	<li><code>preorder</code>&nbsp;和&nbsp;<code>inorder</code>&nbsp;均 <strong>无重复</strong> 元素</li>
	<li><code>inorder</code>&nbsp;均出现在&nbsp;<code>preorder</code></li>
	<li><code>preorder</code>&nbsp;<strong>保证</strong> 为二叉树的前序遍历序列</li>
	<li><code>inorder</code>&nbsp;<strong>保证</strong> 为二叉树的中序遍历序列</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：利用前序遍历确定根节点，通过中序遍历划分左右子树，递归或迭代地构建二叉树。

2. 综合思路：
   - 递归解法：通过前序遍历的第一个元素确定根节点，然后在中序遍历中找到根节点的位置，以此划分左右子树的中序遍历序列，递归地构建左右子树。
   - 迭代解法：使用栈模拟递归过程，逐步构建树节点，利用前序遍历的顺序构建节点，并通过中序遍历确定节点的左右子树关系。

3. 全量伪代码：
   - 递归解法：
     ```
     函数 buildTree(preorder, inorder):
         如果 preorder 为空或 inorder 为空:
             返回 None
         创建根节点 node，值为 preorder 的第一个元素
         在 inorder 中找到 node 的值的位置 midIdx
         递归构建 node 的左子树，使用 preorder[1:1+midIdx] 和 inorder[0:midIdx]
         递归构建 node 的右子树，使用 preorder[1+midIdx:] 和 inorder[midIdx+1:]
         返回 node
     ```
   - 迭代解法：
     ```
     函数 buildTree(preorder, inorder):
         如果 preorder 为空:
             返回 None
         创建根节点 root，值为 preorder 的第一个元素
         初始化栈 stack，包含 root
         初始化指针 inorderIdx 为 0
         遍历 preorder 从第二个元素开始:
             取当前元素 prev
             取栈顶元素 node
             如果 node 的值不等于 inorder[inorderIdx]:
                 创建 node 的左子节点，值为 prev
                 将 node 的左子节点压入栈
             否则:
                 当栈不为空且栈顶元素的值等于 inorder[inorderIdx]:
                     弹出栈顶元素
                     inorderIdx 增加 1
                 创建 node 的右子节点，值为 prev
                 将 node 的右子节点压入栈
         返回 root
     ```

4. 复杂度：
   - 时间复杂度：递归解法的时间复杂度为 $O(n^2)$，因为每次在中序遍历中查找根节点的时间复杂度为 $O(n)$，总共需要查找 $n$ 次。迭代解法的时间复杂度为 $O(n)$，因为每个节点只处理一次。
   - 空间复杂度：递归解法的空间复杂度为 $O(n)$，用于递归栈和存储树节点。迭代解法的空间复杂度为 $O(n)$，用于栈和存储树节点。