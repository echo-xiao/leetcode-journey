# 145. 二叉树的后序遍历 · 要素

1. 函数定义：traverse(node, res)：把以 node 为根的子树按后序把节点值依次追加到 res 里，本身不返回值（外层 postorderTraversal 返回 res 列表）。

2. base case：node 为空就直接 return，什么都不加进 res。

3. 单层主体：当前节点只做一件事——把自己的 val 加到 res 末尾，左右子树的结果由两次递归调用保证已经排在前面。

4. 代码位置：写在后序位置：先 traverse(node.left) 再 traverse(node.right)，最后才 res.append(node.val)。
