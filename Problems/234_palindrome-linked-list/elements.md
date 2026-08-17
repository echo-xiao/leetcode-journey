# 234. 回文链表 · 要素

1. 要不要 dummy：不用 dummy，本题只是读值比较不新建链表；反转后半段时用一个 prev=null 的临时头往前接就够了。

2. 指针关系：slow 一次一步、fast 一次两步，fast 走完时 slow 正好停在中点（前半段末尾或后半段起点），偶数长度时 slow 落在后半段第一个，奇数长度让 slow 再多走一步跳过正中间那个节点。

3. 停止条件：while fast != null and fast.next != null 结束循环；之后从 slow 开始反转后半段，再拿 head 和反转后的头同时往后走，逐个比对值，任一为 null 就停，中途不等就返回 False。
