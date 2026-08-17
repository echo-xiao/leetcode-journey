# 203. 移除链表元素 · 要素

1. 要不要 dummy：要 dummy，因为头节点自己可能就等于 val 且可能连着好几个都要删，加个 dummy 指向 head 就不用单独写删头的分支，最后返回 dummy.next。

2. 指针关系：本题只有一个游标 curr 停在待检查节点的前一个位置，curr.next 才是被判断的节点，靠这个「前驱—当前」的一步之差来做删除；不涉及快慢指针的速度差。

3. 停止条件：当 curr.next == null 时停，即已经检查完最后一个节点；注意删除时 curr 不前进（curr.next = curr.next.next），只有不删才 curr = curr.next，否则会漏掉连续相同值的节点。
