# 15. 三数之和 · 解题思路与伪代码

## 1. 一句话直击本质
**排序 + 固定一个数 + 双指针夹逼**，将三数之和问题转化为在有序数组中寻找两数之和等于目标值的问题，并通过跳过重复元素实现去重。

## 2. 综合思路

两个版本均采用同一种核心算法——**排序 + 固定第一数 + 双指针**，属于同一类解法，区别仅在**去重时机与写法细节**：

- **版本1**：先移动指针（`left+1`, `right-1`），再通过 `while` 循环跳过与**移动后左指针的前一个值**相同的重复项（只对 left 做去重，right 的去重靠下一轮循环的边界收缩自然完成）。
- **版本2**：在移动指针**之前**，分别对 `left` 和 `right` 做去重判断（比较 `nums[left]` 与 `nums[left+1]`，`nums[right]` 与 `nums[right-1]`），然后再统一执行 `left+1`、`right-1`。两边都显式做了去重处理。

两者本质等价，都能正确避免重复三元组，只是去重代码位置和判断方向不同。

## 3. 全量伪代码

```
函数 threeSum(nums):
    对 nums 进行排序
    n = nums 长度
    res = 空列表

    for i from 0 to n-1:
        if i > 0 且 nums[i] == nums[i-1]:
            continue   # 跳过重复的固定数，避免结果重复

        target = -nums[i]
        left = i + 1
        right = n - 1

        while left < right:
            sum = nums[left] + nums[right]

            if sum == target:
                将 [nums[i], nums[left], nums[right]] 加入 res

                # 去重逻辑（两种写法之一）：
                方式A（版本1）：
                    left += 1
                    right -= 1
                    while left < right 且 nums[left] == nums[left-1]:
                        left += 1

                方式B（版本2）：
                    while left < right 且 nums[left] == nums[left+1]:
                        left += 1
                    while left < right 且 nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

            elif sum > target:
                right -= 1   # 和过大，右指针左移
            else:
                left += 1    # 和过小，左指针右移

    返回 res
```

## 4. 复杂度

- **排序**：$O(n \log n)$
- **外层循环 + 双指针遍历**：外层 $O(n)$，内层双指针最坏 $O(n)$，共 $O(n^2)$
- **总时间复杂度**：$O(n^2)$
- **空间复杂度**：不计返回结果空间，排序需要 $O(\log n)$ 栈空间（或 $O(n)$，视排序算法实现而定）；若计入结果存储，最坏情况下为 $O(n)$（结果集大小相关）。

综合表示为：

$$
\text{时间复杂度} = O(n^2), \quad \text{空间复杂度} = O(\log n) \sim O(n)
$$
