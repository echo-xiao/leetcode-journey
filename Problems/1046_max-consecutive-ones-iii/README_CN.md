# 1046. 最大连续1的个数 III

**难度**: Medium | **标签**: `Array` `Binary Search` `Sliding Window` `Prefix Sum`

## 题目描述

<p>给定一个二进制数组&nbsp;<code>nums</code>&nbsp;和一个整数 <code>k</code>，假设最多可以翻转 <code>k</code> 个 <code>0</code> ，则返回执行操作后 <em>数组中连续 <code>1</code> 的最大个数</em> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
<strong>输出：</strong>6
<strong>解释：</strong>[1,1,1,0,0,<strong>1</strong>,1,1,1,1,<strong>1</strong>]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
<strong>输出：</strong>10
<strong>解释：</strong>[0,0,1,1,<strong>1</strong>,<strong>1</strong>,1,1,1,<strong>1</strong>,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code>&nbsp;不是&nbsp;<code>0</code>&nbsp;就是&nbsp;<code>1</code></li>
	<li><code>0 &lt;= k &lt;= nums.length</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用滑动窗口技术，通过调整窗口的左右边界来保持窗口内最多包含 $k$ 个零，从而找到最长的连续1的子数组。

2. 综合思路：
   - 滑动窗口：通过双指针（`left` 和 `right`）构建一个动态窗口，右指针扩展窗口，左指针收缩窗口以确保窗口内的零不超过 $k$ 个。
   - 其他可能解法（未在给定代码中出现）：可以考虑使用二分查找来优化某些场景，但滑动窗口是最直接且高效的解决方案。

3. 全量伪代码：
   ```plaintext
   初始化 left 和 right 指针为 0
   初始化 maxLen 为 0
   初始化 cnt 为 0  // 用于记录窗口内0的个数

   当 right 小于数组长度时，重复以下步骤：
       如果 nums[right] 是 0，则增加 cnt
       增加 right 指针

       当 cnt 大于 k 时，重复以下步骤：
           如果 nums[left] 是 0，则减少 cnt
           增加 left 指针

       更新 maxLen 为 max(maxLen, right - left)

   返回 maxLen
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是数组的长度，因为每个元素最多被访问两次（一次由右指针，一次由左指针）。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外变量。