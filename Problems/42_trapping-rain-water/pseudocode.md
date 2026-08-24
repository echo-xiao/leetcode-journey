# 42. 接雨水 · 解题思路与伪代码

## 1. 一句话本质
每个位置能接的水量取决于其左右两侧最高柱子中较矮的那个减去自身高度，本质是求“每个柱子上方能困住多少水”。

## 2. 综合思路

- **单调栈（版本1）**：维护一个高度递减的下标栈，遇到比栈顶高的柱子时，说明形成了凹槽，弹出栈顶作为"底部"，用新栈顶和当前柱子的较小高度减去底部高度，乘以宽度，按层（水平层）累加雨水量。
- **双指针（版本2）**：左右两个指针从两端向中间移动，同时维护左侧最大值 maxleft 和右侧最大值 maxright；较小的一侧的指针所在位置的积水量已经确定（由较小值的最大值决定），移动较小的一侧指针，直到相遇。
- **动态规划/前后缀数组（版本3）**：预处理两个数组，分别记录每个位置左侧最大高度和右侧最大高度，然后对每个位置取两者较小值减去当前高度，求和即为总积水量。

## 3. 全量伪代码

**（1）单调栈解法**
```
初始化空栈stack，结果res=0
for i in 0..n-1:
    while stack非空 且 height[i] > height[stack顶]:
        bottom = 弹出栈顶
        if stack为空: break（无左边界，退出）
        left = height[stack新顶]
        right = height[i]
        水位高度 = min(left, right) - height[bottom]
        宽度 = i - stack新顶 - 1
        res += 水位高度 * 宽度
    压入i到stack
return res
```

**（2）双指针解法**
```
left=0, right=n-1
maxleft=0, maxright=0, res=0
while left < right:
    maxleft = max(maxleft, height[left])
    maxright = max(maxright, height[right])
    if maxleft <= maxright:
        res += maxleft - height[left]
        left += 1
    else:
        res += maxright - height[right]
        right -= 1
return res
```

**（3）前后缀最大值数组解法**
```
计算left[i] = height[0..i]的最大值（从左到右遍历）
计算right[i] = height[i..n-1]的最大值（从右到左遍历）
res = 0
for i in 0..n-1:
    res += min(left[i], right[i]) - height[i]
return res
```

## 4. 复杂度

| 解法 | 时间复杂度 | 空间复杂度 |
|---|---|---|
| 单调栈 | $O(n)$ | $O(n)$ |
| 双指针 | $O(n)$ | $O(1)$ |
| 前后缀数组 | $O(n)$ | $O(n)$ |

其中双指针解法为空间最优解，是本题的经典最优解法。
