# 47. 全排列 II

**难度**: Medium | **标签**: `Array` `Backtracking` `Sorting`

## 题目描述

<p>给定一个可包含重复数字的序列 <code>nums</code> ，<em><strong>按任意顺序</strong></em> 返回所有不重复的全排列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,2]
<strong>输出：</strong>
[[1,1,2],
 [1,2,1],
 [2,1,1]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 8</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过深度优先搜索（DFS）结合排序和标记数组来生成不重复的全排列。

2. 综合思路：
   - **递归与DFS**：这两种实现都使用了递归和深度优先搜索（DFS）来生成排列。通过排序和一个标记数组来避免重复排列的生成。
   - **排序与标记数组**：在开始递归之前对数组进行排序，并使用一个标记数组来记录当前元素是否被使用过，以此来避免重复的排列。

3. 全量伪代码：
   ```plaintext
   定义函数 permuteUnique(nums):
       初始化结果列表 res
       初始化路径列表 path
       对 nums 进行排序
       初始化标记数组 used，长度为 nums 的长度，所有元素为 False
       调用 dfs(nums, used, path, res)
       返回 res

   定义函数 dfs(nums, used, path, res):
       如果 path 的长度等于 nums 的长度:
           将 path 的副本添加到 res 中
           返回

       对于 i 从 0 到 len(nums) - 1:
           如果 used[i] 为 True:
               跳过当前循环

           如果 i > 0 且 nums[i] 等于 nums[i-1] 且 used[i-1] 为 False:
               跳过当前循环

           将 nums[i] 添加到 path
           将 used[i] 设为 True

           递归调用 dfs(nums, used, path, res)

           从 path 中移除最后一个元素
           将 used[i] 设为 False
   ```

4. 复杂度：
   - 时间复杂度：$O(n! \cdot n)$，其中 $n$ 是输入数组的长度。排序的时间复杂度为 $O(n \log n)$，而生成全排列的复杂度为 $O(n! \cdot n)$，因为每个排列的生成和复制都需要 $O(n)$ 的时间。
   - 空间复杂度：$O(n)$，主要用于递归调用栈和标记数组。