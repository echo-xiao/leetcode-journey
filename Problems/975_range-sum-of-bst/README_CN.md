# 975. 二叉搜索树的范围和

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Binary Search Tree` `Binary Tree`

## 题目描述

<p>给定二叉搜索树的根结点 <code>root</code>，返回值位于范围 <em><code>[low, high]</code></em> 之间的所有结点的值的和。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg" style="width: 400px; height: 222px;" />
<pre>
<strong>输入：</strong>root = [10,5,15,3,7,null,18], low = 7, high = 15
<strong>输出：</strong>32
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/bst2.jpg" style="width: 400px; height: 335px;" />
<pre>
<strong>输入：</strong>root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
<strong>输出：</strong>23
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目在范围 <code>[1, 2 * 10<sup>4</sup>]</code> 内</li>
	<li><code>1 <= Node.val <= 10<sup>5</sup></code></li>
	<li><code>1 <= low <= high <= 10<sup>5</sup></code></li>
	<li>所有 <code>Node.val</code> <strong>互不相同</strong></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过递归遍历二叉搜索树，累加节点值在指定范围内的节点值。

2. 综合思路：
   - **递归遍历**：所有版本都使用递归的方式遍历二叉搜索树。递归的核心是对每个节点进行判断，如果节点值在范围内，则累加到结果中，然后分别递归处理左右子树。
   - **DFS（深度优先搜索）**：由于递归本质上是深度优先搜索，因此所有版本都采用了DFS的策略。
   - **不同数据结构**：在这些实现中，没有使用额外的数据结构，直接在递归调用中处理。

3. 全量伪代码：
   ```plaintext
   定义函数 rangeSumBST(root, low, high):
       如果 root 为空:
           返回 0
       
       初始化 midVal 为 0
       递归计算左子树的和 leftSum = rangeSumBST(root.left, low, high)
       
       如果 root.val 在 [low, high] 范围内:
           midVal = root.val
       
       递归计算右子树的和 rightSum = rangeSumBST(root.right, low, high)
       
       返回 leftSum + rightSum + midVal
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉搜索树的节点数，因为每个节点都需要访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是树的高度，递归调用栈的深度与树的高度成正比。对于平衡树，$h = O(\log n)$；对于不平衡树，最坏情况下 $h = O(n)$。