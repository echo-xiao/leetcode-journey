# 501. 二叉搜索树中的众数

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Binary Search Tree` `Binary Tree`

## 题目描述

<p>给你一个含重复值的二叉搜索树（BST）的根节点 <code>root</code> ，找出并返回 BST 中的所有 <a href="https://baike.baidu.com/item/%E4%BC%97%E6%95%B0/44796" target="_blank">众数</a>（即，出现频率最高的元素）。</p>

<p>如果树中有不止一个众数，可以按 <strong>任意顺序</strong> 返回。</p>

<p>假定 BST 满足如下定义：</p>

<ul>
	<li>结点左子树中所含节点的值 <strong>小于等于</strong> 当前节点的值</li>
	<li>结点右子树中所含节点的值 <strong>大于等于</strong> 当前节点的值</li>
	<li>左子树和右子树都是二叉搜索树</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg" style="width: 142px; height: 222px;" />
<pre>
<strong>输入：</strong>root = [1,null,2,2]
<strong>输出：</strong>[2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = [0]
<strong>输出：</strong>[0]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点的数目在范围 <code>[1, 10<sup>4</sup>]</code> 内</li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）</p>


---
## 解题思路与复盘

1. **一句话直击本质：**  
   利用二叉搜索树的中序遍历特性（有序性），在遍历过程中记录当前值的频率，并更新众数。

2. **综合思路：**  
   - **递归中序遍历：** 所有版本都采用递归的中序遍历方法。通过递归访问左子树、处理当前节点、再访问右子树，确保节点值按升序处理。
   - **状态变量管理：** 使用全局或非局部变量来跟踪当前节点值、当前值的计数、最大计数以及结果列表。
   - **更新逻辑：** 在遍历过程中，根据当前节点值与前一个节点值的比较，更新计数，并根据计数更新结果列表。

3. **全量伪代码：**

   ```plaintext
   定义类 Solution:
       初始化方法:
           初始化 prev 为 None
           初始化 cnt 为 0
           初始化 max_cnt 为 0
           初始化 res 为空列表

       定义方法 findMode(root):
           如果 root 为空:
               返回空列表
           调用 traverse(root)
           返回 res

       定义方法 traverse(node):
           如果 node 为空:
               返回
           调用 traverse(node.left)

           如果 prev 等于 node.val:
               增加 cnt
           否则:
               将 cnt 设为 1
               更新 prev 为 node.val

           如果 cnt 大于 max_cnt:
               更新 max_cnt 为 cnt
               将 res 设为 [prev]
           否则如果 cnt 等于 max_cnt:
               将 prev 添加到 res

           调用 traverse(node.right)
   ```

4. **复杂度：**  
   - **时间复杂度：** $O(n)$，其中 $n$ 是树中节点的数量，因为每个节点都被访问一次。
   - **空间复杂度：** $O(h)$，其中 $h$ 是树的高度，递归调用栈的空间复杂度。对于平衡树，$h = \log n$；对于不平衡树，$h = n$。