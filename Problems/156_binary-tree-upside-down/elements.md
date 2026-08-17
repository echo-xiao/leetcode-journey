# 156. 上下翻转二叉树 · 要素

1. 函数定义：upsideDownBinaryTree(root)：把以 root 为根的这条左链整体翻转，返回翻转后的新根（也就是原树最左下角那个节点）。

2. base case：root 为空、或 root.left 为空（已经到最左下节点）时，直接把 root 自己返回当新根。

3. 单层主体：假设左子树已经翻好了，当前节点只做三件事：让 root.left.left = root.right，root.left.right = root，然后把 root.left 和 root.right 都置空。

4. 代码位置：后序位置——必须先递归拿到 newRoot，再改当前节点的左右指针，否则指针一改就找不到原来的左孩子链了。
