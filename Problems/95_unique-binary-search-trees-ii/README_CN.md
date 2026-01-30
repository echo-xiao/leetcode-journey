# 95. 不同的二叉搜索树 II

**难度**: Medium | **标签**: `Dynamic Programming` `Backtracking` `Tree` `Binary Search Tree` `Binary Tree`

## 题目描述

<p>给你一个整数 <code>n</code> ，请你生成并返回所有由 <code>n</code> 个节点组成且节点值从 <code>1</code> 到 <code>n</code> 互不相同的不同 <strong>二叉搜索树</strong><em> </em>。可以按 <strong>任意顺序</strong> 返回答案。</p>

<p> </p>

<div class="original__bRMd">
<div>
<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg" style="width: 600px; height: 148px;" />
<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>[[1]]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 8</code></li>
</ul>
</div>
</div>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过递归生成所有可能的左子树和右子树组合，构建不同的二叉搜索树。

2. **综合思路：**
   - **递归与记忆化搜索：** 使用递归生成树的所有可能结构，并通过记忆化存储已经计算过的子问题结果以减少重复计算。
   - **动态规划：** 使用动态规划构建树，利用一个二维数组存储不同长度的子树组合，通过克隆右子树并调整节点值来生成不同的树。

3. **全量伪代码：**

   - **递归与记忆化搜索：**
     ```
     定义函数 generateTrees(n):
         如果 n 为 0，返回空列表
         初始化记忆化字典 memo
         返回 generate(1, n)

     定义函数 generate(left, right):
         如果 (left, right) 在 memo 中，返回 memo[(left, right)]
         如果 left > right，返回 [None]
         初始化空列表 trees
         对于 i 从 left 到 right:
             获取左子树列表 leftTrees = generate(left, i-1)
             获取右子树列表 rightTrees = generate(i+1, right)
             对于每个左子树 l 在 leftTrees 中:
                 对于每个右子树 r 在 rightTrees 中:
                     创建根节点 root，值为 i
                     设置 root.left 为 l
                     设置 root.right 为 r
                     将 root 添加到 trees
         将 trees 存入 memo[(left, right)]
         返回 trees
     ```

   - **动态规划：**
     ```
     定义函数 generateTrees(n):
         如果 n 为 0，返回空列表
         初始化 dp 为长度为 n+1 的列表，dp[0] = [None]
         对于长度 length 从 1 到 n:
             对于 j 从 1 到 length:
                 对于每个左子树 leftTree 在 dp[j-1] 中:
                     对于每个右子树 rightTree 在 dp[length-j] 中:
                         创建根节点 root，值为 j
                         设置 root.left 为 leftTree
                         设置 root.right 为 clone(rightTree, j)
                         将 root 添加到 dp[length]
         返回 dp[n]

     定义函数 clone(node, offset):
         如果 node 为 None，返回 None
         创建新节点 newNode，值为 node.val + offset
         设置 newNode.left 为 clone(node.left, offset)
         设置 newNode.right 为 clone(node.right, offset)
         返回 newNode
     ```

4. **复杂度：**
   - **时间复杂度：** $O(C_n)$，其中 $C_n$ 是第 $n$ 个卡塔兰数，表示生成不同二叉搜索树的数量。
   - **空间复杂度：** $O(C_n)$，用于存储生成的树结构。