# 1083. 小于 K 的两数之和

**难度**: Easy | **标签**: `Array` `Two Pointers` `Binary Search` `Sorting`

## 题目描述

None

---
## 解题思路与复盘

1. **一句话直击本质：** 通过排序和双指针或二分查找，寻找小于目标值的最大两数之和。

2. **综合思路：**
   - **双指针法：** 先对数组进行排序，然后使用双指针从数组两端向中间移动，寻找满足条件的最大和。
   - **二分查找法：** 对于每个元素，使用二分查找寻找另一个元素，使得两数之和小于目标值。

3. **全量伪代码：**

   - **双指针法：**
     ```
     将数组排序
     初始化两个指针 left 和 right 分别指向数组的起始和末尾
     初始化 max_num 为 -1
     当 left 小于 right 时：
         计算当前和 sum_num = nums[left] + nums[right]
         如果 sum_num 大于等于 k：
             将 right 左移
         否则：
             更新 max_num 为 max(sum_num, max_num)
             将 left 右移
     返回 max_num
     ```

   - **二分查找法：**
     ```
     将数组排序
     初始化 max_res 为 -1
     对于每个元素 i 从 0 到 n-2：
         初始化 left 为 i+1，right 为 n-1
         当 left 小于等于 right 时：
             计算中间位置 mid
             计算当前和 curr = nums[i] + nums[mid]
             如果 curr 小于 k：
                 更新 max_res 为 max(curr, max_res)
                 将 left 移到 mid+1
             否则：
                 将 right 移到 mid-1
     返回 max_res
     ```

4. **复杂度：**

   - **时间复杂度：** $O(n \log n)$，由于需要对数组进行排序，之后的查找过程为 $O(n)$ 或 $O(n \log n)$。
   - **空间复杂度：** $O(1)$，除了输入和输出外，算法只使用了常数级别的额外空间。