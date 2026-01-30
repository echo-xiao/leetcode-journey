# 94. 二叉树的中序遍历

**难度**: Easy | **标签**: `Stack` `Tree` `Depth-First Search` `Binary Tree`

## 题目描述

<p>给定一个二叉树的根节点 <code>root</code> ，返回 <em>它的 <strong>中序</strong>&nbsp;遍历</em> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg" style="height: 200px; width: 125px;" />
<pre>
<strong>输入：</strong>root = [1,null,2,3]
<strong>输出：</strong>[1,3,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = []
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = [1]
<strong>输出：</strong>[1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目在范围 <code>[0, 100]</code> 内</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶:</strong>&nbsp;递归算法很简单，你可以通过迭代算法完成吗？</p>


---
## 解题思路与复盘

1. 一句话直击本质：中序遍历的核心逻辑是按照“左-根-右”的顺序访问二叉树的节点。

2. 综合思路：
   - 递归解法：通过递归函数实现中序遍历，递归地访问左子树、记录当前节点值、再递归访问右子树。
   - 迭代解法：使用栈来模拟递归过程，先将左子树节点压栈，访问节点后处理右子树。

3. 全量伪代码：
   - 递归解法：
     ```
     定义函数 inorderTraversal(root):
         初始化结果列表 res
         调用递归函数 traverse(node, res)
         返回 res

     定义递归函数 traverse(node, res):
         如果 node 为空，返回
         调用 traverse(node.left, res)
         将 node.val 添加到 res
         调用 traverse(node.right, res)
     ```
   - 迭代解法：
     ```
     定义函数 inorderTraversal(root):
         初始化空栈 stack 和结果列表 res
         设置 curr 为 root
         当 curr 不为空 或者 stack 不为空时:
             当 curr 不为空时:
                 将 curr 压入 stack
                 设置 curr 为 curr.left
             将 stack 顶部元素出栈赋给 curr
             将 curr.val 添加到 res
             设置 curr 为 curr.right
         返回 res
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点都被访问一次。
   - 空间复杂度：递归解法的空间复杂度为 $O(h)$，迭代解法的空间复杂度为 $O(h)$，其中 $h$ 是二叉树的高度。