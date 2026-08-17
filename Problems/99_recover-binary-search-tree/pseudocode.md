# 99. 恢复二叉搜索树 · 解题思路与伪代码

1. **一句话直击本质：** 通过中序遍历找到两个错误的节点并交换它们的值来恢复二叉搜索树。

2. **综合思路：**
   - **递归中序遍历：** 使用递归方法进行中序遍历，记录前一个节点，并在遍历过程中找到两个错误的节点。
   - **迭代中序遍历：** 使用栈模拟递归过程进行中序遍历，同样记录前一个节点并找到错误节点。
   - **Morris遍历（未在给定代码中出现）：** 通过修改树结构实现中序遍历，空间复杂度为 $O(1)$。

3. **全量伪代码：**

   - **递归中序遍历：**
     ```
     定义函数 recoverTree(root):
         初始化 first, second, prev 为 None
         调用递归函数 inorder(root)
         交换 first 和 second 的值

     定义递归函数 inorder(node):
         如果 node 为空，返回
         调用 inorder(node.left)
         如果 prev 的值大于当前 node 的值：
             如果 first 为空，将 first 设为 prev
             将 second 设为 node
         将 prev 设为 node
         调用 inorder(node.right)
     ```

   - **迭代中序遍历：**
     ```
     定义函数 recoverTree(root):
         初始化 stack 为空列表
         初始化 node 为 root
         初始化 prev 为值为负无穷的 TreeNode
         初始化 first 和 second 为 None
         
         当 stack 不为空或 node 不为空时：
             当 node 不为空时：
                 将 node 压入 stack
                 将 node 设为 node.left
             
             将 node 设为 stack 弹出的元素
             
             如果 prev 的值大于 node 的值：
                 如果 first 为空，将 first 设为 prev
                 将 second 设为 node
             
             将 prev 设为 node
             将 node 设为 node.right
         
         交换 first 和 second 的值
     ```

4. **复杂度：**
   - 时间复杂度：$O(n)$，其中 $n$ 是树中节点的数量，因为每个节点都被访问一次。
   - 空间复杂度：
     - 递归中序遍历：$O(h)$，其中 $h$ 是树的高度，递归调用栈的空间。
     - 迭代中序遍历：$O(h)$，栈的空间。
     - Morris遍历（未在给定代码中出现）：$O(1)$，不使用额外空间。
