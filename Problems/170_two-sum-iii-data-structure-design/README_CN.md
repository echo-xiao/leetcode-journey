# 170. 两数之和 III - 数据结构设计

**难度**: Easy | **标签**: `Array` `Hash Table` `Two Pointers` `Design` `Data Stream`

## 题目描述

None

---
## 解题思路与复盘

1. 一句话直击本质：使用哈希表存储每个数字的出现次数，通过遍历检查是否存在两个数之和等于目标值。

2. 综合思路：
   - 哈希表法：利用哈希表存储每个数字的出现次数，`add` 操作将数字加入哈希表，`find` 操作通过遍历哈希表检查是否存在两个数之和等于目标值。
   - 该题目主要有一个实现思路，即使用哈希表来高效地进行查找和存储操作。

3. 全量伪代码：
   ```plaintext
   类 TwoSum:
       初始化:
           创建一个空的哈希表 counts

       方法 add(数字 number):
           如果 number 在 counts 中:
               将 counts[number] 增加 1
           否则:
               将 counts[number] 设为 1

       方法 find(值 value):
           对于 counts 中的每个数字 num:
               计算差值 diff = value - num
               如果 diff 在 counts 中:
                   如果 diff 不等于 num:
                       返回 True
                   否则如果 counts[num] >= 2:
                       返回 True
           返回 False
   ```

4. 复杂度：
   - 时间复杂度：`add` 操作的时间复杂度为 $O(1)$，`find` 操作的时间复杂度为 $O(n)$，其中 $n$ 是哈希表中的不同数字个数。
   - 空间复杂度：空间复杂度为 $O(n)$，其中 $n$ 是哈希表中存储的不同数字个数。