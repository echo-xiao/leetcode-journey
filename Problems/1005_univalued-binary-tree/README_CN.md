# 1005. 单值二叉树

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`

## 题目描述

<p>如果二叉树每个节点都具有相同的值，那么该二叉树就是<em>单值</em>二叉树。</p>

<p>只有给定的树是单值二叉树时，才返回&nbsp;<code>true</code>；否则返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/29/screen-shot-2018-12-25-at-50104-pm.png" style="height: 159px; width: 200px;"></p>

<pre><strong>输入：</strong>[1,1,1,1,1,null,1]
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/29/screen-shot-2018-12-25-at-50050-pm.png" style="height: 158px; width: 200px;"></p>

<pre><strong>输入：</strong>[2,2,2,5,2]
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>给定树的节点数范围是&nbsp;<code>[1, 100]</code>。</li>
	<li>每个节点的值都是整数，范围为&nbsp;<code>[0, 99]</code>&nbsp;。</li>
</ol>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过递归遍历二叉树的所有节点，检查每个节点的值是否与根节点的值相同。

2. 综合思路：
   - 递归解法：使用递归函数遍历二叉树，检查每个节点的值是否等于根节点的值。如果所有节点的值都相同，则返回 `True`，否则返回 `False`。
   - 迭代解法（未在提供的代码中出现，但作为补充）：可以使用栈或队列进行深度优先搜索（DFS）或广度优先搜索（BFS），逐个检查每个节点的值是否与根节点的值相同。

3. 全量伪代码：
   ```plaintext
   定义函数 isUnivalTree(root):
       如果 root 是空:
           返回 True
       
       设定 targetVal 为 root 的值
       返回 check(root, targetVal)

   定义函数 check(node, targetVal):
       如果 node 是空:
           返回 True
       
       如果 node 的值不等于 targetVal:
           返回 False
       
       leftCheck = check(node.left, targetVal)
       rightCheck = check(node.right, targetVal)
       
       返回 leftCheck 且 rightCheck
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树中的节点数，因为每个节点都需要被访问一次。
   - 空间复杂度：$O(h)$，其中 $h$ 是二叉树的高度，递归调用栈的深度取决于树的高度。对于平衡树，$h = \log n$，对于不平衡树，$h = n$。