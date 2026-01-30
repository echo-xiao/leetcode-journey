# 658. 找到 K 个最接近的元素

**难度**: Medium | **标签**: `Array` `Two Pointers` `Binary Search` `Sliding Window` `Sorting` `Heap (Priority Queue)`

## 题目描述

<p>给定一个 <strong>排序好</strong> 的数组&nbsp;<code>arr</code> ，两个整数 <code>k</code> 和 <code>x</code> ，从数组中找到最靠近 <code>x</code>（两数之差最小）的 <code>k</code> 个数。返回的结果必须要是按升序排好的。</p>

<p>整数 <code>a</code> 比整数 <code>b</code> 更接近 <code>x</code> 需要满足：</p>

<ul>
	<li><code>|a - x| &lt; |b - x|</code> 或者</li>
	<li><code>|a - x| == |b - x|</code> 且 <code>a &lt; b</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2,3,4,5], k = 4, x = 3
<strong>输出：</strong>[1,2,3,4]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,1,2,3,4,5], k = 4, x = -1
<strong>输出：</strong>[1,1,2,3]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= arr.length</code></li>
	<li><code>1 &lt;= arr.length&nbsp;&lt;= 10<sup>4</sup></code><meta charset="UTF-8" /></li>
	<li><code>arr</code>&nbsp;按 <strong>升序</strong> 排列</li>
	<li><code>-10<sup>4</sup>&nbsp;&lt;= arr[i], x &lt;= 10<sup>4</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过双指针收缩窗口的方法，找到数组中与目标值最接近的连续子数组。

2. 综合思路：
   - 双指针法：使用两个指针分别指向数组的起始和末尾，通过比较两端元素与目标值的距离，逐步收缩窗口，直到窗口大小为 k。
   - 二分查找法（未在提供的代码中出现，但常见于此类问题）：通过二分查找确定最接近目标值的起始位置，然后直接截取长度为 k 的子数组。

3. 全量伪代码：
   - 双指针法：
     ```
     初始化左指针为 0，右指针为数组长度减 1
     当窗口大小大于 k 时，重复以下步骤：
         如果左端元素与目标值的距离大于右端元素与目标值的距离：
             将左指针右移一位
         否则：
             将右指针左移一位
     返回从左指针到右指针的子数组
     ```
   - 二分查找法（假设存在）：
     ```
     初始化左指针为 0，右指针为数组长度减 k
     当左指针小于右指针时，重复以下步骤：
         计算中间位置 mid
         如果目标值与 arr[mid] 的距离大于目标值与 arr[mid + k] 的距离：
             将左指针移动到 mid + 1
         否则：
             将右指针移动到 mid
     返回从左指针开始长度为 k 的子数组
     ```

4. 复杂度：
   - 双指针法的时间复杂度为 $O(n)$，空间复杂度为 $O(1)$。
   - 二分查找法的时间复杂度为 $O(\log(n-k) + k)$，空间复杂度为 $O(1)$。