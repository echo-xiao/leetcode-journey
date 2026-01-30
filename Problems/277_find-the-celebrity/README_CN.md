# 277. 搜寻名人

**难度**: Medium | **标签**: `Two Pointers` `Graph Theory` `Interactive`

## 题目描述

None

---
## 解题思路与复盘

1. 一句话直击本质：算法的核心逻辑是通过两次遍历确定唯一的候选者，并验证其是否为名人。

2. 综合思路：
   - **迭代法**：所有版本都使用了迭代法，通过两次遍历来确定名人。第一次遍历确定一个可能的候选者，第二次遍历验证该候选者是否满足名人的条件，即所有人都认识他且他不认识其他任何人。

3. 全量伪代码：
   ```plaintext
   定义函数 findCelebrity(n)
       初始化候选者 candidate 为 0
       对于 i 从 1 到 n-1:
           如果 candidate 知道 i:
               将 candidate 更新为 i
       
       对于 i 从 0 到 n-1:
           如果 i 等于 candidate:
               跳过当前循环
           
           如果 candidate 知道 i 或者 i 不知道 candidate:
               返回 -1
       
       返回 candidate
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，因为算法需要两次遍历每个人。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外变量。