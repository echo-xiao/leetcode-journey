# 113. 路径总和 II · 要素

1. 函数定义：dfs(node, rest, path, res)：node 是当前节点，rest 是从这里往下还需要凑出的剩余和，path 是根到当前节点已走过的节点值，res 收集答案，函数本身不返回值，靠往 res 里塞路径来产出结果。

2. base case：node 为空就直接 return，什么都不做（空节点不算叶子，也不能算成一条路径）。

3. 单层主体：把 node.val 压进 path，判断如果是叶子节点且 rest == node.val 就把 path 的拷贝存进 res，然后分别用 rest - node.val 递归左右孩子，最后弹出 path 末尾元素回溯。

4. 代码位置：加入 path 和叶子判断写在前序位置（进入节点就做），从 path 弹出节点写在后序位置（左右都递归完再撤销）。
