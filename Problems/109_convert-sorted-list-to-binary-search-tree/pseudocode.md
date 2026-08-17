# 109. 有序链表转换二叉搜索树 · 解题思路与伪代码

1. 一句话直击本质：利用快慢指针找到链表中点作为根节点，递归构建左右子树，或通过中序遍历模拟构建平衡二叉搜索树。

2. 综合思路：
   - **递归+快慢指针法**：通过快慢指针找到链表的中点，将其作为当前子树的根节点，然后递归地对中点左侧和右侧的链表部分构建左子树和右子树。
   - **递归+全局指针法**：先遍历链表计算长度，然后通过递归模拟中序遍历，利用全局指针逐步构建树节点。

3. 全量伪代码：
   - **递归+快慢指针法**：
     ```
     函数 sortedListToBST(head):
         如果 head 为空，返回 None
         如果 head 只有一个节点，返回 TreeNode(head.val)
         
         使用快慢指针找到链表中点 slow
         如果有前驱节点 prev，断开 prev 和 slow 的连接
         
         创建根节点 root = TreeNode(slow.val)
         root.left = sortedListToBST(head)  // 递归构建左子树
         root.right = sortedListToBST(slow.next)  // 递归构建右子树
         
         返回 root
     ```
   - **递归+全局指针法**：
     ```
     函数 sortedListToBST(head):
         计算链表长度 size
         设置全局指针 curr 指向 head
         返回 buildTree(0, size-1)
     
     函数 buildTree(left, right):
         如果 left > right，返回 None
         
         计算中点 mid = (left + right) // 2
         leftTree = buildTree(left, mid-1)  // 递归构建左子树
         
         创建根节点 root = TreeNode(curr.val)
         root.left = leftTree
         
         移动全局指针 curr = curr.next
         root.right = buildTree(mid+1, right)  // 递归构建右子树
         
         返回 root
     ```

4. 复杂度：
   - **时间复杂度**：$O(n \log n)$，其中 $n$ 是链表的长度。每次递归调用通过快慢指针分割链表需要 $O(n)$，而递归树的高度为 $O(\log n)$。
   - **空间复杂度**：$O(\log n)$，用于递归栈的空间。
