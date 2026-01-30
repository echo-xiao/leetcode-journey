# 46. 全排列

**难度**: Medium | **标签**: `Array` `Backtracking`

## 题目描述

<p>给定一个不含重复数字的数组 <code>nums</code> ，返回其 <em>所有可能的全排列</em> 。你可以 <strong>按任意顺序</strong> 返回答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1]
<strong>输出：</strong>[[0,1],[1,0]]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1]
<strong>输出：</strong>[[1]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 6</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li><code>nums</code> 中的所有整数 <strong>互不相同</strong></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：全排列算法的核心逻辑是通过递归深度优先搜索（DFS）构建所有可能的排列组合。

2. 综合思路：
   - 递归与DFS：所有版本都使用递归和深度优先搜索（DFS）来生成全排列。通过递归调用，逐步构建排列，当排列长度达到输入数组长度时，将其加入结果集。
   - 使用标记数组：版本1使用一个布尔数组来标记哪些元素已经被使用，以避免重复使用。
   - 使用路径检查：版本2和3通过检查当前路径中是否已经包含某个元素来避免重复使用。

3. 全量伪代码：
   - 使用标记数组的递归DFS：
     ```
     定义函数 permute(nums):
         初始化结果列表 res
         初始化路径列表 path
         初始化使用标记数组 used 为 False
         调用 dfs(nums, used, path, res)
         返回 res

     定义函数 dfs(nums, used, path, res):
         如果路径长度等于 nums 长度:
             将路径的副本加入结果列表 res
             返回

         对于每个索引 i 从 0 到 nums 长度 - 1:
             如果 used[i] 为 True:
                 跳过当前循环

             将 nums[i] 加入路径
             将 used[i] 设为 True

             递归调用 dfs(nums, used, path, res)

             从路径中移除最后一个元素
             将 used[i] 设为 False
     ```

   - 使用路径检查的递归DFS：
     ```
     定义函数 permute(nums):
         初始化结果列表 res
         初始化路径列表 path
         调用 dfs(nums, path, res)
         返回 res

     定义函数 dfs(nums, path, res):
         如果路径长度等于 nums 长度:
             将路径的副本加入结果列表 res
             返回

         对于 nums 中的每个元素 n:
             如果 n 在路径中:
                 跳过当前循环

             将 n 加入路径

             递归调用 dfs(nums, path, res)

             从路径中移除最后一个元素
     ```

4. 复杂度：
   - 时间复杂度：$O(n \times n!)$，因为每个排列的生成需要 $O(n)$ 的时间，而总共有 $n!$ 个排列。
   - 空间复杂度：$O(n)$，用于递归调用栈和路径存储。