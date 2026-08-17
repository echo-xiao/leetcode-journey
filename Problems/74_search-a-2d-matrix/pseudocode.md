# 74. 搜索二维矩阵 · 解题思路与伪代码

1. **一句话直击本质：** 将二维矩阵视为一维有序数组进行二分查找。

2. **综合思路：**
   - **二分查找法：** 所有版本都采用了二分查找的思路，将二维矩阵通过行列转换映射为一维数组的索引，进行标准的二分查找操作。
   - **数据结构：** 直接使用数组进行索引转换，没有使用其他复杂的数据结构。

3. **全量伪代码：**

   ```plaintext
   定义函数 searchMatrix(matrix, target):
       如果 matrix 为空:
           返回 False

       设定 m 为 matrix 的行数
       设定 n 为 matrix 的列数

       初始化 left 为 0
       初始化 right 为 m * n - 1

       当 left 小于等于 right 时:
           计算 mid 为 left 和 right 的中间索引
           计算 row 为 mid 除以 n 的商
           计算 col 为 mid 除以 n 的余数
           设定 midVal 为 matrix[row][col]

           如果 midVal 等于 target:
               返回 True
           否则如果 midVal 大于 target:
               将 right 设为 mid - 1
           否则:
               将 left 设为 mid + 1

       返回 False
   ```

4. **复杂度：**
   - **时间复杂度：** $O(\log(m \times n))$，其中 $m$ 是矩阵的行数，$n$ 是矩阵的列数，因为使用了二分查找。
   - **空间复杂度：** $O(1)$，因为只使用了常数空间来存储索引和中间变量。
