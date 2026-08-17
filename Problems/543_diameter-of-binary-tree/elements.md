# 543. 二叉树的直径 · 要素

1. 函数定义：depth(node) 表示以node为根的子树的最大深度（节点数），返回值是这个深度，同时用一个外部变量max_diameter记录遍历过程中出现过的最大直径

2. base case：节点为空时返回深度0，表示空树深度为0

3. 单层主体：分别递归求左子树深度leftDepth和右子树深度rightDepth，用leftDepth+rightDepth去更新max_diameter（这条路径经过当前节点的最长路径长度），然后返回1+max(leftDepth, rightDepth)作为当前节点的深度

4. 代码位置：后序位置，因为要先拿到左右子树的深度结果才能计算当前节点的直径贡献并返回自己的深度
