# 378. 有序矩阵中第 K 小的元素 · 解题思路与伪代码

1. 一句话直击本质：
   - 该算法的核心逻辑是利用二分查找结合计数方法，在有序矩阵中确定第 K 小的元素。

2. 综合思路：
   - 二分查找法：通过在矩阵的最小值和最大值之间进行二分查找，逐步缩小范围，利用计数函数确定当前中间值在矩阵中的排名，调整搜索区间，直到找到第 K 小的元素。

3. 全量伪代码：
   ```plaintext
   定义函数 kthSmallest(matrix, k):
       初始化 left 为矩阵的第一个元素
       初始化 right 为矩阵的最后一个元素

       当 left 小于 right 时:
           计算 mid 为 left 和 right 的中间值
           调用辅助函数 cntElement(matrix, mid) 或 countLessEqual(matrix, mid) 计算小于等于 mid 的元素个数 cnt

           如果 cnt 小于 k:
               更新 left 为 mid + 1
           否则:
               更新 right 为 mid

       返回 left

   定义辅助函数 cntElement(matrix, mid) 或 countLessEqual(matrix, mid):
       初始化 row 为矩阵的最后一行
       初始化 col 为矩阵的第一列
       初始化计数器 cnt 为 0

       当 row 大于等于 0 且 col 小于矩阵的列数时:
           如果 matrix[row][col] 小于等于 mid:
               将 cnt 增加 row + 1
               增加 col
           否则:
               减少 row

       返回 cnt
   ```

4. 复杂度：
   - 时间复杂度：$O(n \log (max - min))$，其中 $n$ 是矩阵的维度，$max$ 和 $min$ 分别是矩阵中的最大值和最小值。
   - 空间复杂度：$O(1)$，因为只使用了常数级别的额外空间。
