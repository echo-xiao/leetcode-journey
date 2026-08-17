# 268. 丢失的数字 · 要素

1. 指针类型：这题用的是左右指针相向而行，也就是二分的 left 和 right，从数组两端往中间夹，找第一个 nums[mid] != mid 的位置

2. slow 含义：本题不涉及，这里没有快慢指针也不用往数组里写数据，只有二分的 left/right 边界

3. 停止条件：排序后的循环停在 left > right（即 right 越到 left 左边）时，此时 left 就是缺失的数字；递归版同样以 left > right 作为返回 left 的出口
