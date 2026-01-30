# 1047. K 次取反后最大化的数组和

**难度**: Easy | **标签**: `Array` `Greedy` `Sorting`

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个整数 <code>k</code> ，按以下方法修改该数组：</p>

<ul>
	<li>选择某个下标 <code>i</code>&nbsp;并将 <code>nums[i]</code> 替换为 <code>-nums[i]</code> 。</li>
</ul>

<p>重复这个过程恰好 <code>k</code> 次。可以多次选择同一个下标 <code>i</code> 。</p>

<p>以这种方式修改数组后，返回数组 <strong>可能的最大和</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,2,3], k = 1
<strong>输出：</strong>5
<strong>解释：</strong>选择下标 1 ，nums 变为 [4,-2,3] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,-1,0,2], k = 3
<strong>输出：</strong>6
<strong>解释：</strong>选择下标 (1, 2, 2) ，nums 变为 [3,1,0,2] 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,-3,-1,5,-4], k = 2
<strong>输出：</strong>13
<strong>解释：</strong>选择下标 (1, 4) ，nums 变为 [2,3,-1,5,4] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过每次取反当前数组中最小的数，逐步增加数组的总和。

2. 综合思路：
   - **贪心算法**：每次将数组中最小的数取反，因为取反最小的负数或最小的正数能最大化当前的增量。
   - **排序与迭代**：每次排序数组以找到当前最小的数，然后进行取反操作，重复此过程 $k$ 次。

3. 全量伪代码：
   ```plaintext
   定义函数 largestSumAfterKNegations(nums, k):
       当 k > 0 时重复以下步骤：
           将数组 nums 按升序排序
           将 nums 的第一个元素取反
           将 k 减 1
       返回数组 nums 的元素和
   ```

4. 复杂度：
   - 时间复杂度：$O(k \cdot n \log n)$，因为每次取反都需要对数组进行排序。
   - 空间复杂度：$O(1)$，因为排序操作是就地进行的，不需要额外的存储空间。