# 117. 填充每个节点的下一个右侧节点指针 II

**难度**: Medium | **标签**: `Linked List` `Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`

## 题目描述

<p>给定一个二叉树：</p>

<pre>
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}</pre>

<p>填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 <code>NULL</code> 。</p>

<p>初始状态下，所有&nbsp;next 指针都被设置为 <code>NULL</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/15/117_sample.png" style="width: 500px; height: 171px;" />
<pre>
<strong>输入</strong>：root = [1,2,3,4,5,null,7]
<strong>输出：</strong>[1,#,2,3,#,4,5,7,#]
<strong>解释：</strong>给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指针连接），'#' 表示每层的末尾。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = []
<strong>输出：</strong>[]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中的节点数在范围 <code>[0, 6000]</code> 内</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p><strong>进阶：</strong></p>

<ul>
	<li>你只能使用常量级额外空间。</li>
	<li>使用递归解题也符合要求，本题中递归程序的隐式栈空间不计入额外空间复杂度。</li>
</ul>

<ul>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过层序遍历或逐层连接的方式，逐层设置每个节点的 `next` 指针指向其右侧的节点。

2. **综合思路：**
   - **BFS（广度优先搜索）解法：** 使用队列进行层序遍历，每次处理一层的节点，并将每个节点的 `next` 指针指向队列中的下一个节点。
   - **DFS（深度优先搜索）解法：** 递归地处理每个节点，首先处理右子树，再处理左子树，确保每个节点的 `next` 指针正确连接。
   - **逐层连接法：** 使用一个虚拟节点和尾指针逐层连接每个节点的子节点，模拟层序遍历的效果。

3. **全量伪代码：**

   - **BFS 解法：**
     ```
     如果根节点为空，返回空
     初始化队列，将根节点加入队列
     当队列不为空时：
         获取当前队列的大小 size
         遍历 size 次：
             弹出队列头节点 node
             如果不是当前层的最后一个节点，将 node.next 指向队列的下一个节点
             如果 node 有左子节点，将其加入队列
             如果 node 有右子节点，将其加入队列
     返回根节点
     ```

   - **DFS 解法：**
     ```
     如果根节点为空，返回空
     初始化指针 p 指向根节点的 next
     初始化 nxt 为 None
     当 p 不为空时：
         如果 p 有左子节点，将 nxt 指向 p 的左子节点并退出循环
         如果 p 有右子节点，将 nxt 指向 p 的右子节点并退出循环
         将 p 移动到 p.next
     如果根节点有右子节点，将其 next 指向 nxt
     如果根节点有左子节点，将其 next 指向根节点的右子节点或 nxt
     递归处理根节点的右子节点
     递归处理根节点的左子节点
     返回根节点
     ```

   - **逐层连接法：**
     ```
     如果根节点为空，返回空
     初始化 curr 指向根节点
     当 curr 不为空时：
         初始化虚拟节点 dummy 和尾指针 tail 指向 dummy
         当 curr 不为空时：
             如果 curr 有左子节点，将 tail.next 指向 curr 的左子节点，并移动 tail
             如果 curr 有右子节点，将 tail.next 指向 curr 的右子节点，并移动 tail
             将 curr 移动到 curr.next
         将 curr 指向 dummy.next
     返回根节点
     ```

4. **复杂度：**

   - **时间复杂度：** 所有解法的时间复杂度均为 $O(n)$，其中 $n$ 是节点的数量，因为每个节点仅被访问一次。
   - **空间复杂度：** 
     - BFS 解法的空间复杂度为 $O(w)$，其中 $w$ 是二叉树的最大宽度。
     - DFS 解法的空间复杂度为 $O(h)$，其中 $h$ 是二叉树的高度，主要是递归调用栈的空间。
     - 逐层连接法的空间复杂度为 $O(1)$，因为只使用了常数级别的额外空间。