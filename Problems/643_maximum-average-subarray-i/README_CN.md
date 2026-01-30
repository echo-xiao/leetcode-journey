# 643. 子数组最大平均数 I

**难度**: Easy | **标签**: `Array` `Sliding Window`

## 题目描述

<p>给你一个由 <code>n</code> 个元素组成的整数数组 <code>nums</code> 和一个整数 <code>k</code> 。</p>

<p>请你找出平均数最大且 <strong>长度为 <code>k</code></strong> 的连续子数组，并输出该最大平均数。</p>

<p>任何误差小于 <code>10<sup>-5</sup></code> 的答案都将被视为正确答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,12,-5,-6,50,3], k = 4
<strong>输出：</strong>12.75
<strong>解释：</strong>最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [5], k = 1
<strong>输出：</strong>5.00000
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= k &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法通过滑动窗口技术计算固定长度子数组的和，并在每次移动窗口时更新最大和以找到最大平均值。

2. 综合思路：
   - 滑动窗口：通过维护一个长度为 `k` 的滑动窗口，计算窗口内元素的和，并在每次移动窗口时更新和，最终找到最大和对应的平均值。
   - 该题目主要采用滑动窗口的迭代方法，没有递归或其他复杂数据结构的使用。

3. 全量伪代码：
   ```
   初始化 right 为 k-1，left 为 0
   初始化 msum 为一个很小的数
   计算初始窗口（从 left 到 right）的和 ksum
   将 msum 更新为 ksum

   对于 right 从 k 到 nums 的长度 - 1，执行以下步骤：
       更新 ksum 为 ksum 加上 nums[right] 减去 nums[left]
       更新 msum 为 msum 和 ksum 中的较大值
       将 left 增加 1

   返回 msum 除以 k 的结果作为最大平均值
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是数组 `nums` 的长度，因为我们只需遍历数组一次。
   - 空间复杂度：$O(1)$，因为我们只使用了常数个额外变量来存储和、最大和等信息。