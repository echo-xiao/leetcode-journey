# 530. 二叉搜索树的最小绝对差

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Breadth-First Search` `Binary Search Tree` `Binary Tree`

## 题目描述

<p>给你一个二叉搜索树的根节点 <code>root</code> ，返回 <strong>树中任意两不同节点值之间的最小差值</strong> 。</p>

<p>差值是一个正数，其数值等于两值之差的绝对值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg" style="width: 292px; height: 301px;" />
<pre>
<strong>输入：</strong>root = [4,2,6,1,3]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg" style="width: 282px; height: 301px;" />
<pre>
<strong>输入：</strong>root = [1,0,48,null,null,12,49]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点的数目范围是 <code>[2, 10<sup>4</sup>]</code></li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与 783 <a href="https://leetcode.cn/problems/minimum-distance-between-bst-nodes/">https://leetcode.cn/problems/minimum-distance-between-bst-nodes/</a> 相同</p>


---
## 解题思路与复盘

1. 一句话直击本质：通过中序遍历二叉搜索树，比较相邻节点的值以找到最小的绝对差。

2. 综合思路：
   - 递归中序遍历：利用递归的方式进行中序遍历，维护一个前驱节点的值，并在遍历过程中更新最小绝对差。
   - 迭代中序遍历：虽然提供的代码没有迭代版本，但可以通过栈模拟递归实现中序遍历，逻辑类似于递归版本。

3. 全量伪代码：
   - 初始化最小差值为正无穷，前驱节点值为负无穷。
   - 定义递归函数 `traverse(node)`：
     - 如果节点为空，返回。
     - 递归调用左子节点。
     - 计算当前节点与前驱节点的差值，并更新最小差值。
     - 更新前驱节点为当前节点。
     - 递归调用右子节点。
   - 调用 `traverse(root)` 开始遍历。
   - 返回最小差值。

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是节点数，因为每个节点访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是树的高度，递归调用栈的深度。