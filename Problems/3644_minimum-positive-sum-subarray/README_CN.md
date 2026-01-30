# 3644. 最小正和子数组

**难度**: Easy | **标签**: `Array` `Sliding Window` `Prefix Sum`

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和 <strong>两个</strong> 整数 <code>l</code> 和 <code>r</code>。你的任务是找到一个长度在 <code>l</code> 和 <code>r</code> 之间（包含）且和大于 0 的 <strong>子数组</strong> 的 <strong>最小</strong> 和。</p>

<p>返回满足条件的子数组的 <strong>最小</strong> 和。如果不存在这样的子数组，则返回 -1。</p>

<p><strong>子数组</strong> 是数组中的一个连续 <b>非空</b> 元素序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [3, -2, 1, 4], l = 2, r = 3</span></p>

<p><strong>输出：</strong> <span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<p>长度在 <code>l = 2</code> 和 <code>r = 3</code> 之间且和大于 0 的子数组有：</p>

<ul>
	<li><code>[3, -2]</code> 和为 1</li>
	<li><code>[1, 4]</code> 和为 5</li>
	<li><code>[3, -2, 1]</code> 和为 2</li>
	<li><code>[-2, 1, 4]</code> 和为 3</li>
</ul>

<p>其中，子数组 <code>[3, -2]</code> 的和为 1，是所有正和中最小的。因此，答案为 1。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [-2, 2, -3, 1], l = 2, r = 3</span></p>

<p><strong>输出：</strong> <span class="example-io">-1</span></p>

<p><strong>解释：</strong></p>

<p>不存在长度在 <code>l</code> 和 <code>r</code> 之间且和大于 0 的子数组。因此，答案为 -1。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1, 2, 3, 4], l = 2, r = 4</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p>子数组 <code>[1, 2]</code> 的长度为 2，和为&nbsp;3，是所有正和中最小的。因此，答案为 3。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= l &lt;= r &lt;= nums.length</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


---
## 解题思路与复盘

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