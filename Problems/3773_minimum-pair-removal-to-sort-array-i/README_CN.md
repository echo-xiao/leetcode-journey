# 3773. 移除最小数对使数组有序 I

**难度**: Easy | **标签**: `Array` `Hash Table` `Linked List` `Heap (Priority Queue)` `Simulation` `Doubly-Linked List` `Ordered Set`

## 题目描述

<p>给你一个数组 <code>nums</code>，你可以执行以下操作任意次数：</p>

<ul>
	<li>选择 <strong>相邻&nbsp;</strong>元素对中 <strong>和最小</strong> 的一对。如果存在多个这样的对，选择最左边的一个。</li>
	<li>用它们的和替换这对元素。</li>
</ul>

<p>返回将数组变为&nbsp;<strong>非递减&nbsp;</strong>所需的&nbsp;<strong>最小操作次数&nbsp;</strong>。</p>

<p>如果一个数组中每个元素都大于或等于它前一个元素（如果存在的话），则称该数组为<strong>非递减</strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [5,2,3,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>元素对 <code>(3,1)</code> 的和最小，为 4。替换后&nbsp;<code>nums = [5,2,4]</code>。</li>
	<li>元素对 <code>(2,4)</code> 的和为 6。替换后&nbsp;<code>nums = [5,6]</code>。</li>
</ul>

<p>数组 <code>nums</code> 在两次操作后变为非递减。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,2]</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p>数组 <code>nums</code> 已经是非递减的。</p>
</div>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>-1000&nbsp;&lt;= nums[i] &lt;= 1000</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过不断移除和最小的相邻数对并将其和插入原位置，逐步使数组变为非递减顺序。

2. 综合思路：
   - 迭代法：通过循环检查数组是否为非递减顺序，如果不是，则找到和最小的相邻数对，将其移除并将其和插入原位置，直到数组有序。

3. 全量伪代码：
   ```
   定义函数 minimumPairRemoval(nums):
       初始化计数器 cnt 为 0
       当数组未排序时:
           初始化标志 if_non_decreasing 为 True
           遍历数组，检查是否为非递减顺序:
               如果发现 nums[j] > nums[j+1]:
                   设置 if_non_decreasing 为 False
                   退出循环
           如果数组已经有序:
               退出循环
           初始化最小和 min_sum 为一个很大的数
           遍历数组，寻找和最小的相邻数对:
               计算当前相邻数对的和 tmp_sum
               如果 tmp_sum 小于 min_sum:
                   更新 min_sum 和对应的索引 tmp_index
           从数组中移除该相邻数对
           在原位置插入其和 min_sum
           计数器 cnt 增加 1
       返回计数器 cnt
   ```

4. 复杂度：
   - 时间复杂度：$O(n^2)$，因为每次移除数对后需要重新遍历数组以检查是否有序和寻找最小和的数对。
   - 空间复杂度：$O(1)$，因为算法在原地修改数组，不需要额外的空间。