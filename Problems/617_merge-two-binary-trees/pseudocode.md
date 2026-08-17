# 617. 合并二叉树 · 解题思路与伪代码

1. 一句话直击本质：合并二叉树的核心逻辑是通过递归遍历两个二叉树的节点，将对应节点的值相加，并构建新的合并树。

2. 综合思路：
   - **递归解法**：通过递归遍历两个二叉树的节点，若某个节点在其中一个树中不存在，则直接返回另一个树的节点；否则，将两个节点的值相加，并递归合并它们的左右子树。
   - **迭代解法**：虽然在提供的代码集中没有迭代解法，但可以通过使用栈或队列来实现迭代版本，逐层合并节点。

3. 全量伪代码：
   - **递归解法伪代码**：
     ```
     定义函数 mergeTrees(root1, root2):
         如果 root1 为空，返回 root2
         如果 root2 为空，返回 root1
         
         创建新节点 newNode，其值为 root1.val + root2.val
         newNode.left = mergeTrees(root1.left, root2.left)
         newNode.right = mergeTrees(root1.right, root2.right)
         
         返回 newNode
     ```
   - **迭代解法伪代码（假设使用栈）**：
     ```
     定义函数 mergeTrees(root1, root2):
         如果 root1 为空，返回 root2
         如果 root2 为空，返回 root1
         
         初始化栈 stack，初始值为 [(root1, root2)]
         
         当栈不为空时:
             弹出节点对 (node1, node2) 从栈中
             
             如果 node1 为空或 node2 为空，继续下一个循环
             
             node1.val += node2.val
             
             如果 node1.left 和 node2.left 都不为空，将 (node1.left, node2.left) 压入栈
             如果 node1.right 和 node2.right 都不为空，将 (node1.right, node2.right) 压入栈
             
             如果 node1.left 为空，将 node2.left 赋值给 node1.left
             如果 node1.right 为空，将 node2.right 赋值给 node1.right
         
         返回 root1
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是两个二叉树中节点数的较大值，因为每个节点最多访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是递归调用栈的深度，最坏情况下为树的高度。对于平衡树，$h = \log n$，对于不平衡树，$h = n$。
