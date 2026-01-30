# 2112. 学生分数的最小差值

**难度**: Easy | **标签**: `Array` `Sliding Window` `Sorting`

## 题目描述

<p>给你一个 <strong>下标从 0 开始</strong> 的整数数组 <code>nums</code> ，其中 <code>nums[i]</code> 表示第 <code>i</code> 名学生的分数。另给你一个整数 <code>k</code> 。</p>

<p>从数组中选出任意 <code>k</code> 名学生的分数，使这 <code>k</code> 个分数间 <strong>最高分</strong> 和 <strong>最低分</strong> 的 <strong>差值</strong> 达到<strong> 最小化</strong> 。</p>

<p>返回可能的 <strong>最小差值</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [90], k = 1
<strong>输出：</strong>0
<strong>解释：</strong>选出 1 名学生的分数，仅有 1 种方法：
- [<em><strong>90</strong></em>] 最高分和最低分之间的差值是 90 - 90 = 0
可能的最小差值是 0
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [9,4,1,7], k = 2
<strong>输出：</strong>2
<strong>解释：</strong>选出 2 名学生的分数，有 6 种方法：
- [<em><strong>9</strong></em>,<em><strong>4</strong></em>,1,7] 最高分和最低分之间的差值是 9 - 4 = 5
- [<em><strong>9</strong></em>,4,<em><strong>1</strong></em>,7] 最高分和最低分之间的差值是 9 - 1 = 8
- [<em><strong>9</strong></em>,4,1,<em><strong>7</strong></em>] 最高分和最低分之间的差值是 9 - 7 = 2
- [9,<em><strong>4</strong></em>,<em><strong>1</strong></em>,7] 最高分和最低分之间的差值是 4 - 1 = 3
- [9,<em><strong>4</strong></em>,1,<em><strong>7</strong></em>] 最高分和最低分之间的差值是 7 - 4 = 3
- [9,4,<em><strong>1</strong></em>,<em><strong>7</strong></em>] 最高分和最低分之间的差值是 7 - 1 = 6
可能的最小差值是 2</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过排序数组并使用滑动窗口技术，找到长度为 k 的子数组中最大值与最小值的最小差值。

2. 综合思路：
   - 排序 + 滑动窗口：首先对数组进行排序，然后使用滑动窗口技术遍历数组，计算每个长度为 k 的子数组的最大值与最小值的差值，并记录最小的差值。

3. 全量伪代码：
   ```
   函数 minimumDifference(数组 nums, 整数 k):
       将数组 nums 进行排序
       初始化 j 为 0
       初始化 min_diff 为一个很大的数

       对于 i 从 k-1 到 nums 的长度 - 1:
           计算当前窗口 win 为 nums 从 j 到 i 的子数组
           计算当前窗口的差值 diff 为 nums[i] - nums[j]
           如果 diff 小于 min_diff:
               更新 min_diff 为 diff
           j 增加 1

       返回 min_diff
   ```

4. 复杂度：
   - 时间复杂度：$O(n \log n)$，其中 $n$ 是数组的长度，因为排序操作的时间复杂度为 $O(n \log n)$，而滑动窗口的遍历为 $O(n)$。
   - 空间复杂度：$O(1)$，因为只使用了常数级别的额外空间。