# 145. 二叉树的后序遍历 · 解题思路与伪代码

1. **一句话直击本质：**  
   后序遍历的核心在于访问左子树、右子树，然后访问根节点。

2. **综合思路：**  
   - **递归解法：**  
     通过递归函数，先递归访问左子树，再递归访问右子树，最后访问根节点。
   - **迭代解法：**  
     使用栈模拟递归过程，通过栈记录节点，先处理左子树，再处理右子树，最后处理根节点。可以通过标记或逆序等方式确保访问顺序。

3. **全量伪代码：**

   **递归解法：**
   ```
   定义函数 traverse(node, res):
       如果 node 为空:
           返回
       调用 traverse(node.left, res)
       调用 traverse(node.right, res)
       将 node.val 添加到 res

   定义函数 postorderTraversal(root):
       初始化 res 为一个空列表
       调用 traverse(root, res)
       返回 res
   ```

   **迭代解法（使用栈）：**
   ```
   定义函数 postorderTraversal(root):
       初始化 res 为一个空列表
       初始化 stack 为一个空列表
       初始化 curr 为 root
       初始化 prev 为 None

       当 curr 不为空 或 stack 不为空 时:
           当 curr 不为空 时:
               将 curr 压入 stack
               将 curr 移动到 curr.left

           取 stack 的栈顶元素为 peek
           如果 peek.right 不为空 且 prev 不等于 peek.right:
               将 curr 移动到 peek.right
           否则:
               从 stack 弹出一个节点 node
               将 node.val 添加到 res
               将 prev 更新为 node
               将 curr 置为 None

       返回 res
   ```

   **迭代解法（逆序）：**
   ```
   定义函数 postorderTraversal(root):
       初始化 res 为一个空列表
       初始化 stack 为一个空列表
       初始化 curr 为 root

       当 curr 不为空 或 stack 不为空 时:
           当 curr 不为空 时:
               将 curr.val 添加到 res
               将 curr 压入 stack
               将 curr 移动到 curr.right

           从 stack 弹出一个节点 node
           将 curr 移动到 node.left

       返回 res 的逆序
   ```

4. **复杂度：**  
   - **时间复杂度：** $O(n)$，其中 $n$ 是二叉树中的节点数，因为每个节点都被访问一次。
   - **空间复杂度：** $O(n)$，在最坏情况下（例如，树是一个链表），递归调用栈或迭代栈的深度可能达到 $n$。
