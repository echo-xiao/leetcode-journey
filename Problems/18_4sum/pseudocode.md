# 18. 四数之和 · 解题思路与伪代码

# 《四数之和》AC版本分析

## 1. 一句话直击本质
**排序后固定前两个数，利用双指针在剩余区间内收缩查找，通过跳过重复元素实现去重，将四数之和转化为双指针的两数之和问题。**

## 2. 综合思路

本题所有 AC 版本均采用**排序 + 双重循环固定 + 双指针收缩**的思路，属于同一种解法范式，具体如下：

- **排序预处理**：先对数组排序，为剪枝去重和双指针移动提供有序性保证。
- **外层双重遍历（i, j）**：固定第一个数 `nums[i]` 和第二个数 `nums[j]`，将问题降维为两数之和。
- **内层双指针（left, right）**：在 `j+1` 到 `n-1` 区间内使用左右指针向中间收缩，寻找满足 `nums[i]+nums[j]+nums[left]+nums[right] == target` 的组合。
- **去重策略**：
  - 外层 `i`、`j` 遍历时跳过与前一个相同的元素，避免重复的 `(i,j)` 组合。
  - 内层找到一组解后，`left`、`right` 分别跳过重复值，避免重复解。
- **两种版本对比**：版本1与版本2代码逻辑完全一致，仅命名和排版有细微差异，本质是同一实现（无算法差异）。

（未见其他如哈希表、回溯/DFS等实现方式，两版本均为标准的"排序+双指针"解法。）

## 3. 全量伪代码

```
函数 四数之和(数组nums, 目标值target):
    对 nums 进行排序
    n = nums 长度
    res = 空列表

    for i from 0 to n-1:
        如果 i > 0 且 nums[i] == nums[i-1]:
            跳过本次循环（去重）

        for j from i+1 to n-1:
            如果 j > i+1 且 nums[j] == nums[j-1]:
                跳过本次循环（去重）

            left = j + 1
            right = n - 1

            while left < right:
                sum = nums[i] + nums[j] + nums[left] + nums[right]

                如果 sum == target:
                    将 [nums[i], nums[j], nums[left], nums[right]] 加入 res
                    left += 1
                    right -= 1
                    # 跳过重复的 left 值
                    while left < right 且 nums[left] == nums[left-1]:
                        left += 1
                    # 跳过重复的 right 值
                    while left < right 且 nums[right] == nums[right+1]:
                        right -= 1

                否则如果 sum > target:
                    right -= 1   # 总和过大，右指针左移

                否则:
                    left += 1    # 总和过小，左指针右移

    返回 res
```

## 4. 复杂度

**时间复杂度**：
$$O(n^3)$$
排序耗时 $O(n\log n)$，双重循环 $O(n^2)$，内层双指针遍历 $O(n)$，总体为 $O(n^2) \times O(n) = O(n^3)$。

**空间复杂度**：
$$O(\log n)$$
排序算法（如快排）的递归栈空间开销为 $O(\log n)$（不计输出结果 `res` 所占空间；若计入结果集空间，则为 $O(n^3)$ 最坏情况下的组合数量级别，但通常认为输出空间不计入复杂度分析）。
