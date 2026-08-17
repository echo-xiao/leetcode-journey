# 1982. 从未排序的链表中移除重复元素 · 要素

1. 要不要 dummy：要，因为头结点自己可能就是重复值要被删掉，用 dummy 指向 head，prev 从 dummy 开始，最后返回 dummy.next，省得单独处理删头的情况。

2. 指针关系：不是快慢指针，是 prev 紧跟在 curr 后面一位的前驱关系：curr 保留时 prev 才前移到 curr，curr 要删就让 prev.next 直接跳到 curr.next、prev 原地不动。

3. 停止条件：第二趟遍历的条件就是 curr != null，走到链表尾部（curr 为空）就停，不需要判断 curr.next；第一趟统计计数同样走到 curr == null 为止。
