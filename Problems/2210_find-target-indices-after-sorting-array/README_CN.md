# 2210. 找出数组排序后的目标下标

**难度**: Easy | **标签**: `Array` `Binary Search` `Sorting`

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 以及一个目标元素 <code>target</code> 。</p>

<p><strong>目标下标</strong> 是一个满足&nbsp;<code>nums[i] == target</code> 的下标 <code>i</code> 。</p>

<p>将 <code>nums</code> 按 <strong>非递减</strong> 顺序排序后，返回由 <code>nums</code> 中目标下标组成的列表。如果不存在目标下标，返回一个 <strong>空</strong> 列表。返回的列表必须按 <strong>递增</strong> 顺序排列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,5,2,3], target = 2
<strong>输出：</strong>[1,2]
<strong>解释：</strong>排序后，nums 变为 [1,<em><strong>2</strong></em>,<em><strong>2</strong></em>,3,5] 。
满足 nums[i] == 2 的下标是 1 和 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,5,2,3], target = 3
<strong>输出：</strong>[3]
<strong>解释：</strong>排序后，nums 变为 [1,2,2,<em><strong>3</strong></em>,5] 。
满足 nums[i] == 3 的下标是 3 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,5,2,3], target = 5
<strong>输出：</strong>[4]
<strong>解释：</strong>排序后，nums 变为 [1,2,2,3,<em><strong>5</strong></em>] 。
满足 nums[i] == 5 的下标是 4 。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,5,2,3], target = 4
<strong>输出：</strong>[]
<strong>解释：</strong>nums 中不含值为 4 的元素。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i], target &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过对数组进行排序后，使用二分查找或线性扫描来找到目标值的起始下标，并收集所有目标值的下标。

2. **综合思路：**
   - **二分查找法：** 先对数组进行排序，然后使用二分查找找到目标值的起始下标，再通过线性扫描收集所有目标值的下标。
   - **线性扫描法：** 先对数组进行排序，然后直接通过线性扫描找到所有目标值的下标。

3. **全量伪代码：**

   - **排序数组：**
     ```
     对数组 nums 进行排序
     ```

   - **二分查找法：**
     ```
     初始化 left 为 0，right 为数组长度减 1
     当 left 小于等于 right 时：
         计算 mid 为 left 和 right 的中间索引
         如果 nums[mid] 大于等于 target：
             将 right 更新为 mid - 1
         否则：
             将 left 更新为 mid + 1
     初始化结果列表 res
     当 left 小于数组长度且 nums[left] 等于 target 时：
         将 left 添加到 res
         将 left 增加 1
     返回 res
     ```

   - **递归二分查找法：**
     ```
     定义递归函数 helper(nums, target, left, right):
         如果 left 大于 right：
             返回 left
         计算 mid 为 left 和 right 的中间索引
         如果 nums[mid] 大于等于 target：
             返回 helper(nums, target, left, mid-1)
         否则：
             返回 helper(nums, target, mid+1, right)
     调用 helper 函数获取目标值的起始下标
     初始化结果列表 res
     当 left 小于数组长度且 nums[left] 等于 target 时：
         将 left 添加到 res
         将 left 增加 1
     返回 res
     ```

   - **线性扫描法：**
     ```
     初始化结果列表 res
     初始化索引 i 为 0
     当 i 小于数组长度时：
         如果 nums[i] 等于 target：
             将 i 添加到 res
             将 i 增加 1
         如果 nums[i] 大于 target：
             终止循环
         如果 nums[i] 小于 target：
             将 i 增加 1
     返回 res
     ```

4. **复杂度：**

   - **时间复杂度：** $O(n \log n)$，其中 $n$ 是数组的长度，因为需要对数组进行排序。
   - **空间复杂度：** $O(1)$，如果不考虑排序所需的额外空间，或者 $O(n)$，如果排序算法需要额外的空间。