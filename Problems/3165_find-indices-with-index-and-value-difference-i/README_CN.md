# 3165. 找出满足差值条件的下标 I

**难度**: Easy | **标签**: `Array` `Two Pointers`

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的整数数组 <code>nums</code> ，以及整数 <code>indexDifference</code> 和整数 <code>valueDifference</code> 。</p>

<p>你的任务是从范围 <code>[0, n - 1]</code> 内找出&nbsp; <strong>2</strong> 个满足下述所有条件的下标 <code>i</code> 和 <code>j</code> ：</p>

<ul>
	<li><code>abs(i - j) &gt;= indexDifference</code> 且</li>
	<li><code>abs(nums[i] - nums[j]) &gt;= valueDifference</code></li>
</ul>

<p>返回整数数组 <code>answer</code>。如果存在满足题目要求的两个下标，则 <code>answer = [i, j]</code> ；否则，<code>answer = [-1, -1]</code> 。如果存在多组可供选择的下标对，只需要返回其中任意一组即可。</p>

<p><strong>注意：</strong><code>i</code> 和 <code>j</code> 可能 <strong>相等</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,1,4,1], indexDifference = 2, valueDifference = 4
<strong>输出：</strong>[0,3]
<strong>解释：</strong>在示例中，可以选择 i = 0 和 j = 3 。
abs(0 - 3) &gt;= 2 且 abs(nums[0] - nums[3]) &gt;= 4 。
因此，[0,3] 是一个符合题目要求的答案。
[3,0] 也是符合题目要求的答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,1], indexDifference = 0, valueDifference = 0
<strong>输出：</strong>[0,0]
<strong>解释：</strong>
在示例中，可以选择 i = 0 和 j = 0 。 
abs(0 - 0) &gt;= 0 且 abs(nums[0] - nums[0]) &gt;= 0 。 
因此，[0,0] 是一个符合题目要求的答案。 
[0,1]、[1,0] 和 [1,1] 也是符合题目要求的答案。 
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3], indexDifference = 2, valueDifference = 4
<strong>输出：</strong>[-1,-1]
<strong>解释：</strong>在示例中，可以证明无法找出 2 个满足所有条件的下标。
因此，返回 [-1,-1] 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 50</code></li>
	<li><code>0 &lt;= indexDifference &lt;= 100</code></li>
	<li><code>0 &lt;= valueDifference &lt;= 50</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过遍历数组，寻找满足给定索引差和数值差条件的两个下标。

2. 综合思路：
   - **版本 1**：使用滑动窗口的思想，通过维护当前窗口内的最小和最大值的索引，快速判断是否满足条件。
   - **版本 2**：使用双重循环暴力搜索所有可能的索引对，检查是否满足条件。

3. 全量伪代码：
   - **版本 1 伪代码**：
     ```
     初始化 min_idx 和 max_idx 为 0
     遍历数组从 indexDifference 到 n-1 的每个元素 j：
         计算 i = j - indexDifference
         如果 nums[i] 小于 nums[min_idx]，更新 min_idx 为 i
         如果 nums[i] 大于 nums[max_idx]，更新 max_idx 为 i
         如果 nums[j] 与 nums[min_idx] 的差值大于等于 valueDifference，返回 [min_idx, j]
         如果 nums[j] 与 nums[max_idx] 的差值大于等于 valueDifference，返回 [max_idx, j]
     如果没有找到满足条件的下标对，返回 [-1, -1]
     ```
   - **版本 2 伪代码**：
     ```
     初始化空列表 answer
     遍历数组的每个元素 i：
         从 i + indexDifference 开始遍历数组的每个元素 j：
             如果 i 和 j 的索引差大于等于 indexDifference 且 nums[i] 和 nums[j] 的值差大于等于 valueDifference：
                 更新 answer 为 [i, j]
     如果 answer 为空，返回 [-1, -1]
     否则，返回 answer
     ```

4. 复杂度：
   - **版本 1**：
     - 时间复杂度：$O(n)$，因为每个元素最多被访问两次。
     - 空间复杂度：$O(1)$，只使用了常数个额外变量。
   - **版本 2**：
     - 时间复杂度：$O(n^2)$，因为使用了双重循环遍历所有可能的索引对。
     - 空间复杂度：$O(1)$，只使用了常数个额外变量。