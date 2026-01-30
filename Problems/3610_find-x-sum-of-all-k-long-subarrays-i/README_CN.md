# 3610. 计算子数组的 x-sum I

**难度**: Easy | **标签**: `Array` `Hash Table` `Sliding Window` `Heap (Priority Queue)`

## 题目描述

<p>给你一个由 <code>n</code> 个整数组成的数组 <code>nums</code>，以及两个整数 <code>k</code> 和 <code>x</code>。</p>

<p>数组的 <strong>x-sum</strong> 计算按照以下步骤进行：</p>

<ul>
	<li>统计数组中所有元素的出现次数。</li>
	<li>仅保留出现频率最高的前 <code>x</code> 种元素。如果两种元素的出现次数相同，则数值<strong> 较大 </strong>的元素被认为出现次数更多。</li>
	<li>计算结果数组的和。</li>
</ul>

<p><strong>注意</strong>，如果数组中的不同元素少于 <code>x</code> 个，则其 <strong>x-sum</strong> 是数组的元素总和。</p>

<p>返回一个长度为 <code>n - k + 1</code> 的整数数组 <code>answer</code>，其中 <code>answer[i]</code> 是 <span data-keyword="subarray-nonempty">子数组</span> <code>nums[i..i + k - 1]</code> 的 <strong>x-sum</strong>。</p>

<p><strong>子数组</strong> 是数组内的一个连续<b> 非空</b> 的元素序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [1,1,2,2,3,4,2,3], k = 6, x = 2</span></p>

<p><strong>输出：</strong><span class="example-io">[6,10,12]</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>对于子数组 <code>[1, 1, 2, 2, 3, 4]</code>，只保留元素 1 和 2。因此，<code>answer[0] = 1 + 1 + 2 + 2</code>。</li>
	<li>对于子数组 <code>[1, 2, 2, 3, 4, 2]</code>，只保留元素 2 和 4。因此，<code>answer[1] = 2 + 2 + 2 + 4</code>。注意 4 被保留是因为其数值大于出现其他出现次数相同的元素（3 和 1）。</li>
	<li>对于子数组 <code>[2, 2, 3, 4, 2, 3]</code>，只保留元素 2 和 3。因此，<code>answer[2] = 2 + 2 + 2 + 3 + 3</code>。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [3,8,7,8,7,5], k = 2, x = 2</span></p>

<p><strong>输出：</strong><span class="example-io">[11,15,15,15,12]</span></p>

<p><strong>解释：</strong></p>

<p>由于 <code>k == x</code>，<code>answer[i]</code> 等于子数组 <code>nums[i..i + k - 1]</code> 的总和。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
	<li><code>1 &lt;= x &lt;= k &lt;= nums.length</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过滑动窗口和最小堆或排序，计算每个子数组中频率最高的前 x 个元素的加权和。

2. **综合思路：**
   - **滑动窗口与最小堆：** 对于每个长度为 k 的子数组，使用字典统计元素频率，然后使用最小堆维护频率最高的 x 个元素，最后计算这些元素的加权和。
   - **滑动窗口与排序：** 对于每个长度为 k 的子数组，使用 `Counter` 统计元素频率，然后对频率进行排序，选择前 x 个频率最高的元素计算加权和。

3. **全量伪代码：**

   ```plaintext
   初始化结果列表 res
   对于每个可能的子数组起始索引 i 从 0 到 n-k:
       取出当前子数组 newNums = nums[i: i+k]
       初始化频率字典 mapp
       对于子数组中的每个元素 num:
           更新 mapp 中 num 的频率
       
       初始化一个最小堆 minHeap
       对于 mapp 中的每个元素及其频率 (val, freq):
           如果 minHeap 的大小小于 x:
               将 (freq, val) 插入 minHeap
           否则:
               将 (freq, val) 插入 minHeap 并弹出最小元素

       初始化当前子数组的和 summ = 0
       对于 minHeap 中的每个元素 (freq, val):
           summ 增加 freq * val
       
       将 summ 添加到结果列表 res

   返回结果列表 res
   ```

   或者：

   ```plaintext
   初始化结果列表 res_arr
   对于每个可能的子数组起始索引 l 从 0 到 n-k:
       取出当前子数组 win = nums[l: l+k]
       使用 Counter 统计 win 中的元素频率 counts
       初始化当前子数组的和 res = 0
       
       如果 counts 的长度小于 x:
           res = win 中所有元素的和
       否则:
           将 counts 转换为列表 freq
           按照频率和元素值对 freq 进行降序排序
           取出前 x 个元素 top
           对于 top 中的每个元素 (n, f):
               res 增加 n * f

       将 res 添加到结果列表 res_arr

   返回结果列表 res_arr
   ```

4. **复杂度：**

   - 时间复杂度：$O((n-k+1) \cdot (k + x \log x))$，其中 $n$ 是数组的长度，$k$ 是子数组的长度，$x$ 是需要计算的频率最高的元素个数。
   - 空间复杂度：$O(k + x)$，用于存储子数组和最小堆。