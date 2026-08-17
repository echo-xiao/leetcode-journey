# 119. 杨辉三角 II · 解题思路与伪代码

1. 一句话直击本质：该算法通过递归计算上一行的杨辉三角值，并利用其生成当前行。

2. 综合思路：
   - 递归解法：通过递归调用计算前一行的值，然后根据杨辉三角的性质生成当前行。
   - 迭代解法（未在代码集中出现）：可以通过迭代逐行计算，避免递归的额外开销。

3. 全量伪代码：
   - 递归解法：
     ```
     定义函数 getRow(rowIndex):
         如果 rowIndex 等于 0:
             返回 [1]
         如果 rowIndex 等于 1:
             返回 [1, 1]
         
         lastRow = 调用 getRow(rowIndex - 1)
         newRow = 调用 newRow(lastRow)
         
         返回 newRow

     定义函数 newRow(lastRow):
         初始化 newRow 为 [1]
         对于 idx 从 0 到 len(lastRow) - 2:
             计算 num = lastRow[idx] + lastRow[idx + 1]
             将 num 添加到 newRow
         将 1 添加到 newRow
         返回 newRow
     ```

4. 复杂度：
   - 时间复杂度：递归解法的时间复杂度为 $O(n^2)$，因为每一行的生成需要遍历上一行的所有元素。
   - 空间复杂度：递归解法的空间复杂度为 $O(n)$，主要由于递归调用栈的深度为 $n$。
