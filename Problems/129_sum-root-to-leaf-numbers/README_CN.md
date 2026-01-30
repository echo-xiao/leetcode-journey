# 129. 求根节点到叶节点数字之和

**难度**: Medium | **标签**: `Tree` `Depth-First Search` `Binary Tree`

## 题目描述

给你一个二叉树的根节点 <code>root</code> ，树中每个节点都存放有一个 <code>0</code> 到 <code>9</code> 之间的数字。
<div class="original__bRMd">
<div>
<p>每条从根节点到叶节点的路径都代表一个数字：</p>

<ul>
	<li>例如，从根节点到叶节点的路径 <code>1 -> 2 -> 3</code> 表示数字 <code>123</code> 。</li>
</ul>

<p>计算从根节点到叶节点生成的 <strong>所有数字之和</strong> 。</p>

<p><strong>叶节点</strong> 是指没有子节点的节点。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg" style="width: 212px; height: 182px;" />
<pre>
<strong>输入：</strong>root = [1,2,3]
<strong>输出：</strong>25
<strong>解释：</strong>
从根到叶子节点路径 <code>1->2</code> 代表数字 <code>12</code>
从根到叶子节点路径 <code>1->3</code> 代表数字 <code>13</code>
因此，数字总和 = 12 + 13 = <code>25</code></pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg" style="width: 292px; height: 302px;" />
<pre>
<strong>输入：</strong>root = [4,9,0,5,1]
<strong>输出：</strong>1026
<strong>解释：</strong>
从根到叶子节点路径 <code>4->9->5</code> 代表数字 495
从根到叶子节点路径 <code>4->9->1</code> 代表数字 491
从根到叶子节点路径 <code>4->0</code> 代表数字 40
因此，数字总和 = 495 + 491 + 40 = <code>1026</code>
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点的数目在范围 <code>[1, 1000]</code> 内</li>
	<li><code>0 <= Node.val <= 9</code></li>
	<li>树的深度不超过 <code>10</code></li>
</ul>
</div>
</div>


---
## 解题思路与复盘

1. **一句话直击本质：**  
   通过深度优先搜索（DFS）遍历二叉树，将路径上的节点值累积成数字，并在到达叶节点时累加到总和。

2. **综合思路：**  
   所有给出的版本都采用了递归的深度优先搜索（DFS）方法，没有涉及迭代或广度优先搜索（BFS）的实现。DFS通过递归遍历每个节点，构建从根到叶节点的路径数字，并在叶节点处返回该路径的数字值。以下是不同解法的简述：
   - **递归 DFS：** 通过递归函数遍历树，累积路径上的数字值，遇到叶节点时返回累积的数字值。
   - **路径累积：** 在递归过程中，将当前节点的值与之前累积的值结合成新的数字，传递给子节点。
   - **叶节点判断：** 当节点没有左子节点和右子节点时，认为该节点是叶节点，返回当前累积的数字。

3. **全量伪代码：**  
   以下是所有 AC 版本中涉及的不同类型逻辑的中文伪代码：
   ```plaintext
   定义函数 sumNumbers(root):
       返回 dfs(root, 0)

   定义函数 dfs(node, currSum):
       如果 node 是空:
           返回 0

       更新 currSum 为 currSum * 10 + node.val

       如果 node 是叶节点 (没有左子节点和右子节点):
           返回 currSum

       计算左子树的和 leftSum = dfs(node.left, currSum)
       计算右子树的和 rightSum = dfs(node.right, currSum)

       返回 leftSum + rightSum
   ```

4. **复杂度：**  
   - **时间复杂度：** $O(n)$，其中 $n$ 是二叉树中的节点数。每个节点在递归中被访问一次。
   - **空间复杂度：** $O(h)$，其中 $h$ 是二叉树的高度。递归调用栈的深度取决于树的高度。对于平衡树，$h = \log n$；对于不平衡树，$h = n$。