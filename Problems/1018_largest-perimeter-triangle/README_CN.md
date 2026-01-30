# 1018. 三角形的最大周长

**难度**: Easy | **标签**: `Array` `Math` `Greedy` `Sorting`

## 题目描述

<p>给定由一些正数（代表长度）组成的数组 <code>nums</code>&nbsp;，返回 <em>由其中三个长度组成的、<strong>面积不为零</strong>的三角形的最大周长</em>&nbsp;。如果不能形成任何面积不为零的三角形，返回&nbsp;<code>0</code>。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,1,2]
<strong>输出：</strong>5
<strong>解释：</strong>你可以用三个边长组成一个三角形:1 2 2。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,1,10]
<strong>输出：</strong>0
<strong>解释：</strong>
你不能用边长 1,1,2 来组成三角形。
不能用边长 1,1,10 来构成三角形。
不能用边长 1、2 和 10 来构成三角形。
因为我们不能用任何三条边长来构成一个非零面积的三角形，所以我们返回 0。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过排序数组并检查最大的三个连续边是否能构成三角形，以找到最大周长。

2. 综合思路：
   - 排序与贪心：将数组从大到小排序，然后从最大的三个边开始检查是否能构成三角形，找到第一个满足条件的即为最大周长。
   - 该题目主要采用贪心策略，通过排序后从大到小检查，确保找到的第一个满足条件的三角形即为最大周长。

3. 全量伪代码：
   ```
   函数 largestPerimeter(数组 nums):
       将 nums 按降序排序
       对于 i 从 0 到 len(nums) - 3:
           如果 nums[i] < nums[i+1] + nums[i+2]:
               返回 nums[i] + nums[i+1] + nums[i+2]
       返回 0
   ```

4. 复杂度：
   - 时间复杂度：$O(n \log n)$，其中 $n$ 是数组的长度，主要来自于排序操作。
   - 空间复杂度：$O(1)$，只使用了常数级别的额外空间。