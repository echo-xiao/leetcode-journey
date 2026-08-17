# 2469. 和有限的最长子序列 · 要素

1. 区间定义：在长度 n+1 的前缀和数组 pre 上二分（pre[0]=0 一定合法），搜索区间取两端都闭的 [1, n]，找最大的下标 k 使 pre[k] <= target，答案变量 ans 初始化为 0。

2. while 条件：用 while (left <= right)，因为区间两端都闭，left == right 时那个位置还没验证过，必须进循环判一次。

3. 判定条件：不是找等于 target，而是判单调条件 pre[mid] <= target（排序后前缀和递增，所以合法性是前面全真后面全假）。

4. 边界收缩：pre[mid] <= target 时说明 mid 个元素能选，记下 ans = mid 并把 left = mid + 1 继续往右找更长的；pre[mid] > target 时 right = mid - 1；不因为凑巧相等就提前返回，循环结束后把 ans 作为该查询的答案。
