# 1046. 最大连续1的个数 III · 要素

1. 定长还是变长：变长窗口，窗口大小随0的个数动态变化，目标是找满足「0不超过k个」的最长窗口。

2. 进窗口更新：right每轮都往右走一格，把nums[right]吃进来，如果它是0就cnt++，然后right++。

3. 出窗口时机：只在cnt>k（窗口里0太多）时缩左边，移出nums[left]若为0就cnt--，然后left++，直到cnt<=k。

4. 记结果时机：每次缩完左边、窗口重新合法后，用maxLen=max(maxLen, right-left)更新一次（right已加过1，所以长度就是right-left）。
