# 154. 寻找旋转排序数组中的最小值 II · 要素

1. 区间定义：[left, right] 两端都闭，left=0、right=n-1，最小值始终在这个闭区间里。

2. while 条件：用 while (left < right)，收缩到只剩一个元素时它就是最小值，不能用 <= 否则死循环。

3. 判定条件：不是找 target，而是拿 nums[mid] 跟右端点 nums[right] 比，判断 mid 落在哪一段。

4. 边界收缩：nums[mid] > nums[right] 说明最小值在右半，left = mid+1；nums[mid] < nums[right] 说明 mid 可能就是最小值，right = mid；相等时无法判断，只能 right-- 丢掉一个重复的右端点；全程不提前返回，最后返回 nums[left]。
