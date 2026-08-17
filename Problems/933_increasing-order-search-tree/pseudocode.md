# 933. 递增顺序搜索树 · 解题思路与伪代码

1. 一句话直击本质：通过中序遍历将二叉树节点按递增顺序重新连接成单链表形式的树。

2. 综合思路：
   - 递归方法：使用中序遍历递归地访问每个节点，将其连接到一个新的树结构中。
   - 迭代方法：使用栈模拟中序遍历，逐步访问每个节点并重新连接。

3. 全量伪代码：
   - 递归方法：
     ```
     定义函数 increasingBST(root):
         如果 root 为空，返回 None
         初始化 dummy_head 为新节点(-1)
         初始化 curr 指向 dummy_head
         调用 traverse(root)
         返回 dummy_head.right

     定义函数 traverse(node):
         如果 node 为空，返回
         调用 traverse(node.left)
         curr.right 指向新节点(node.val)
         curr 更新为 curr.right
         调用 traverse(node.right)
     ```
   - 迭代方法：
     ```
     定义函数 increasingBST(root):
         如果 root 为空，返回 None
         初始化 stack 为空列表
         初始化 curr 指向 root
         初始化 dummy 为新节点(-1)
         初始化 prev 指向 dummy
         当 curr 不为空或 stack 不为空时:
             当 curr 不为空时:
                 将 curr 压入 stack
                 curr 更新为 curr.left
             从 stack 弹出节点 node
             node.left 置为 None
             prev.right 指向 node
             prev 更新为 node
             curr 更新为 node.right
         返回 dummy.right
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是树中节点的数量，因为每个节点都被访问一次。
   - 空间复杂度：$O(n)$，在递归方法中，递归栈的深度和在迭代方法中栈的最大空间都可能达到 $n$。
