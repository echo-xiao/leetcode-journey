# 3788. 删除后的最大子数组元素和

**难度**: Easy | **标签**: `Array` `Hash Table` `Greedy`

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>你可以从数组 <code>nums</code> 中删除任意数量的元素，但不能将其变为 <strong>空</strong> 数组。执行删除操作后，选出&nbsp;<code>nums</code>&nbsp;中满足下述条件的一个子数组：</p>

<ol>
	<li>子数组中的所有元素 <strong>互不相同</strong> 。</li>
	<li><strong>最大化</strong> 子数组的元素和。</li>
</ol>

<p>返回子数组的 <strong>最大元素和</strong> 。</p>
<strong>子数组</strong> 是数组的一个连续、<strong>非空</strong> 的元素序列。

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,3,4,5]</span></p>

<p><span class="example-io"><b>输出：</b>15</span></p>

<p><b>解释：</b></p>

<p>不删除任何元素，选中整个数组得到最大元素和。</p>
</div>

<p><b>示例 2：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span><span class="example-io">nums = [1,1,0,1,1]</span></p>

<p><span class="example-io"><b>输出：</b></span>1</p>

<p><b>解释：</b></p>

<p>删除元素&nbsp;<code>nums[0] == 1</code>、<code>nums[1] == 1</code>、<code>nums[2] == 0</code>&nbsp;和&nbsp;<code>nums[3] == 1</code>&nbsp;。选中整个数组&nbsp;<code>[1]</code>&nbsp;得到最大元素和。</p>
</div>

<p><b>示例 3：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span><span class="example-io">nums = [1,2,-1,-2,1,0,-1]</span></p>

<p><span class="example-io"><b>输出：</b></span>3</p>

<p><b>解释：</b></p>

<p>删除元素&nbsp;<code>nums[2] == -1</code>&nbsp;和&nbsp;<code>nums[3] == -2</code>&nbsp;，从&nbsp;<code>[1, 2, 1, 0, -1]</code>&nbsp;中选中子数组&nbsp;<code>[2, 1]</code>&nbsp;以获得最大元素和。</p>
</div>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过将数组转换为集合去重后，计算所有非负数的和，或者返回最大负数。

2. 综合思路：
   - **集合去重与迭代求和**：将数组转换为集合以去重，然后迭代集合中的元素，计算所有非负数的和。如果集合中所有元素均为负数，则返回最大负数。
   - **最大值判断**：首先判断集合中的最大值是否为正数，以决定是计算非负数的和还是直接返回最大负数。

3. 全量伪代码：
   ```
   定义函数 maxSum(nums):
       将 nums 转换为集合 arr 去重
       初始化结果 res 为 0
       找到集合 arr 中的最大值 maxVal

       如果 maxVal 大于 0:
           对于集合 arr 中的每个元素 i:
               如果 i 大于等于 0:
                   将 i 加到 res 上
           返回 res
       否则:
           返回 maxVal
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是输入数组的长度。转换为集合和迭代集合的操作都是线性的。
   - 空间复杂度：$O(n)$，用于存储集合 arr。