# 904. 叶子相似的树 · 解题思路与伪代码

1. 一句话直击本质：通过深度优先搜索（DFS）遍历两棵树，提取叶子节点序列并进行比较。

2. 综合思路：
   - 递归 DFS：使用递归的方式遍历树，将叶子节点的值存储在列表中，然后比较两个列表是否相同。
   - 迭代 DFS：可以使用栈来模拟递归的过程，非递归地遍历树，提取叶子节点。
   - BFS：虽然不常用，但也可以通过队列进行广度优先搜索，提取叶子节点。

3. 全量伪代码：
   - 递归 DFS 伪代码：
     ```
     定义函数 leafSimilar(root1, root2):
         如果 root1 和 root2 都为空，返回 True
         初始化 res1 和 res2 为空列表
         调用 traverse(root1, res1)
         调用 traverse(root2, res2)
         返回 res1 是否等于 res2

     定义函数 traverse(node, res):
         如果 node 为空，返回
         调用 traverse(node.left, res)
         调用 traverse(node.right, res)
         如果 node 是叶子节点（即 node.left 和 node.right 都为空），将 node.val 添加到 res
     ```

   - 迭代 DFS 伪代码（未在给定代码集中出现，但作为可能的解法）：
     ```
     定义函数 leafSimilar(root1, root2):
         如果 root1 和 root2 都为空，返回 True
         初始化 res1 和 res2 为空列表
         调用 iterativeDFS(root1, res1)
         调用 iterativeDFS(root2, res2)
         返回 res1 是否等于 res2

     定义函数 iterativeDFS(root, res):
         初始化栈 stack 并将 root 压入栈
         当栈不为空时：
             弹出栈顶节点 node
             如果 node 是叶子节点，将 node.val 添加到 res
             如果 node.right 不为空，将 node.right 压入栈
             如果 node.left 不为空，将 node.left 压入栈
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是树中节点的总数，因为每个节点都需要访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是树的高度，递归调用栈或迭代栈的空间取决于树的高度。
