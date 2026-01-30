# 2416. 计算布尔二叉树的值

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Binary Tree`

## 题目描述

<p>给你一棵 <strong>完整二叉树</strong>&nbsp;的根，这棵树有以下特征：</p>

<ul>
	<li><strong>叶子节点</strong>&nbsp;要么值为&nbsp;<code>0</code>&nbsp;要么值为&nbsp;<code>1</code>&nbsp;，其中&nbsp;<code>0</code> 表示&nbsp;<code>False</code>&nbsp;，<code>1</code> 表示&nbsp;<code>True</code>&nbsp;。</li>
	<li><strong>非叶子节点 </strong>要么值为 <code>2</code>&nbsp;要么值为 <code>3</code>&nbsp;，其中&nbsp;<code>2</code>&nbsp;表示逻辑或&nbsp;<code>OR</code> ，<code>3</code>&nbsp;表示逻辑与&nbsp;<code>AND</code>&nbsp;。</li>
</ul>

<p><strong>计算</strong>&nbsp;一个节点的值方式如下：</p>

<ul>
	<li>如果节点是个叶子节点，那么节点的 <strong>值</strong>&nbsp;为它本身，即&nbsp;<code>True</code>&nbsp;或者&nbsp;<code>False</code>&nbsp;。</li>
	<li>否则，<strong>计算</strong>&nbsp;两个孩子的节点值，然后将该节点的运算符对两个孩子值进行 <strong>运算</strong>&nbsp;。</li>
</ul>

<p>返回根节点<em>&nbsp;</em><code>root</code>&nbsp;的布尔运算值。</p>

<p><strong>完整二叉树</strong>&nbsp;是每个节点有 <code>0</code>&nbsp;个或者 <code>2</code>&nbsp;个孩子的二叉树。</p>

<p><strong>叶子节点</strong>&nbsp;是没有孩子的节点。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/05/16/example1drawio1.png" style="width: 700px; height: 252px;"></p>

<pre><b>输入：</b>root = [2,1,3,null,null,0,1]
<b>输出：</b>true
<b>解释：</b>上图展示了计算过程。
AND 与运算节点的值为 False AND True = False 。
OR 运算节点的值为 True OR False = True 。
根节点的值为 True ，所以我们返回 true 。</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>root = [0]
<b>输出：</b>false
<b>解释：</b>根节点是叶子节点，且值为 false，所以我们返回 false 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目在&nbsp;<code>[1, 1000]</code>&nbsp;之间。</li>
	<li><code>0 &lt;= Node.val &lt;= 3</code></li>
	<li>每个节点的孩子数为&nbsp;<code>0</code> 或&nbsp;<code>2</code>&nbsp;。</li>
	<li>叶子节点的值为&nbsp;<code>0</code>&nbsp;或&nbsp;<code>1</code>&nbsp;。</li>
	<li>非叶子节点的值为&nbsp;<code>2</code>&nbsp;或&nbsp;<code>3</code> 。</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过递归遍历布尔二叉树，根据节点值执行相应的逻辑运算（或运算、与运算）来计算树的布尔值。

2. **综合思路：**
   - **递归解法：** 所有版本都使用递归方法遍历二叉树。递归地计算左右子树的布尔值，然后根据当前节点的值（0, 1, 2, 3）执行相应的布尔运算。
   - **DFS（深度优先搜索）：** 递归本质上是一种深度优先搜索，所有版本都采用这种方式。
   - **数据结构：** 使用二叉树结构，其中每个节点包含一个值和指向左右子节点的指针。

3. **全量伪代码：**
   ```plaintext
   定义函数 evaluateTree(root):
       如果 root 是叶子节点:
           如果 root.val 是 1:
               返回 True
           否则:
               返回 False

       递归计算左子树的布尔值 leftCheck = evaluateTree(root.left)
       递归计算右子树的布尔值 rightCheck = evaluateTree(root.right)

       如果 root.val 是 2 (表示 OR 操作):
           返回 leftCheck 或 rightCheck
       如果 root.val 是 3 (表示 AND 操作):
           返回 leftCheck 且 rightCheck
   ```

4. **复杂度：**
   - **时间复杂度：** $O(n)$，其中 $n$ 是二叉树中的节点数，因为每个节点都需要被访问一次。
   - **空间复杂度：** $O(h)$，其中 $h$ 是二叉树的高度，递归调用栈的深度与树的高度成正比。对于平衡树，$h = O(\log n)$；对于不平衡树，最坏情况是 $h = O(n)$。