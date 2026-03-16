# 156. 上下翻转二叉树

**难度**: Medium | **标签**: `Tree` `Depth-First Search` `Binary Tree`

## 题目描述

<p>给定一个二叉树的 <code>root</code>，将树翻转并返回 <em>新的根节点</em>。</p>

<p>你可以通过以下步骤将二叉树翻转：</p>

<ol>
	<li>原来的左子节点变成新的根节点。</li>
	<li>原来的根节点变成新的右子节点。</li>
	<li>原来的右子节点变成新的左子节点。</li>
</ol>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/29/main.jpg" style="width: 600px; height: 95px;" />
<p>上述步骤是逐层进行的。<strong>保证</strong>每个右节点都有一个兄弟节点（同一父节点的左节点），并且没有子节点。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/29/updown.jpg" style="width: 800px; height: 161px;" />
<pre>
<strong>输入:</strong> root = [1,2,3,4,5]
<strong>输出:</strong> [4,5,2,null,null,3,1]
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> root = []
<strong>输出:</strong> []
</pre>

<p><strong class="example">示例 3:</strong></p>

<pre>
<strong>输入:</strong> root = [1]
<strong>输出:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li>树中的节点数量范围为 <code>[0, 10]</code>。</li>
	<li><code>1 &lt;= Node.val &lt;= 10</code></li>
	<li>树中的每个右节点都有一个兄弟节点（共享同一父节点的左节点）。</li>
	<li>树中的每个右节点没有子节点。</li>
</ul>

---
## 解题思路与复盘

1. 一句话直击本质：通过递归翻转二叉树的每个节点，将左子节点变为新的根节点，并将原根节点和右子节点分别作为其右子节点和左子节点。

2. 综合思路：
   - 递归解法：通过递归调用，将二叉树的左子树翻转为新的根节点，然后调整当前节点的左右子节点指向，最终返回新的根节点。
   - 迭代解法：可以使用栈或队列来模拟递归过程，逐层翻转节点，调整指针指向。

3. 全量伪代码：
   - 递归解法：
     ```
     函数 翻转二叉树(节点 root):
         如果 root 为空 或 root 的左子节点为空:
             返回 root
         
         newRoot = 递归调用 翻转二叉树(root 的左子节点)

         将 root 的左子节点的左子节点指向 root 的右子节点
         将 root 的左子节点的右子节点指向 root

         将 root 的左子节点置为空
         将 root 的右子节点置为空

         返回 newRoot
     ```
   - 迭代解法（伪代码示例，未在代码集中出现）：
     ```
     函数 翻转二叉树(节点 root):
         初始化一个栈
         当前节点 = root
         上一个节点 = 空
         上一个右子节点 = 空

         当 当前节点 不为空:
             将 当前节点 的左子节点入栈
             将 当前节点 的左子节点指向 上一个右子节点
             将 当前节点 的右子节点指向 上一个节点

             上一个节点 = 当前节点
             上一个右子节点 = 当前节点 的右子节点
             当前节点 = 栈顶元素出栈

         返回 上一个节点
     ```

4. 复杂度：
   - 时间复杂度：递归和迭代解法的时间复杂度均为 $O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点都需要访问一次。
   - 空间复杂度：递归解法的空间复杂度为 $O(h)$，其中 $h$ 是二叉树的高度，主要是递归调用栈的空间；迭代解法的空间复杂度也为 $O(h)$，因为需要使用栈来模拟递归过程。