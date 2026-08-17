# 148. 排序链表 · 要素

1. 要不要 dummy：合并两条有序子链表时要用 dummy，因为要新拼一条链，有了 dummy 就不用单独判断第一个节点该接 left 还是 right，最后返回 dummy.next；拆分找中点那步不需要 dummy。

2. 指针关系：slow 一次一步、fast 一次两步，速度差 2:1；关键是让 slow 停在左半段的最后一个节点（比如 fast 从 head.next 起跑，或另存一个 prev 记住 slow 前一个），这样才能 slow.next=null 把链表真正切成两段。

3. 停止条件：fast 从 head.next 出发时，循环条件是 fast != null && fast.next != null，跳出时 slow 正好是左半段末尾；只有两个节点时切成 1+1，保证递归能缩小规模不死循环。合并那步的停止条件是 left 或 right 有一个走到 null，剩下的一截直接整条接到 curr.next。
