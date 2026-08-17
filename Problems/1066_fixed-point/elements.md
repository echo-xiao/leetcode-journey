# 1066. 不动点 · 要素

1. 区间定义：用 left=0、right=len(arr)-1 的两端都闭区间，整个数组都是候选下标。

2. while 条件：用 left <= right，因为区间右端闭，left==right 时那个下标还没检查过。

3. 判定条件：比较 arr[mid] 和 mid 本身：相等就是不动点，arr[mid] > mid 说明不动点只可能在左边，arr[mid] < mid 说明只可能在右边（严格递增数组里 arr[i]-i 单调不减）。

4. 边界收缩：arr[mid]==mid 时不立刻返回，先记 res=mid 再让 right=mid-1 继续往左找更小的不动点；arr[mid]>mid 时 right=mid-1；arr[mid]<mid 时 left=mid+1；循环结束返回 res，没找到就是 -1。
