# 116. 填充每个节点的下一个右侧节点指针 · 要素

1. 函数定义：connect(root)：给以 root 为根的完美二叉树内部所有节点接好 next，返回处理完的 root（递归时只关心把 root 的两个孩子及其下面全部连好）。

2. base case：root 为空或 root.left 为空（即叶子）时什么都不做，直接返回 root。

3. 单层主体：只做两件连接：root.left.next = root.right；若 root.next 存在，则 root.right.next = root.next.left；然后递归左右孩子。

4. 代码位置：前序位置——先把当前层的两条 next 连好，再往下递归，因为右子树需要父层的 next 已经就位。
