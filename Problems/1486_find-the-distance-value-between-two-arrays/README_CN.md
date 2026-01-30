# 1486. 两个数组间的距离值

**难度**: Easy | **标签**: `Array` `Two Pointers` `Binary Search` `Sorting`

## 题目描述

<p>给你两个整数数组&nbsp;<code>arr1</code>&nbsp;，&nbsp;<code>arr2</code>&nbsp;和一个整数&nbsp;<code>d</code>&nbsp;，请你返回两个数组之间的&nbsp;<strong>距离值</strong>&nbsp;。</p>

<p>「<strong>距离值</strong>」<strong>&nbsp;</strong>定义为符合此距离要求的元素数目：对于元素&nbsp;<code>arr1[i]</code>&nbsp;，不存在任何元素&nbsp;<code>arr2[j]</code>&nbsp;满足 <code>|arr1[i]-arr2[j]| &lt;= d</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
<strong>输出：</strong>2
<strong>解释：</strong>
对于 arr1[0]=4 我们有：
|4-10|=6 &gt; d=2 
|4-9|=5 &gt; d=2 
|4-1|=3 &gt; d=2 
|4-8|=4 &gt; d=2 
所以 arr1[0]=4 符合距离要求

对于 arr1[1]=5 我们有：
|5-10|=5 &gt; d=2 
|5-9|=4 &gt; d=2 
|5-1|=4 &gt; d=2 
|5-8|=3 &gt; d=2
所以 arr1[1]=5 也符合距离要求

对于 arr1[2]=8 我们有：
<strong>|8-10|=2 &lt;= d=2</strong>
<strong>|8-9|=1 &lt;= d=2</strong>
|8-1|=7 &gt; d=2
<strong>|8-8|=0 &lt;= d=2</strong>
存在距离小于等于 2 的情况，不符合距离要求 

故而只有 arr1[0]=4 和 arr1[1]=5 两个符合距离要求，距离值为 2</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr1.length, arr2.length &lt;= 500</code></li>
	<li><code>-10^3 &lt;= arr1[i], arr2[j] &lt;= 10^3</code></li>
	<li><code>0 &lt;= d &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过排序和二分查找或直接遍历来判断数组元素之间的距离是否超过给定阈值。

2. 综合思路：
   - **排序 + 二分查找**：首先对 `arr2` 进行排序，然后对于 `arr1` 中的每个元素，使用二分查找在 `arr2` 中找到不小于 `arr1[i] - d` 的最小元素位置，检查该位置的元素是否小于等于 `arr1[i] + d`，从而判断是否存在满足条件的元素。
   - **直接遍历**：对于 `arr1` 中的每个元素，直接遍历 `arr2`，计算两者的绝对差值，如果差值小于等于 `d`，则跳出循环并减少计数。

3. 全量伪代码：
   - **排序 + 二分查找**：
     ```
     对 arr2 进行排序
     初始化计数器 cnt 为 0
     对于 arr1 中的每个元素 val1:
         计算 low = val1 - d 和 high = val1 + d
         使用二分查找在 arr2 中找到不小于 low 的最小元素位置 insert
         如果 insert 位置的元素小于等于 high:
             该元素在范围内，跳过
         否则:
             增加计数器 cnt
     返回 cnt
     ```
   - **直接遍历**：
     ```
     初始化计数器 k 为 arr1 的长度
     对于 arr1 中的每个元素 val1:
         对于 arr2 中的每个元素 val2:
             计算 dis = abs(val1 - val2)
             如果 dis <= d:
                 减少计数器 k
                 跳出内层循环
     返回 k
     ```

4. 复杂度：
   - **排序 + 二分查找**：
     - 时间复杂度：$O(n \log n + m \log n)$，其中 $n$ 是 `arr2` 的长度，$m$ 是 `arr1` 的长度。
     - 空间复杂度：$O(1)$，不需要额外的空间。
   - **直接遍历**：
     - 时间复杂度：$O(m \times n)$，其中 $m$ 是 `arr1` 的长度，$n$ 是 `arr2` 的长度。
     - 空间复杂度：$O(1)$，不需要额外的空间。