# 144. 二叉树的前序遍历 · 复盘

二叉树的遍历，**有两种方式，一种stack是模拟路径指针走法**/指针游走，关注点在于left和right的方向，stack的信息是帮你回溯之前的所有路。**另外一种stack的方式是作为列表储存叶子节点left和right，纯栈迭代法，**孩子节点里面谁先出谁后出。然后因为要倒着出栈，所以先reverse整个列表。

---

前序遍历，跟94、binary tree inorder traversal 一致
