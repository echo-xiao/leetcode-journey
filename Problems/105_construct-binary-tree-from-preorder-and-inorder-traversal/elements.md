# 105. 从前序与中序遍历序列构造二叉树 · 要素

1. 函数定义：buildTree(preorder, inorder)：接一段前序序列和一段对应的中序序列（同一棵子树的所有节点），返回这棵子树的根节点。

2. base case：preorder（或 inorder）为空时返回 None，表示这段区间没有节点。

3. 单层主体：拿 preorder[0] 当根建节点，在 inorder 里找到它的下标 midIdx，左边 midIdx 个元素配 preorder[1:1+midIdx] 建左子树，右边剩下的配 preorder[1+midIdx:] 建右子树，挂上后返回根。

4. 代码位置：前序位置——先用 preorder 首元素造出根节点再往下递归，左右子树返回值挂到 root.left/right 上即可，不需要后序汇总。
