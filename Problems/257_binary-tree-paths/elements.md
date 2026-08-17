# 257. 二叉树的所有路径 · 要素

1. 函数定义：traverse(node, path, res)：node 是当前走到的节点，path 是从根到 node 父节点已经拼好的字符串（含末尾的"->"），res 收集结果，函数本身不返回值，靠往 res 里塞完整路径产出答案。

2. base case：node 为空就直接 return 什么都不做；外层 binaryTreePaths 里 root 为空返回空列表。

3. 单层主体：把当前节点值接到 path 后面得到 new_path，若左右孩子都为空说明是叶子就把 new_path 存进 res，否则对存在的左右孩子分别用 new_path+"->" 递归下去。

4. 代码位置：前序位置：先拼好当前节点的路径字符串再往下递归，路径必须自上而下带下去，后序拿不到父链信息。
