# 1005. 单值二叉树 · 解题思路与伪代码

1. 一句话直击本质：该算法的核心逻辑是通过递归遍历二叉树的所有节点，检查每个节点的值是否与根节点的值相同。

2. 综合思路：
   - 递归解法：使用递归函数遍历二叉树，检查每个节点的值是否等于根节点的值。如果所有节点的值都相同，则返回 `True`，否则返回 `False`。
   - 迭代解法（未在提供的代码中出现，但作为补充）：可以使用栈或队列进行深度优先搜索（DFS）或广度优先搜索（BFS），逐个检查每个节点的值是否与根节点的值相同。

3. 全量伪代码：
   ```plaintext
   定义函数 isUnivalTree(root):
       如果 root 是空:
           返回 True
       
       设定 targetVal 为 root 的值
       返回 check(root, targetVal)

   定义函数 check(node, targetVal):
       如果 node 是空:
           返回 True
       
       如果 node 的值不等于 targetVal:
           返回 False
       
       leftCheck = check(node.left, targetVal)
       rightCheck = check(node.right, targetVal)
       
       返回 leftCheck 且 rightCheck
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树中的节点数，因为每个节点都需要被访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是二叉树的高度，递归调用栈的深度取决于树的高度。对于平衡树，$h = \log n$，对于不平衡树，$h = n$。
