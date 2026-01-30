# 617. 合并二叉树

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`

## 题目描述

<p>给你两棵二叉树： <code>root1</code> 和 <code>root2</code> 。</p>

<p>想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，<strong>不为</strong> null 的节点将直接作为新二叉树的节点。</p>

<p>返回合并后的二叉树。</p>

<p><strong>注意:</strong> 合并过程必须从两个树的根节点开始。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/merge.jpg" style="height: 163px; width: 600px;" />
<pre>
<strong>输入：</strong>root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
<strong>输出：</strong>[3,4,5,5,4,null,7]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root1 = [1], root2 = [1,2]
<strong>输出：</strong>[2,2]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>两棵树中的节点数目在范围 <code>[0, 2000]</code> 内</li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：合并二叉树的核心逻辑是通过递归遍历两个二叉树的节点，将对应节点的值相加，并构建新的合并树。

2. 综合思路：
   - **递归解法**：通过递归遍历两个二叉树的节点，若某个节点在其中一个树中不存在，则直接返回另一个树的节点；否则，将两个节点的值相加，并递归合并它们的左右子树。
   - **迭代解法**：虽然在提供的代码集中没有迭代解法，但可以通过使用栈或队列来实现迭代版本，逐层合并节点。

3. 全量伪代码：
   - **递归解法伪代码**：
     ```
     定义函数 mergeTrees(root1, root2):
         如果 root1 为空，返回 root2
         如果 root2 为空，返回 root1
         
         创建新节点 newNode，其值为 root1.val + root2.val
         newNode.left = mergeTrees(root1.left, root2.left)
         newNode.right = mergeTrees(root1.right, root2.right)
         
         返回 newNode
     ```
   - **迭代解法伪代码（假设使用栈）**：
     ```
     定义函数 mergeTrees(root1, root2):
         如果 root1 为空，返回 root2
         如果 root2 为空，返回 root1
         
         初始化栈 stack，初始值为 [(root1, root2)]
         
         当栈不为空时:
             弹出节点对 (node1, node2) 从栈中
             
             如果 node1 为空或 node2 为空，继续下一个循环
             
             node1.val += node2.val
             
             如果 node1.left 和 node2.left 都不为空，将 (node1.left, node2.left) 压入栈
             如果 node1.right 和 node2.right 都不为空，将 (node1.right, node2.right) 压入栈
             
             如果 node1.left 为空，将 node2.left 赋值给 node1.left
             如果 node1.right 为空，将 node2.right 赋值给 node1.right
         
         返回 root1
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是两个二叉树中节点数的较大值，因为每个节点最多访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是递归调用栈的深度，最坏情况下为树的高度。对于平衡树，$h = \log n$，对于不平衡树，$h = n$。