# 3359. 链表频率

**难度**: Easy | **标签**: `Hash Table` `Linked List` `Counting`

## 题目描述

None

---
## 解题思路与复盘

1. 一句话直击本质：遍历链表并使用哈希表记录每个元素的频率，然后构建一个新的链表来存储这些频率。

2. 综合思路：
   - 迭代法：通过迭代遍历链表，使用字典（哈希表）记录每个节点值出现的次数，然后再通过这些频率构建新的链表。

3. 全量伪代码：
   ```plaintext
   定义一个函数 frequenciesOfElements，输入为链表头节点 head
       初始化一个空字典 tmp 用于存储元素频率
       初始化 curr 指向 head

       当 curr 不为空时，重复以下步骤：
           如果 curr.val 不在 tmp 中：
               将 curr.val 作为键，1 作为值存入 tmp
           否则：
               将 curr.val 对应的值加 1
           将 curr 移动到下一个节点

       创建一个虚拟头节点 dummy
       初始化 curr 指向 dummy

       对于 tmp 中的每个频率值：
           创建一个新节点 new_node，其值为频率值
           将 curr.next 指向 new_node
           将 curr 移动到 curr.next

       返回 dummy.next 作为结果链表的头节点
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是链表的节点数，因为需要遍历链表两次：一次用于记录频率，一次用于构建结果链表。
   - 空间复杂度：$O(n)$，因为需要存储链表中每个不同元素的频率。