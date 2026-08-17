# 1764. 最大重复子字符串 · 解题思路与伪代码

1. 一句话直击本质：通过滑动窗口或递归方式，逐个检查子字符串是否与目标字符串匹配，并记录最大匹配次数。

2. 综合思路：
   - 递归解法：使用递归和记忆化搜索，从字符串的每个位置开始，递归地检查以该位置结尾的子字符串是否与目标字符串匹配，并记录匹配次数。
   - 迭代解法：使用双指针（滑动窗口）方法，从字符串的每个位置开始，逐个检查子字符串是否与目标字符串匹配，并记录最大匹配次数。

3. 全量伪代码：
   - 递归解法：
     ```
     定义函数 maxRepeating(sequence, word):
         初始化 n 为 sequence 的长度
         初始化 m 为 word 的长度
         初始化 memo 为一个空字典
         初始化 maxk 为 0

         对于 i 从 0 到 n-1:
             更新 maxk 为 max(maxk, 调用 recursion(i))

         返回 maxk

     定义递归函数 recursion(i):
         如果 i 小于 m-1:
             返回 0

         如果 i 在 memo 中:
             返回 memo[i]

         取 curr 为 sequence 从 i-m+1 到 i+1 的子字符串

         如果 curr 等于 word:
             结果 res 为 1 + 调用 recursion(i-m)
         否则:
             结果 res 为 0

         将 res 存入 memo[i]
         返回 res
     ```

   - 迭代解法：
     ```
     定义函数 maxRepeating(sequence, word):
         初始化 n 为 sequence 的长度
         初始化 m 为 word 的长度
         初始化 k 为 0

         初始化 left 为 0

         当 left 小于 n 时:
             初始化 curr 为 0
             初始化 right 为 left

             当 right + m 小于等于 n 时:
                 如果 sequence 从 right 到 right+m 的子字符串等于 word:
                     curr 增加 1
                     right 增加 m
                 否则:
                     退出循环

             更新 k 为 max(k, curr)
             left 增加 1

         返回 k
     ```

4. 复杂度：
   - 递归解法：
     - 时间复杂度：$O(n)$，因为每个位置最多被访问一次，且使用了记忆化。
     - 空间复杂度：$O(n)$，用于存储递归调用栈和记忆化字典。
   - 迭代解法：
     - 时间复杂度：$O(n \cdot m)$，因为每个起始位置最多需要检查 $m$ 个字符。
     - 空间复杂度：$O(1)$，只使用了常数级别的额外空间。
