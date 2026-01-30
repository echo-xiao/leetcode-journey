# 3226. 最小数字游戏

**难度**: Easy | **标签**: `Array` `Sorting` `Heap (Priority Queue)` `Simulation`

## 题目描述

<p>你有一个下标从 <strong>0</strong> 开始、长度为 <strong>偶数</strong> 的整数数组 <code>nums</code> ，同时还有一个空数组 <code>arr</code> 。Alice 和 Bob 决定玩一个游戏，游戏中每一轮 Alice 和 Bob 都会各自执行一次操作。游戏规则如下：</p>

<ul>
	<li>每一轮，Alice 先从 <code>nums</code> 中移除一个<strong> 最小</strong> 元素，然后 Bob 执行同样的操作。</li>
	<li>接着，Bob 会将移除的元素添加到数组 <code>arr</code> 中，然后 Alice 也执行同样的操作。</li>
	<li>游戏持续进行，直到 <code>nums</code> 变为空。</li>
</ul>

<p>返回结果数组 <code>arr</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,4,2,3]
<strong>输出：</strong>[3,2,5,4]
<strong>解释：</strong>第一轮，Alice 先移除 2 ，然后 Bob 移除 3 。然后 Bob 先将 3 添加到 arr 中，接着 Alice 再将 2 添加到 arr 中。于是 arr = [3,2] 。
第二轮开始时，nums = [5,4] 。Alice 先移除 4 ，然后 Bob 移除 5 。接着他们都将元素添加到 arr 中，arr 变为 [3,2,5,4] 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,5]
<strong>输出：</strong>[5,2]
<strong>解释：</strong>第一轮，Alice 先移除 2 ，然后 Bob 移除 5 。然后 Bob 先将 5 添加到 arr 中，接着 Alice 再将 2 添加到 arr 中。于是 arr = [5,2] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>nums.length % 2 == 0</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是使用最小堆对数组进行排序，并在排序后按特定顺序重组数组。

2. 综合思路：
   - 堆排序：利用最小堆（优先队列）对数组进行排序，然后通过弹出堆顶元素的方式获取从小到大的元素。
   - 重组顺序：在排序后，通过将两个最小元素交换位置的方式重组数组。

3. 全量伪代码：
   ```plaintext
   定义函数 numberGame(nums):
       初始化一个空的最小堆 minHeap
       初始化一个空数组 arr
       
       对于 nums 中的每个元素 num:
           将 num 插入到 minHeap 中
       
       当 minHeap 非空时:
           从 minHeap 弹出最小元素 num1
           从 minHeap 弹出下一个最小元素 num2
           将 num2 添加到 arr 中
           将 num1 添加到 arr 中
       
       返回 arr
   ```

4. 复杂度：
   - 时间复杂度：$O(n \log n)$，其中 $n$ 是数组的长度，因为每次插入和弹出堆的操作都是 $O(\log n)$，而我们需要对每个元素进行这样的操作。
   - 空间复杂度：$O(n)$，因为我们使用了一个额外的数组和堆来存储元素。