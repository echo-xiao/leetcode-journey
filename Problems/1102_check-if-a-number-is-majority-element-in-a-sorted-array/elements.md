# 1102. 检查一个数是否在数组中占绝大多数 · 要素

1. 区间定义：用左闭右闭 [left, right]，找最后一个出现位置时 left 初始为 first（目标首次出现的下标），right 初始为 nums.length-1。

2. while 条件：用 while (left <= right)，两端都闭所以要让 left==right 这个单点也被检查到。

3. 判定条件：判定的是 nums[mid] 与 target 的大小关系，但命中 target 时不返回，而是把它当成「候选的最后位置」继续往右压。

4. 边界收缩：nums[mid] < target 时 left = mid+1；nums[mid] > target 时 right = mid-1；nums[mid] == target 时记下 last = mid 并 left = mid+1 继续右探，循环结束后用 last-first+1 和 n/2 比较得出答案。
