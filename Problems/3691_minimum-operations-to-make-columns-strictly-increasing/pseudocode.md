# 3691. 使每一列严格递增的最少操作次数 · 解题思路与伪代码

1. 一句话直击本质：通过逐列检查并调整每列元素，使其严格递增，计算所需的最小操作次数。

2. 综合思路：
   - 迭代法：遍历每一列，将列中的元素提取为一维数组，然后通过线性扫描调整数组元素，使其严格递增，记录所需的调整次数。

3. 全量伪代码：
   ```
   定义函数 minimumOperations(grid):
       初始化总操作次数 ttl 为 0
       获取行数 rows 和列数 cols
       
       如果行数为 0:
           返回 0
       
       对于每一列 j 从 0 到 cols-1:
           初始化一个空数组 arr
           对于每一行 i 从 0 到 rows-1:
               将 grid[i][j] 添加到 arr 中
           计算调整 arr 为严格递增所需的操作次数 cal
           将 cal 添加到 ttl 中
       
       返回 ttl

   定义函数 cntOperation(nums):
       初始化操作次数 cnt 为 0
       对于每个元素 i 从 1 到 len(nums)-1:
           如果 nums[i-1] >= nums[i]:
               计算目标值 target 为 nums[i-1] + 1
               计算需要增加的值 needed 为 target - nums[i]
               增加 cnt 的值为 needed
               将 nums[i] 更新为 target
       返回 cnt
   ```

4. 复杂度：
   - 时间复杂度：$O(n \times m)$，其中 $n$ 是行数，$m$ 是列数，因为需要遍历每个元素。
   - 空间复杂度：$O(n)$，用于存储每列的元素。
