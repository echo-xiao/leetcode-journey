# 563. 二叉树的坡度 · 要素

1. 函数定义：sumTree(node) 传入当前子树根节点node，返回值是这棵子树所有节点值的和（同时在过程中把坡度累加到self.res里）

2. base case：节点为空时返回0，表示空树的和为0，也不产生坡度

3. 单层主体：分别递归拿到左子树和leftSum、右子树和rightSum，用abs(leftSum-rightSum)累加到坡度累加器res里，然后返回node.val+leftSum+rightSum作为当前子树的和

4. 代码位置：后序位置，因为要先拿到左右子树的和才能算当前节点的坡度并累加
