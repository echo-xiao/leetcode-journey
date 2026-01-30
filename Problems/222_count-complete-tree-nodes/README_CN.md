# 222. 完全二叉树的节点个数

**难度**: Easy | **标签**: `Binary Search` `Bit Manipulation` `Tree` `Binary Tree`

## 题目描述

<p>给你一棵<strong> 完全二叉树</strong> 的根节点 <code>root</code> ，求出该树的节点个数。</p>

<p><a href="https://baike.baidu.com/item/%E5%AE%8C%E5%85%A8%E4%BA%8C%E5%8F%89%E6%A0%91/7773232?fr=aladdin">完全二叉树</a> 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 <code>h</code> 层（从第 0 层开始），则该层包含 <code>1~&nbsp;2<sup>h</sup></code>&nbsp;个节点。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/14/complete.jpg" style="width: 372px; height: 302px;" />
<pre>
<strong>输入：</strong>root = [1,2,3,4,5,6]
<strong>输出：</strong>6
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = []
<strong>输出：</strong>0
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = [1]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点的数目范围是<code>[0, 5 * 10<sup>4</sup>]</code></li>
	<li><code>0 &lt;= Node.val &lt;= 5 * 10<sup>4</sup></code></li>
	<li>题目数据保证输入的树是 <strong>完全二叉树</strong></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>遍历树来统计节点是一种时间复杂度为 <code>O(n)</code> 的简单解决方案。你可以设计一个更快的算法吗？</p>


---
## 解题思路与复盘

1. 一句话直击本质：利用递归或完全二叉树的特性，通过计算左右子树的节点数来求解整个树的节点总数。

2. 综合思路：
   - 递归法：直接递归遍历整棵树，分别计算左右子树的节点数，然后加上根节点。
   - 完全二叉树特性法：通过计算左右子树的深度，判断子树是否为满二叉树，从而快速计算节点数。

3. 全量伪代码：
   - 递归法：
     ```
     如果树为空，返回 0
     递归计算左子树的节点数
     递归计算右子树的节点数
     返回 左子树节点数 + 右子树节点数 + 1（根节点）
     ```
   - 完全二叉树特性法：
     ```
     如果树为空，返回 0
     计算左子树的深度
     计算右子树的深度
     如果左子树深度等于右子树深度：
         返回 1 + (2^左子树深度 - 1) + 递归计算右子树的节点数
     否则：
         返回 1 + 递归计算左子树的节点数 + (2^右子树深度 - 1)
     ```

4. 复杂度：
   - 递归法的时间复杂度为 $O(n)$，空间复杂度为 $O(h)$，其中 $n$ 是节点数，$h$ 是树的高度。
   - 完全二叉树特性法的时间复杂度为 $O(\log^2 n)$，空间复杂度为 $O(h)$。