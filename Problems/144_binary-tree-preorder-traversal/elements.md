# 144. 二叉树的前序遍历 · 要素

1. 函数定义：traverse(node, res)：node 是当前要访问的节点，res 是共用的结果数组，函数本身不返回值，只负责把以 node 为根的子树的值按前序顺序追加进 res。

2. base case：node 为空就直接 return，什么也不加进 res。

3. 单层主体：当前节点只做一件事：把 node.val 塞进 res，然后交给左子树、右子树各自去填自己的部分。

4. 代码位置：写在前序位置——先 res.add(node.val)，再递归 left，最后递归 right；迭代版对应压栈时先压 right 后压 left。
