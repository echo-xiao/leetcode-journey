# 1514. 逐步求和得到正数的最小值

**难度**: Easy | **标签**: `Array` `Prefix Sum`

## 题目描述

<p>给你一个整数数组 <code>nums</code>&nbsp;。你可以选定任意的&nbsp;<strong>正数</strong> startValue 作为初始值。</p>

<p>你需要从左到右遍历 <code>nums</code>&nbsp;数组，并将 startValue 依次累加上&nbsp;<code>nums</code>&nbsp;数组中的值。</p>

<p>请你在确保累加和始终大于等于 1 的前提下，选出一个最小的&nbsp;<strong>正数</strong>&nbsp;作为 startValue 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [-3,2,-3,4,2]
<strong>输出：</strong>5
<strong>解释：</strong>如果你选择 startValue = 4，在第三次累加时，和小于 1 。
<strong>                累加求和
&nbsp;               startValue = 4 | startValue = 5 | nums
</strong>&nbsp;                 (4 <strong>-3</strong> ) = 1  | (5 <strong>-3</strong> ) = 2    |  -3
&nbsp;                 (1 <strong>+2</strong> ) = 3  | (2 <strong>+2</strong> ) = 4    |   2
&nbsp;                 (3 <strong>-3</strong> ) = 0  | (4 <strong>-3</strong> ) = 1    |  -3
&nbsp;                 (0 <strong>+4</strong> ) = 4  | (1 <strong>+4</strong> ) = 5    |   4
&nbsp;                 (4 <strong>+2</strong> ) = 6  | (5 <strong>+2</strong> ) = 7    |   2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2]
<strong>输出：</strong>1
<strong>解释：</strong>最小的 startValue 需要是正数。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,-2,-3]
<strong>输出：</strong>5
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：算法的核心逻辑是通过计算累积和的最小值来确定初始值，使得累积和始终为正。

2. 综合思路：
   - 迭代法：通过迭代计算累积和，并在过程中记录累积和的最小值，最终根据最小值计算所需的初始值。
   - 递归法：虽然在提供的代码中没有递归实现，但理论上可以通过递归计算累积和并跟踪最小值来实现相同的逻辑。
   - 数据结构：使用数组来存储累积和的中间结果，便于计算和比较。

3. 全量伪代码：
   ```
   函数 minStartValue(输入数组 nums):
       初始化 curr 数组，长度为 len(nums) + 1，所有元素为 0
       对于每个索引 i 从 0 到 len(nums) - 1:
           curr[i+1] = curr[i] + nums[i]
       如果 curr 中的最小值小于 0:
           返回 1 - curr 中的最小值
       否则:
           返回 1
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是数组 `nums` 的长度，因为需要遍历整个数组来计算累积和。
   - 空间复杂度：$O(n)$，因为使用了一个与输入数组长度相关的辅助数组 `curr`。