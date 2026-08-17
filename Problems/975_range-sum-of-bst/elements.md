# 975. 二叉搜索树的范围和 · 要素

1. 函数定义：rangeSumBST(root, low, high) 表示以root为根的子树中，所有值落在[low, high]区间内的节点值之和，参数low和high是范围边界固定不变，返回值是这个子树的范围和

2. base case：root为空时返回0，因为空节点没有值可累加

3. 单层主体：判断当前节点root.val是否在[low, high]范围内，如果在就把它算进结果（midVal=root.val），不在就当0，然后和左右子树已经算好的和相加

4. 代码位置：后序位置，因为要先拿到左右子树的和（leftSum、rightSum）再加上当前节点的值一起返回
