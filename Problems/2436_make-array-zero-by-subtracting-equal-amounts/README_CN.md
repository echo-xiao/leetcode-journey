# 2436. 使数组中所有元素都等于零

**难度**: Easy | **标签**: `Array` `Hash Table` `Greedy` `Sorting` `Heap (Priority Queue)` `Simulation`

## 题目描述

<p>给你一个非负整数数组 <code>nums</code> 。在一步操作中，你必须：</p>

<ul>
	<li>选出一个正整数 <code>x</code> ，<code>x</code> 需要小于或等于 <code>nums</code> 中 <strong>最小</strong> 的 <strong>非零</strong> 元素。</li>
	<li><code>nums</code> 中的每个正整数都减去 <code>x</code>。</li>
</ul>

<p>返回使 <code>nums</code> 中所有元素都等于<em> </em><code>0</code> 需要的 <strong>最少</strong> 操作数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,5,0,3,5]
<strong>输出：</strong>3
<strong>解释：</strong>
第一步操作：选出 x = 1 ，之后 nums = [0,4,0,2,4] 。
第二步操作：选出 x = 2 ，之后 nums = [0,2,0,0,2] 。
第三步操作：选出 x = 2 ，之后 nums = [0,0,0,0,0] 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0]
<strong>输出：</strong>0
<strong>解释：</strong>nums 中的每个元素都已经是 0 ，所以不需要执行任何操作。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：算法的核心逻辑是通过统计数组中不同正数的个数来确定将所有元素变为零所需的操作次数。

2. 综合思路：
   - **版本 1 和 2（使用最小堆）**：这两个版本利用最小堆来逐步处理数组中的正数，确保每次操作都能减少数组中至少一个正数的值。通过堆的性质，能够有效地找到当前最小的正数，并判断是否需要进行新的操作。
   - **版本 3（使用集合）**：这个版本通过将数组转换为集合来去除重复元素，然后直接统计集合中正数的个数。由于集合自动去重且忽略零，因此可以直接计算需要的操作次数。

3. 全量伪代码：
   - **使用最小堆的版本**：
     ```
     初始化一个空的最小堆 minHeap
     对于数组中的每个元素 num：
         如果 num 大于 0，则将 num 压入 minHeap
     初始化 last 和 cnt 为 0
     当 minHeap 不为空时：
         弹出 minHeap 的最小元素 curr
         如果 curr 大于 last：
             增加 cnt
             更新 last 为 curr
     返回 cnt
     ```
   - **使用集合的版本**：
     ```
     将数组转换为集合 arr
     如果 0 在 arr 中：
         返回 arr 的大小减 1
     否则：
         返回 arr 的大小
     ```

4. 复杂度：
   - **时间复杂度**：
     - 使用最小堆的版本：$O(n \log n)$，其中 $n$ 是数组的长度，因为需要对每个元素进行堆操作。
     - 使用集合的版本：$O(n)$，因为集合的构建和操作都是线性的。
   - **空间复杂度**：
     - 使用最小堆的版本：$O(n)$，因为最坏情况下堆中可能包含所有正数。
     - 使用集合的版本：$O(n)$，因为集合中最多包含所有不同的元素。