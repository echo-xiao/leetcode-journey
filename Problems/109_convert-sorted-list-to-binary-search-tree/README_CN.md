# 109. 有序链表转换二叉搜索树

**难度**: Medium | **标签**: `Linked List` `Divide and Conquer` `Tree` `Binary Search Tree` `Binary Tree`

## 题目描述

<p>给定一个单链表的头节点 &nbsp;<code>head</code>&nbsp;，其中的元素 <strong>按升序排序</strong> ，将其转换为 <span data-keyword="height-balanced">平衡</span> 二叉搜索树。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2020/08/17/linked.jpg" style="height: 388px; width: 500px;" /></p>

<pre>
<strong>输入:</strong> head = [-10,-3,0,5,9]
<strong>输出:</strong> [0,-3,9,-10,null,5]
<strong>解释:</strong> 一个可能的答案是[0，-3,9，-10,null,5]，它表示所示的高度平衡的二叉搜索树。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> head = []
<strong>输出:</strong> []
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>head</code>&nbsp;中的节点数在<code>[0, 2 * 10<sup>4</sup>]</code>&nbsp;范围内</li>
	<li><code>-10<sup>5</sup>&nbsp;&lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：利用快慢指针找到链表中点作为根节点，递归构建左右子树，或通过中序遍历模拟构建平衡二叉搜索树。

2. 综合思路：
   - **递归+快慢指针法**：通过快慢指针找到链表的中点，将其作为当前子树的根节点，然后递归地对中点左侧和右侧的链表部分构建左子树和右子树。
   - **递归+全局指针法**：先遍历链表计算长度，然后通过递归模拟中序遍历，利用全局指针逐步构建树节点。

3. 全量伪代码：
   - **递归+快慢指针法**：
     ```
     函数 sortedListToBST(head):
         如果 head 为空，返回 None
         如果 head 只有一个节点，返回 TreeNode(head.val)
         
         使用快慢指针找到链表中点 slow
         如果有前驱节点 prev，断开 prev 和 slow 的连接
         
         创建根节点 root = TreeNode(slow.val)
         root.left = sortedListToBST(head)  // 递归构建左子树
         root.right = sortedListToBST(slow.next)  // 递归构建右子树
         
         返回 root
     ```
   - **递归+全局指针法**：
     ```
     函数 sortedListToBST(head):
         计算链表长度 size
         设置全局指针 curr 指向 head
         返回 buildTree(0, size-1)
     
     函数 buildTree(left, right):
         如果 left > right，返回 None
         
         计算中点 mid = (left + right) // 2
         leftTree = buildTree(left, mid-1)  // 递归构建左子树
         
         创建根节点 root = TreeNode(curr.val)
         root.left = leftTree
         
         移动全局指针 curr = curr.next
         root.right = buildTree(mid+1, right)  // 递归构建右子树
         
         返回 root
     ```

4. 复杂度：
   - **时间复杂度**：$O(n \log n)$，其中 $n$ 是链表的长度。每次递归调用通过快慢指针分割链表需要 $O(n)$，而递归树的高度为 $O(\log n)$。
   - **空间复杂度**：$O(\log n)$，用于递归栈的空间。