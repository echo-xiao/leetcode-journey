# 144. 二叉树的前序遍历

**难度**: Easy | **标签**: `Stack` `Tree` `Depth-First Search` `Binary Tree`

## 题目描述

<p>给你二叉树的根节点 <code>root</code> ，返回它节点值的&nbsp;<strong>前序</strong><em>&nbsp;</em>遍历。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">root = [1,null,2,3]</span></p>

<p><strong>输出：</strong><span class="example-io">[1,2,3]</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png" style="width: 200px; height: 264px;" /></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>root = [1,2,3,4,5,null,8,null,null,6,7,9]</span></p>

<p><span class="example-io"><b>输出：</b>[1,2,4,5,6,7,3,8,9]</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/08/29/tree_2.png" style="width: 350px; height: 286px;" /></p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>root = []</span></p>

<p><span class="example-io"><b>输出：</b>[]</span></p>
</div>

<p><strong class="example">示例 4：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">root = [1]</span></p>

<p><span class="example-io"><b>输出：</b>[1]</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目在范围 <code>[0, 100]</code> 内</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>递归算法很简单，你可以通过迭代算法完成吗？</p>


---
## 解题思路与复盘

1. 一句话直击本质：前序遍历的核心逻辑是按照“根-左-右”的顺序访问每个节点。

2. 综合思路：
   - 递归解法：通过递归函数实现前序遍历，先访问根节点，然后递归遍历左子树，最后递归遍历右子树。
   - 迭代解法：使用栈来模拟递归调用栈，首先访问根节点并将其压入栈中，然后依次访问左子树和右子树。

3. 全量伪代码：
   - 递归解法：
     ```
     定义函数 traverse(node, res):
         如果 node 为空:
             返回
         将 node.val 添加到 res
         调用 traverse(node.left, res)
         调用 traverse(node.right, res)

     定义函数 preorderTraversal(root):
         初始化 res 为一个空列表
         调用 traverse(root, res)
         返回 res
     ```
   - 迭代解法：
     ```
     定义函数 preorderTraversal(root):
         如果 root 为空:
             返回空列表
         初始化 stack 为包含 root 的列表
         初始化 res 为一个空列表
         当 stack 不为空时:
             弹出 stack 的最后一个元素 curr
             将 curr.val 添加到 res
             如果 curr.right 不为空:
                 将 curr.right 压入 stack
             如果 curr.left 不为空:
                 将 curr.left 压入 stack
         返回 res
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树中的节点数，因为每个节点都被访问一次。
   - 空间复杂度：$O(n)$，在最坏情况下（例如，树是一个链表），栈或递归调用栈的深度可能达到 $n$。