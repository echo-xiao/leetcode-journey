# 86. 分隔链表 · 要素

1. 要不要 dummy：要，本题用了两个dummy节点lessDummy和greaterDummy分别构建小于x和大于等于x的两条新链表，最后拼接，避免处理头节点特殊情况

2. 指针关系：本题不涉及快慢指针的步数/速度关系，只用less和greater两个指针各自在自己的链表末尾追加节点

3. 停止条件：停止条件是curr遍历到原链表末尾（curr为null），然后把less的next接到greaterDummy.next完成合并
