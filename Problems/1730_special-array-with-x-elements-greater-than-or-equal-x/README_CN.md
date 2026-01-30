# 1730. 特殊数组的特征值

**难度**: Easy | **标签**: `Array` `Binary Search` `Sorting`

## 题目描述

<p>给你一个非负整数数组 <code>nums</code> 。如果存在一个数 <code>x</code> ，使得 <code>nums</code> 中恰好有 <code>x</code> 个元素 <strong>大于或者等于</strong> <code>x</code> ，那么就称 <code>nums</code> 是一个 <strong>特殊数组</strong> ，而 <code>x</code> 是该数组的 <strong>特征值</strong> 。</p>

<p>注意： <code>x</code> <strong>不必</strong> 是 <code>nums</code> 的中的元素。</p>

<p>如果数组 <code>nums</code> 是一个 <strong>特殊数组</strong> ，请返回它的特征值 <code>x</code> 。否则，返回<em> </em><code>-1</code> 。可以证明的是，如果 <code>nums</code> 是特殊数组，那么其特征值 <code>x</code> 是 <strong>唯一的</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [3,5]
<strong>输出：</strong>2
<strong>解释：</strong>有 2 个元素（3 和 5）大于或等于 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [0,0]
<strong>输出：</strong>-1
<strong>解释：</strong>没有满足题目要求的特殊数组，故而也不存在特征值 x 。
如果 x = 0，应该有 0 个元素 &gt;= x，但实际有 2 个。
如果 x = 1，应该有 1 个元素 &gt;= x，但实际有 0 个。
如果 x = 2，应该有 2 个元素 &gt;= x，但实际有 0 个。
x 不能取更大的值，因为 nums 中只有两个元素。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [0,4,3,0,4]
<strong>输出：</strong>3
<strong>解释：</strong>有 3 个元素大于或等于 3 。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>nums = [3,6,7,7,0]
<strong>输出：</strong>-1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质**：通过排序和二分查找或线性扫描，寻找一个整数 \( x \) 使得数组中至少有 \( x \) 个元素大于等于 \( x \)。

2. **综合思路**：
   - **二分查找法**：对数组进行降序排序后，使用二分查找来确定特征值 \( x \)，通过计算大于等于 \( x \) 的元素个数来调整搜索区间。
   - **线性扫描法**：对数组进行降序排序后，线性扫描数组，检查每个可能的特征值 \( x \) 是否满足条件。

3. **全量伪代码**：
   - **二分查找法**：
     ```
     对数组进行降序排序
     初始化左右边界 left 和 right
     当 left 小于等于 right 时：
         计算中间值 guess
         初始化计数器 cnt 为 0
         对于数组中的每个元素 num：
             如果 num 大于等于 guess，增加计数器 cnt
         如果 cnt 等于 guess，返回 guess
         如果 cnt 大于 guess，更新 left 为 guess + 1
         如果 cnt 小于 guess，更新 right 为 guess - 1
     返回 -1
     ```
   - **线性扫描法**：
     ```
     对数组进行降序排序
     初始化索引 i 为 0
     当 i 小于数组长度时：
         如果 nums[i] 大于等于 i+1 且 (i+1 等于数组长度 或 nums[i+1] 小于 i+1)，返回 i+1
         增加索引 i
     返回 -1
     ```

4. **复杂度**：
   - **时间复杂度**：
     - 二分查找法：$O(n \log n)$，其中 $O(n \log n)$ 是排序的复杂度，$O(n)$ 是每次二分查找中计数的复杂度。
     - 线性扫描法：$O(n \log n)$，其中 $O(n \log n)$ 是排序的复杂度，$O(n)$ 是线性扫描的复杂度。
   - **空间复杂度**：
     - 所有版本的空间复杂度均为 $O(1)$，因为排序可以在原地进行，且只使用了常数级别的额外空间。