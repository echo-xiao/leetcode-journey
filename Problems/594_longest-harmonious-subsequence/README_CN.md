# 594. 最长和谐子序列

**难度**: Easy | **标签**: `Array` `Hash Table` `Sliding Window` `Sorting` `Counting`

## 题目描述

<p>和谐数组是指一个数组里元素的最大值和最小值之间的差别 <strong>正好是 <code>1</code></strong> 。</p>

<p>给你一个整数数组 <code>nums</code> ，请你在所有可能的 <span data-keyword="subsequence-array">子序列</span> 中找到最长的和谐子序列的长度。</p>

<p>数组的 <strong>子序列</strong> 是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [1,3,2,2,5,2,3,7]</span></p>

<p><span class="example-io"><b>输出：</b>5</span></p>

<p><strong>解释：</strong></p>

<p>最长和谐子序列是&nbsp;<code>[3,2,2,2,3]</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,3,4]</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p>最长和谐子序列是&nbsp;<code>[1,2]</code>，<code>[2,3]</code>&nbsp;和&nbsp;<code>[3,4]</code>，长度都为 2。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [1,1,1,1]</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><strong>解释：</strong></p>

<p>不存在和谐子序列。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过排序和双指针或哈希表来找到数组中最长的和谐子序列。

2. 综合思路：
   - **排序 + 双指针**：首先对数组进行排序，然后使用双指针遍历数组，寻找差值为1的最长子序列。
   - **哈希表**：使用哈希表记录每个数字出现的次数，然后检查每个数字与其相邻数字的组合长度，找出最大值。

3. 全量伪代码：
   - **排序 + 双指针**：
     ```
     对数组进行排序
     初始化左指针left和右指针right为0
     初始化最大长度max_length为0
     当右指针小于数组长度时：
         如果nums[right] - nums[left] == 1：
             更新max_length为当前最大值
         如果nums[right] - nums[left] > 1：
             增加左指针
         增加右指针
     返回max_length
     ```
   - **哈希表**：
     ```
     初始化哈希表seen为空
     初始化最大长度max_len为0
     遍历数组：
         如果数字在哈希表中，增加其计数
         否则，将其加入哈希表并计数为1
         如果数字-1在哈希表中：
             计算当前和谐子序列长度sum_len1
         如果数字+1在哈希表中：
             计算当前和谐子序列长度sum_len2
         更新max_len为当前最大值
     返回max_len
     ```

4. 复杂度：
   - **排序 + 双指针**：
     - 时间复杂度：$O(n \log n)$，因为需要对数组进行排序。
     - 空间复杂度：$O(1)$，如果不考虑排序所需的额外空间。
   - **哈希表**：
     - 时间复杂度：$O(n)$，因为只需遍历数组一次。
     - 空间复杂度：$O(n)$，因为需要存储每个数字的计数。