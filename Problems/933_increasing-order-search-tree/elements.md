# 933. 递增顺序搜索树 · 要素

1. 函数定义：traverse(node) 表示对以node为根的子树做中序遍历，把节点按顺序接到curr.right上，本身不返回值，靠外部curr指针和dummy_head传递结果

2. base case：node为空时直接return，不做任何连接操作

3. 单层主体：先递归处理左子树，再新建一个只含当前节点值的节点接到curr.right，curr后移，再递归处理右子树

4. 代码位置：中序位置，即先traverse左子树，再处理当前节点（新建节点接到curr.right），最后traverse右子树
