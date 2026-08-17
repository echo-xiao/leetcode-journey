# 792. 二分查找 · 要素

1. 区间定义：用左右两端都闭区间[left, right]，初始left=0，right=len(nums)-1

2. while 条件：用left<=right，因为闭区间里left==right时那个位置还没检查，必须再循环一次

3. 判定条件：判定条件就是nums[mid]是否等于target，这是单点查找不是找边界

4. 边界收缩：nums[mid]==target时直接返回mid；nums[mid]>target时right=mid-1；nums[mid]<target时left=mid+1，循环结束还没找到就返回-1
