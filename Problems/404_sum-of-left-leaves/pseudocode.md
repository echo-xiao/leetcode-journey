# 404. 左叶子之和 · 解题思路与伪代码

1. **一句话直击本质：** 通过递归遍历二叉树，识别并累加所有左叶子节点的值。

2. **综合思路：**
   - **递归方法：** 使用递归遍历二叉树，判断每个节点是否为左叶子节点，如果是则累加其值。递归过程中需要传递父节点信息以判断当前节点是否为左子节点。
   - **递归分治法：** 直接在递归过程中判断当前节点的左子节点是否为叶子节点，如果是则累加其值，同时递归计算左右子树的左叶子之和。

3. **全量伪代码：**

   - **递归遍历法：**
     ```
     定义函数 sumOfLeftLeaves(root):
         如果 root 为空，返回 0
         初始化结果 res 为 0
         调用辅助函数 traverse(node, prev) 传入 root 和 None
         返回 res

     定义辅助函数 traverse(node, prev):
         如果 node 为空，返回
         判断 node 是否为叶子节点
         判断 node 是否为左子节点
         如果 node 是左叶子节点，累加 node.val 到 res
         递归调用 traverse(node.left, node)
         递归调用 traverse(node.right, node)
     ```

   - **递归分治法：**
     ```
     定义函数 sumOfLeftLeaves(root):
         如果 root 为空，返回 0
         初始化 leftVal 为 0
         如果 root.left 存在且是叶子节点，设置 leftVal 为 root.left.val
         计算左子树的左叶子之和 leftSum = sumOfLeftLeaves(root.left)
         计算右子树的左叶子之和 rightSum = sumOfLeftLeaves(root.right)
         返回 leftVal + leftSum + rightSum
     ```

4. **复杂度：**
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树中的节点数，因为每个节点都被访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是二叉树的高度，递归调用栈的深度取决于树的高度。
