# 209. 长度最小的子数组 · 要素

1. 定长还是变长：变长窗口，窗口长度不固定，要找的是和≥target的最短那段，所以左右边界都在动。

2. 进窗口更新：right 每轮都往右走一格，把 nums[right] 累加到 res 里，只需维护这一个窗口和。

3. 出窗口时机：只要 res >= target 就不停地缩：先记长度，再 res 减去 nums[left]，然后 left++，直到 res < target。

4. 记结果时机：在窗口和刚满足 res >= target、还没弹出左端元素之前记一次 minLen = min(minLen, right-left)；全程没满足过就返回 0。
