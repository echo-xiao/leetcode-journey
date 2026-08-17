# 112. 路径总和 · 要素

1. 函数定义：hasPathSum(root, targetSum) 表示：以 root 为根的子树里，是否存在一条从 root 走到叶子、节点值之和正好等于 targetSum 的路径，返回布尔值。

2. base case：root 为空返回 false（空树没有叶子路径，也不能算成功）；另外遇到叶子节点时判断 targetSum - root.val == 0 返回对应真假。

3. 单层主体：当前节点先把自己的值从目标里扣掉得到 sumVal = targetSum - root.val，若是叶子就看 sumVal 是否为 0，否则把 sumVal 传给左右子树，左右任一返回 true 就 true。

4. 代码位置：前序位置：先扣掉当前节点值再往下递归，返回时只做左右结果的或运算，不需要后序额外处理。
