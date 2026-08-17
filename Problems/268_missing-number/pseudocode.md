# 268. 丢失的数字 · 解题思路与伪代码

1. 一句话直击本质：利用排序后的数组，通过二分查找法找到第一个索引与元素不匹配的位置，即为丢失的数字。

2. 综合思路：
   - 递归二分查找：通过递归的方式实现二分查找，逐步缩小查找范围，直到找到丢失的数字。
   - 迭代二分查找：通过迭代的方式实现二分查找，使用循环来调整查找范围，最终找到丢失的数字。

3. 全量伪代码：
   - 递归二分查找：
     ```
     函数 missingNumber(nums):
         对 nums 进行排序
         返回 helper(nums, 0, len(nums) - 1)

     函数 helper(nums, left, right):
         如果 left > right:
             返回 left
         计算 mid = left + (right - left) // 2
         如果 nums[mid] == mid:
             返回 helper(nums, mid + 1, right)
         否则如果 nums[mid] > mid:
             返回 helper(nums, left, mid - 1)
     ```
   - 迭代二分查找：
     ```
     函数 missingNumber(nums):
         对 nums 进行排序
         初始化 left = 0, right = len(nums) - 1
         当 left <= right 时:
             计算 mid = left + (right - left) // 2
             如果 nums[mid] == mid:
                 更新 left = mid + 1
             否则如果 nums[mid] > mid:
                 更新 right = mid - 1
         返回 left
     ```

4. 复杂度：
   - 时间复杂度：$O(n \log n)$，由于需要对数组进行排序，排序的时间复杂度为 $O(n \log n)$，二分查找的时间复杂度为 $O(\log n)$，但排序是主要的时间消耗。
   - 空间复杂度：$O(1)$，不考虑排序所需的额外空间，递归版本的空间复杂度为 $O(\log n)$，因为递归调用栈的深度为 $O(\log n)$。
