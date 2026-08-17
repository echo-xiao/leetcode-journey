# 222. 完全二叉树的节点个数 · 复盘

有几种写法，直接调用递归+判断满二叉树、或者binary search，但是需要知道如何写树的代码，并且要了解二叉树的特性2树的深度-1。

---

用递归，semantics是整个树的nodes count = 左子树 nodes counts + 右子树 nodes counts + 1。主体就是左遍历、右遍历，返回公式。termination case就是root为空，返回0。==**这个题目不需要单独写出叶子节点的情况，因为叶子节点的情况会被base case以及递归公式自然而然的处理。**==调用leftcount，返回0，调用rightcount，返回0，然后最终计算就是1。
