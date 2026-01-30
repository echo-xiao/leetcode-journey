# 563. 二叉树的坡度

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Binary Tree`

## 题目描述

<p>给你一个二叉树的根节点 <code>root</code> ，计算并返回 <strong>整个树 </strong>的坡度 。</p>

<p>一个树的<strong> 节点的坡度 </strong>定义即为，该节点左子树的节点之和和右子树节点之和的 <strong>差的绝对值 </strong>。如果没有左子树的话，左子树的节点之和为 0 ；没有右子树的话也是一样。空结点的坡度是 0 。</p>

<p><strong>整个树</strong> 的坡度就是其所有节点的坡度之和。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/20/tilt1.jpg" style="width: 712px; height: 182px;" />
<pre>
<strong>输入：</strong>root = [1,2,3]
<strong>输出：</strong>1
<strong>解释：</strong>
节点 2 的坡度：|0-0| = 0（没有子节点）
节点 3 的坡度：|0-0| = 0（没有子节点）
节点 1 的坡度：|2-3| = 1（左子树就是左子节点，所以和是 2 ；右子树就是右子节点，所以和是 3 ）
坡度总和：0 + 0 + 1 = 1
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/20/tilt2.jpg" style="width: 800px; height: 203px;" />
<pre>
<strong>输入：</strong>root = [4,2,9,3,5,null,7]
<strong>输出：</strong>15
<strong>解释：</strong>
节点 3 的坡度：|0-0| = 0（没有子节点）
节点 5 的坡度：|0-0| = 0（没有子节点）
节点 7 的坡度：|0-0| = 0（没有子节点）
节点 2 的坡度：|3-5| = 2（左子树就是左子节点，所以和是 3 ；右子树就是右子节点，所以和是 5 ）
节点 9 的坡度：|0-7| = 7（没有左子树，所以和是 0 ；右子树正好是右子节点，所以和是 7 ）
节点 4 的坡度：|(3+5+2)-(9+7)| = |10-16| = 6（左子树值为 3、5 和 2 ，和是 10 ；右子树值为 9 和 7 ，和是 16 ）
坡度总和：0 + 0 + 0 + 2 + 7 + 6 = 15
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/20/tilt3.jpg" style="width: 800px; height: 293px;" />
<pre>
<strong>输入：</strong>root = [21,7,14,1,1,2,2,3,3]
<strong>输出：</strong>9
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目的范围在 <code>[0, 10<sup>4</sup>]</code> 内</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过后序遍历计算每个节点的左右子树和的差值，并累加得到整个二叉树的坡度。

2. 综合思路：
   - 递归后序遍历：所有版本都采用递归的后序遍历方法，计算每个节点的左右子树和，并利用这些和计算坡度。
   - 递归与迭代：目前提供的代码版本中仅有递归实现，没有迭代实现。
   - DFS与BFS：所有版本均使用深度优先搜索（DFS）的方式进行遍历，没有广度优先搜索（BFS）的实现。
   - 数据结构：使用二叉树的节点结构进行递归遍历，没有使用其他复杂的数据结构。

3. 全量伪代码：
   ```plaintext
   定义二叉树节点类 TreeNode:
       初始化方法 __init__(val=0, left=None, right=None):
           设置节点值 val
           设置左子节点 left
           设置右子节点 right

   定义解决方案类 Solution:
       初始化方法 __init__():
           初始化坡度累加器为 0

       方法 findTilt(root):
           如果根节点为空，返回 0
           调用递归方法计算坡度并返回累加器值

       递归方法 sumTree(node):
           如果节点为空，返回 0
           递归计算左子树和 leftSum
           递归计算右子树和 rightSum
           计算当前节点的坡度并累加到累加器
           返回当前节点的总和（节点值加上左右子树和）
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点都被访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是二叉树的高度，递归调用栈的最大深度。