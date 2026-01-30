# 637. 二叉树的层平均值

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`

## 题目描述

<p>给定一个非空二叉树的根节点<meta charset="UTF-8" />&nbsp;<code>root</code>&nbsp;, 以数组的形式返回每一层节点的平均值。与实际答案相差&nbsp;<code>10<sup>-5</sup></code> 以内的答案可以被接受。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/03/09/avg1-tree.jpg" /></p>

<pre>
<strong>输入：</strong>root = [3,9,20,null,null,15,7]
<strong>输出：</strong>[3.00000,14.50000,11.00000]
<strong>解释：</strong>第 0 层的平均值为 3,第 1 层的平均值为 14.5,第 2 层的平均值为 11 。
因此返回 [3, 14.5, 11] 。
</pre>

<p><strong>示例 2:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/03/09/avg2-tree.jpg" /></p>

<pre>
<strong>输入：</strong>root = [3,9,20,15,7]
<strong>输出：</strong>[3.00000,14.50000,11.00000]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<p><meta charset="UTF-8" /></p>

<ul>
	<li>树中节点数量在&nbsp;<code>[1, 10<sup>4</sup>]</code> 范围内</li>
	<li><code>-2<sup>31</sup>&nbsp;&lt;= Node.val &lt;= 2<sup>31</sup>&nbsp;- 1</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过层序遍历（BFS）或递归（DFS）遍历二叉树，计算每一层节点值的平均值。

2. **综合思路：**
   - **递归（DFS）解法：** 使用递归遍历二叉树的每一层，维护一个列表来记录每层的节点值总和和节点数量，最后计算平均值。
   - **迭代（BFS）解法：** 使用队列进行层序遍历，逐层计算节点值总和和节点数量，最后计算平均值。

3. **全量伪代码：**

   - **递归（DFS）解法：**
     ```
     定义函数 averageOfLevels(root):
         如果 root 为空，返回空列表
         初始化 stats 列表用于存储每层的总和和节点数量
         调用 traverse(root, 0)
         返回 stats 中每层总和除以节点数量的结果列表

     定义递归函数 traverse(node, depth):
         如果 node 为空，返回
         如果 depth 等于 stats 的长度，向 stats 添加一个新的 [0, 0] 列表
         stats[depth][0] 增加 node.val
         stats[depth][1] 增加 1
         递归调用 traverse(node.left, depth + 1)
         递归调用 traverse(node.right, depth + 1)
     ```

   - **迭代（BFS）解法：**
     ```
     定义函数 averageOfLevels(root):
         如果 root 为空，返回空列表
         初始化队列 q 并将 root 加入队列
         初始化 res 列表用于存储每层的平均值
         当队列 q 不为空时:
             记录当前队列的大小 sz
             初始化 ttl 为 0
             遍历当前层的每个节点:
                 从队列中弹出节点 cur
                 ttl 增加 cur.val
                 如果 cur.left 不为空，将 cur.left 加入队列
                 如果 cur.right 不为空，将 cur.right 加入队列
             将 ttl 除以 sz 的结果加入 res
         返回 res
     ```

4. **复杂度：**
   - **时间复杂度：** $O(n)$，其中 $n$ 是二叉树中的节点总数，因为每个节点都被访问一次。
   - **空间复杂度：** $O(m)$，其中 $m$ 是二叉树的最大宽度（即某一层的最大节点数），用于存储队列或递归调用栈。