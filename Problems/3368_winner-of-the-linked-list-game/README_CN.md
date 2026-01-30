# 3368. 链表游戏的获胜者

**难度**: Easy | **标签**: `Linked List`

## 题目描述

None

---
## 解题思路与复盘

1. 一句话直击本质：算法通过遍历链表的相邻节点比较值大小，统计偶数和奇数位置的胜利次数来决定游戏的胜者。

2. 综合思路：
   - 迭代法：遍历链表，比较每对相邻节点的值，分别统计偶数和奇数位置的胜利次数，最后根据统计结果判断胜者。

3. 全量伪代码：
   ```
   定义函数 gameResult(head):
       如果 head 是空节点:
           返回 'Tie'
       
       初始化 curr 为 head
       初始化 even 和 odd 为 0

       当 curr 和 curr.next 都不是空节点时:
           如果 curr.val > curr.next.val:
               even 增加 1
           否则如果 curr.val < curr.next.val:
               odd 增加 1

           curr 移动到 curr.next.next

       如果 even > odd:
           返回 'Even'
       否则如果 even < odd:
           返回 'Odd'
       否则:
           返回 'Tie'
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是链表的节点数，因为每个节点最多被访问一次。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外变量。