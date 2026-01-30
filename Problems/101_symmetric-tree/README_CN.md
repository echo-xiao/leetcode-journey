# 101. 对称二叉树

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`

## 题目描述

<p>给你一个二叉树的根节点 <code>root</code> ， 检查它是否轴对称。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://pic.leetcode.cn/1698026966-JDYPDU-image.png" style="width: 354px; height: 291px;" />
<pre>
<strong>输入：</strong>root = [1,2,2,3,4,4,3]
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://pic.leetcode.cn/1698027008-nPFLbM-image.png" style="width: 308px; height: 258px;" />
<pre>
<strong>输入：</strong>root = [1,2,2,null,3,null,3]
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目在范围 <code>[1, 1000]</code> 内</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你可以运用递归和迭代两种方法解决这个问题吗？</p>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过递归比较二叉树的左右子树是否镜像对称。

2. 综合思路：
   - 递归解法：通过递归函数 `isMirror`，比较两个子树的根节点值是否相等，并递归比较左子树的左节点与右子树的右节点、左子树的右节点与右子树的左节点。
   - 迭代解法（未在提供的代码中出现，但常见）：使用队列或栈进行广度优先搜索（BFS）或深度优先搜索（DFS），逐层比较节点是否对称。

3. 全量伪代码：
   - 递归解法：
     ```
     函数 isSymmetric(根节点):
         如果根节点为空，返回 True
         返回 isMirror(根节点的左子树, 根节点的右子树)

     函数 isMirror(节点 p, 节点 q):
         如果 p 和 q 都为空，返回 True
         如果 p 或 q 为空，返回 False
         如果 p 的值不等于 q 的值，返回 False
         返回 isMirror(p 的左子树, q 的右子树) 且 isMirror(p 的右子树, q 的左子树)
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点都会被访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是二叉树的高度，递归调用栈的深度取决于树的高度。对于平衡树，$h = \log n$，对于不平衡树，最坏情况下 $h = n$。