# 1966. 最高频元素的频数 · 要素

1. 定长还是变长：变长窗口，窗口大小随着能否用不超过k次操作把窗口内数补齐到最大值而动态变化

2. 进窗口更新：right每次向右移动一位就把nums[right]加入窗口，更新窗口和ttl，并按cost = nums[right]*(right-left+1) - ttl算出把窗口补齐到nums[right]所需操作数

3. 出窗口时机：当cost > k时移动left收缩窗口，移出nums[left]时要把ttl减去nums[left]、left加1，并重新计算cost直到cost <= k

4. 记结果时机：每次right移动、窗口调整满足cost <= k后，用当前窗口长度right-left+1去更新最大频数maxlen
