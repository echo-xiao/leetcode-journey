# 24. 两两交换链表中的节点 · 要素

1. 要不要 dummy：要，因为头两个节点也要交换，头结点会变，用 dummy 指向 head，最后返回 dummy.next，这样每对交换都能统一用 prev.next 接上。

2. 指针关系：不是快慢指针，而是三个挨着的指针：prev 是已处理部分的尾巴，first 和 second 是待交换的相邻两个（second = first.next），每轮交换完 prev 挪到 first，first 挪到原来的 nxt。

3. 停止条件：while second 不为空就继续，也就是当剩下不足两个节点（first 为空或 first.next 为空导致 second 为 None）时停下，剩的单个节点原样挂着不动。
