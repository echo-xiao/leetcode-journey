# 799. 二叉搜索树节点最小距离

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Breadth-First Search` `Binary Search Tree` `Binary Tree`

## 题目描述

<p>给你一个二叉搜索树的根节点 <code>root</code> ，返回 <strong>树中任意两不同节点值之间的最小差值</strong> 。</p>

<p>差值是一个正数，其数值等于两值之差的绝对值。</p>

<p>&nbsp;</p>

<div class="original__bRMd">
<div>
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
	<li>树中节点的数目范围是 <code>[2, 100]</code></li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与 530：<a href="https://leetcode.cn/problems/minimum-absolute-difference-in-bst/">https://leetcode.cn/problems/minimum-absolute-difference-in-bst/</a> 相同</p>
</div>
</div>


---
## 解题思路与复盘

1. 一句话直击本质：通过中序遍历二叉搜索树，比较相邻节点的值以找到最小差值。

2. 综合思路：
   - **递归中序遍历**：利用递归方法进行中序遍历，保持一个全局变量记录上一个访问的节点值，并在每次访问节点时计算当前节点与上一个节点的差值，更新最小差值。
   - **迭代中序遍历**（未在提供的代码中出现，但作为一种可能的解法）：可以使用栈来模拟递归过程，进行中序遍历，同样比较相邻节点的差值。

3. 全量伪代码：
   - **递归中序遍历伪代码**：
     ```
     定义函数 minDiffInBST(root):
         初始化 prev 为 None
         初始化 min_diff 为正无穷
         调用 traverse(root)
         返回 min_diff

     定义函数 traverse(node):
         如果 node 为空，返回
         调用 traverse(node.left)
         如果 prev 不为空:
             计算 diff 为 abs(prev - node.val)
             更新 min_diff 为 min(min_diff, diff)
         更新 prev 为 node.val
         调用 traverse(node.right)
     ```
   - **迭代中序遍历伪代码**（假设实现）：
     ```
     定义函数 minDiffInBST(root):
         初始化栈 stack 为空
         初始化 prev 为 None
         初始化 min_diff 为正无穷
         初始化当前节点 current 为 root

         当 stack 不为空或 current 不为空时:
             如果 current 不为空:
                 将 current 压入栈
                 current 移动到左子节点
             否则:
                 从栈中弹出节点作为 current
                 如果 prev 不为空:
                     计算 diff 为 abs(prev - current.val)
                     更新 min_diff 为 min(min_diff, diff)
                 更新 prev 为 current.val
                 current 移动到右子节点

         返回 min_diff
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉搜索树的节点数，因为每个节点都需要访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是树的高度，递归调用栈或迭代栈的空间消耗。对于平衡树，$h = \log n$；对于不平衡树，$h = n$。