# 190. 颠倒二进制位 · 复盘

这个题目属于bit manipulation；res <<= 1 左边移动1位，last = n & 1 取最低位，res |= last 是把last最后一个位置放到res腾出来的最低位置，n >>= 1 表示右边移动1位。
