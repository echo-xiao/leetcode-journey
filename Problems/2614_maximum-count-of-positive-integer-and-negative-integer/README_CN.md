# 2614. 正整数和负整数的最大计数

**难度**: Easy | **标签**: `Array` `Binary Search` `Counting`

## 题目描述

<p>给你一个按 <strong>非递减顺序</strong> 排列的数组 <code>nums</code> ，返回正整数数目和负整数数目中的最大值。</p>

<ul>
	<li>换句话讲，如果 <code>nums</code> 中正整数的数目是 <code>pos</code> ，而负整数的数目是 <code>neg</code> ，返回 <code>pos</code> 和 <code>neg</code>二者中的最大值。</li>
</ul>

<p><strong>注意：</strong><code>0</code> 既不是正整数也不是负整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [-2,-1,-1,1,2,3]
<strong>输出：</strong>3
<strong>解释：</strong>共有 3 个正整数和 3 个负整数。计数得到的最大值是 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [-3,-2,-1,0,0,1,2]
<strong>输出：</strong>3
<strong>解释：</strong>共有 2 个正整数和 3 个负整数。计数得到的最大值是 3 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,20,66,1314]
<strong>输出：</strong>4
<strong>解释：</strong>共有 4 个正整数和 0 个负整数。计数得到的最大值是 4 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2000</code></li>
	<li><code>-2000 &lt;= nums[i] &lt;= 2000</code></li>
	<li><code>nums</code> 按 <strong>非递减顺序</strong> 排列。</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你可以设计并实现时间复杂度为 <code>O(log(n))</code> 的算法解决此问题吗？</p>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过二分查找找到第一个非负数的位置，然后计算负数和正数的数量，返回两者中的最大值。

2. 综合思路：
   - 二分查找：所有版本都使用了二分查找来定位第一个非负数的位置。版本 1 使用递归实现二分查找，而版本 2 和版本 3 使用迭代实现。
   - 计数计算：在找到第一个非负数的位置后，通过简单的计数计算负数和正数的数量。

3. 全量伪代码：
   ```plaintext
   方法 maximumCount(nums):
       初始化 left 为 0, right 为 nums 的长度减 1
       当 left 小于等于 right 时:
           计算 mid 为 left 和 right 的中间索引
           如果 nums[mid] 大于等于 0:
               将 right 更新为 mid 减 1
           否则:
               将 left 更新为 mid 加 1

       计算 neg 为从索引 0 到 left 的元素数量
       当 left 小于 nums 的长度且 nums[left] 小于等于 0 时:
           增加 left
       计算 pos 为从 left 到 nums 末尾的元素数量

       返回 neg 和 pos 中的最大值

   方法 helper(nums, left, right):
       如果 left 大于 right:
           返回 left

       计算 mid 为 left 和 right 的中间索引
       如果 nums[mid] 大于等于 0:
           返回 helper(nums, left, mid-1)
       否则:
           返回 helper(nums, mid+1, right)
   ```

4. 复杂度：
   - 时间复杂度：$O(\log n)$，因为二分查找的时间复杂度为 $O(\log n)$，后续的计数操作为线性时间复杂度 $O(n)$，但由于二分查找是主导操作，所以整体复杂度为 $O(\log n)$。
   - 空间复杂度：$O(1)$，因为只使用了常数级别的额外空间。