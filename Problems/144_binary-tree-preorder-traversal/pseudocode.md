# 144. 二叉树的前序遍历 · 解题思路与伪代码

1. 一句话直击本质：前序遍历的核心逻辑是按照“根-左-右”的顺序访问每个节点。

2. 综合思路：
   - 递归解法：通过递归函数实现前序遍历，先访问根节点，然后递归遍历左子树，最后递归遍历右子树。
   - 迭代解法：使用栈来模拟递归调用栈，首先访问根节点并将其压入栈中，然后依次访问左子树和右子树。

3. 全量伪代码：
   - 递归解法：
     ```
     定义函数 traverse(node, res):
         如果 node 为空:
             返回
         将 node.val 添加到 res
         调用 traverse(node.left, res)
         调用 traverse(node.right, res)

     定义函数 preorderTraversal(root):
         初始化 res 为一个空列表
         调用 traverse(root, res)
         返回 res
     ```
   - 迭代解法：
     ```
     定义函数 preorderTraversal(root):
         如果 root 为空:
             返回空列表
         初始化 stack 为包含 root 的列表
         初始化 res 为一个空列表
         当 stack 不为空时:
             弹出 stack 的最后一个元素 curr
             将 curr.val 添加到 res
             如果 curr.right 不为空:
                 将 curr.right 压入 stack
             如果 curr.left 不为空:
                 将 curr.left 压入 stack
         返回 res
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树中的节点数，因为每个节点都被访问一次。
   - 空间复杂度：$O(n)$，在最坏情况下（例如，树是一个链表），栈或递归调用栈的深度可能达到 $n$。
