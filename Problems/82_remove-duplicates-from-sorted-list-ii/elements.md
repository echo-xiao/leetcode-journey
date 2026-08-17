# 82. 删除排序链表中的重复元素 II · 要素

1. 要不要 dummy：要dummy，因为头节点本身可能就是重复元素被删掉，用dummy.next连接prev可以统一处理头部被删的情况

2. 指针关系：这里不是快慢指针，而是prev和curr两个指针，prev始终指向最后一个确认不重复的节点，curr用来向前探测和当前节点值相同的重复节点

3. 停止条件：当curr为空或curr.next为空时停止外层遍历，内层跳过重复节点的循环在curr.next为空或curr.val不等于curr.next.val时停止
