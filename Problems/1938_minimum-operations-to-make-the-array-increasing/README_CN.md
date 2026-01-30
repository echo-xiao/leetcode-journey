# 1938. 最少操作使数组递增

**难度**: Easy | **标签**: `Array` `Greedy`

## 题目描述

<p>给你一个整数数组 <code>nums</code> （<strong>下标从 0 开始</strong>）。每一次操作中，你可以选择数组中一个元素，并将它增加 <code>1</code> 。</p>

<ul>
	<li>比方说，如果 <code>nums = [1,2,3]</code> ，你可以选择增加 <code>nums[1]</code> 得到 <code>nums = [1,<b>3</b>,3]</code> 。</li>
</ul>

<p>请你返回使 <code>nums</code> <strong>严格递增</strong> 的 <strong>最少</strong> 操作次数。</p>

<p>我们称数组 <code>nums</code> 是 <strong>严格递增的</strong> ，当它满足对于所有的 <code>0 &lt;= i &lt; nums.length - 1</code> 都有 <code>nums[i] &lt; nums[i+1]</code> 。一个长度为 <code>1</code> 的数组是严格递增的一种特殊情况。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [1,1,1]
<b>输出：</b>3
<b>解释：</b>你可以进行如下操作：
1) 增加 nums[2] ，数组变为 [1,1,<strong>2</strong>] 。
2) 增加 nums[1] ，数组变为 [1,<strong>2</strong>,2] 。
3) 增加 nums[2] ，数组变为 [1,2,<strong>3</strong>] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [1,5,2,4,1]
<b>输出：</b>14
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums = [8]
<b>输出：</b>0
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过遍历数组，逐步调整每个元素以确保其大于前一个元素，并累加所需的操作次数。

2. 综合思路：
   - 迭代法：遍历数组，从第二个元素开始，检查当前元素是否大于前一个元素，如果不是，则调整当前元素并记录调整次数。
   - 递归法：虽然题目中没有递归实现，但可以通过递归方式处理，即从后向前递归检查并调整元素。

3. 全量伪代码：
   ```
   定义函数 minOperations(nums):
       初始化操作计数器 cnt 为 0
       从第二个元素开始遍历数组 nums:
           如果当前元素小于等于前一个元素:
               计算需要增加的值为 前一个元素 + 1 - 当前元素
               将当前元素更新为 前一个元素 + 1
               将增加的值累加到操作计数器 cnt
       返回操作计数器 cnt
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是数组的长度，因为我们需要遍历整个数组一次。
   - 空间复杂度：$O(1)$，因为我们只使用了常数个额外变量。