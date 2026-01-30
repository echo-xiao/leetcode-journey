# 114. 二叉树展开为链表

**难度**: Medium | **标签**: `Linked List` `Stack` `Tree` `Depth-First Search` `Binary Tree`

## 题目描述

<p>给你二叉树的根结点 <code>root</code> ，请你将它展开为一个单链表：</p>

<ul>
	<li>展开后的单链表应该同样使用 <code>TreeNode</code> ，其中 <code>right</code> 子指针指向链表中下一个结点，而左子指针始终为 <code>null</code> 。</li>
	<li>展开后的单链表应该与二叉树 <a href="https://baike.baidu.com/item/%E5%85%88%E5%BA%8F%E9%81%8D%E5%8E%86/6442839?fr=aladdin" target="_blank"><strong>先序遍历</strong></a> 顺序相同。</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg" style="width: 500px; height: 226px;" />
<pre>
<strong>输入：</strong>root = [1,2,5,3,4,null,6]
<strong>输出：</strong>[1,null,2,null,3,null,4,null,5,null,6]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = []
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = [0]
<strong>输出：</strong>[0]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中结点数在范围 <code>[0, 2000]</code> 内</li>
	<li><code>-100 <= Node.val <= 100</code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong>你可以使用原地算法（<code>O(1)</code> 额外空间）展开这棵树吗？</p>


---
## 解题思路与复盘

1. 一句话直击本质：
   - 将二叉树的每个节点的左子树转移到右子树，并将原右子树接到左子树的最右节点上，最终将二叉树展开为链表。

2. 综合思路：
   - **迭代法（Morris遍历）**：通过迭代遍历树，找到每个节点左子树的最右节点，将当前节点的右子树接到这个最右节点上，然后将左子树转移到右子树。
   - **递归法（后序遍历）**：通过递归后序遍历树，先处理右子树，再处理左子树，将每个节点的右子树指向上一个处理的节点。
   - **前序遍历 + 栈**：使用栈进行前序遍历，将节点按前序顺序存储，然后重构树为链表。

3. 全量伪代码：
   - **迭代法（Morris遍历）**：
     ```
     当前节点 = 根节点
     当 当前节点 不为空：
         如果 当前节点 有左子树：
             找到左子树的最右节点
             将当前节点的右子树接到左子树的最右节点的右子树上
             将左子树转移到右子树
             将左子树置空
         移动到下一个右子节点
     ```
   - **递归法（后序遍历）**：
     ```
     定义递归函数 flatten(root):
         如果 root 为空，返回
         递归处理 root 的右子树
         递归处理 root 的左子树
         将 root 的右子树指向上一个处理的节点
         将 root 的左子树置空
         更新上一个处理的节点为 root
     ```
   - **前序遍历 + 栈**：
     ```
     如果根节点为空，返回
     初始化栈，压入根节点
     初始化前一个节点 prev 为 None
     当栈不为空：
         弹出栈顶节点 curr
         如果 prev 不为空，将 prev 的右子树指向 curr，左子树置空
         如果 curr 有右子树，将右子树压入栈
         如果 curr 有左子树，将左子树压入栈
         更新 prev 为 curr
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点都被访问一次。
   - 空间复杂度：
     - 迭代法（Morris遍历）：$O(1)$，因为是原地修改。
     - 递归法（后序遍历）：$O(n)$，因为递归栈的深度可能达到 $n$。
     - 前序遍历 + 栈：$O(n)$，因为栈的大小可能达到 $n$。