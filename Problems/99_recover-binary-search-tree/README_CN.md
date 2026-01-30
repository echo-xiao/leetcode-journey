# 99. 恢复二叉搜索树

**难度**: Medium | **标签**: `Tree` `Depth-First Search` `Binary Search Tree` `Binary Tree`

## 题目描述

<p>给你二叉搜索树的根节点 <code>root</code> ，该树中的 <strong>恰好</strong> 两个节点的值被错误地交换。<em>请在不改变其结构的情况下，恢复这棵树&nbsp;</em>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/28/recover1.jpg" style="width: 300px;" />
<pre>
<strong>输入：</strong>root = [1,3,null,null,2]
<strong>输出：</strong>[3,1,null,null,2]
<strong>解释：</strong>3 不能是 1 的左孩子，因为 3 &gt; 1 。交换 1 和 3 使二叉搜索树有效。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/28/recover2.jpg" style="height: 208px; width: 400px;" />
<pre>
<strong>输入：</strong>root = [3,1,4,null,null,2]
<strong>输出：</strong>[2,1,4,null,null,3]
<strong>解释：</strong>2 不能在 3 的右子树中，因为 2 &lt; 3 。交换 2 和 3 使二叉搜索树有效。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树上节点的数目在范围 <code>[2, 1000]</code> 内</li>
	<li><code>-2<sup>31</sup> &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>使用 <code>O(n)</code> 空间复杂度的解法很容易实现。你能想出一个只使用&nbsp;<code>O(1)</code> 空间的解决方案吗？</p>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过中序遍历找到两个错误的节点并交换它们的值来恢复二叉搜索树。

2. **综合思路：**
   - **递归中序遍历：** 使用递归方法进行中序遍历，记录前一个节点，并在遍历过程中找到两个错误的节点。
   - **迭代中序遍历：** 使用栈模拟递归过程进行中序遍历，同样记录前一个节点并找到错误节点。
   - **Morris遍历（未在给定代码中出现）：** 通过修改树结构实现中序遍历，空间复杂度为 $O(1)$。

3. **全量伪代码：**

   - **递归中序遍历：**
     ```
     定义函数 recoverTree(root):
         初始化 first, second, prev 为 None
         调用递归函数 inorder(root)
         交换 first 和 second 的值

     定义递归函数 inorder(node):
         如果 node 为空，返回
         调用 inorder(node.left)
         如果 prev 的值大于当前 node 的值：
             如果 first 为空，将 first 设为 prev
             将 second 设为 node
         将 prev 设为 node
         调用 inorder(node.right)
     ```

   - **迭代中序遍历：**
     ```
     定义函数 recoverTree(root):
         初始化 stack 为空列表
         初始化 node 为 root
         初始化 prev 为值为负无穷的 TreeNode
         初始化 first 和 second 为 None
         
         当 stack 不为空或 node 不为空时：
             当 node 不为空时：
                 将 node 压入 stack
                 将 node 设为 node.left
             
             将 node 设为 stack 弹出的元素
             
             如果 prev 的值大于 node 的值：
                 如果 first 为空，将 first 设为 prev
                 将 second 设为 node
             
             将 prev 设为 node
             将 node 设为 node.right
         
         交换 first 和 second 的值
     ```

4. **复杂度：**
   - 时间复杂度：$O(n)$，其中 $n$ 是树中节点的数量，因为每个节点都被访问一次。
   - 空间复杂度：
     - 递归中序遍历：$O(h)$，其中 $h$ 是树的高度，递归调用栈的空间。
     - 迭代中序遍历：$O(h)$，栈的空间。
     - Morris遍历（未在给定代码中出现）：$O(1)$，不使用额外空间。