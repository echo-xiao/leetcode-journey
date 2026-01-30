# 783. 二叉搜索树中的搜索

**难度**: Easy | **标签**: `Tree` `Binary Search Tree` `Binary Tree`

## 题目描述

<p>给定二叉搜索树（BST）的根节点<meta charset="UTF-8" />&nbsp;<code>root</code>&nbsp;和一个整数值<meta charset="UTF-8" />&nbsp;<code>val</code>。</p>

<p>你需要在 BST 中找到节点值等于&nbsp;<code>val</code>&nbsp;的节点。 返回以该节点为根的子树。 如果节点不存在，则返回<meta charset="UTF-8" />&nbsp;<code>null</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg" style="height: 179px; width: 250px;" /><meta charset="UTF-8" /></p>

<pre>
<b>输入：</b>root = [4,2,7,1,3], val = 2
<b>输出：</b>[2,1,3]
</pre>

<p><strong>示例 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/12/tree2.jpg" style="height: 179px; width: 250px;" />
<pre>
<b>输入：</b>root = [4,2,7,1,3], val = 5
<b>输出：</b>[]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数在&nbsp;<code>[1, 5000]</code>&nbsp;范围内</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>7</sup></code></li>
	<li><code>root</code>&nbsp;是二叉搜索树</li>
	<li><code>1 &lt;= val &lt;= 10<sup>7</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：利用二叉搜索树的性质，通过比较节点值与目标值，递归或迭代地在树中搜索目标节点。

2. 综合思路：
   - 递归解法：通过递归函数调用，比较当前节点值与目标值，决定在左子树或右子树中继续搜索。
   - 迭代解法（未在提供的代码中出现，但常见）：使用循环代替递归，逐步更新当前节点为其左子节点或右子节点，直到找到目标节点或遍历完整棵树。

3. 全量伪代码：
   - 递归解法：
     ```
     定义函数 searchBST(root, val):
         如果 root 为空:
             返回 None
         如果 root.val 等于 val:
             返回 root
         如果 val 小于 root.val:
             返回 searchBST(root.left, val)
         否则:
             返回 searchBST(root.right, val)
     ```
   - 迭代解法（未在提供的代码中出现，但常见）：
     ```
     定义函数 searchBST(root, val):
         当前节点 = root
         当 当前节点 不为空:
             如果 当前节点.val 等于 val:
                 返回 当前节点
             如果 val 小于 当前节点.val:
                 当前节点 = 当前节点.left
             否则:
                 当前节点 = 当前节点.right
         返回 None
     ```

4. 复杂度：
   - 时间复杂度：$O(h)$，其中 $h$ 是树的高度。在最坏情况下（例如退化为链表），$h$ 可以是 $n$。
   - 空间复杂度：递归解法的空间复杂度为 $O(h)$（由于递归调用栈），迭代解法的空间复杂度为 $O(1)$。