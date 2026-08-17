# 81. 搜索旋转排序数组 II · 要素

1. 区间定义：用两端都闭的区间[left, right]，left和right都是有效下标

2. while 条件：用left<=right，因为要遍历完所有可能才能确定没有该元素

3. 判定条件：先判断nums[mid]==target直接返回true；再判断nums[left]==nums[mid]时无法判断哪边有序就left+=1缩小重复；否则判断左半部分[nums[left],nums[mid])还是右半部分(nums[mid],nums[right]]是有序的，再看target是否落在有序那段里

4. 边界收缩：命中target直接返回true；如果左边有序且target在[nums[left],nums[mid])内则right=mid-1，否则left=mid+1；如果右边有序且target在(nums[mid],nums[right]]内则left=mid+1，否则right=mid-1；遇到nums[left]==nums[mid]时无法判断有序性就left+=1去重复元素
