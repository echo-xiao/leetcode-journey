# 1035. 二叉树的堂兄弟节点

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`

## 题目描述

<p>在二叉树中，根节点位于深度 <code>0</code> 处，每个深度为 <code>k</code> 的节点的子节点位于深度 <code>k+1</code> 处。</p>

<p>如果二叉树的两个节点深度相同，但<strong> 父节点不同</strong> ，则它们是一对<em>堂兄弟节点</em>。</p>

<p>我们给出了具有唯一值的二叉树的根节点 <code>root</code> ，以及树中两个不同节点的值 <code>x</code> 和 <code>y</code> 。</p>

<p>只有与值 <code>x</code> 和 <code>y</code> 对应的节点是堂兄弟节点时，才返回 <code>true</code> 。否则，返回 <code>false</code>。</p>

<p> </p>

<p><strong>示例 1：<br />
<img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/02/16/q1248-01.png" style="height: 160px; width: 180px;" /></strong></p>

<pre>
<strong>输入：</strong>root = [1,2,3,4], x = 4, y = 3
<strong>输出：</strong>false
</pre>

<p><strong>示例 2：<br />
<img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/02/16/q1248-02.png" style="height: 160px; width: 201px;" /></strong></p>

<pre>
<strong>输入：</strong>root = [1,2,3,null,4,null,5], x = 5, y = 4
<strong>输出：</strong>true
</pre>

<p><strong>示例 3：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/02/16/q1248-03.png" style="height: 160px; width: 156px;" /></strong></p>

<pre>
<strong>输入：</strong>root = [1,2,3,null,4], x = 2, y = 3
<strong>输出：</strong>false</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>二叉树的节点数介于 <code>2</code> 到 <code>100</code> 之间。</li>
	<li>每个节点的值都是唯一的、范围为 <code>1</code> 到 <code>100</code> 的整数。</li>
</ul>

<p> </p>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过深度优先搜索（DFS）遍历二叉树，记录目标节点的深度和父节点，判断两节点是否在同一深度且父节点不同。

2. **综合思路：**
   - **递归 DFS：** 使用递归的深度优先搜索遍历树，记录每个节点的深度和父节点信息，最后判断目标节点的深度和父节点是否符合堂兄弟节点的条件。
   - **迭代 BFS（未在给定代码中出现，但为常见解法）：** 使用队列进行广度优先搜索，逐层遍历树，记录每个节点的深度和父节点信息，判断目标节点是否在同一层且父节点不同。

3. **全量伪代码：**
   - 初始化变量：`dx` 和 `dy` 为 -1，`px` 和 `py` 为 `None`，用于记录节点 x 和 y 的深度和父节点。
   - 定义递归函数 `traverse(node, prev, depth)`：
     - 如果节点为空，返回。
     - 如果节点值等于 x，记录当前深度和父节点。
     - 如果节点值等于 y，记录当前深度和父节点。
     - 递归调用左子节点，传入当前节点和深度加一。
     - 递归调用右子节点，传入当前节点和深度加一。
   - 在主函数中调用 `traverse` 函数从根节点开始。
   - 返回 `dx == dy` 且 `px != py` 的判断结果。

4. **复杂度：**
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点都被访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是二叉树的高度，递归调用栈的深度。