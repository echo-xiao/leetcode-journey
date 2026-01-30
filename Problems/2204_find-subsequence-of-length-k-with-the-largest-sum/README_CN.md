# 2204. 找到和最大的长度为 K 的子序列

**难度**: Easy | **标签**: `Array` `Hash Table` `Sorting` `Heap (Priority Queue)`

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。你需要找到&nbsp;<code>nums</code>&nbsp;中长度为 <code>k</code>&nbsp;的 <strong>子序列</strong>&nbsp;，且这个子序列的&nbsp;<strong>和最大&nbsp;</strong>。</p>

<p>请你返回 <strong>任意</strong> 一个长度为&nbsp;<code>k</code>&nbsp;的整数子序列。</p>

<p><strong>子序列</strong>&nbsp;定义为从一个数组里删除一些元素后，不改变剩下元素的顺序得到的数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [2,1,3,3], k = 2
<b>输出：</b>[3,3]
<strong>解释：</strong>
子序列有最大和：3 + 3 = 6 。</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [-1,-2,3,4], k = 3
<b>输出：</b>[-1,3,4]
<b>解释：</b>
子序列有最大和：-1 + 3 + 4 = 6 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums = [3,4,3,3], k = 2
<b>输出：</b>[3,4]
<strong>解释：</strong>
子序列有最大和：3 + 4 = 7 。
另一个可行的子序列为 [4, 3] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-10<sup>5</sup>&nbsp;&lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 使用最小堆维护当前最大的 k 个元素及其索引，并根据索引排序以保持原序。

2. **综合思路：**
   - **堆排序法：** 使用最小堆（优先队列）来动态维护当前最大的 k 个元素。每次遍历新元素时，若堆的大小小于 k，则直接加入堆中；若堆的大小等于 k，则将新元素与堆顶元素比较，若新元素更大则替换堆顶元素。最后根据元素的原始索引对堆中的元素进行排序，以保持原序。
   - **排序法（未在代码集中出现，但为常见解法）：** 对数组元素按值从大到小排序，选择前 k 个元素，然后根据这些元素的原始索引排序以保持原序。

3. **全量伪代码：**

   - **堆排序法：**
     ```
     初始化一个空的最小堆 minHeap
     对于数组 nums 中的每个元素 num 及其索引 idx：
         创建一个项 item = [num, idx]
         如果 minHeap 的大小小于 k：
             将 item 压入 minHeap
         否则如果 minHeap 的大小等于 k：
             将 item 与 minHeap 的堆顶元素比较，若 item 更大则替换堆顶元素
     将 minHeap 按照索引排序
     返回排序后的 minHeap 中的值部分
     ```

   - **排序法（假设）：**
     ```
     将 nums 中的每个元素与其索引组成一个元组列表 pairs
     将 pairs 按照值从大到小排序
     选择前 k 个元素
     将选择的元素按原始索引排序
     返回排序后的元素的值部分
     ```

4. **复杂度：**

   - **时间复杂度：** $O(n \log k)$，其中 $n$ 是数组的长度，因为每次插入堆的操作复杂度为 $O(\log k)$，且需要对堆进行 $O(k \log k)$ 的排序。
   
   - **空间复杂度：** $O(k)$，因为堆中最多存储 k 个元素。