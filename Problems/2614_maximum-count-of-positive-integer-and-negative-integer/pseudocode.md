# 2614. 正整数和负整数的最大计数 · 解题思路与伪代码

1. 一句话直击本质：该算法的核心逻辑是通过二分查找找到第一个非负数的位置，然后计算负数和正数的数量，返回两者中的最大值。

2. 综合思路：
   - 二分查找：所有版本都使用了二分查找来定位第一个非负数的位置。版本 1 使用递归实现二分查找，而版本 2 和版本 3 使用迭代实现。
   - 计数计算：在找到第一个非负数的位置后，通过简单的计数计算负数和正数的数量。

3. 全量伪代码：
   ```plaintext
   方法 maximumCount(nums):
       初始化 left 为 0, right 为 nums 的长度减 1
       当 left 小于等于 right 时:
           计算 mid 为 left 和 right 的中间索引
           如果 nums[mid] 大于等于 0:
               将 right 更新为 mid 减 1
           否则:
               将 left 更新为 mid 加 1

       计算 neg 为从索引 0 到 left 的元素数量
       当 left 小于 nums 的长度且 nums[left] 小于等于 0 时:
           增加 left
       计算 pos 为从 left 到 nums 末尾的元素数量

       返回 neg 和 pos 中的最大值

   方法 helper(nums, left, right):
       如果 left 大于 right:
           返回 left

       计算 mid 为 left 和 right 的中间索引
       如果 nums[mid] 大于等于 0:
           返回 helper(nums, left, mid-1)
       否则:
           返回 helper(nums, mid+1, right)
   ```

4. 复杂度：
   - 时间复杂度：$O(\log n)$，因为二分查找的时间复杂度为 $O(\log n)$，后续的计数操作为线性时间复杂度 $O(n)$，但由于二分查找是主导操作，所以整体复杂度为 $O(\log n)$。
   - 空间复杂度：$O(1)$，因为只使用了常数级别的额外空间。
