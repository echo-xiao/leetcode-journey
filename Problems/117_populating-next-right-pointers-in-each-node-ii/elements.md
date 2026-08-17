# 117. 填充每个节点的下一个右侧节点指针 II · 要素

1. 函数定义：connect(root) 表示把以 root 为根的这棵子树里所有节点的 next 指针都连好，并把连好后的 root 原样返回（外层递归只借它做副作用，不看返回值）。

2. base case：root 为空就直接返回 None，什么都不用连。

3. 单层主体：当前节点已经有正确的 next：顺着 root.next 往右扫兄弟节点，找到第一个有左孩子或右孩子的节点，把那个孩子记为 nxt；然后 root.right.next = nxt，root.left.next = root.right（没有 right 就指 nxt）。

4. 代码位置：前序位置——必须先把当前层两个孩子的 next 连好，再递归；而且要先递归右子树后递归左子树，保证进入左子树时右边的 next 链已经就绪。
