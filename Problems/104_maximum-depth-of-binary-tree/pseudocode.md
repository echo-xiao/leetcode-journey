# 104. 二叉树的最大深度 · 解题思路与伪代码

1. 一句话直击本质：通过递归或迭代遍历二叉树，计算从根节点到叶子节点的最长路径长度，即最大深度。

2. 综合思路：
   - 递归法（DFS）：通过递归遍历每个节点，计算其左右子树的最大深度，最终返回左右子树深度的最大值加一。
   - 迭代法（BFS）：使用队列进行层次遍历，每遍历一层深度加一，直到遍历完整个树。

3. 全量伪代码：
   - 递归法（DFS）：
     ```
     定义函数 maxDepth(root):
         如果 root 为空:
             返回 0
         否则:
             计算左子树的最大深度 left_depth = maxDepth(root.left)
             计算右子树的最大深度 right_depth = maxDepth(root.right)
             返回 max(left_depth, right_depth) + 1
     ```
   - 递归法（DFS）使用辅助函数：
     ```
     定义函数 maxDepth(root):
         初始化最大深度 ans = 0
         调用辅助函数 traverse(node, depth)
         返回 ans

     定义辅助函数 traverse(node, depth):
         如果 node 为空:
             返回
         更新最大深度 ans = max(ans, depth)
         递归遍历左子树 traverse(node.left, depth + 1)
         递归遍历右子树 traverse(node.right, depth + 1)
     ```
   - 迭代法（BFS）：
     ```
     定义函数 maxDepth(root):
         如果 root 为空:
             返回 0
         初始化队列 queue 并将 root 入队
         初始化深度 depth = 0
         当队列不为空时:
             当前层的节点数 size = 队列的长度
             遍历当前层的所有节点:
                 取出队首节点 node
                 如果 node 有左子节点:
                     将左子节点入队
                 如果 node 有右子节点:
                     将右子节点入队
             当前层遍历完毕，深度加一 depth += 1
         返回 depth
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点都需要被访问一次。
   - 空间复杂度：递归法的空间复杂度为 $O(h)$，其中 $h$ 是树的高度，主要是递归调用栈的空间；迭代法的空间复杂度为 $O(w)$，其中 $w$ 是树的最大宽度，主要是队列的空间。
