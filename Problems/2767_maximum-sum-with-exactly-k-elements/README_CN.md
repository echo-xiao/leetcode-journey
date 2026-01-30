# 2767. K 个元素的最大和

**难度**: Easy | **标签**: `Array` `Greedy`

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code> 和一个整数&nbsp;<code>k</code>&nbsp;。你需要执行以下操作<strong>&nbsp;恰好</strong> <code>k</code>&nbsp;次，最大化你的得分：</p>

<ol>
	<li>从 <code>nums</code>&nbsp;中选择一个元素&nbsp;<code>m</code>&nbsp;。</li>
	<li>将选中的元素&nbsp;<code>m</code>&nbsp;从数组中删除。</li>
	<li>将新元素&nbsp;<code>m + 1</code>&nbsp;添加到数组中。</li>
	<li>你的得分增加&nbsp;<code>m</code>&nbsp;。</li>
</ol>

<p>请你返回执行以上操作恰好 <code>k</code>&nbsp;次后的最大得分。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3,4,5], k = 3
<b>输出：</b>18
<b>解释：</b>我们需要从 nums 中恰好选择 3 个元素并最大化得分。
第一次选择 5 。和为 5 ，nums = [1,2,3,4,6] 。
第二次选择 6 。和为 6 ，nums = [1,2,3,4,7] 。
第三次选择 7 。和为 5 + 6 + 7 = 18 ，nums = [1,2,3,4,8] 。
所以我们返回 18 。
18 是可以得到的最大答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [5,5,5], k = 2
<b>输出：</b>11
<b>解释：</b>我们需要从 nums 中恰好选择 2 个元素并最大化得分。
第一次选择 5 。和为 5 ，nums = [5,5,6] 。
第二次选择 6 。和为 6 ，nums = [5,5,7] 。
所以我们返回 11 。
11 是可以得到的最大答案。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过排序找到最大元素，并利用等差数列求和公式计算前 K 个元素的最大和。

2. 综合思路：
   - 排序法：首先对数组进行排序，然后选择最大的元素，通过等差数列的求和公式计算前 K 个元素的最大和。
   - 直接选择法：直接遍历数组找到最大元素，然后同样利用等差数列求和公式计算结果。

3. 全量伪代码：
   ```plaintext
   方法：最大化和
   输入：整数数组 nums，整数 k
   输出：整数，前 K 个元素的最大和

   1. 对数组 nums 进行降序排序
   2. 选择排序后的第一个元素作为最大元素 max_num
   3. 计算结果为 (max_num + max_num + k - 1) * k // 2
   4. 返回结果
   ```

4. 复杂度：
   - 时间复杂度：$O(n \log n)$，其中 $n$ 是数组的长度，因为需要对数组进行排序。
   - 空间复杂度：$O(1)$，因为只使用了常数级别的额外空间。