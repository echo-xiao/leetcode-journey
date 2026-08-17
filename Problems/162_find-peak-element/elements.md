# 162. 寻找峰值 · 要素

1. 区间定义：left=0、right=n-1，两端都闭，区间里始终保证至少存在一个峰值。

2. while 条件：用 left < right，不用 <=，因为区间缩到只剩一个元素时那个元素就是答案，不需要再判一次。

3. 判定条件：不是比 target，而是比较 nums[mid] 和 nums[mid+1]，看当前是在上坡还是下坡。

4. 边界收缩：nums[mid] >= nums[mid+1]（下坡）时 right = mid，保留 mid 自己；否则（上坡）left = mid + 1；没有"命中直接返回"这一支，循环结束后返回 left。
