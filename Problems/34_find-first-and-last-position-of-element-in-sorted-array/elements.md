# 34. 在排序数组中查找元素的第一个和最后一个位置 · 要素

1. 区间定义：用两端都闭的区间[left, right]，初始left=0，right=nums.length-1

2. while 条件：while用 left<=right，因为区间是闭区间，left>right时区间为空才停止

3. 判定条件：判定条件是 nums[mid] 与 target 的三种大小关系（等于、小于、大于），不是单调check函数

4. 边界收缩：nums[mid]<target时left=mid+1，nums[mid]>target时right=mid-1，nums[mid]==target时不直接返回，找左边界就收right=mid-1继续往左找，找右边界就收left=mid+1继续往右找，循环结束后再判断left或right位置是否等于target
