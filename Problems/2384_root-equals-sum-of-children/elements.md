# 2384. 判断根结点是否等于子结点之和 · 要素

1. 函数定义：checkTree(root) 接一棵三节点树的根，返回布尔值：root.val 是否等于 root.left.val + root.right.val。

2. base case：本题不涉及真正的递归 base case，只是防御性判断：root 为空或左右孩子缺一个就返回 false；题目保证是完整三节点树，实际不会走到。

3. 单层主体：就一层：取出 root.val、root.left.val、root.right.val，直接比较 root.val == 左值+右值 并返回结果。

4. 代码位置：本题不涉及遍历顺序，只访问根和它的两个直接孩子，一次比较就结束，没有递归下探。
