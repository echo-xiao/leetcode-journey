# 2384. 判断根结点是否等于子结点之和

**难度**: Easy | **标签**: `Tree` `Binary Tree`

## 题目描述

<p>给你一个 <strong>二叉树 </strong>的根结点&nbsp;<code>root</code>，该二叉树由恰好&nbsp;<code>3</code>&nbsp;个结点组成：根结点、左子结点和右子结点。</p>

<p>如果根结点值等于两个子结点值之和，返回&nbsp;<code>true</code>&nbsp;，否则返回<em>&nbsp;</em><code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/04/08/graph3drawio.png" style="width: 281px; height: 199px;" />
<pre>
<strong>输入：</strong>root = [10,4,6]
<strong>输出：</strong>true
<strong>解释：</strong>根结点、左子结点和右子结点的值分别是 10 、4 和 6 。
由于 10 等于 4 + 6 ，因此返回 true 。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/04/08/graph3drawio-1.png" style="width: 281px; height: 199px;" />
<pre>
<strong>输入：</strong>root = [5,3,1]
<strong>输出：</strong>false
<strong>解释：</strong>根结点、左子结点和右子结点的值分别是 5 、3 和 1 。
由于 5 不等于 3 + 1 ，因此返回 false 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树只包含根结点、左子结点和右子结点</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 判断根节点的值是否等于其左右子节点值之和。

2. **综合思路：**
   - **直接比较法：** 由于题目要求判断根节点值是否等于其左右子节点值之和，直接访问根节点和其左右子节点的值进行比较即可。这种方法简单直接，不需要递归或迭代。
   - **递归与迭代：** 在这个特定问题中，递归和迭代并不适用，因为问题只涉及根节点和其直接子节点的值比较，不需要遍历整个树。
   - **DFS与BFS：** 同样，由于问题只涉及根节点和其直接子节点的值比较，深度优先搜索（DFS）和广度优先搜索（BFS）并不适用。

3. **全量伪代码：**

   - **直接比较法：**
     ```
     定义函数 checkTree(root):
         如果 root 是空:
             返回 False
         如果 root.left 是空 或 root.right 是空:
             返回 False
         返回 root.val 是否等于 root.left.val + root.right.val
     ```

4. **复杂度：**

   - **时间复杂度：** $O(1)$，因为只涉及对根节点及其左右子节点的常数次访问和比较。
   - **空间复杂度：** $O(1)$，因为不需要额外的数据结构来存储信息。