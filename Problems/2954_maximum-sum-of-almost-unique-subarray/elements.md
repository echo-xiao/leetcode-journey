# 2954. 几乎唯一子数组的最大和 · 要素

1. 定长还是变长：定长窗口，窗口大小固定为k，每次滑动整体右移一格

2. 进窗口更新：right每次向右移一格纳入nums[right]，把它加到windowSum里，并在counter里给它计数+1

3. 出窗口时机：窗口大小固定为k，所以每次right进窗口后立刻让left也同步右移移出nums[left-k]（即最左端旧元素），把它从windowSum减掉，并在counter里给它计数-1，若计数归零就把这个key从counter里删掉

4. 记结果时机：每次窗口滑动完（更新完windowSum和counter后），只要counter的键数量（不同元素个数）>=m，就用windowSum更新maxSum
