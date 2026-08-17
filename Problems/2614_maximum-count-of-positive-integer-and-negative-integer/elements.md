# 2614. 正整数和负整数的最大计数 · 要素

1. 区间定义：用 left=0、right=nums.length-1 的两端都闭区间，找第一个 >=0 的下标。

2. while 条件：用 while (left <= right)，循环结束时 left 正好停在第一个非负数的位置。

3. 判定条件：不是找等于 target，而是 check：nums[mid] >= 0 就算「满足」，往左继续找更早的满足位置。

4. 边界收缩：nums[mid] >= 0 时不返回、令 right = mid - 1 继续往左找边界；nums[mid] < 0 时 left = mid + 1；循环退出后 left 就是第一个非负数下标，负数个数 = left，再把 left 跳过所有 0（nums[left] <= 0 时 left++），正数个数 = n - left，取两者较大值。
