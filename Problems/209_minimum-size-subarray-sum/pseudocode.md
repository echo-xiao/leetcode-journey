# 209. 长度最小的子数组 · 解题思路与伪代码

1. 一句话直击本质：
   - 使用前缀和与二分查找或滑动窗口技术，找到满足条件的最短子数组长度。

2. 综合思路：
   - 前缀和与二分查找：通过计算前缀和数组，然后利用二分查找快速定位满足条件的子数组的右边界，从而确定最短长度。
   - 滑动窗口：通过动态调整窗口的左右边界，保持窗口内的和大于等于目标值，并在此过程中记录最短长度。

3. 全量伪代码：
   - 前缀和与二分查找：
     ```
     初始化前缀和数组 arr，长度为 n+1，初始值为 0
     对于每个元素 i 从 0 到 n-1：
         计算 arr[i+1] = arr[i] + nums[i]
     初始化最小长度 minLen 为无穷大
     对于每个起始位置 i 从 0 到 n-1：
         计算目标值 val = target + arr[i]
         初始化二分查找的左右边界 left = i+1, right = n
         初始化 bound = -1
         当 left <= right 时：
             计算中间位置 mid = left + (right - left) // 2
             如果 arr[mid] >= val：
                 更新 bound = mid
                 更新 right = mid - 1
             否则：
                 更新 left = mid + 1
         如果 bound != -1：
             更新 minLen = min(minLen, bound-i)
     如果 minLen == 无穷大：
         返回 0
     否则：
         返回 minLen
     ```

   - 滑动窗口：
     ```
     初始化左右指针 left = 0, right = 0
     初始化当前和 res = 0
     初始化最小长度 minLen 为无穷大
     当 right < 数组长度时：
         增加 res 为 nums[right]
         增加 right
         当 res >= target 时：
             更新 minLen = min(minLen, right-left)
             减少 res 为 nums[left]
             增加 left
     如果 minLen == 无穷大：
         返回 0
     否则：
         返回 minLen
     ```

4. 复杂度：
   - 前缀和与二分查找：
     - 时间复杂度：$O(n \log n)$，其中 $n$ 是数组的长度，前缀和计算为 $O(n)$，每次二分查找为 $O(\log n)$。
     - 空间复杂度：$O(n)$，用于存储前缀和数组。
   
   - 滑动窗口：
     - 时间复杂度：$O(n)$，每个元素最多被访问两次（一次作为右边界，一次作为左边界）。
     - 空间复杂度：$O(1)$，只使用了常数级别的额外空间。
