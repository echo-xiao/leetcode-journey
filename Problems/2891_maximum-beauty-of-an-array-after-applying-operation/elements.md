# 2891. 数组的最大美丽值 · 要素

1. 定长还是变长：变长窗口：先把数组排序，right不断右移扩展窗口，只有当窗口内nums[right]-nums[left]>2k时才收缩left，窗口大小不固定。

2. 进窗口更新：right每次遍历时自动加入nums[right]，不需要额外更新其他数据，因为排序后只需比较当前右端点和左端点的值。

3. 出窗口时机：当nums[right]-nums[left]>2k时，说明窗口内最大值和最小值差太大，就把left右移，直到差值不超过2k为止，移出元素时也不需要额外维护数据，只是让left指针前移。

4. 记结果时机：每次right移动确定窗口合法后（即nums[right]-nums[left]<=2k），就用right-left+1更新一次最大长度maxlen。
