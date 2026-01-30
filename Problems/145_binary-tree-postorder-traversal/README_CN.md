# 145. 二叉树的后序遍历

**难度**: Easy | **标签**: `Stack` `Tree` `Depth-First Search` `Binary Tree`

## 题目描述

<p>给你一棵二叉树的根节点 <code>root</code> ，返回其节点值的 <strong>后序遍历 </strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>root = [1,null,2,3]</span></p>

<p><span class="example-io"><b>输出：</b>[3,2,1]</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png" style="width: 200px; height: 264px;" /></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>root = [1,2,3,4,5,null,8,null,null,6,7,9]</span></p>

<p><span class="example-io"><b>输出：</b>[4,6,7,5,2,9,8,3,1]</span></p>

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
<p><span class="example-io"><b>输入：</b>root = [1]</span></p>

<p><span class="example-io"><b>输出：</b>[1]</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点的数目在范围 <code>[0, 100]</code> 内</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>递归算法很简单，你可以通过迭代算法完成吗？</p>


---
## 解题思路与复盘

1. **一句话直击本质：**  
   后序遍历的核心在于访问左子树、右子树，然后访问根节点。

2. **综合思路：**  
   - **递归解法：**  
     通过递归函数，先递归访问左子树，再递归访问右子树，最后访问根节点。
   - **迭代解法：**  
     使用栈模拟递归过程，通过栈记录节点，先处理左子树，再处理右子树，最后处理根节点。可以通过标记或逆序等方式确保访问顺序。

3. **全量伪代码：**

   **递归解法：**
   ```
   定义函数 traverse(node, res):
       如果 node 为空:
           返回
       调用 traverse(node.left, res)
       调用 traverse(node.right, res)
       将 node.val 添加到 res

   定义函数 postorderTraversal(root):
       初始化 res 为一个空列表
       调用 traverse(root, res)
       返回 res
   ```

   **迭代解法（使用栈）：**
   ```
   定义函数 postorderTraversal(root):
       初始化 res 为一个空列表
       初始化 stack 为一个空列表
       初始化 curr 为 root
       初始化 prev 为 None

       当 curr 不为空 或 stack 不为空 时:
           当 curr 不为空 时:
               将 curr 压入 stack
               将 curr 移动到 curr.left

           取 stack 的栈顶元素为 peek
           如果 peek.right 不为空 且 prev 不等于 peek.right:
               将 curr 移动到 peek.right
           否则:
               从 stack 弹出一个节点 node
               将 node.val 添加到 res
               将 prev 更新为 node
               将 curr 置为 None

       返回 res
   ```

   **迭代解法（逆序）：**
   ```
   定义函数 postorderTraversal(root):
       初始化 res 为一个空列表
       初始化 stack 为一个空列表
       初始化 curr 为 root

       当 curr 不为空 或 stack 不为空 时:
           当 curr 不为空 时:
               将 curr.val 添加到 res
               将 curr 压入 stack
               将 curr 移动到 curr.right

           从 stack 弹出一个节点 node
           将 curr 移动到 node.left

       返回 res 的逆序
   ```

4. **复杂度：**  
   - **时间复杂度：** $O(n)$，其中 $n$ 是二叉树中的节点数，因为每个节点都被访问一次。
   - **空间复杂度：** $O(n)$，在最坏情况下（例如，树是一个链表），递归调用栈或迭代栈的深度可能达到 $n$。