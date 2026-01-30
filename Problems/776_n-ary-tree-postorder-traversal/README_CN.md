# 776. N 叉树的后序遍历

**难度**: Easy | **标签**: `Stack` `Tree` `Depth-First Search`

## 题目描述

<p>给定一个 n&nbsp;叉树的根节点<meta charset="UTF-8" />&nbsp;<code>root</code>&nbsp;，返回 <em>其节点值的<strong> 后序遍历</strong></em> 。</p>

<p>n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 <code>null</code> 分隔（请参见示例）。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="height: 193px; width: 300px;" /></p>

<pre>
<strong>输入：</strong>root = [1,null,3,2,4,null,5,6]
<strong>输出：</strong>[5,6,3,2,4,1]
</pre>

<p><strong class="example">示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" style="height: 269px; width: 296px;" /></p>

<pre>
<strong>输入：</strong>root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
<strong>输出：</strong>[2,6,14,11,7,3,12,8,4,13,9,10,5,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>节点总数在范围 <code>[0, 10<sup>4</sup>]</code> 内</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li>n 叉树的高度小于或等于 <code>1000</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>递归法很简单，你可以使用迭代法完成此题吗?</p>


---
## 解题思路与复盘

1. 一句话直击本质：后序遍历的核心逻辑是先递归或迭代访问所有子节点，再访问当前节点。

2. 综合思路：
   - 递归解法：通过递归函数遍历每个节点的子节点，在所有子节点被访问后，再访问当前节点。
   - 迭代解法：使用栈模拟递归过程，先将根节点入栈，然后依次将节点的子节点入栈，最后反转结果以实现后序遍历。

3. 全量伪代码：
   - 递归解法：
     ```
     定义函数 traverse(node, res):
         如果 node 为空:
             返回
         对于 node 的每个子节点 child:
             调用 traverse(child, res)
         将 node 的值添加到 res

     定义函数 postorder(root):
         初始化 res 为一个空列表
         调用 traverse(root, res)
         返回 res
     ```
   - 迭代解法：
     ```
     定义函数 postorder(root):
         如果 root 为空:
             返回空列表
         初始化 stack 为包含 root 的列表
         初始化 res 为一个空列表
         当 stack 不为空:
             弹出 stack 的顶部元素 curr
             将 curr 的值添加到 res
             对于 curr 的每个子节点 child:
                 将 child 添加到 stack
         返回 res 的反转
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是节点的数量，因为每个节点都被访问一次。
   - 空间复杂度：$O(n)$，在最坏情况下（例如链状树），递归栈或迭代栈的深度可能达到 $n$。