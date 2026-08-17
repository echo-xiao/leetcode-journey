# 2210. 找出数组排序后的目标下标 · 解题思路与伪代码

1. **一句话直击本质：** 通过对数组进行排序后，使用二分查找或线性扫描来找到目标值的起始下标，并收集所有目标值的下标。

2. **综合思路：**
   - **二分查找法：** 先对数组进行排序，然后使用二分查找找到目标值的起始下标，再通过线性扫描收集所有目标值的下标。
   - **线性扫描法：** 先对数组进行排序，然后直接通过线性扫描找到所有目标值的下标。

3. **全量伪代码：**

   - **排序数组：**
     ```
     对数组 nums 进行排序
     ```

   - **二分查找法：**
     ```
     初始化 left 为 0，right 为数组长度减 1
     当 left 小于等于 right 时：
         计算 mid 为 left 和 right 的中间索引
         如果 nums[mid] 大于等于 target：
             将 right 更新为 mid - 1
         否则：
             将 left 更新为 mid + 1
     初始化结果列表 res
     当 left 小于数组长度且 nums[left] 等于 target 时：
         将 left 添加到 res
         将 left 增加 1
     返回 res
     ```

   - **递归二分查找法：**
     ```
     定义递归函数 helper(nums, target, left, right):
         如果 left 大于 right：
             返回 left
         计算 mid 为 left 和 right 的中间索引
         如果 nums[mid] 大于等于 target：
             返回 helper(nums, target, left, mid-1)
         否则：
             返回 helper(nums, target, mid+1, right)
     调用 helper 函数获取目标值的起始下标
     初始化结果列表 res
     当 left 小于数组长度且 nums[left] 等于 target 时：
         将 left 添加到 res
         将 left 增加 1
     返回 res
     ```

   - **线性扫描法：**
     ```
     初始化结果列表 res
     初始化索引 i 为 0
     当 i 小于数组长度时：
         如果 nums[i] 等于 target：
             将 i 添加到 res
             将 i 增加 1
         如果 nums[i] 大于 target：
             终止循环
         如果 nums[i] 小于 target：
             将 i 增加 1
     返回 res
     ```

4. **复杂度：**

   - **时间复杂度：** $O(n \log n)$，其中 $n$ 是数组的长度，因为需要对数组进行排序。
   - **空间复杂度：** $O(1)$，如果不考虑排序所需的额外空间，或者 $O(n)$，如果排序算法需要额外的空间。
