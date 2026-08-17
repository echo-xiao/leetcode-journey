# 617. 合并二叉树 · 要素

1. 函数定义：mergeTrees(root1, root2) 表示合并以root1和root2为根的两棵树，返回值是合并后新树的根节点

2. base case：如果root1为空返回root2，如果root2为空返回root1，两个都空自然也返回空

3. 单层主体：把root1和root2的值相加放进新节点（或直接累加到root1上），然后分别对左子树对(root1.left, root2.left)和右子树对(root1.right, root2.right)递归合并，结果挂到新节点的左右孩子上

4. 代码位置：前序位置，先算当前节点的合并值，再递归处理左右子树
