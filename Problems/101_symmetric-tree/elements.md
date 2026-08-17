# 101. 对称二叉树 · 要素

1. 函数定义：辅助函数 isMirror(p, q) 接两个节点，返回布尔值表示以 p、q 为根的两棵子树是否互为镜像；主函数 isSymmetric(root) 空树返回 true，否则返回 isMirror(root.left, root.right)。

2. base case：p 和 q 都为空返回 true；只有一个为空返回 false；两个都不空但值不相等也返回 false。

3. 单层主体：当前这一对节点值相等的前提下，交叉递归比较：isMirror(p.left, q.right) 和 isMirror(p.right, q.left) 都为真才返回真。

4. 代码位置：前序位置：先在当前层比较 p、q 的值和空情况，再往下递归两对子树。
