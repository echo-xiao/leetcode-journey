# 257. 二叉树的所有路径

**难度**: Easy | **标签**: `String` `Backtracking` `Tree` `Depth-First Search` `Binary Tree`

## 题目描述

<p>给你一个二叉树的根节点 <code>root</code> ，按 <strong>任意顺序</strong> ，返回所有从根节点到叶子节点的路径。</p>

<p><strong>叶子节点</strong> 是指没有子节点的节点。</p>
&nbsp;

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg" style="width: 207px; height: 293px;" />
<pre>
<strong>输入：</strong>root = [1,2,3,null,5]
<strong>输出：</strong>["1-&gt;2-&gt;5","1-&gt;3"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = [1]
<strong>输出：</strong>["1"]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点的数目在范围 <code>[1, 100]</code> 内</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过深度优先搜索（DFS）遍历二叉树，将每条从根到叶节点的路径记录为字符串。

2. 综合思路：
   - 递归 DFS：所有版本都采用递归的深度优先搜索方法，遍历每个节点时构建路径字符串，当到达叶节点时将路径添加到结果列表中。
   - 迭代 DFS：虽然提供的代码中没有迭代版本，但可以通过使用栈来模拟递归过程，从而实现迭代的深度优先搜索。
   - 数据结构：使用字符串来构建路径，使用列表来存储所有路径。

3. 全量伪代码：
   - 递归 DFS 版本：
     ```
     定义函数 binaryTreePaths(root):
         如果 root 为空，返回空列表
         初始化结果列表 res
         调用 traverse(root, "", res)
         返回 res

     定义函数 traverse(node, path, res):
         如果 node 为空，返回
         更新路径 new_path = path + 当前节点值
         如果当前节点是叶节点，将 new_path 添加到 res
         如果左子节点存在，递归调用 traverse(node.left, new_path + "->", res)
         如果右子节点存在，递归调用 traverse(node.right, new_path + "->", res)
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点都被访问一次。
   - 空间复杂度：$O(n)$，在最坏情况下（例如链状树），递归调用栈的深度为 $n$。