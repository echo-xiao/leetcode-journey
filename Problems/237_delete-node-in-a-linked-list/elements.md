# 237. 删除链表中的节点 · 要素

1. 要不要 dummy：不要 dummy，题目只给了待删节点 node，根本拿不到头结点，也没在建新链表，全程就改 node 和 node.next 两个节点。

2. 指针关系：只有 node 和它后继 nxt = node.next 这一对相邻指针（差一步），没有快慢指针赛跑，把 nxt 的值抄给 node 再让 node.next 跳过 nxt 即可。

3. 停止条件：本题不涉及循环停止条件，操作是 O(1) 的一次性动作；唯一要判的是 nxt.next 是否为空，为空就把 node.next 置为 None。
