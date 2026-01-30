# 718. 最长重复子数组

**难度**: Medium | **标签**: `Array` `Binary Search` `Dynamic Programming` `Sliding Window` `Rolling Hash` `Hash Function`

## 题目描述

<p>给两个整数数组&nbsp;<code>nums1</code>&nbsp;和&nbsp;<code>nums2</code>&nbsp;，返回 <em>两个数组中 <strong>公共的</strong> 、长度最长的子数组的长度&nbsp;</em>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
<strong>输出：</strong>3
<strong>解释：</strong>长度最长的公共子数组是 [3,2,1] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
<strong>输出：</strong>5
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过滑动窗口比较两个数组的不同起始位置的子数组，寻找最长的重复子数组。

2. 综合思路：
   - 滑动窗口：通过在两个数组上滑动窗口，逐个比较不同起始位置的子数组，计算最长的重复子数组长度。
   - 动态规划（未在给定代码集中出现，但常见解法）：利用二维动态规划数组记录以每对元素结尾的最长公共子数组长度。

3. 全量伪代码：
   - 滑动窗口方法：
     ```
     初始化 n 为 nums1 的长度，m 为 nums2 的长度，最大长度 ret 为 0
     对于 nums1 的每个起始位置 i：
         计算当前比较的长度 length 为 min(m, n-i)
         调用 getMaxLen 函数，获取从 nums1[i] 和 nums2[0] 开始的最长重复子数组长度 currLen
         更新 ret 为 max(ret, currLen)
     对于 nums2 的每个起始位置 i：
         计算当前比较的长度 length 为 min(n, m-i)
         调用 getMaxLen 函数，获取从 nums1[0] 和 nums2[i] 开始的最长重复子数组长度 currLen
         更新 ret 为 max(ret, currLen)
     返回 ret

     getMaxLen 函数：
     初始化计数器 cnt 为 0，最大值 maxVal 为 0
     对于长度 length 内的每个索引 i：
         如果 nums1[addA + i] 等于 nums2[addB + i]：
             增加 cnt
             更新 maxVal 为 max(maxVal, cnt)
         否则：
             重置 cnt 为 0
     返回 maxVal
     ```

4. 复杂度：
   - 时间复杂度：$O((n+m) \cdot \min(n, m))$，其中 $n$ 和 $m$ 分别是两个数组的长度。
   - 空间复杂度：$O(1)$，因为只使用了常数额外空间。