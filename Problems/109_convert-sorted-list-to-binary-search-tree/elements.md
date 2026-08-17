# 109. 有序链表转换二叉搜索树 · 要素

1. 函数定义：sortedListToBST(head) 表示把以 head 开头的这段有序链表建成一棵平衡 BST，返回这棵子树的根节点；全局指针法里 buildTree(left, right) 表示用链表第 left 到第 right 个节点建子树并返回根。

2. base case：head 为空返回 None（单节点时直接返回 TreeNode(head.val)）；全局指针法是 left > right 返回 None。

3. 单层主体：快慢指针找到这段链表中点 slow 当根，在 prev 处把链表切断，然后左半段递归给 root.left、slow.next 那段递归给 root.right，返回 root。

4. 代码位置：快慢指针法是前序（先定根再递归左右）；全局指针法必须中序——先建完左子树，再用当前 curr.val 建根并把 curr 后移，最后建右子树。
