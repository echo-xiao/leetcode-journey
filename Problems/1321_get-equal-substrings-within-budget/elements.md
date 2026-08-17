# 1321. 尽可能使字符串相等 · 要素

1. 定长还是变长：变长窗口，窗口大小随代价约束动态变化，不是固定长度

2. 进窗口更新：right每次向右移动一步扩大窗口，把|s[right]-t[right]|加到总代价ttl里

3. 出窗口时机：当ttl超过maxCost时就要移动left收缩窗口，移出s[left]和t[left]的差值，从ttl中减去，直到ttl不超过maxCost为止

4. 记结果时机：每次right移动、窗口调整合法后，用right-left+1更新最大长度maxlen
