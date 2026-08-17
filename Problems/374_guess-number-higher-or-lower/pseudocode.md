# 374. 猜数字大小 · 解题思路与伪代码

1. 一句话直击本质：该算法的核心逻辑是使用二分查找法来有效地缩小搜索范围，直到找到目标数字。

2. 综合思路：
   - 递归解法：通过递归调用函数来实现二分查找，每次根据 `guess` 函数的返回值调整搜索范围。
   - 迭代解法：使用一个循环来实现二分查找，通过调整左右边界来逐步缩小搜索范围，直到找到目标数字。

3. 全量伪代码：
   - 递归解法伪代码：
     ```
     定义函数 guessNumber(n):
         返回 helper(n, 1, n)

     定义函数 helper(n, left, right):
         计算 mid 为 left 和 right 的中间值
         如果 guess(mid) 返回 0:
             返回 mid
         如果 guess(mid) 返回 -1:
             返回 helper(n, left, mid-1)
         如果 guess(mid) 返回 1:
             返回 helper(n, mid+1, right)
     ```

   - 迭代解法伪代码：
     ```
     定义函数 guessNumber(n):
         初始化 left 为 1, right 为 n
         当 left 小于等于 right 时:
             计算 mid 为 left 和 right 的中间值
             如果 guess(mid) 返回 0:
                 返回 mid
             如果 guess(mid) 返回 -1:
                 将 right 更新为 mid - 1
             如果 guess(mid) 返回 1:
                 将 left 更新为 mid + 1
     ```

4. 复杂度：
   - 时间复杂度：$O(\log n)$，因为每次查找都将搜索范围缩小一半。
   - 空间复杂度：
     - 递归解法：$O(\log n)$，由于递归调用栈的深度。
     - 迭代解法：$O(1)$，因为只使用了有限的额外变量。
