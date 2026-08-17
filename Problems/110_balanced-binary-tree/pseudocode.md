# 110. 平衡二叉树 · 解题思路与伪代码

1. 一句话直击本质：通过递归计算每个节点的左右子树高度，若高度差超过1则返回-1表示不平衡，否则返回实际高度。

2. 综合思路：
   - 递归解法：通过递归函数计算每个节点的左右子树高度，若某个节点的左右子树高度差超过1或者子树本身不平衡，则返回-1表示不平衡；否则返回当前节点的高度。
   - 迭代解法：虽然题目中没有提供迭代解法，但通常可以使用栈或队列进行层序遍历，记录每个节点的高度并判断平衡性。

3. 全量伪代码：
   - 递归解法：
     ```
     定义函数 isBalanced(root):
         如果 root 为空，返回 True
         调用 calcHeight(root) 函数
         如果 calcHeight(root) 返回 -1，返回 False
         否则返回 True

     定义函数 calcHeight(node):
         如果 node 为空，返回 0
         计算左子树高度 left_height = calcHeight(node.left)
         计算右子树高度 right_height = calcHeight(node.right)
         如果 left_height 或 right_height 为 -1，或者左右高度差大于 1，返回 -1
         返回 max(left_height, right_height) + 1
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点都被访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是二叉树的高度，递归调用栈的深度。
