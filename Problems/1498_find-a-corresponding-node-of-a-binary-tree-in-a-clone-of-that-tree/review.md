# 1498. 找出克隆二叉树中的相同节点 · 复盘

semantics是两棵树按照同样的了逻辑遍历，当original树遍历到target的时候，cloned树也遍历到了target，所以直接返回就行。这样的话，是写一个traverse函数，然后传入一个node参数，然后分解遍历origianl和cloned两棵树，还是写一个traverse函数，然后传入两个node参数，同时遍历original、clone两棵树呢？答案，选择同时遍历，因为如果分开遍历的话，还要一个储存结构来记忆路径。
