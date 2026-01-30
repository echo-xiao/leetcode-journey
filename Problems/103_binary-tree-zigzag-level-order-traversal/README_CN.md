# 103. 二叉树的锯齿形层序遍历

**难度**: Medium | **标签**: `Tree` `Breadth-First Search` `Binary Tree`

## 题目描述

<p>给你二叉树的根节点 <code>root</code> ，返回其节点值的 <strong>锯齿形层序遍历</strong> 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>输入：</strong>root = [3,9,20,null,null,15,7]
<strong>输出：</strong>[[3],[20,9],[15,7]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = [1]
<strong>输出：</strong>[[1]]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = []
<strong>输出：</strong>[]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目在范围 <code>[0, 2000]</code> 内</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：**  
   使用广度优先搜索（BFS）遍历二叉树的每一层，并根据层数的奇偶性决定是否反转节点值的顺序。

2. **综合思路：**  
   - **迭代 BFS 解法：** 使用队列（`deque`）进行层序遍历，每次遍历一层节点后，根据当前层的奇偶性决定是否反转节点值的顺序。
   - **递归 DFS 解法：** 使用递归方法遍历树的每一层，利用双端队列（`deque`）在每层的头部或尾部插入节点值，从而实现锯齿形顺序。

3. **全量伪代码：**

   - **迭代 BFS 解法：**
     ```
     如果根节点为空，返回空列表
     初始化队列 q 并将根节点加入队列
     初始化结果列表 ans 和层数变量 depth
     当队列不为空时：
         初始化当前层节点值列表 vals
         遍历当前层的所有节点：
             从队列中弹出节点
             将节点值加入 vals
             如果节点有左子节点，将其加入队列
             如果节点有右子节点，将其加入队列
         如果当前层数为奇数，反转 vals
         将 vals 加入结果列表 ans
         增加层数 depth
     返回结果列表 ans
     ```

   - **递归 DFS 解法：**
     ```
     如果根节点为空，返回空列表
     初始化结果列表 res
     定义递归函数 traverse(node, level, res):
         如果节点为空，返回
         如果 res 的长度等于当前层数 level，向 res 添加一个新的双端队列
         如果当前层数为偶数，将节点值加入当前层的双端队列尾部
         否则，将节点值加入当前层的双端队列头部
         递归调用 traverse 处理左子节点和右子节点，层数加一
     调用 traverse 函数从根节点开始遍历
     将 res 中的每个双端队列转换为列表并返回
     ```

4. **复杂度：**  
   - **时间复杂度：** $O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点都被访问一次。
   - **空间复杂度：** $O(n)$，用于存储结果列表和队列（或递归调用栈）的空间。