# 112. 路径总和 · 解题思路与伪代码

1. **一句话直击本质：** 通过递归或迭代遍历二叉树，检查从根节点到叶子节点的路径和是否等于目标值。

2. **综合思路：**
   - **递归解法：** 通过递归遍历树，逐步减少目标和，检查在叶子节点时路径和是否等于目标值。
   - **迭代解法（未在提供的代码中出现，但作为补充）：** 使用栈或队列进行深度优先搜索（DFS）或广度优先搜索（BFS），在遍历过程中计算路径和。

3. **全量伪代码：**

   - **递归解法：**
     ```
     函数 hasPathSum(节点 root, 整数 targetSum):
         如果 root 为空:
             返回 False
         
         计算当前路径和: sumVal = targetSum - root.val
         
         如果 root 是叶子节点:
             返回 sumVal 是否等于 0
         
         返回 hasPathSum(root.left, sumVal) 或 hasPathSum(root.right, sumVal)
     ```

   - **迭代解法（DFS）：**
     ```
     函数 hasPathSum(节点 root, 整数 targetSum):
         如果 root 为空:
             返回 False
         
         初始化栈 stack，初始元素为 (root, root.val)
         
         当栈不为空时:
             弹出栈顶元素 (node, currentSum)
             
             如果 node 是叶子节点且 currentSum 等于 targetSum:
                 返回 True
             
             如果 node.right 存在:
                 将 (node.right, currentSum + node.right.val) 压入栈
             
             如果 node.left 存在:
                 将 (node.left, currentSum + node.left.val) 压入栈
         
         返回 False
     ```

4. **复杂度：**
   - **时间复杂度：** $O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点都需要访问一次。
   - **空间复杂度：** $O(h)$，其中 $h$ 是二叉树的高度，递归调用栈或迭代栈的最大深度。对于平衡树，$h = \log n$；对于不平衡树，$h = n$。
