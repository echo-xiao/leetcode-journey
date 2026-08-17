# 153. 寻找旋转排序数组中的最小值 · 复盘

其实有两个逻辑，一个是nums[mid]跟nums[left]进行比较，一个是nums[mid]跟nums[right]进行比较。如果是跟nums[right]进行比较的话，**三个问题，1. 为什么left≤right**，这个里面right=mid，所以最终停止的时候是left=right，这个取决于left和right是如何移动的。**2. 为什么要跟nums[right]进行比较**，因为要判断最小值是在mid的左边还是有变，如果nums[mid]<nums[right]，这个的目的是判断悬崖点在哪边，如果<的话，说明右边一定是递增的，**3. 为什么right=mid**，nums[mid]肯定是这段里面最小的，但是不一定是整个arr里面最小的。
