# 933. 递增顺序搜索树

**难度**: Easy | **标签**: `Stack` `Tree` `Depth-First Search` `Binary Search Tree` `Binary Tree`

## 题目描述

<p>给你一棵二叉搜索树的<meta charset="UTF-8" />&nbsp;<code>root</code>&nbsp;，请你 <strong>按中序遍历</strong> 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/17/ex1.jpg" style="height: 350px; width: 600px;" />
<pre>
<strong>输入：</strong>root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
<strong>输出：</strong>[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/17/ex2.jpg" style="height: 114px; width: 300px;" />
<pre>
<strong>输入：</strong>root = [5,1,7]
<strong>输出：</strong>[1,null,5,null,7]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数的取值范围是 <code>[1, 100]</code></li>
	<li><code>0 &lt;= Node.val &lt;= 1000</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过中序遍历将二叉树节点按递增顺序重新连接成单链表形式的树。

2. 综合思路：
   - 递归方法：使用中序遍历递归地访问每个节点，将其连接到一个新的树结构中。
   - 迭代方法：使用栈模拟中序遍历，逐步访问每个节点并重新连接。

3. 全量伪代码：
   - 递归方法：
     ```
     定义函数 increasingBST(root):
         如果 root 为空，返回 None
         初始化 dummy_head 为新节点(-1)
         初始化 curr 指向 dummy_head
         调用 traverse(root)
         返回 dummy_head.right

     定义函数 traverse(node):
         如果 node 为空，返回
         调用 traverse(node.left)
         curr.right 指向新节点(node.val)
         curr 更新为 curr.right
         调用 traverse(node.right)
     ```
   - 迭代方法：
     ```
     定义函数 increasingBST(root):
         如果 root 为空，返回 None
         初始化 stack 为空列表
         初始化 curr 指向 root
         初始化 dummy 为新节点(-1)
         初始化 prev 指向 dummy
         当 curr 不为空或 stack 不为空时:
             当 curr 不为空时:
                 将 curr 压入 stack
                 curr 更新为 curr.left
             从 stack 弹出节点 node
             node.left 置为 None
             prev.right 指向 node
             prev 更新为 node
             curr 更新为 node.right
         返回 dummy.right
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是树中节点的数量，因为每个节点都被访问一次。
   - 空间复杂度：$O(n)$，在递归方法中，递归栈的深度和在迭代方法中栈的最大空间都可能达到 $n$。