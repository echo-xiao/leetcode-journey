# 103. 二叉树的锯齿形层序遍历 · 要素

1. 函数定义：traverse(node, level, res)：node 是当前节点，level 是它所在的层号（根为0），res 是按层存放的双端队列数组，函数本身不返回值，只负责把 node 的值塞进 res[level] 里。

2. base case：node 为空就直接 return，什么都不做不动 res；另外整棵树根为空时直接返回空列表。

3. 单层主体：当前节点只做两件事：若 res 长度等于 level 就先新开一个空双端队列，然后按 level 偶数从队尾 append、奇数从队头 appendleft 把 node.val 放进 res[level]，再带 level+1 递归左右孩子。

4. 代码位置：写在前序位置——必须先把当前节点值按层放好再往下递归，这样同层节点的插入顺序才是从左到右，锯齿反转才正确。
