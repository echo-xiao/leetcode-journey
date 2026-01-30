# 259. 较小的三数之和

**难度**: Medium | **标签**: `Array` `Two Pointers` `Binary Search` `Sorting`

## 题目描述

None

---
## 解题思路与复盘

1. 一句话直击本质：通过排序和双指针技术，遍历数组并计算满足条件的三元组数量。

2. 综合思路：
   - 排序 + 双指针：首先对数组进行排序，然后固定一个数，使用双指针在剩余数组中寻找满足条件的两数之和。

3. 全量伪代码：
   ```
   函数 threeSumSmaller(数组 nums, 整数 target):
       对 nums 进行排序
       初始化计数器 res 为 0
       对于 i 从 0 到 len(nums) - 2:
           计算 targetSum = target - nums[i]
           初始化双指针 j = i + 1, k = len(nums) - 1
           当 j < k 时:
               如果 nums[j] + nums[k] >= targetSum:
                   将 k 左移一位
               否则:
                   将 res 增加 (k - j)
                   将 j 右移一位
       返回 res
   ```

4. 复杂度：
   - 时间复杂度：$O(n^2)$，其中 $n$ 是数组的长度，因为排序需要 $O(n \log n)$，而双指针遍历需要 $O(n^2)$。
   - 空间复杂度：$O(1)$，因为除了输入和输出外，算法只使用了常数空间。