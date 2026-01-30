# 294. 翻转游戏 II

**难度**: Medium | **标签**: `Math` `Dynamic Programming` `Backtracking` `Memoization` `Game Theory`

## 题目描述

None

---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过递归和记忆化搜索判断当前玩家是否能通过一次合法翻转操作使对手处于必败状态。

2. 综合思路：
   - 递归与记忆化搜索：通过递归遍历所有可能的翻转操作，并使用记忆化技术缓存已经计算过的状态结果，避免重复计算。
   - 纯递归：直接递归遍历所有可能的翻转操作，不使用记忆化技术，可能导致重复计算。

3. 全量伪代码：
   ```plaintext
   定义函数 canWin(currentState):
       初始化一个字典 memo 用于记忆化搜索

       定义递归函数 solve(s):
           如果 s 在 memo 中:
               返回 memo[s]

           遍历 s 中的每一个可能的翻转位置 i:
               如果 s[i:i+2] 是 "++":
                   生成新的状态 nxt = s[:i] + "--" + s[i+2:]
                   如果 solve(nxt) 返回 False:
                       记录 memo[s] = True
                       返回 True

           记录 memo[s] = False
           返回 False

       返回 solve(currentState)

   定义函数 canWin(currentState):
       遍历 currentState 中的每一个可能的翻转位置 i:
           如果 currentState[i:i+2] 是 "++":
               生成新的状态 nxt = currentState[:i] + "--" + currentState[i+2:]
               如果 canWin(nxt) 返回 False:
                   返回 True

       返回 False
   ```

4. 复杂度：
   - 时间复杂度：递归版本的时间复杂度为 $O(2^n)$，其中 $n$ 是字符串的长度，因为每个位置的翻转可能性是二叉树的分支。
   - 空间复杂度：使用记忆化搜索的版本空间复杂度为 $O(n)$，因为需要存储每个状态的计算结果。