# 1646. 第 k 个缺失的正整数 · 要素

1. 区间定义：left=0、right=n-1，两端都闭，找的是第一个「缺失个数≥k」的下标。

2. while 条件：用 while(left<=right)，退出时 left 正好是第一个缺失数不少于 k 的位置，也就是前面完整满足 cnt<k 的元素个数。

3. 判定条件：不是比 target，而是算 cnt = arr[mid]-(mid+1)（前 mid+1 个数前面缺了多少个），判断 cnt < k 是否成立。

4. 边界收缩：cnt<k 时 left=mid+1；cnt>=k 时 right=mid-1，中间命中也不提前返回，一直缩到 left 为分界点，最后返回 left+k。
