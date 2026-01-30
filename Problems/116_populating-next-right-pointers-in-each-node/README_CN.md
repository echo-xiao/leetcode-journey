# 116. 填充每个节点的下一个右侧节点指针

**难度**: Medium | **标签**: `Linked List` `Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`

## 题目描述

<p>给定一个&nbsp;<strong>完美二叉树&nbsp;</strong>，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：</p>

<pre>
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}</pre>

<p>填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 <code>NULL</code>。</p>

<p>初始状态下，所有&nbsp;next 指针都被设置为 <code>NULL</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/02/14/116_sample.png" style="height: 171px; width: 500px;" /></p>

<pre>
<b>输入：</b>root = [1,2,3,4,5,6,7]
<b>输出：</b>[1,#,2,3,#,4,5,6,7,#]
<b>解释：</b>给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。
</pre>

<p><meta charset="UTF-8" /></p>

<p><strong>示例 2:</strong></p>

<pre>
<b>输入：</b>root = []
<b>输出：</b>[]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点的数量在<meta charset="UTF-8" />&nbsp;<code>[0, 2<sup>12</sup>&nbsp;- 1]</code>&nbsp;范围内</li>
	<li><code>-1000 &lt;= node.val &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>你只能使用常量级额外空间。</li>
	<li>使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过层级遍历或递归方式，将每个节点的 `next` 指针指向其右侧相邻节点。

2. **综合思路：**
   - **BFS（广度优先搜索）迭代法：** 使用队列进行层级遍历，每层节点依次连接到其右侧相邻节点。
   - **DFS（深度优先搜索）递归法：** 直接递归处理每个节点的左右子节点，连接其右侧相邻节点。
   - **常量空间迭代法：** 通过使用两个指针在树的每一层进行遍历，连接每个节点的左右子节点。

3. **全量伪代码：**

   - **BFS 迭代法：**
     ```
     如果根节点为空，返回 None
     初始化队列 q，包含根节点
     当队列 q 不为空时：
         获取当前层的节点数量 size
         对于当前层的每个节点：
             从队列中弹出节点 node
             如果不是当前层的最后一个节点，将 node.next 指向队列的下一个节点
             如果 node 有左子节点，将其加入队列
             如果 node 有右子节点，将其加入队列
     返回根节点
     ```

   - **DFS 递归法：**
     ```
     如果根节点为空或没有左子节点，返回根节点
     将根节点的左子节点的 next 指向右子节点
     如果根节点有 next，将右子节点的 next 指向根节点 next 的左子节点
     递归处理左子节点
     递归处理右子节点
     返回根节点
     ```

   - **常量空间迭代法：**
     ```
     初始化 cur 为根节点，nxt 为根节点的左子节点（如果存在）
     当 cur 和 nxt 不为空时：
         将 cur 的左子节点的 next 指向右子节点
         如果 cur 有 next，将右子节点的 next 指向 cur.next 的左子节点
         将 cur 移动到 cur.next
         如果 cur 为空，将 cur 设为 nxt，并将 nxt 设为 cur 的左子节点
     返回根节点
     ```

4. **复杂度：**
   - **时间复杂度：** 所有方法的时间复杂度均为 $O(n)$，其中 $n$ 是节点的数量，因为每个节点都被访问一次。
   - **空间复杂度：**
     - **BFS 迭代法：** $O(n)$，因为队列最多可能包含一整层的节点。
     - **DFS 递归法：** $O(\log n)$，因为递归栈的深度等于树的高度。
     - **常量空间迭代法：** $O(1)$，因为只使用了有限的指针变量。