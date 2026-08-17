# 1538. 可获得的最大点数 · 要素

1. 定长还是变长：定长窗口，窗口大小固定为 length = n - k，即需要排除的中间牌数

2. 进窗口更新：i 从 length 遍历到 n-1，每次把 cardPoints[i] 加入窗口并累加到 windowSum 里

3. 出窗口时机：窗口大小固定，每进一个新元素就要同时移出最左边的元素 cardPoints[i-length]，把它从 windowSum 中减掉，实现窗口整体右移

4. 记结果时机：每次更新完 windowSum 后立刻比较并更新 minWindowSum，遍历结束后用 total - minWindowSum 得到最终答案
