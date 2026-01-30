# 713. 乘积小于 K 的子数组

**难度**: Medium | **标签**: `Array` `Binary Search` `Sliding Window` `Prefix Sum`

## 题目描述

给你一个整数数组 <code>nums</code> 和一个整数 <code>k</code> ，请你返回子数组内所有元素的乘积严格小于<em> </em><code>k</code> 的连续子数组的数目。
<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [10,5,2,6], k = 100
<strong>输出：</strong>8
<strong>解释：</strong>8 个乘积小于 100 的子数组分别为：[10]、[5]、[2]、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3], k = 0
<strong>输出：</strong>0</pre>

<p>&nbsp;</p>

<p><strong>提示:&nbsp;</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>6</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用滑动窗口维护一个乘积小于 K 的子数组范围，通过调整窗口的左右边界来计算满足条件的子数组数量。

2. 综合思路：
   - 滑动窗口：通过双指针（left 和 right）构成的滑动窗口，动态维护当前窗口内元素的乘积，当乘积大于等于 K 时，移动左指针缩小窗口，直到乘积小于 K，然后计算以当前右指针为结尾的所有子数组数量。

3. 全量伪代码：
   ```
   定义函数 numSubarrayProductLessThanK(nums, k):
       如果 k <= 1:
           返回 0

       初始化 left 为 0
       初始化 right 为 0
       初始化 res 为 1
       初始化 ans 为 0

       当 right 小于 nums 的长度时:
           将 res 乘以 nums[right]
           将 right 增加 1

           当 res 大于等于 k 时:
               将 res 除以 nums[left]
               将 left 增加 1

           将 ans 增加 (right - left)

       返回 ans
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是数组的长度。每个元素最多被访问两次（一次作为右边界，一次作为左边界）。
   - 空间复杂度：$O(1)$，只使用了常数个额外变量。