# 1574. 数组中两元素的最大乘积

**难度**: Easy | **标签**: `Array` `Sorting` `Heap (Priority Queue)`

## 题目描述

<p>给你一个整数数组 <code>nums</code>，请你选择数组的两个不同下标 <code>i</code> 和 <code>j</code><em>，</em>使 <code>(nums[i]-1)*(nums[j]-1)</code> 取得最大值。</p>

<p>请你计算并返回该式的最大值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [3,4,5,2]
<strong>输出：</strong>12 
<strong>解释：</strong>如果选择下标 i=1 和 j=2（下标从 0 开始），则可以获得最大值，(nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12 。 
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,5,4,5]
<strong>输出：</strong>16
<strong>解释：</strong>选择下标 i=1 和 j=3（下标从 0 开始），则可以获得最大值 (5-1)*(5-1) = 16 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [3,7]
<strong>输出：</strong>12
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10^3</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过维护一个大小为2的最大堆来找到数组中最大的两个元素，并计算其乘积。

2. 综合思路：
   - 堆排序思路：利用最大堆（或最小堆）来动态维护数组中最大的两个元素。通过遍历数组，将元素插入堆中，确保堆中始终保留最大的两个元素。最后计算这两个元素减一后的乘积。
   - 排序思路（未在代码集中出现）：可以先对数组进行排序，然后直接选择最后两个元素进行计算。
   - 线性扫描思路（未在代码集中出现）：通过一次遍历找到最大的两个元素，记录下来并计算其乘积。

3. 全量伪代码：
   ```plaintext
   初始化一个空的最大堆 maxHeap
   对于数组中的每个元素 num:
       如果 maxHeap 的大小小于 2:
           将 num 插入 maxHeap
       否则:
           将 num 插入 maxHeap，并弹出堆中最小的元素
   从 maxHeap 中弹出两个元素 num1 和 num2
   计算并返回 (num1 - 1) * (num2 - 1)
   ```

4. 复杂度：
   - 时间复杂度：$O(n \log 2) = O(n)$，因为每次插入堆的操作复杂度为 $O(\log 2)$，而我们需要遍历整个数组。
   - 空间复杂度：$O(1)$，因为堆的大小固定为2，与输入大小无关。