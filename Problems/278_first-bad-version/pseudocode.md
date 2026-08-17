# 278. 第一个错误的版本 · 解题思路与伪代码

1. 一句话直击本质：该算法的核心逻辑是使用二分查找法在版本序列中找到第一个错误的版本。

2. 综合思路：
   - 递归解法：通过递归调用辅助函数 `helper`，在每次调用中更新搜索区间的左右边界，直到找到第一个错误的版本。
   - 迭代解法：使用循环迭代的方式，在每次迭代中更新搜索区间的左右边界，直到找到第一个错误的版本。

3. 全量伪代码：
   - 递归解法：
     ```
     定义函数 firstBadVersion(n)
         返回 helper(n, 1, n)
     
     定义辅助函数 helper(n, left, right)
         计算 mid 为 left 和 right 的中间值
         
         如果 left 大于 right
             返回 left
         
         如果 mid 版本不是错误版本
             返回 helper(n, mid + 1, right)
         否则
             返回 helper(n, left, mid - 1)
     ```
   
   - 迭代解法：
     ```
     定义函数 firstBadVersion(n)
         初始化 left 为 1, right 为 n
         
         当 left 小于等于 right 时
             计算 mid 为 left 和 right 的中间值
             
             如果 mid 版本不是错误版本
                 更新 left 为 mid + 1
             否则
                 更新 right 为 mid - 1
         
         返回 left
     ```

4. 复杂度：
   - 时间复杂度：$O(\log n)$，因为每次检查都将搜索空间减半。
   - 空间复杂度：
     - 递归解法：$O(\log n)$，由于递归调用栈的深度。
     - 迭代解法：$O(1)$，因为只使用了常数级别的额外空间。
