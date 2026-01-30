# 113. 路径总和 II

**难度**: Medium | **标签**: `Backtracking` `Tree` `Depth-First Search` `Binary Tree`

## 题目描述

<p>给你二叉树的根节点 <code>root</code> 和一个整数目标和 <code>targetSum</code> ，找出所有 <strong>从根节点到叶子节点</strong> 路径总和等于给定目标和的路径。</p>

<p><strong>叶子节点</strong> 是指没有子节点的节点。</p>

<div class="original__bRMd">
<div>
<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg" style="width: 500px; height: 356px;" />
<pre>
<strong>输入：</strong>root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
<strong>输出：</strong>[[5,4,11,2],[5,8,4,5]]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg" style="width: 212px; height: 181px;" />
<pre>
<strong>输入：</strong>root = [1,2,3], targetSum = 5
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = [1,2], targetSum = 0
<strong>输出：</strong>[]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点总数在范围 <code>[0, 5000]</code> 内</li>
	<li><code>-1000 <= Node.val <= 1000</code></li>
	<li><code>-1000 <= targetSum <= 1000</code></li>
</ul>
</div>
</div>


---
## 解题思路与复盘

1. **一句话直击本质：** 使用深度优先搜索（DFS）遍历二叉树，记录路径和，找到所有路径和等于目标值的路径。

2. **综合思路：**
   - **递归 DFS：** 通过递归遍历二叉树，从根节点到叶子节点，累加路径上的节点值，并在叶子节点检查路径和是否等于目标值。
   - **路径记录：** 使用一个列表记录当前路径，遍历到叶子节点时，如果路径和满足条件，则将该路径加入结果集中。
   - **回溯：** 在递归返回时，移除当前节点以回溯到上一个状态，继续探索其他路径。

3. **全量伪代码：**

   ```plaintext
   定义函数 pathSum(root, targetSum):
       初始化结果列表 res
       初始化路径列表 path
       调用 dfs(root, targetSum, path, res)
       返回 res

   定义函数 dfs(node, targetSum, path, res):
       如果节点为空:
           返回

       将节点值添加到路径 path

       如果节点是叶子节点且路径和等于目标值:
           将路径的副本添加到结果 res

       递归调用 dfs(node.left, targetSum - node.val, path, res)
       递归调用 dfs(node.right, targetSum - node.val, path, res)

       从路径 path 中移除最后一个节点 (回溯)
   ```

4. **复杂度：**
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树中的节点数，因为每个节点访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是二叉树的高度，主要用于递归调用栈和存储路径。