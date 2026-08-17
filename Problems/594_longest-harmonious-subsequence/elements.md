# 594. 最长和谐子序列 · 要素

1. 定长还是变长：这题用排序+双指针法时窗口是变长的，窗口大小随nums[right]-nums[left]的值动态变化。

2. 进窗口更新：排序后right从0开始每次循环都右移，把nums[right]纳入窗口，不需要额外更新统计量，只看nums[right]和nums[left]的差值。

3. 出窗口时机：当nums[right]-nums[left]>1时说明窗口内最大最小差超过1，要移动left缩小窗口，直到差值回到1或0，出窗口时不需要更新其他数据，因为直接用两端下标做差判断。

4. 记结果时机：当nums[right]-nums[left]==1时说明窗口内是和谐子序列，此时用right-left+1更新最大长度max_length。
