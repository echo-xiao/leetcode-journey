# 637. 二叉树的层平均值 · 要素

1. 函数定义：traverse(node, depth) 表示把 node 这个节点的值累加到 stats[depth] 对应层的[总和,计数]里，depth 记录当前是第几层，没有返回值，靠外部 stats 列表收集结果

2. base case：node 为空直接返回，不做任何统计，因为空节点不该计入某层的总和和计数

3. 单层主体：看当前 depth 是否是新出现的层（等于 stats 长度就新建一个[0,0]），然后把 node.val 累加进 stats[depth][0]，节点数 stats[depth][1] 加一

4. 代码位置：前序位置，因为要先统计当前节点的值，再递归处理左右子节点
