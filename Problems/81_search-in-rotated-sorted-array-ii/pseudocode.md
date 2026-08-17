# 81. 搜索旋转排序数组 II · 解题思路与伪代码

1. **一句话直击本质：** 通过找到旋转点将数组分为两部分，然后在可能的部分进行二分查找，或者直接在旋转数组中进行调整后的二分查找。

2. **综合思路：**
   - **分段二分查找法：** 先通过二分法找到数组的旋转点（最小值），然后在旋转点的两侧分别进行标准的二分查找。
   - **调整后的二分查找法：** 直接在旋转数组上进行二分查找，通过判断中间值与左右边界的关系来调整搜索区间。

3. **全量伪代码：**

   - **分段二分查找法：**
     ```
     定义函数 search(nums, target):
         pivot = 找到旋转点(nums)
         在 [0, pivot-1] 区间进行二分查找(target)
         在 [pivot, len(nums)-1] 区间进行二分查找(target)
         返回是否找到 target

     定义函数 找到旋转点(nums):
         初始化 left = 0, right = len(nums) - 1
         当 left <= right 时:
             计算 mid = (left + right) // 2
             如果 nums[mid] > nums[right]:
                 left = mid + 1
             否则如果 nums[mid] < nums[right]:
                 right = mid
             否则:
                 如果 right > 0 且 nums[right] < nums[right - 1]:
                     返回 right
                 right -= 1
         返回 0

     定义函数 二分查找(nums, left, right, target):
         当 left <= right 时:
             计算 mid = (left + right) // 2
             如果 nums[mid] == target:
                 返回 True
             否则如果 nums[mid] < target:
                 left = mid + 1
             否则:
                 right = mid - 1
         返回 False
     ```

   - **调整后的二分查找法：**
     ```
     定义函数 search(nums, target):
         初始化 left = 0, right = len(nums) - 1
         当 left <= right 时:
             计算 mid = (left + right) // 2
             如果 nums[mid] == target:
                 返回 True
             如果 nums[left] == nums[mid]:
                 left += 1
             否则如果 nums[left] < nums[mid]:
                 如果 nums[left] <= target < nums[mid]:
                     right = mid - 1
                 否则:
                     left = mid + 1
             否则:
                 如果 nums[mid] < target <= nums[right]:
                     left = mid + 1
                 否则:
                     right = mid - 1
         返回 False
     ```

4. **复杂度：**
   - **时间复杂度：** $O(n)$，在最坏情况下，例如数组中有大量重复元素时，可能需要线性扫描。
   - **空间复杂度：** $O(1)$，只使用了常数级别的额外空间。
