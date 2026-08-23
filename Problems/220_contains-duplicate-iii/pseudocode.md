# 220. 存在重复元素 III · 解题思路与伪代码

## 1. 一句话直击本质
**滑动窗口 + 桶排序（分桶）**：将值域按 `valueDiff+1` 分桶，只需比较当前元素与相邻桶内元素，即可在 $O(1)$ 判断是否存在满足值差和下标差条件的重复元素。

## 2. 综合思路

本题的常见 AC 解法主要有两类：

**思路一：桶（Bucket）+ 滑动窗口（本题代码采用）**
- 把值域按宽度 `w = valueDiff + 1` 分桶：`bucket_id = x // w`。
- 保证：只要两个数落在同一个桶，其差值必然 `<= valueDiff`。
- 维护一个大小为 `indexDiff` 的滑动窗口（用哈希表存储 `桶号 -> 值`），每个桶最多存一个值（因为一旦同桶出现两个数就已经满足条件，直接返回 True）。
- 对于新元素，只需检查：自身桶、左邻桶、右邻桶，共 3 个桶是否有满足条件的值。
- 窗口滑出范围时删除对应的旧桶记录。

**思路二：有序集合（TreeMap / SortedList）+ 滑动窗口**（另一种常见 AC 写法，思路对比）
- 维护一个大小为 `indexDiff` 的有序集合（如 Java `TreeMap`，Python 用 `SortedList`）。
- 对每个新元素 `x`，在有序结构中二分查找是否存在值在 `[x-valueDiff, x+valueDiff]` 区间内的元素。
- 若窗口超出 `indexDiff`，移除最早加入的元素。
- 这种做法基于二分查找，时间复杂度稍高（$O(n \log k)$），但逻辑更直观。

两者本质都是**限定下标窗口内查询值域邻近元素**，区别在于“桶”是 $O(1)$ 近似匹配，“有序集合”是 $O(\log k)$ 精确匹配。

## 3. 全量伪代码

### （方法一）桶 + 哈希滑动窗口
```
函数 存在重复元素III(nums, indexDiff, valueDiff):
    若 indexDiff <= 0 或 valueDiff < 0: 返回 False
    
    w = valueDiff + 1
    buckets = 空哈希表   # 桶号 -> 值

    对 i, x 在 nums 中枚举:
        b = x // w   # 计算所属桶号

        若 b 在 buckets 中:
            返回 True   # 同桶必然满足
        若 (b-1) 在 buckets 且 |x - buckets[b-1]| <= valueDiff:
            返回 True
        若 (b+1) 在 buckets 且 |x - buckets[b+1]| <= valueDiff:
            返回 True

        buckets[b] = x   # 插入新值

        若 i >= indexDiff:
            从 buckets 中删除 nums[i - indexDiff] 所在桶  # 窗口收缩

    返回 False
```

### （方法二）有序集合 + 滑动窗口（补充思路）
```
函数 存在重复元素III(nums, indexDiff, valueDiff):
    window = 空有序集合（大小限制为 indexDiff）

    对 i, x 在 nums 中枚举:
        在 window 中查找是否存在值 v 满足 |v - x| <= valueDiff
        （利用二分查找定位 x-valueDiff 的插入位置，检查邻近元素）
        若存在: 返回 True

        插入 x 到 window
        若 window 大小 > indexDiff:
            移除 nums[i - indexDiff]

    返回 False
```

## 4. 复杂度

**方法一（桶 + 哈希表）：**
- 时间复杂度：$O(n)$
- 空间复杂度：$O(\min(n, indexDiff))$

**方法二（有序集合 + 二分查找）：**
- 时间复杂度：$O(n \log(\min(n, indexDiff)))$
- 空间复杂度：$O(\min(n, indexDiff))$
