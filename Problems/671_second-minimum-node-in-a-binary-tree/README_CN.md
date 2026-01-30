# 671. 二叉树中第二小的节点

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Binary Tree`

## 题目描述

<p>给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为&nbsp;<code>2</code>&nbsp;或&nbsp;<code>0</code>。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。</p>

<p>更正式地说，即&nbsp;<code>root.val = min(root.left.val, root.right.val)</code> 总成立。</p>

<p>给出这样的一个二叉树，你需要输出所有节点中的&nbsp;<strong>第二小的值 </strong>。</p>

<p>如果第二小的值不存在的话，输出 -1 <strong>。</strong></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/smbt1.jpg" style="height: 210px; width: 300px;" />
<pre>
<strong>输入：</strong>root = [2,2,5,null,null,5,7]
<strong>输出：</strong>5
<strong>解释：</strong>最小的值是 2 ，第二小的值是 5 。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/smbt2.jpg" style="height: 113px; width: 200px;" />
<pre>
<strong>输入：</strong>root = [2,2,2]
<strong>输出：</strong>-1
<strong>解释：</strong>最小的值是 2, 但是不存在第二小的值。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目在范围 <code>[1, 25]</code> 内</li>
	<li><code>1 &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
	<li>对于树中每个节点 <code>root.val == min(root.left.val, root.right.val)</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过遍历二叉树，寻找大于根节点值的最小节点值作为第二小的节点值。

2. **综合思路：**
   - **递归遍历（DFS）：** 使用深度优先搜索递归遍历整棵树，记录大于根节点值的最小值。此方法在遍历过程中可以进行剪枝，即当发现一个节点值大于根节点值时，不再继续遍历其子节点。
   - **迭代遍历（BFS）：** 虽然在提供的代码中没有出现，但可以使用广度优先搜索的方式遍历树，逐层检查节点值，更新大于根节点值的最小值。

3. **全量伪代码：**

   ```plaintext
   定义类 Solution:
       定义方法 findSecondMinimumValue(根节点):
           如果根节点为空:
               返回 -1

           初始化最小值 min1 为根节点值
           初始化第二小值 second_min 为正无穷

           调用递归函数 dfs(根节点)

           如果 second_min 未被更新:
               返回 -1
           否则:
               返回 second_min

       定义递归函数 dfs(节点):
           如果节点为空:
               返回

           如果节点值大于 min1:
               更新 second_min 为节点值和 second_min 的较小值
               返回

           递归调用 dfs(节点的左子节点)
           递归调用 dfs(节点的右子节点)
   ```

4. **复杂度：**
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树中的节点数，因为每个节点最多访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是二叉树的高度，递归调用栈的深度取决于树的高度。