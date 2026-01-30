# 1498. 找出克隆二叉树中的相同节点

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`

## 题目描述

<p>给你两棵二叉树，原始树 <code>original</code> 和克隆树 <code>cloned</code>，以及一个位于原始树 <code>original</code>&nbsp;中的目标节点&nbsp;<code>target</code>。</p>

<p>其中，克隆树 <code>cloned</code>&nbsp;是原始树 <code>original</code>&nbsp;的一个<strong> 副本 </strong>。</p>

<p>请找出在树&nbsp;<code>cloned</code>&nbsp;中，与&nbsp;<code>target</code>&nbsp;<strong>相同&nbsp;</strong>的节点，并返回对该节点的引用（在 C/C++ 等有指针的语言中返回 节点指针，其他语言返回节点本身）。</p>

<p>&nbsp;</p>

<p><strong>注意：</strong>你 <strong>不能</strong> 对两棵二叉树，以及 <code>target</code>&nbsp;节点进行更改。<strong>只能</strong> 返回对克隆树&nbsp;<code>cloned</code>&nbsp;中已有的节点的引用。</p>

<ul>
</ul>

<p>&nbsp;</p>

<ul>
</ul>

<p><strong>示例 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e1.png" /></p>

<pre>
<strong>输入:</strong> tree = [7,4,3,null,null,6,19], target = 3
<strong>输出:</strong> 3
<strong>解释:</strong> 上图画出了树 original 和 cloned。target 节点在树 original 中，用绿色标记。答案是树 cloned 中的黄颜色的节点（其他示例类似）。</pre>

<p><strong>示例 2:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e2.png" /></p>

<pre>
<strong>输入:</strong> tree = [7], target =  7
<strong>输出:</strong> 7
</pre>

<p><strong>示例 3:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e3.png" /></p>

<pre>
<strong>输入:</strong> tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
<strong>输出:</strong> 4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点的数量范围为<meta charset="UTF-8" />&nbsp;<code>[1, 10<sup>4</sup>]</code>&nbsp;。</li>
	<li>同一棵树中，没有值相同的节点。</li>
	<li><code>target</code>&nbsp;节点是树&nbsp;<code>original</code>&nbsp;中的一个节点，并且不会是&nbsp;<code>null</code>&nbsp;。</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>如果树中允许出现值相同的节点，将如何解答？</p>


---
## 解题思路与复盘

1. 一句话直击本质：通过同步遍历原始二叉树和克隆二叉树，找到与目标节点相同位置的节点。

2. 综合思路：
   - 递归深度优先搜索（DFS）：通过递归的方式同时遍历原始树和克隆树，检查当前节点是否为目标节点，如果是，则记录克隆树中对应节点。
   - 迭代深度优先搜索（DFS）：可以使用栈来模拟递归过程，逐步遍历树的节点。
   - 广度优先搜索（BFS）：可以使用队列来同时遍历原始树和克隆树的每一层，直到找到目标节点。

3. 全量伪代码：
   - 递归 DFS 版本：
     ```
     定义函数 getTargetCopy(original, cloned, target):
         初始化结果变量 res 为 None
         调用 dfs(original, cloned, target)
         返回 res

     定义函数 dfs(p, q, target):
         如果 p 或 q 为空，返回
         如果 p 是目标节点 target:
             将 q 赋值给结果变量 res
             返回
         递归调用 dfs(p.left, q.left, target)
         递归调用 dfs(p.right, q.right, target)
     ```

   - 迭代 DFS 版本（伪代码示例）：
     ```
     定义函数 getTargetCopy(original, cloned, target):
         初始化栈 stack，包含 (original, cloned)
         当栈不为空时:
             弹出栈顶元素 (p, q)
             如果 p 是目标节点 target:
                 返回 q
             如果 p.left 和 q.left 都不为空:
                 将 (p.left, q.left) 压入栈
             如果 p.right 和 q.right 都不为空:
                 将 (p.right, q.right) 压入栈
     ```

   - BFS 版本（伪代码示例）：
     ```
     定义函数 getTargetCopy(original, cloned, target):
         初始化队列 queue，包含 (original, cloned)
         当队列不为空时:
             取出队列头部元素 (p, q)
             如果 p 是目标节点 target:
                 返回 q
             如果 p.left 和 q.left 都不为空:
                 将 (p.left, q.left) 加入队列
             如果 p.right 和 q.right 都不为空:
                 将 (p.right, q.right) 加入队列
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点都需要访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是二叉树的高度，递归调用栈或迭代使用的栈/队列的最大深度。对于平衡树，$h = O(\log n)$；对于非平衡树，$h = O(n)$。