# 775. N 叉树的前序遍历

**难度**: Easy | **标签**: `Stack` `Tree` `Depth-First Search`

## 题目描述

<p>给定一个 n&nbsp;叉树的根节点 <meta charset="UTF-8" />&nbsp;<code>root</code>&nbsp;，返回 <em>其节点值的<strong> 前序遍历</strong></em> 。</p>

<p>n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 <code>null</code> 分隔（请参见示例）。</p>

<p><br />
<strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="height: 193px; width: 300px;" /></p>

<pre>
<strong>输入：</strong>root = [1,null,3,2,4,null,5,6]
<strong>输出：</strong>[1,3,5,6,2,4]
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" style="height: 272px; width: 300px;" /></p>

<pre>
<strong>输入：</strong>root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
<strong>输出：</strong>[1,2,3,6,7,11,14,4,8,12,5,9,13,10]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>节点总数在范围<meta charset="UTF-8" />&nbsp;<code>[0, 10<sup>4</sup>]</code>内</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li>n 叉树的高度小于或等于 <code>1000</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>递归法很简单，你可以使用迭代法完成此题吗?</p>


---
## 解题思路与复盘

1. 一句话直击本质：N 叉树的前序遍历核心在于先访问节点自身，再递归或迭代访问其子节点。

2. 综合思路：
   - **递归解法**：通过递归函数，先访问当前节点并记录其值，然后依次递归访问每个子节点。
   - **迭代解法**：使用栈来模拟递归过程，先将根节点入栈，循环过程中弹出栈顶节点，记录其值，然后将其子节点逆序入栈，以确保子节点按从左到右的顺序被访问。

3. 全量伪代码：
   - **递归解法伪代码**：
     ```
     定义函数 traverse(node, res):
         如果 node 为空:
             返回
         将 node 的值添加到 res
         对于 node 的每个子节点 child:
             调用 traverse(child, res)

     定义函数 preorder(root):
         初始化 res 为一个空列表
         调用 traverse(root, res)
         返回 res
     ```
   - **迭代解法伪代码**：
     ```
     定义函数 preorder(root):
         如果 root 为空:
             返回空列表
         初始化 stack 为包含 root 的列表
         初始化 res 为一个空列表
         当 stack 不为空时:
             弹出 stack 的最后一个元素 curr
             将 curr 的值添加到 res
             逆序遍历 curr 的子节点:
                 将每个子节点 child 添加到 stack
         返回 res
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是树中节点的数量，因为每个节点都被访问一次。
   - 空间复杂度：递归解法的空间复杂度为 $O(h)$，迭代解法的空间复杂度为 $O(n)$，其中 $h$ 是树的高度，$n$ 是节点数量。