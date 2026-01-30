# 199. 二叉树的右视图

**难度**: Medium | **标签**: `Tree` `Depth-First Search` `Breadth-First Search` `Binary Tree`

## 题目描述

<p>给定一个二叉树的 <strong>根节点</strong> <code>root</code>，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>root = [1,2,3,null,5,null,4]</span></p>

<p><strong>输出：</strong><span class="example-io">[1,3,4]</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/11/24/tmpd5jn43fs-1.png" style="width: 400px; height: 207px;" /></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>root = [1,2,3,4,null,null,null,5]</span></p>

<p><span class="example-io"><b>输出：</b>[1,3,4,5]</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/11/24/tmpkpe40xeh-1.png" style="width: 400px; height: 214px;" /></p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">root = [1,null,3]</span></p>

<p><strong>输出：</strong><span class="example-io">[1,3]</span></p>
</div>

<p><strong class="example">示例 4：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>root = []</span></p>

<p><strong>输出：</strong><span class="example-io">[]</span></p>

<p>&nbsp;</p>
</div>

<p><strong>提示:</strong></p>

<ul>
	<li>二叉树的节点个数的范围是 <code>[0,100]</code></li>
	<li><meta charset="UTF-8" /><code>-100&nbsp;&lt;= Node.val &lt;= 100</code>&nbsp;</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过层序遍历（BFS）或深度优先搜索（DFS）来记录每一层的最右侧节点值。

2. 综合思路：
   - **BFS（广度优先搜索）迭代法**：使用队列进行层序遍历，每次记录每层最后一个节点的值。
   - **DFS（深度优先搜索）递归法**：优先访问右子树，记录每层首次访问的节点值。

3. 全量伪代码：
   - **BFS 迭代法**：
     ```
     如果根节点为空，返回空列表
     初始化队列 q，包含根节点
     初始化结果列表 res
     当队列 q 非空时：
         记录当前层的节点数量 size
         初始化临时列表 vals
         遍历当前层的所有节点：
             从队列中弹出一个节点 node
             将 node 的值添加到 vals
             如果 node 有左子节点，将其加入队列
             如果 node 有右子节点，将其加入队列
         将 vals 中最后一个值添加到结果列表 res
     返回结果列表 res
     ```
   - **DFS 递归法**：
     ```
     定义递归函数 dfs(node, level, res)
         如果节点 node 为空，返回
         如果 level 等于结果列表 res 的长度，将 node 的值添加到 res
         递归调用 dfs 访问 node 的右子节点，level 增加 1
         递归调用 dfs 访问 node 的左子节点，level 增加 1
     如果根节点为空，返回空列表
     初始化结果列表 res
     调用 dfs 函数从根节点开始
     返回结果列表 res
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点都被访问一次。
   - 空间复杂度：$O(n)$，在最坏情况下（例如完全不平衡的树），队列或递归栈可能需要存储所有节点。