# 2707. 合并两个二维数组 - 求和法

**难度**: Easy | **标签**: `Array` `Hash Table` `Two Pointers`

## 题目描述

<p>给你两个 <strong>二维</strong> 整数数组 <code>nums1</code> 和 <code>nums2.</code></p>

<ul>
	<li><code>nums1[i] = [id<sub>i</sub>, val<sub>i</sub>]</code> 表示编号为 <code>id<sub>i</sub></code> 的数字对应的值等于 <code>val<sub>i</sub></code> 。</li>
	<li><code>nums2[i] = [id<sub>i</sub>, val<sub>i</sub>]</code>&nbsp;表示编号为 <code>id<sub>i</sub></code> 的数字对应的值等于 <code>val<sub>i</sub></code> 。</li>
</ul>

<p>每个数组都包含 <strong>互不相同</strong> 的 id ，并按 id 以 <strong>递增</strong> 顺序排列。</p>

<p>请你将两个数组合并为一个按 id 以递增顺序排列的数组，并符合下述条件：</p>

<ul>
	<li>只有在两个数组中至少出现过一次的 id 才能包含在结果数组内。</li>
	<li>每个 id 在结果数组中 <strong>只能出现一次</strong> ，并且其对应的值等于两个数组中该 id 所对应的值求和。如果某个数组中不存在该 id ，则假定其对应的值等于 <code>0</code> 。</li>
</ul>

<p>返回结果数组。返回的数组需要按 id 以递增顺序排列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
<strong>输出：</strong>[[1,6],[2,3],[3,2],[4,6]]
<strong>解释：</strong>结果数组中包含以下元素：
- id = 1 ，对应的值等于 2 + 4 = 6 。
- id = 2 ，对应的值等于 3 。
- id = 3 ，对应的值等于 2 。
- id = 4 ，对应的值等于 5 + 1 = 6 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
<strong>输出：</strong>[[1,3],[2,4],[3,6],[4,3],[5,5]]
<strong>解释：</strong>不存在共同 id ，在结果数组中只需要包含每个 id 和其对应的值。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 200</code></li>
	<li><code>nums1[i].length == nums2[j].length == 2</code></li>
	<li><code>1 &lt;= id<sub>i</sub>, val<sub>i</sub> &lt;= 1000</code></li>
	<li>数组中的 id 互不相同</li>
	<li>数据均按 id 以严格递增顺序排列</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过双指针遍历两个有序二维数组，合并相同索引的元素并求和，不同索引的元素直接添加到结果中。

2. 综合思路：
   - 双指针法：使用两个指针分别遍历两个数组，根据索引值的大小关系决定如何合并或添加元素。
   - 迭代法：通过循环迭代的方式实现合并操作，确保所有元素都被处理。

3. 全量伪代码：
   ```
   初始化指针 i 和 j 为 0，结果数组 nums 为空
   当 i 和 j 都在各自数组范围内时：
       如果 nums1[i] 的索引等于 nums2[j] 的索引：
           合并两个元素的值并添加到结果数组
           增加 i 和 j
       否则如果 nums1[i] 的索引大于 nums2[j] 的索引：
           将 nums2[j] 添加到结果数组
           增加 j
       否则：
           将 nums1[i] 添加到结果数组
           增加 i
   当 i 超出 nums1 范围而 j 在 nums2 范围内时：
       将 nums2[j] 添加到结果数组
       增加 j
   当 j 超出 nums2 范围而 i 在 nums1 范围内时：
       将 nums1[i] 添加到结果数组
       增加 i
   返回结果数组 nums
   ```

4. 复杂度：
   - 时间复杂度：$O(n + m)$，其中 $n$ 和 $m$ 分别是两个数组的长度，因为每个元素最多被访问一次。
   - 空间复杂度：$O(n + m)$，用于存储合并后的结果数组。