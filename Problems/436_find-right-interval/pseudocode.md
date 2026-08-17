# 436. 寻找右区间 · 解题思路与伪代码

1. 一句话直击本质：该算法的核心逻辑是通过对起始点进行排序并使用二分查找来快速找到每个区间的右区间。

2. 综合思路：
   - 排序与二分查找：所有版本都采用了先对区间的起始点进行排序，然后使用二分查找来寻找每个区间的右区间。
   - 二分查找的变体：不同版本在二分查找的实现上略有不同，但核心思想是相同的，即在排序后的数组中寻找第一个大于或等于目标值的起始点。

3. 全量伪代码：
   ```
   函数 findRightInterval(intervals):
       创建空数组 arr
       对于每个区间 i 从 0 到 intervals 的长度:
           将 (intervals[i][0], i) 添加到 arr
       按照第一个元素对 arr 进行排序
       创建结果数组 res
       对于每个区间 i 从 0 到 intervals 的长度:
           设 target 为 intervals[i][1]
           调用 binarySearch(arr, target) 并将结果添加到 res
       返回 res

   函数 binarySearch(arr, target):
       初始化 left 为 0, right 为 arr 的长度减 1
       初始化 ans 为 -1
       当 left 小于等于 right 时:
           计算 mid 为 left 和 right 的中间值
           设 start 为 arr[mid][0], idx 为 arr[mid][1]
           如果 start 大于等于 target:
               更新 ans 为 idx
               将 right 更新为 mid - 1
           否则:
               将 left 更新为 mid + 1
       返回 ans
   ```

4. 复杂度：
   - 时间复杂度：$O(n \log n)$，其中 $n$ 是区间的数量。排序的时间复杂度为 $O(n \log n)$，每次二分查找的时间复杂度为 $O(\log n)$，总共进行 $n$ 次二分查找。
   - 空间复杂度：$O(n)$，用于存储排序后的起始点和索引的数组。
