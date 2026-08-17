# 904. 叶子相似的树 · 复盘

semantics就是写一个traverse的辅助函数，任何一种方式遍历整个树，当遇到叶子节点的时候就加入list。然后主函数就是分别traverse两个树，得到的list结果进行比较。
