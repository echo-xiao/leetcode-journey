# 112. 路径总和

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`

## 题目描述

<p>给你二叉树的根节点&nbsp;<code>root</code> 和一个表示目标和的整数&nbsp;<code>targetSum</code> 。判断该树中是否存在 <strong>根节点到叶子节点</strong> 的路径，这条路径上所有节点值相加等于目标和&nbsp;<code>targetSum</code> 。如果存在，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p><strong>叶子节点</strong> 是指没有子节点的节点。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg" style="width: 500px; height: 356px;" />
<pre>
<strong>输入：</strong>root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
<strong>输出：</strong>true
<strong>解释：</strong>等于目标和的根节点到叶节点路径如上图所示。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg" />
<pre>
<strong>输入：</strong>root = [1,2,3], targetSum = 5
<strong>输出：</strong>false
<strong>解释：</strong>树中存在两条根节点到叶子节点的路径：
(1 --&gt; 2): 和为 3
(1 --&gt; 3): 和为 4
不存在 sum = 5 的根节点到叶子节点的路径。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = [], targetSum = 0
<strong>输出：</strong>false
<strong>解释：</strong>由于树是空的，所以不存在根节点到叶子节点的路径。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点的数目在范围 <code>[0, 5000]</code> 内</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
	<li><code>-1000 &lt;= targetSum &lt;= 1000</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过递归或迭代遍历二叉树，检查从根节点到叶子节点的路径和是否等于目标值。

2. **综合思路：**
   - **递归解法：** 通过递归遍历树，逐步减少目标和，检查在叶子节点时路径和是否等于目标值。
   - **迭代解法（未在提供的代码中出现，但作为补充）：** 使用栈或队列进行深度优先搜索（DFS）或广度优先搜索（BFS），在遍历过程中计算路径和。

3. **全量伪代码：**

   - **递归解法：**
     ```
     函数 hasPathSum(节点 root, 整数 targetSum):
         如果 root 为空:
             返回 False
         
         计算当前路径和: sumVal = targetSum - root.val
         
         如果 root 是叶子节点:
             返回 sumVal 是否等于 0
         
         返回 hasPathSum(root.left, sumVal) 或 hasPathSum(root.right, sumVal)
     ```

   - **迭代解法（DFS）：**
     ```
     函数 hasPathSum(节点 root, 整数 targetSum):
         如果 root 为空:
             返回 False
         
         初始化栈 stack，初始元素为 (root, root.val)
         
         当栈不为空时:
             弹出栈顶元素 (node, currentSum)
             
             如果 node 是叶子节点且 currentSum 等于 targetSum:
                 返回 True
             
             如果 node.right 存在:
                 将 (node.right, currentSum + node.right.val) 压入栈
             
             如果 node.left 存在:
                 将 (node.left, currentSum + node.left.val) 压入栈
         
         返回 False
     ```

4. **复杂度：**
   - **时间复杂度：** $O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点都需要访问一次。
   - **空间复杂度：** $O(h)$，其中 $h$ 是二叉树的高度，递归调用栈或迭代栈的最大深度。对于平衡树，$h = \log n$；对于不平衡树，$h = n$。