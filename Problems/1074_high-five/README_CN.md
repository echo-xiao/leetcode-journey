# 1074. 前五科的均分

**难度**: Easy | **标签**: `Array` `Hash Table` `Sorting` `Heap (Priority Queue)`

## 题目描述

None

---
## 解题思路与复盘

1. 一句话直击本质：使用最小堆维护每个学生的最高五个成绩，并计算其平均值。

2. 综合思路：
   - 使用最小堆：对于每个学生，使用一个大小为5的最小堆来存储最高的五个成绩。遍历所有成绩时，如果当前成绩大于堆顶且堆已满，则替换堆顶元素。
   - 排序与遍历：对最终结果进行排序，以确保学生的成绩按照学生ID的顺序输出。

3. 全量伪代码：
   ```plaintext
   初始化一个字典 students 用于存储每个学生的成绩堆
   遍历 items 中的每个 (idx, score):
       如果 idx 不在 students 中:
           初始化 students[idx] 为一个空列表
       获取 students[idx] 对应的最小堆 heap
       如果 heap 的长度小于 5:
           将 score 插入到 heap 中
       否则如果 score 大于 heap 的最小值:
           将 heap 的最小值替换为 score
   初始化结果列表 res
   遍历 students 中的每个 (idx, heap):
       计算 heap 的平均值 avg
       将 [idx, avg] 添加到 res 中
   对 res 按照学生 ID 进行排序
   返回 res
   ```

4. 复杂度：
   - 时间复杂度：$O(n \log k)$，其中 $n$ 是成绩的总数，$k$ 是堆的大小（固定为5）。
   - 空间复杂度：$O(m \cdot k)$，其中 $m$ 是学生的数量，$k$ 是堆的大小（固定为5）。