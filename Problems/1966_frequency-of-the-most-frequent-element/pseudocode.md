# 1966. 最高频元素的频数 · 解题思路与伪代码

## 1. 一句话直击本质
将数组排序后，用**滑动窗口**维护一个区间，使得把窗口内所有元素都增加到当前窗口最大值（即右端点值）所需的总操作数不超过 `k`，从而找到最大可行窗口长度。

## 2. 综合思路
两个版本本质上是**同一种解法**——排序 + 双指针滑动窗口，仅代码风格略有差异：

- **版本1**：在 while 循环条件中直接内联计算 `cost`（`nums[right]*(right-left+1) - ttl`），每次判断时重新计算一次。
- **版本2**：将 `cost` 提取为独立变量，先计算一次，循环内更新后重新赋值，逻辑等价，只是可读性略优。

核心思路都是：
1. 排序数组，使得窗口内最大值为右指针元素。
2. 用窗口和 `ttl` 快速计算“将窗口所有元素补齐到 `nums[right]` ”所需代价：`cost = nums[right]*(窗口长度) - ttl`。
3. 若代价超过 `k`，收缩左边界，直到满足条件。
4. 用窗口长度更新最大频数。

## 3. 全量伪代码

```
函数 maxFrequency(nums, k):
    对 nums 进行排序
    left ← 0
    ttl ← 0        # 当前窗口元素和
    maxlen ← 0

    对 right 从 0 到 n-1:
        ttl ← ttl + nums[right]
        cost ← nums[right] * (right - left + 1) - ttl   # 将窗口所有数补齐到nums[right]所需操作数
        
        当 cost > k:
            ttl ← ttl - nums[left]
            left ← left + 1
            重新计算 cost ← nums[right] * (right - left + 1) - ttl
        
        maxlen ← max(maxlen, right - left + 1)
    
    返回 maxlen
```

## 4. 复杂度

- 时间复杂度：排序 $O(n\log n)$，滑动窗口遍历 $O(n)$，总体 $O(n\log n)$。
- 空间复杂度：$O(\log n)$（排序所需栈空间，若原地排序则不计入额外数组空间）或 $O(1)$（忽略排序内部实现开销）。

$$
\text{时间复杂度：} O(n\log n), \quad \text{空间复杂度：} O(\log n) \text{ 或 } O(1)
$$
