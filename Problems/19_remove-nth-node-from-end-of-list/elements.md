# 19. 删除链表的倒数第 N 个结点 · 要素

1. 要不要 dummy：要，因为可能删的就是头结点，用 dummy 指向 head 后返回 dummy.next，就不用单独判断删头的情况。

2. 指针关系：两个指针都从 dummy 出发，fast 先走 n 步，之后同速前进，始终让 fast 领先 slow 恰好 n 个节点，这样 slow 停下时正好停在待删节点的前一个。

3. 停止条件：当 fast.next == null 时停（fast 到达最后一个节点），此时 slow.next 就是倒数第 n 个，执行 slow.next = slow.next.next。
