# 147. 对链表进行插入排序 · 要素

1. 要不要 dummy：要，dummy 挂在已排序链表前面，这样把最小的节点插到头部也不用特判，最后返回 dummy.next。

2. 指针关系：不是快慢指针，而是 curr 指向待插入节点、prev 从 dummy 起在已排序段里往后扫找插入点，另外还要先用 nxt 存住 curr.next 防止断链。

3. 停止条件：内层 prev 在 prev.next 为空或 prev.next.val >= curr.val 时停下就地插入；外层 curr 走到 null（原链表遍历完）整个排序结束。
