# 774. N 叉树的最大深度

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Breadth-First Search`

## 题目描述

<p>给定一个 N 叉树，找到其最大深度。</p>

<p class="MachineTrans-lang-zh-CN">最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。</p>

<p class="MachineTrans-lang-zh-CN">N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。</p>

<p class="MachineTrans-lang-zh-CN"> </p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;" /></p>

<pre>
<strong>输入：</strong>root = [1,null,3,2,4,null,5,6]
<strong>输出：</strong>3
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" style="width: 296px; height: 241px;" /></p>

<pre>
<strong>输入：</strong>root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
<strong>输出：</strong>5
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>树的深度不会超过 <code>1000</code> 。</li>
	<li>树的节点数目位于 <code>[0, 10<sup>4</sup>]</code> 之间。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过递归地计算每个子节点的最大深度，并在此基础上加一，来求解 N 叉树的最大深度。

2. 综合思路：
   - 递归解法：通过递归遍历每个节点，计算其子节点的最大深度，然后返回该深度加一。
   - 迭代解法（未在给定代码中出现，但常见）：可以使用广度优先搜索（BFS）或深度优先搜索（DFS）结合栈或队列来实现迭代版本。

3. 全量伪代码：
   - 递归解法：
     ```
     定义函数 maxDepth(root):
         如果 root 是空:
             返回 0
         如果 root 没有子节点:
             返回 1
         初始化空列表 depths
         对于每个子节点 child 在 root.children 中:
             将 maxDepth(child) 的结果添加到 depths 中
         返回 1 加上 depths 中的最大值
     ```
   - 迭代解法（BFS 示例）：
     ```
     定义函数 maxDepth(root):
         如果 root 是空:
             返回 0
         初始化队列 queue，初始元素为 (root, 1)
         初始化最大深度 max_depth 为 0
         当队列 queue 不为空时:
             取出队列的第一个元素 (node, depth)
             更新 max_depth 为 max(max_depth, depth)
             对于每个子节点 child 在 node.children 中:
                 将 (child, depth + 1) 添加到队列 queue 中
         返回 max_depth
     ```

4. 复杂度：
   - 时间复杂度：递归解法的时间复杂度为 $O(n)$，其中 $n$ 是节点的数量，因为每个节点都被访问一次。
   - 空间复杂度：递归解法的空间复杂度为 $O(h)$，其中 $h$ 是树的高度，主要由递归调用栈的深度决定。对于迭代解法，空间复杂度也是 $O(h)$，因为队列或栈的最大深度与树的高度相关。