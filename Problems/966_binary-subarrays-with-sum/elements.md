# 966. 和相同的二元子数组 · 要素

1. 定长还是变长：变长窗口，因为要用atMost(k)辅助函数求最多为k的子数组个数，窗口大小随和的限制动态变化

2. 进窗口更新：right每次循环都右移扩大窗口，并把nums[right]加到窗口和res里再right+1

3. 出窗口时机：当res>k（窗口和超过k）时，就减去nums[left]并left+1，一直缩到res<=k为止

4. 记结果时机：每次内层while结束后，把(right-left)累加到cnt里，代表以right-1结尾且和不超过k的子数组个数，最后用atMost(goal)-atMost(goal-1)得到答案
