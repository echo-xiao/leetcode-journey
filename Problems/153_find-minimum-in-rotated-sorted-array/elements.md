# 153. 寻找旋转排序数组中的最小值 · 要素

1. 区间定义：两端都闭 [left, right]，left=0、right=nums.length-1，最小值始终被夹在这个区间里，right 本身也是候选答案不能排除。

2. while 条件：用 left < right（区间只剩一个元素时它就是最小值，直接返回 nums[left]）；如果按伪代码写 <=，就必须靠 nums[mid]==nums[right] 时 return 或收缩来跳出，容易死循环。

3. 判定条件：不是找等于某个 target，而是拿 nums[mid] 和右端 nums[right] 比大小：mid 比右端小说明 mid 落在后半段（含最小值的那段），mid 比右端大说明最小值在 mid 右边。

4. 边界收缩：nums[mid] < nums[right] 时 right = mid（mid 可能就是最小值，不能跳过）；nums[mid] > nums[right] 时 left = mid + 1（mid 肯定不是最小值）；相等（有重复元素时）就 right -= 1 保守缩一格，本题无重复所以不会出现，全程不提前返回，循环结束后返回 nums[left]。
