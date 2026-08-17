# 33. 搜索旋转排序数组 · 要素

1. 区间定义：用两端都闭的写法，left=0，right=len(nums)-1，初始覆盖整个数组

2. while 条件：while用left<=right，因为闭区间里left==right时那个位置还没检查完

3. 判定条件：先判nums[mid]==target直接返回，再判nums[left]<=nums[mid]看左半是否有序，从而决定target落在左半还是右半有序区间里

4. 边界收缩：命中target直接返回mid；若左半[left,mid]有序且target在[nums[left],nums[mid])内则right=mid-1，否则left=mid+1；若右半有序且target在(nums[mid],nums[right]]内则left=mid+1，否则right=mid-1
