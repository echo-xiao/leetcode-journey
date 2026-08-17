# 94. 二叉树的中序遍历 · 解题思路与伪代码

1. 一句话直击本质：中序遍历的核心逻辑是按照“左-根-右”的顺序访问二叉树的节点。

2. 综合思路：
   - 递归解法：通过递归函数实现中序遍历，递归地访问左子树、记录当前节点值、再递归访问右子树。
   - 迭代解法：使用栈来模拟递归过程，先将左子树节点压栈，访问节点后处理右子树。

3. 全量伪代码：
   - 递归解法：
     ```
     定义函数 inorderTraversal(root):
         初始化结果列表 res
         调用递归函数 traverse(node, res)
         返回 res

     定义递归函数 traverse(node, res):
         如果 node 为空，返回
         调用 traverse(node.left, res)
         将 node.val 添加到 res
         调用 traverse(node.right, res)
     ```
   - 迭代解法：
     ```
     定义函数 inorderTraversal(root):
         初始化空栈 stack 和结果列表 res
         设置 curr 为 root
         当 curr 不为空 或者 stack 不为空时:
             当 curr 不为空时:
                 将 curr 压入 stack
                 设置 curr 为 curr.left
             将 stack 顶部元素出栈赋给 curr
             将 curr.val 添加到 res
             设置 curr 为 curr.right
         返回 res
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点都被访问一次。
   - 空间复杂度：递归解法的空间复杂度为 $O(h)$，迭代解法的空间复杂度为 $O(h)$，其中 $h$ 是二叉树的高度。
