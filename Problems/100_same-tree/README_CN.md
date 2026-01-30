# 100. 相同的树

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`

## 题目描述

<p>给你两棵二叉树的根节点 <code>p</code> 和 <code>q</code> ，编写一个函数来检验这两棵树是否相同。</p>

<p>如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg" style="width: 622px; height: 182px;" />
<pre>
<strong>输入：</strong>p = [1,2,3], q = [1,2,3]
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg" style="width: 382px; height: 182px;" />
<pre>
<strong>输入：</strong>p = [1,2], q = [1,null,2]
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg" style="width: 622px; height: 182px;" />
<pre>
<strong>输入：</strong>p = [1,2,1], q = [1,1,2]
<strong>输出：</strong>false
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>两棵树上的节点数目都在范围 <code>[0, 100]</code> 内</li>
	<li><code>-10<sup>4</sup> <= Node.val <= 10<sup>4</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过递归比较两棵树的节点值及其子树的结构和内容是否完全相同。

2. 综合思路：
   - 递归解法：通过递归函数逐层比较两棵树的节点值和结构，若两节点均为空则返回 `True`，若一个为空或值不等则返回 `False`，否则递归比较左右子树。
   - 迭代解法（未在提供的代码集中出现，但常见于此类问题）：使用栈或队列进行深度优先搜索（DFS）或广度优先搜索（BFS），逐层比较节点，确保所有对应节点的值和结构相同。

3. 全量伪代码：
   - 递归解法：
     ```
     函数 isSameTree(p, q):
         如果 p 和 q 都为空:
             返回 True
         如果 p 为空 或 q 为空:
             返回 False
         如果 p.val 不等于 q.val:
             返回 False
         返回 isSameTree(p.left, q.left) 且 isSameTree(p.right, q.right)
     ```
   - 迭代解法（DFS 使用栈）：
     ```
     函数 isSameTree(p, q):
         初始化栈 stack，初始元素为 (p, q)
         当栈不为空时:
             弹出栈顶元素 (node1, node2)
             如果 node1 和 node2 都为空:
                 继续
             如果 node1 为空 或 node2 为空 或 node1.val 不等于 node2.val:
                 返回 False
             将 (node1.left, node2.left) 和 (node1.right, node2.right) 压入栈
         返回 True
     ```
   - 迭代解法（BFS 使用队列）：
     ```
     函数 isSameTree(p, q):
         初始化队列 queue，初始元素为 (p, q)
         当队列不为空时:
             取出队首元素 (node1, node2)
             如果 node1 和 node2 都为空:
                 继续
             如果 node1 为空 或 node2 为空 或 node1.val 不等于 node2.val:
                 返回 False
             将 (node1.left, node2.left) 和 (node1.right, node2.right) 加入队列
         返回 True
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是树中节点的数量，因为每个节点最多访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是树的高度，递归解法的空间复杂度由递归栈深度决定，迭代解法的空间复杂度由栈或队列的最大深度决定。