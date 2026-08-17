# 141. 环形链表 · 要素

1. 要不要 dummy：不用 dummy，本题只判断有没有环、不新建也不改动链表，slow 和 fast 都直接从 head 出发即可

2. 指针关系：速度差：slow 每次走 1 步（slow = slow.next），fast 每次走 2 步（fast = fast.next.next），有环时 fast 每轮相对 slow 靠近 1 步，必定追上

3. 停止条件：while fast 且 fast.next 都不为空才继续走（走两步要保证这两个都在），一旦 fast 或 fast.next 为 null 说明到头无环返回 False；循环里 slow == fast 就返回 True
