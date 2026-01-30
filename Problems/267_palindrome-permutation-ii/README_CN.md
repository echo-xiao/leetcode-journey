# 267. 回文排列 II

**难度**: Medium | **标签**: `Hash Table` `String` `Backtracking`

## 题目描述

None

---
## 解题思路与复盘

1. 一句话直击本质：通过统计字符频率，构造半个回文字符串并使用深度优先搜索（DFS）生成所有可能的回文排列。

2. 综合思路：
   - **递归与DFS**：两个版本都采用了递归和DFS的方式来生成回文排列。首先统计字符串中每个字符的频率，判断是否可以形成回文，然后通过DFS构造半个回文字符串的所有排列，最后拼接成完整的回文。
   - **数据结构**：使用字典（或Counter）统计字符频率，列表存储半个回文字符串，布尔数组用于标记DFS中的字符使用状态。

3. 全量伪代码：
   ```plaintext
   定义函数 generatePalindromes(s):
       统计字符串 s 中每个字符的频率
       初始化中间字符 mid 为 ""
       初始化半个回文字符串的字符列表 half 为 []
       初始化奇数频率字符计数 oddCnt 为 0

       遍历字符频率字典:
           如果字符频率为奇数:
               增加 oddCnt
               将字符设为 mid
               如果 oddCnt 大于 1:
                   返回空列表

           将字符的频率整除 2 的结果加入 half

       对 half 进行排序
       初始化结果列表 res 为 []
       初始化使用状态列表 used 为 [False] * len(half)

       调用 dfs(half, used, [], mid, res)
       返回 res

   定义函数 dfs(nums, used, path, mid, res):
       如果 path 的长度等于 nums 的长度:
           构造左半部分字符串 left
           将 left + mid + left[::-1] 加入 res
           返回

       遍历 nums 的每个索引 i:
           如果 used[i] 为 True:
               跳过

           如果 i > 0 且 nums[i] 等于 nums[i-1] 且 used[i-1] 为 False:
               跳过

           将 used[i] 设为 True
           将 nums[i] 加入 path
           递归调用 dfs(nums, used, path, mid, res)
           从 path 中移除最后一个元素
           将 used[i] 设为 False
   ```

4. 复杂度：
   - 时间复杂度：$O(n \cdot n!)$，其中 $n$ 是字符串的一半长度，因为需要生成半个字符串的所有排列。
   - 空间复杂度：$O(n)$，用于存储字符频率、半个字符串和递归调用栈。