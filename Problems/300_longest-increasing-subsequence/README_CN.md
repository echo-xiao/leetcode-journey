# 300. 最长递增子序列

**难度**: Medium | **标签**: `Array` `Binary Search` `Dynamic Programming`

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，找到其中最长严格递增子序列的长度。</p>

<p><strong>子序列&nbsp;</strong>是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，<code>[3,6,2,7]</code> 是数组 <code>[0,3,1,6,2,2,7]</code> 的<span data-keyword="subsequence-array">子序列</span>。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [10,9,2,5,3,7,101,18]
<strong>输出：</strong>4
<strong>解释：</strong>最长递增子序列是 [2,3,7,101]，因此长度为 4 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1,0,3,2,3]
<strong>输出：</strong>4
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [7,7,7,7,7,7,7]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2500</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><b>进阶：</b></p>

<ul>
	<li>你能将算法的时间复杂度降低到&nbsp;<code>O(n log(n))</code> 吗?</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过维护一个递增序列的尾部数组，使用二分查找来高效更新该数组，从而找到最长递增子序列的长度。

2. **综合思路：**
   - **动态规划 + 二分查找：** 维护一个数组 `tail`，其中 `tail[i]` 表示长度为 `i+1` 的递增子序列的最小可能结尾元素。遍历输入数组 `nums`，对于每个元素 `num`，使用二分查找在 `tail` 中找到第一个大于等于 `num` 的位置并更新，或者将 `num` 添加到 `tail` 的末尾。
   - **直接遍历：** 直接遍历 `nums`，对于每个元素，使用二分查找在 `tail` 中找到合适的位置进行更新。

3. **全量伪代码：**

   ```plaintext
   方法 lengthOfLIS(nums):
       如果 nums 为空，返回 0
       初始化 tail 数组，包含第一个元素 nums[0]
       
       对于 nums 中的每个元素 num:
           如果 num 大于 tail 的最后一个元素:
               将 num 添加到 tail 的末尾
           否则:
               找到 tail 中第一个大于等于 num 的位置 idx
               将 tail[idx] 更新为 num
       
       返回 tail 的长度

   方法 insertToTail(tail, num):
       初始化 left 为 0，right 为 tail 的长度减 1
       当 left 小于等于 right 时:
           计算 mid 为 left 和 right 的中间位置
           如果 tail[mid] 大于等于 num:
               将 right 更新为 mid 减 1
           否则:
               将 left 更新为 mid 加 1
       返回 left
   ```

4. **复杂度：**

   - **时间复杂度：** $O(n \log n)$，其中 $n$ 是输入数组 `nums` 的长度。每个元素都需要通过二分查找更新 `tail` 数组，二分查找的时间复杂度为 $O(\log n)$。
   - **空间复杂度：** $O(n)$，用于存储 `tail` 数组，最坏情况下 `tail` 的长度与 `nums` 相同。