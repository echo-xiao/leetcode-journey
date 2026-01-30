# 1066. 不动点

**难度**: Easy | **标签**: `Array` `Binary Search`

## 题目描述

None

---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是寻找数组中第一个满足 `arr[i] == i` 的索引，使用二分查找或线性扫描来实现。

2. 综合思路：
   - **二分查找（递归）**：通过递归的方式进行二分查找，缩小搜索范围，寻找第一个不动点。
   - **二分查找（迭代）**：使用迭代的方式进行二分查找，逐步调整左右边界，寻找第一个不动点。
   - **线性扫描**：直接遍历数组，找到第一个满足条件的索引。

3. 全量伪代码：
   - **递归二分查找**：
     ```
     函数 fixedPoint(arr):
         返回 helper(arr, 0, len(arr) - 1)

     函数 helper(arr, left, right):
         如果 left > right:
             返回 -1
         mid = left + (right - left) // 2
         如果 arr[mid] == mid:
             idx = helper(arr, left, mid - 1)
             如果 idx != -1:
                 返回 idx
             否则:
                 返回 mid
         否则如果 arr[mid] > mid:
             返回 helper(arr, left, mid - 1)
         否则:
             返回 helper(arr, mid + 1, right)
     ```

   - **迭代二分查找**：
     ```
     函数 fixedPoint(arr):
         left, right = 0, len(arr) - 1
         res = -1
         当 left <= right:
             mid = left + (right - left) // 2
             如果 arr[mid] == mid:
                 res = mid
                 right = mid - 1
             否则如果 arr[mid] > mid:
                 right = mid - 1
             否则:
                 left = mid + 1
         返回 res
     ```

   - **线性扫描**：
     ```
     函数 fixedPoint(arr):
         对于 i 从 0 到 len(arr) - 1:
             如果 arr[i] == i:
                 返回 i
         返回 -1
     ```

4. 复杂度：
   - **递归二分查找**：时间复杂度 $O(\log n)$，空间复杂度 $O(\log n)$（递归栈）。
   - **迭代二分查找**：时间复杂度 $O(\log n)$，空间复杂度 $O(1)$。
   - **线性扫描**：时间复杂度 $O(n)$，空间复杂度 $O(1)$。