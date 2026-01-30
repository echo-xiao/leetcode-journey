# 3343. 统计各位数字都不同的数字个数 II

**难度**: Easy | **标签**: `Hash Table` `Math` `Dynamic Programming`

## 题目描述

None

---
## 解题思路与复盘

1. 一句话直击本质：通过递归和记忆化搜索（版本1）或直接枚举（版本2）来统计在给定范围内各位数字都不同的数字个数。

2. 综合思路：
   - 版本1使用递归和记忆化搜索（DFS）来构建数字，利用位掩码记录已使用的数字，并通过限制条件（isTight和isLeadingZero）来优化搜索空间。
   - 版本2采用简单的迭代方法，直接枚举范围内的每个数字，检查其各位数字是否不同。

3. 全量伪代码：
   - 版本1（递归+记忆化搜索）：
     ```
     定义函数 numberCount(a, b):
         初始化字符串 s, 长度 L, 记忆化字典 memo
         返回 solve(b) - solve(a - 1)

     定义函数 solve(n):
         将 n 转换为字符串 s
         设置 L 为 s 的长度
         清空 memo
         返回 dfs(0, 0, True, True) - 1

     定义函数 dfs(index, mask, isTight, isLeadingZero):
         如果 index 等于 L:
             返回 1
         如果不是 isTight 且不是 isLeadingZero 且 (index, mask) 在 memo 中:
             返回 memo[(index, mask)]
         初始化计数器 count 为 0
         设定 upper_bound 为 s[index] 的整数值如果 isTight 否则为 9
         对于 d 从 0 到 upper_bound:
             如果 isLeadingZero 且 d 为 0:
                 递归调用 dfs(index + 1, mask, isTight 且 (d == upper_bound), True)
             否则如果 mask 中没有 d:
                 递归调用 dfs(index + 1, mask | (1 << d), isTight 且 (d == upper_bound), False)
         如果不是 isTight 且不是 isLeadingZero:
             将 count 存入 memo[(index, mask)]
         返回 count
     ```

   - 版本2（直接枚举）：
     ```
     定义函数 numberCount(a, b):
         初始化计数器 cnt 为 0
         对于 i 从 a 到 b:
             将 i 转换为字符串 num
             如果 num 的长度等于 num 转换为集合后的长度:
                 增加 cnt
         返回 cnt
     ```

4. 复杂度：
   - 版本1的时间复杂度为 $O(10^d \cdot d)$，其中 $d$ 是数字的位数，因为每个位最多有10种选择，且使用记忆化减少重复计算。空间复杂度为 $O(d \cdot 2^{10})$，用于存储记忆化状态。
   - 版本2的时间复杂度为 $O(n \cdot d)$，其中 $n$ 是范围的大小，$d$ 是数字的位数，因为需要检查每个数字的各位。空间复杂度为 $O(d)$，用于存储数字的字符串表示和集合。