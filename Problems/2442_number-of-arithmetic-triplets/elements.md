# 2442. 等差三元组的数目 · 要素

1. 指针类型：用同向的三指针（都从左往右走、不回头）：i 枚举最小元素，j 追 nums[i]+diff，k 追 nums[i]+2*diff；因为数组严格递增，不需要相向的左右指针

2. slow 含义：本题没有「待写入位置」的含义，慢的那个是枚举三元组最小值的 i，而 j、k 是各自单调右移的指针，分别停在第一个 ≥ nums[i]+diff 和第一个 ≥ nums[i]+2*diff 的下标

3. 停止条件：j、k 只在 nums[j] < nums[i]+diff、nums[k] < nums[i]+2*diff 时右移，一旦越界就结束：k>=n 直接 break（i 再大也没救），j>=n 或 nums[j] > nums[i]+diff 则 continue 换下一个 i；外层 i 遍历到 n-2 结束
