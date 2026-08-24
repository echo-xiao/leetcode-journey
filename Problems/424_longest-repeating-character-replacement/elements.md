# 424. 替换后的最长重复字符 · 要素

1. 定长还是变长：变长窗口，right一直往右扩，窗口不满足条件时收缩left

2. 进窗口更新：right每往右移一步就把s[right]计数加一（counter[c]+=1），并更新maxCount为该字符历史最大出现次数

3. 出窗口时机：当(right-left+1)-maxCount>k时，说明替换次数超过k，把s[left]计数减一并left+1（懒惰更新版本不重新计算maxCount，只减小窗口一步）

4. 记结果时机：每次right移动完、窗口调整完之后，用right-left+1更新maxLen
