# 1005. 单值二叉树 · 要素

1. 函数定义：check(node, targetVal)：判断以 node 为根的子树里所有节点值是否都等于 targetVal，是就返回 True，否则 False；外层 isUnivalTree 先把根节点值取出来当 targetVal。

2. base case：node 为空时返回 True，空子树不破坏单值性。

3. 单层主体：当前节点值如果不等于 targetVal 就直接返回 False，否则返回左子树结果和右子树结果的与。

4. 代码位置：前序位置就能判掉当前节点（值不对立刻 False），左右结果的合并在后序位置返回。
