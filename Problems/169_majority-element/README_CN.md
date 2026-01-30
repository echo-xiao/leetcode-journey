# 169. 多数元素

**难度**: Easy | **标签**: `Array` `Hash Table` `Divide and Conquer` `Sorting` `Counting`

## 题目描述

<p>给定一个大小为 <code>n</code><em> </em>的数组&nbsp;<code>nums</code> ，返回其中的多数元素。多数元素是指在数组中出现次数 <strong>大于</strong>&nbsp;<code>⌊ n/2 ⌋</code>&nbsp;的元素。</p>

<p>你可以假设数组是非空的，并且给定的数组总是存在多数元素。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,3]
<strong>输出：</strong>3</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,2,1,1,1,2,2]
<strong>输出：</strong>2
</pre>

<p>&nbsp;</p>
<strong>提示：</strong>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li>输入保证数组中一定有一个多数元素。</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。</p>


---
## 解题思路与复盘

1. 一句话直击本质：
   - 版本 1：通过递归分治法将数组分成左右两部分，分别找出多数元素并比较其出现次数。
   - 版本 2 和 3：使用 Boyer-Moore 投票算法，通过计数器维护当前候选多数元素。
   - 版本 4：使用哈希表记录每个元素的出现次数，找到超过半数的元素。

2. 综合思路：
   - 分治法（版本 1）：将数组递归地分成两部分，分别找出多数元素，然后比较两部分的多数元素的出现次数，返回出现次数较多的那个。
   - Boyer-Moore 投票算法（版本 2 和 3）：遍历数组，使用计数器维护一个候选多数元素，当计数器为零时更新候选元素，最终返回候选元素。
   - 哈希表法（版本 4）：遍历数组，用哈希表记录每个元素的出现次数，当某个元素的出现次数超过半数时，返回该元素。

3. 全量伪代码：
   - 分治法：
     ```
     函数 majorityElement(nums):
         如果 nums 的长度为 1:
             返回 nums[0]
         mid = nums 的长度 // 2
         left = majorityElement(nums 的前半部分)
         right = majorityElement(nums 的后半部分)
         如果 left 出现的次数 >= right 出现的次数:
             返回 left
         否则:
             返回 right
     ```
   - Boyer-Moore 投票算法：
     ```
     函数 majorityElement(nums):
         初始化 cnt 为 0
         初始化 candidate 为 None
         对于 nums 中的每个元素 i:
             如果 cnt 为 0:
                 candidate = i
             如果 i 等于 candidate:
                 cnt 增加 1
             否则:
                 cnt 减少 1
         返回 candidate
     ```
   - 哈希表法：
     ```
     函数 majorityElement(nums):
         初始化 seen 为空字典
         对于 nums 中的每个元素 i:
             如果 i 不在 seen 中:
                 seen[i] = 1
             否则:
                 seen[i] 增加 1
             如果 seen[i] > len(nums) // 2:
                 返回 i
     ```

4. 复杂度：
   - 分治法（版本 1）：时间复杂度 $O(n \log n)$，空间复杂度 $O(\log n)$。
   - Boyer-Moore 投票算法（版本 2 和 3）：时间复杂度 $O(n)$，空间复杂度 $O(1)$。
   - 哈希表法（版本 4）：时间复杂度 $O(n)$，空间复杂度 $O(n)$。