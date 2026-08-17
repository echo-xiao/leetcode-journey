# 543. 二叉树的直径 · 解题思路与伪代码

1. 一句话直击本质：通过递归计算每个节点的左右子树深度，并更新最大直径为左右子树深度之和的最大值。

2. 综合思路：
   - 递归深度优先搜索（DFS）：通过递归遍历二叉树，计算每个节点的左右子树深度，并在过程中更新最大直径。
   - 迭代方法：虽然在提供的代码中没有迭代实现，但理论上可以使用栈模拟递归过程来实现迭代版本。

3. 全量伪代码：
   - 递归 DFS 版本：
     ```
     定义函数 diameterOfBinaryTree(root):
         初始化 max_diameter 为 0
         调用 depth(root)
         返回 max_diameter

     定义函数 depth(node):
         如果 node 为空:
             返回 0
         计算左子树深度 leftDepth = depth(node.left)
         计算右子树深度 rightDepth = depth(node.right)
         更新 max_diameter 为 max(max_diameter, leftDepth + rightDepth)
         返回 1 + max(leftDepth, rightDepth)
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点都被访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是二叉树的高度，主要是递归调用栈的空间消耗。
