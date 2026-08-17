# 404. 左叶子之和 · 复盘

semantics就是整棵树的left leaves的和，就是左子树的left leaves的和，加上右子树的left leaves的和。left leaves 的定义需要满足两个条件：1. 需要是子节点 node.left is None and node.right is None 2. 这个节点需要是父节点的左孩子。那么这个traverse就会比较好定义，需要传入父节点这个参数，同时需要一个外部变量来更新累加之后的sum。那么主体就是当是叶子节点同时也是父节点的左孩子的时候，累加外部变量，然后再遍历左子树，右子树。最后的termination case就是当node节点为空的时候返回。但是这么写的时候出现了个问题，判断逻辑中的prev访问不安全，少了一个条件，就是prev is not none的条件，并且这个prev is not `none需要写在prev.left == node之前`，一定要写在之前，这个里面就是一些edge case，需要注意。
