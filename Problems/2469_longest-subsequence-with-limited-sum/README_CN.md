# 2469. 和有限的最长子序列

**难度**: Easy | **标签**: `Array` `Binary Search` `Greedy` `Sorting` `Prefix Sum`

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;的整数数组 <code>nums</code> ，和一个长度为 <code>m</code> 的整数数组 <code>queries</code> 。</p>

<p>返回一个长度为 <code>m</code> 的数组<em> </em><code>answer</code><em> </em>，其中<em> </em><code>answer[i]</code><em> </em>是 <code>nums</code> 中<span style=""> </span>元素之和小于等于 <code>queries[i]</code> 的 <strong>子序列</strong> 的 <strong>最大</strong> 长度<span style="">&nbsp;</span><span style=""> </span>。</p>

<p><strong>子序列</strong> 是由一个数组删除某些元素（也可以不删除）但不改变剩余元素顺序得到的一个数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,5,2,1], queries = [3,10,21]
<strong>输出：</strong>[2,3,4]
<strong>解释：</strong>queries 对应的 answer 如下：
- 子序列 [2,1] 的和小于或等于 3 。可以证明满足题目要求的子序列的最大长度是 2 ，所以 answer[0] = 2 。
- 子序列 [4,5,1] 的和小于或等于 10 。可以证明满足题目要求的子序列的最大长度是 3 ，所以 answer[1] = 3 。
- 子序列 [4,5,2,1] 的和小于或等于 21 。可以证明满足题目要求的子序列的最大长度是 4 ，所以 answer[2] = 4 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,3,4,5], queries = [1]
<strong>输出：</strong>[0]
<strong>解释：</strong>空子序列是唯一一个满足元素和小于或等于 1 的子序列，所以 answer[0] = 0 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>m == queries.length</code></li>
	<li><code>1 &lt;= n, m &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i], queries[i] &lt;= 10<sup>6</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过对数组进行排序并使用前缀和或二分查找来确定满足条件的最长子序列长度。

2. 综合思路：
   - **贪心算法**：通过排序数组并逐个累加元素，直到累加和超过目标值为止，确定最长子序列长度。
   - **前缀和与二分查找**：先计算数组的前缀和，然后使用二分查找来快速确定满足条件的最长子序列长度。

3. 全量伪代码：
   - **贪心算法**：
     ```
     对数组进行排序
     初始化结果列表 res
     对于每个查询 target:
         初始化总和 ttl 为 0，长度 length 为 0
         对于数组中的每个元素 num:
             如果 ttl + num <= target:
                 增加 ttl 和 length
             否则:
                 跳出循环
         将 length 添加到 res
     返回 res
     ```
   - **前缀和与二分查找**：
     ```
     对数组进行排序
     计算数组的前缀和
     初始化结果列表 res
     对于每个查询 target:
         初始化左右指针 left 和 right
         使用二分查找:
             计算中间位置 mid
             如果前缀和 nums[mid] <= target:
                 更新 left
             否则:
                 更新 right
         将 left 或者 length 添加到 res
     返回 res
     ```

4. 复杂度：
   - **时间复杂度**：
     - 贪心算法：$O(n \log n + m \cdot n)$，其中 $n$ 是数组长度，$m$ 是查询数目。
     - 前缀和与二分查找：$O(n \log n + m \log n)$。
   - **空间复杂度**：
     - 贪心算法：$O(1)$，不考虑输入和输出。
     - 前缀和与二分查找：$O(n)$，用于存储前缀和。