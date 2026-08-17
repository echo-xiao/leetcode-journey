# 501. 二叉搜索树中的众数 · 要素

1. 函数定义：traverse(node)负责中序遍历以node为根的子树，没有返回值，靠更新prev、cnt、max_cnt、res这些外部状态来记录众数信息

2. base case：node为空时直接返回，不做任何统计，因为空节点没有值可比较

3. 单层主体：比较当前节点值node.val和prev：相等就cnt+1，不等就cnt重置为1并更新prev；然后看cnt是否超过max_cnt来更新res列表（超过则清空res只留当前值，等于则把当前值加进res）

4. 代码位置：写在中序位置，即先traverse(node.left)，中间处理当前节点的计数和众数更新逻辑，再traverse(node.right)，这样能保证按升序处理节点值
