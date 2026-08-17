# 792. 二分查找 · 解题思路与伪代码

1. 一句话直击本质：
   - 二分查找的核心逻辑是通过不断将搜索范围缩小一半来高效地查找有序数组中的目标元素。

2. 综合思路：
   - 递归解法：通过递归函数不断缩小搜索范围，直到找到目标元素或搜索范围为空。
   - 迭代解法：使用循环来调整搜索范围的边界，直到找到目标元素或搜索范围为空。

3. 全量伪代码：
   - 递归版本：
     ```
     函数 search(nums, target):
         返回 helper(nums, target, 0, len(nums) - 1)

     函数 helper(nums, target, left, right):
         如果 left > right:
             返回 -1
         mid = left + (right - left) // 2
         如果 nums[mid] == target:
             返回 mid
         否则如果 nums[mid] > target:
             返回 helper(nums, target, left, mid - 1)
         否则:
             返回 helper(nums, target, mid + 1, right)
     ```

   - 迭代版本：
     ```
     函数 search(nums, target):
         left = 0
         right = len(nums) - 1
         当 left <= right 时:
             mid = left + (right - left) // 2
             如果 nums[mid] == target:
                 返回 mid
             否则如果 nums[mid] > target:
                 right = mid - 1
             否则:
                 left = mid + 1
         返回 -1
     ```

4. 复杂度：
   - 时间复杂度：$O(\log n)$，因为每次操作将搜索范围缩小一半。
   - 空间复杂度：递归版本为 $O(\log n)$（由于递归栈），迭代版本为 $O(1)$。
