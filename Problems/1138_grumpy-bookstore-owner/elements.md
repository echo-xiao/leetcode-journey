# 1138. 爱生气的书店老板 · 要素

1. 定长还是变长：定长窗口，窗口大小固定为 minutes

2. 进窗口更新：right从0滑到n-1，每次right位置若grumpy为1，就把customers[right]加到flex里

3. 出窗口时机：当窗口大小超过minutes（即i>=minutes）时，同时移除left=i-minutes位置，如果该位置grumpy为1就从flex里减去customers[i-minutes]，left随之右移

4. 记结果时机：每次窗口滑动更新完flex后都要立即计算fixed+flex并更新maxres，取最大值
