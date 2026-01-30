# 219. 存在重复元素 II

**难度**: Easy | **标签**: `Array` `Hash Table` `Sliding Window`

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code> 和一个整数&nbsp;<code>k</code> ，判断数组中是否存在两个 <strong>不同的索引</strong><em>&nbsp;</em><code>i</code>&nbsp;和<em>&nbsp;</em><code>j</code> ，满足 <code>nums[i] == nums[j]</code> 且 <code>abs(i - j) &lt;= k</code> 。如果存在，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,1], k<em> </em>= 3
<strong>输出：</strong>true</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,0,1,1], k<em> </em>=<em> </em>1
<strong>输出：</strong>true</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,1,2,3], k<em> </em>=<em> </em>2
<strong>输出：</strong>false</pre>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用滑动窗口和哈希集合来检查数组中是否存在两个索引的元素相等且索引差不超过给定的 k。

2. 综合思路：
   - 滑动窗口法：使用一个固定大小为 k 的窗口（通过哈希集合实现）来记录当前窗口内的元素，遍历数组时检查当前元素是否在集合中，如果在则返回 True，否则将其加入集合并移除窗口外的元素。
   - 哈希表法：虽然代码中没有直接实现哈希表，但滑动窗口的集合操作本质上与哈希表查找相似。

3. 全量伪代码：
   ```
   定义函数 containsNearbyDuplicate(nums, k)
       初始化一个空集合 seen
       遍历数组 nums 的每个元素，索引为 j
           如果 nums[j] 在集合 seen 中
               返回 True
           否则
               将 nums[j] 添加到集合 seen 中
           如果集合 seen 的大小大于 k
               从集合 seen 中移除 nums[j-k]
       返回 False
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 n 是数组 nums 的长度，因为每个元素最多被添加和移除集合一次。
   - 空间复杂度：$O(\min(n, k))$，因为集合 seen 的大小最多为 k。