# 42. 接雨水 · 解题思路与伪代码

# 接雨水 算法分析

## 1. 一句话直击本质
每个位置能接的雨水量 = min(左侧最高柱, 右侧最高柱) - 当前柱高，将所有位置累加即为答案。

## 2. 综合思路

两个版本本质上都是基于"木桶效应"（接水量取决于较矮的一侧），但在**空间优化**上采取了不同策略：

- **版本2：动态规划（前后缀分解）**
  预先计算每个位置左侧的最大值数组 `left[]` 和右侧的最大值数组 `right[]`，再遍历一次利用公式求解。思路直观，但需要 $O(n)$ 额外数组空间。

- **版本1：双指针（空间优化）**
  利用双指针 `left`、`right` 从两端向中间收缩，动态维护 `maxleft` 和 `maxright`。
  核心贪心思想：**若 `maxleft <= maxright`，则左指针处的接水量必然由 `maxleft` 决定**（因为右边必然存在比 `maxleft` 更高的挡板），从而避免了预先存储整个数组，将空间复杂度优化至 $O(1)$。

## 3. 全量伪代码

### 解法一：前后缀最大值法（DP）
```
函数 trap(height):
    n = 数组长度
    初始化 left_max[n], right_max[n] 数组

    // 正向遍历，计算每个位置左边的最大值
    当前最大值 = 0
    对于 i 从 0 到 n-1:
        当前最大值 = max(当前最大值, height[i])
        left_max[i] = 当前最大值

    // 反向遍历，计算每个位置右边的最大值
    当前最大值 = 0
    对于 i 从 n-1 到 0:
        当前最大值 = max(当前最大值, height[i])
        right_max[i] = 当前最大值

    // 汇总结果
    res = 0
    对于 i 从 0 到 n-1:
        木桶短板 = min(left_max[i], right_max[i])
        res += 木桶短板 - height[i]
    
    返回 res
```

### 解法二：双指针法
```
函数 trap(height):
    left = 0, right = n - 1
    maxleft = 0, maxright = 0
    res = 0

    当 left < right 时循环:
        更新 maxleft = max(maxleft, height[left])
        更新 maxright = max(maxright, height[right])

        如果 maxleft <= maxright:
            // 左边的最大值是决定短板的关键
            res += maxleft - height[left]
            left 右移一位
        否则:
            // 右边的最大值是决定短板的关键
            res += maxright - height[right]
            right 左移一位

    返回 res
```

## 4. 复杂度

| 解法 | 时间复杂度 | 空间复杂度 |
| :--- | :--- | :--- |
| **版本2 (DP前后缀)** | $O(n)$ | $O(n)$ (存储两个辅助数组) |
| **版本1 (双指针)** | $O(n)$ | $O(1)$ (仅使用常数个变量) |
