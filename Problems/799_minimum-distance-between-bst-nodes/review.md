# 799. 二叉搜索树节点最小距离 · 复盘

返回BST里面，任意两个node之间的最小diff，其实就是中序遍历里面，找prev和现在这个node的最小dif，所以semantics就是中序遍历整个tree，然后node跟prev相比，进行比较，更新最小的diff，最后prev等于现在的node.val。
