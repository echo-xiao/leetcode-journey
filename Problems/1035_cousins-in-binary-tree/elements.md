# 1035. 二叉树的堂兄弟节点 · 要素

1. 函数定义：traverse(node, prev, depth)：node 是当前节点，prev 是它的父节点，depth 是它所在层数，不返回值，只负责把 x、y 的深度和父节点写进外部变量 dx/px、dy/py。

2. base case：node 为空就直接 return，不做任何记录。

3. 单层主体：看当前节点值是不是 x 或 y，是就把 depth 和 prev 存到对应的 dx/px 或 dy/py，然后带着 self 作为父节点、depth+1 递归左右子树。

4. 代码位置：前序位置，一进节点就判断并记录，因为深度和父节点在往下走之前就已知，不依赖子树结果。
