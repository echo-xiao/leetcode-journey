# 110. 平衡二叉树

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Binary Tree`

## 题目描述

<p>给定一个二叉树，判断它是否是 <span data-keyword="height-balanced">平衡二叉树</span> &nbsp;</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg" style="width: 342px; height: 221px;" />
<pre>
<strong>输入：</strong>root = [3,9,20,null,null,15,7]
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg" style="width: 452px; height: 301px;" />
<pre>
<strong>输入：</strong>root = [1,2,2,3,3,null,null,4,4]
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = []
<strong>输出：</strong>true
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中的节点数在范围 <code>[0, 5000]</code> 内</li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过递归计算每个节点的左右子树高度，若高度差超过1则返回-1表示不平衡，否则返回实际高度。

2. 综合思路：
   - 递归解法：通过递归函数计算每个节点的左右子树高度，若某个节点的左右子树高度差超过1或者子树本身不平衡，则返回-1表示不平衡；否则返回当前节点的高度。
   - 迭代解法：虽然题目中没有提供迭代解法，但通常可以使用栈或队列进行层序遍历，记录每个节点的高度并判断平衡性。

3. 全量伪代码：
   - 递归解法：
     ```
     定义函数 isBalanced(root):
         如果 root 为空，返回 True
         调用 calcHeight(root) 函数
         如果 calcHeight(root) 返回 -1，返回 False
         否则返回 True

     定义函数 calcHeight(node):
         如果 node 为空，返回 0
         计算左子树高度 left_height = calcHeight(node.left)
         计算右子树高度 right_height = calcHeight(node.right)
         如果 left_height 或 right_height 为 -1，或者左右高度差大于 1，返回 -1
         返回 max(left_height, right_height) + 1
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点都被访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是二叉树的高度，递归调用栈的深度。