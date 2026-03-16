# 1609. 寻找所有的独生节点

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`

## 题目描述

<p>在二叉树中，<strong>孤独</strong>节点是指其父节点唯一的子节点。树的根节点不是孤独的，因为它没有父节点。</p>

<p>给定一个二叉树的 <code>root</code>，返回 <em>一个包含树中所有孤独节点值的数组</em>。返回的列表 <strong>可以是任意顺序</strong>。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/06/03/e1.png" style="width: 203px; height: 202px;" />
<pre>
<strong>输入:</strong> root = [1,2,3,null,4]
<strong>输出:</strong> [4]
<strong>解释:</strong> 浅蓝色节点是唯一的孤独节点。
节点 1 是根节点，不是孤独的。
节点 2 和 3 具有相同的父节点，不是孤独的。
</pre>

<p><strong class="example">示例 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/06/03/e2.png" style="width: 442px; height: 282px;" />
<pre>
<strong>输入:</strong> root = [7,1,4,6,null,5,3,null,null,null,null,null,2]
<strong>输出:</strong> [6,2]
<strong>解释:</strong> 浅蓝色节点是孤独节点。
请记住顺序无关紧要，[2,6] 也是一个可接受的答案。
</pre>

<p><strong class="example">示例 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/06/03/tree.png" style="width: 363px; height: 202px;" />
<pre>
<strong>输入:</strong> root = [11,99,88,77,null,null,66,55,null,null,44,33,null,null,22]
<strong>输出:</strong> [77,55,33,66,44,22]
<strong>解释:</strong> 节点 99 和 88 共享相同的父节点。节点 11 是根节点。
所有其他节点都是孤独的。
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li>树中节点的数量在 <code>[1, 1000].</code> 范围内。</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>6</sup></code></li>
</ul>

---
## 解题思路与复盘

1. 一句话直击本质：通过深度优先搜索遍历二叉树，检查每个节点的父节点是否只有一个子节点，从而找到所有的独生节点。

2. 综合思路：
   - 递归 DFS：所有版本都使用递归的深度优先搜索（DFS）来遍历二叉树。通过递归函数传递当前节点及其父节点的信息，判断当前节点是否为独生节点。
   - 版本 1：直接检查当前节点的左右子节点是否为空来判断独生节点。
   - 版本 2-6：通过传递父节点信息，检查父节点是否只有一个子节点来判断独生节点。

3. 全量伪代码：
   ```plaintext
   定义二叉树节点类 TreeNode:
       初始化函数 __init__(值=0, 左子节点=None, 右子节点=None):
           设置节点值
           设置左子节点
           设置右子节点

   定义解决方案类 Solution:
       定义函数 getLonelyNodes(根节点):
           初始化结果列表 res
           调用 dfs 函数传入根节点和空父节点
           返回结果列表 res

       定义递归函数 dfs(当前节点, 父节点):
           如果当前节点为空:
               返回

           如果父节点不为空且父节点只有一个子节点:
               将当前节点的值添加到结果列表 res

           递归调用 dfs 函数传入当前节点的左子节点和当前节点
           递归调用 dfs 函数传入当前节点的右子节点和当前节点
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树中的节点数，因为每个节点都被访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是二叉树的高度，递归调用栈的深度取决于树的高度。