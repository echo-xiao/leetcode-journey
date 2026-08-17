# 33. 搜索旋转排序数组 · 解题思路与伪代码

1. 一句话直击本质：利用二分查找法，通过判断中点与边界值的关系来确定目标值所在的有序区间。

2. 综合思路：
   - **版本 1 和 2**：先通过二分查找找到旋转数组的旋转点（即最小值位置），然后在确定的有序区间内再次使用二分查找寻找目标值。
   - **版本 3 和 4**：类似于版本 1 和 2，但在寻找旋转点时，直接通过比较中点与末尾元素的关系来确定旋转点。
   - **版本 5 到 9**：直接在一次二分查找过程中，通过判断中点与左右边界的关系来确定目标值所在的有序区间，并在该区间内继续二分查找。

3. 全量伪代码：
   - **寻找旋转点的二分查找**：
     ```
     定义函数 findPivotIndex(nums):
         初始化 left 为 0, right 为 len(nums) - 1
         当 left <= right 时:
             计算 mid 为 left + (right - left) // 2
             如果 nums[mid] > nums[right]:
                 left = mid + 1
             否则:
                 right = mid - 1
         返回 left
     ```
   - **在有序区间内进行二分查找**：
     ```
     定义函数 binarySearch(nums, left, right, target):
         当 left <= right 时:
             计算 mid 为 left + (right - left) // 2
             如果 nums[mid] == target:
                 返回 mid
             如果 nums[mid] < target:
                 left = mid + 1
             否则:
                 right = mid - 1
         返回 -1
     ```
   - **直接在旋转数组中进行二分查找**：
     ```
     定义函数 search(nums, target):
         初始化 left 为 0, right 为 len(nums) - 1
         当 left <= right 时:
             计算 mid 为 left + (right - left) // 2
             如果 nums[mid] == target:
                 返回 mid
             如果 nums[left] <= nums[mid]:
                 如果 nums[left] <= target < nums[mid]:
                     right = mid - 1
                 否则:
                     left = mid + 1
             否则:
                 如果 nums[mid] < target <= nums[right]:
                     left = mid + 1
                 否则:
                     right = mid - 1
         返回 -1
     ```

4. 复杂度：
   - 时间复杂度：$O(\log n)$，因为每次操作都将搜索空间减半。
   - 空间复杂度：$O(1)$，因为只使用了常数级别的额外空间。
