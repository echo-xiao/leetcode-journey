# 291. 单词规律 II

**难度**: Medium | **标签**: `Hash Table` `String` `Backtracking`

## 题目描述

None

---
## 解题思路与复盘

1. 一句话直击本质：该算法通过递归回溯的方法尝试为模式中的每个字符分配唯一的字符串子串，并检查是否能匹配整个输入字符串。

2. 综合思路：
   - 递归回溯：对于模式中的每个字符，尝试将其映射到字符串中的一个子串，并递归检查剩余部分是否匹配；如果当前映射不成功，则回溯并尝试其他可能的映射。
   - 数据结构：使用字典和集合来分别记录字符到字符串的映射关系和已使用的字符串子串，确保每个字符映射到唯一的子串。

3. 全量伪代码：
   ```
   定义函数 wordPatternMatch(pattern, s):
       初始化字典 charToStr 为空
       初始化集合 usedStrs 为空
       返回 isMatch(pattern, 0, s, 0)

   定义函数 isMatch(pattern, pidx, s, sidx):
       如果 pidx 等于 pattern 的长度:
           返回 sidx 等于 s 的长度

       取出 pattern 中的当前字符 char

       如果 char 在 charToStr 中:
           取出 char 对应的目标字符串 target
           如果 s 从 sidx 开始不以 target 开头:
               返回 False
           递归调用 isMatch(pattern, pidx+1, s, sidx+len(target))

       对于 end 从 sidx+1 到 len(s)+1:
           取出 s 的子串 sub 从 sidx 到 end

           如果 sub 在 usedStrs 中:
               跳过当前循环

           将 char 映射到 sub
           将 sub 添加到 usedStrs

           如果递归调用 isMatch(pattern, pidx+1, s, end) 返回 True:
               返回 True

           删除 char 的映射
           从 usedStrs 中移除 sub

       返回 False
   ```

4. 复杂度：
   - 时间复杂度：$O(n^m)$，其中 $n$ 是字符串 $s$ 的长度，$m$ 是模式 $pattern$ 的长度。最坏情况下，每个字符可能尝试匹配多个子串。
   - 空间复杂度：$O(m + n)$，用于存储字符到字符串的映射和已使用的字符串子串。