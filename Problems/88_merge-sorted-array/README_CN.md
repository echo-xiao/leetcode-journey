# 88. 合并两个有序数组

**难度**: Easy | **标签**: `Array` `Two Pointers` `Sorting`

## 题目描述

<p>给你两个按 <strong>非递减顺序</strong> 排列的整数数组&nbsp;<code>nums1</code><em> </em>和 <code>nums2</code>，另有两个整数 <code>m</code> 和 <code>n</code> ，分别表示 <code>nums1</code> 和 <code>nums2</code> 中的元素数目。</p>

<p>请你 <strong>合并</strong> <code>nums2</code><em> </em>到 <code>nums1</code> 中，使合并后的数组同样按 <strong>非递减顺序</strong> 排列。</p>

<p><strong>注意：</strong>最终，合并后数组不应由函数返回，而是存储在数组 <code>nums1</code> 中。为了应对这种情况，<code>nums1</code> 的初始长度为 <code>m + n</code>，其中前 <code>m</code> 个元素表示应合并的元素，后 <code>n</code> 个元素为 <code>0</code> ，应忽略。<code>nums2</code> 的长度为 <code>n</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
<strong>输出：</strong>[1,2,2,3,5,6]
<strong>解释：</strong>需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [<em><strong>1</strong></em>,<em><strong>2</strong></em>,2,<em><strong>3</strong></em>,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1], m = 1, nums2 = [], n = 0
<strong>输出：</strong>[1]
<strong>解释：</strong>需要合并 [1] 和 [] 。
合并结果是 [1] 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [0], m = 0, nums2 = [1], n = 1
<strong>输出：</strong>[1]
<strong>解释：</strong>需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>nums1.length == m + n</code></li>
	<li><code>nums2.length == n</code></li>
	<li><code>0 &lt;= m, n &lt;= 200</code></li>
	<li><code>1 &lt;= m + n &lt;= 200</code></li>
	<li><code>-10<sup>9</sup> &lt;= nums1[i], nums2[j] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你可以设计实现一个时间复杂度为 <code>O(m + n)</code> 的算法解决此问题吗？</p>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过从后向前遍历两个数组，将较大的元素放入目标数组的末尾，从而实现原地合并。

2. **综合思路：**
   - **迭代法：** 使用双指针从两个数组的末尾开始比较，将较大的元素放入 `nums1` 的末尾，并移动指针，直到所有元素合并完成。
   - **特殊处理：** 如果 `nums2` 中还有剩余元素（即 `nums1` 已经遍历完），则直接将 `nums2` 中的剩余元素复制到 `nums1` 的前面。

3. **全量伪代码：**

   ```
   定义函数 merge(nums1, m, nums2, n):
       初始化指针 p1 为 m-1, p2 为 n-1, i 为 m+n-1
       当 p1 和 p2 都大于等于 0 时:
           如果 nums1[p1] 大于等于 nums2[p2]:
               将 nums1[p1] 赋值给 nums1[i]
               将 p1 减 1
           否则:
               将 nums2[p2] 赋值给 nums1[i]
               将 p2 减 1
           将 i 减 1
       如果 p2 大于等于 0:
           当 p2 大于等于 0 时:
               将 nums2[p2] 赋值给 nums1[i]
               将 p2 减 1
               将 i 减 1
   ```

4. **复杂度：**

   - 时间复杂度：$O(m + n)$，因为每个元素最多被访问一次。
   - 空间复杂度：$O(1)$，因为合并是在 `nums1` 上原地进行的，不需要额外的空间。