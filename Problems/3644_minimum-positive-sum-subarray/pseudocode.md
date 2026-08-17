# 3644. 最小正和子数组 · 解题思路与伪代码

### 一句话直击本质
利用前缀和数组快速计算子数组和，遍历所有可能的子数组长度和起点，寻找最小的正和子数组。

### 综合思路
1. **前缀和与暴力枚举**：通过构建前缀和数组，快速计算任意子数组的和，然后遍历所有可能的子数组长度和起点，寻找最小的正和子数组。
2. **滑动窗口与有序集合**：利用滑动窗口和有序集合（如二分查找）优化子数组和的计算，减少不必要的计算。

### 全量伪代码
```plaintext
函数 minimumSumSubarray(nums, l, r):
    n = 数组 nums 的长度
    初始化 min_sum 为正无穷大

    # 构建前缀和数组
    prefix = 长度为 n+1 的数组，初始值为 0
    对于 i 从 0 到 n-1:
        prefix[i+1] = prefix[i] + nums[i]

    # 遍历所有可能的子数组长度和起点
    对于 size 从 l 到 r:
        对于 i 从 0 到 n-size:
            j = i + size - 1
            current_sum = prefix[j+1] - prefix[i]
            如果 current_sum > 0:
                min_sum = min(min_sum, current_sum)

    如果 min_sum 仍为正无穷大:
        返回 -1
    否则:
        返回 min_sum

# 滑动窗口与有序集合的伪代码（简化版）
函数 minimumSumSubarray(nums, l, r):
    n = 数组 nums 的长度
    初始化 min_sum 为正无穷大

    # 构建前缀和数组
    prefix = 长度为 n+1 的数组，初始值为 0
    对于 i 从 0 到 n-1:
        prefix[i+1] = prefix[i] + nums[i]

    # 使用滑动窗口和有序集合
    sorted_window = 空列表
    对于 j 从 l 到 n:
        如果 j == l:
            初始化窗口，包含 prefix[0] 到 prefix[l-l=0]
        否则:
            更新窗口，移除旧的，添加新的

        在有序窗口中查找 < prefix[j] 的最大值
        如果找到:
            计算 current_sum
            min_sum = min(min_sum, current_sum)

    如果 min_sum 仍为正无穷大:
        返回 -1
    否则:
        返回 min_sum
```

### 复杂度
- **时间复杂度**：$O(n^2)$，因为需要遍历所有可能的子数组长度和起点。
- **空间复杂度**：$O(n)$，用于存储前缀和数组。
