# 1538. 可获得的最大点数 · 解题思路与伪代码

## 1. 一句话直击本质

从两端取k张牌的最大和 = 总和 - 中间连续(n-k)张牌的最小和，用**滑动窗口**求这个最小子数组和。

## 2. 综合思路

本题核心是"正难则反"的转化思想：

- **暴力/双指针枚举法**：直接枚举从左边取i张、右边取k-i张的所有组合，取最大值（未在本代码出现，但为常见解法）。
- **滑动窗口法（本代码采用）**：将问题转化为求长度为`n-k`的连续子数组的最小和，总和减去这个最小和即为答案。这是因为"取两端共k张牌"等价于"排除中间连续n-k张牌"。

## 3. 全量伪代码

```
函数 maxScore(牌面数组cardPoints, 抽取次数k):
    n ← 数组长度
    total ← 数组所有元素之和
    length ← n - k   # 需要排除的中间窗口长度

    若 n <= length:  # 即 k >= n，全部都能取到
        返回 total

    # 初始化窗口：数组前length个元素之和
    windowSum ← sum(cardPoints[0 : length])
    minWindowSum ← windowSum

    # 滑动窗口，从左到右移动，窗口大小固定为length
    对于 i 从 length 到 n-1:
        windowSum ← windowSum + cardPoints[i] - cardPoints[i - length]
        minWindowSum ← min(minWindowSum, windowSum)

    返回 total - minWindowSum
```

## 4. 复杂度

- **时间复杂度**：$O(n)$，只需遍历数组常数次（求和 + 滑动窗口遍历）。
- **空间复杂度**：$O(1)$，只使用了常数个额外变量（不计输入数组本身占用空间）。
