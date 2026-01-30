# 230. 二叉搜索树中第 K 小的元素

**难度**: Medium | **标签**: `Tree` `Depth-First Search` `Binary Search Tree` `Binary Tree`

## 题目描述

<p>给定一个二叉搜索树的根节点 <code>root</code> ，和一个整数 <code>k</code> ，请你设计一个算法查找其中第&nbsp;<code>k</code><strong>&nbsp;</strong>小的元素（<code>k</code> 从 1 开始计数）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg" style="width: 212px; height: 301px;" />
<pre>
<strong>输入：</strong>root = [3,1,4,null,2], k = 1
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg" style="width: 382px; height: 302px;" />
<pre>
<strong>输入：</strong>root = [5,3,6,2,4,null,null,1], k = 3
<strong>输出：</strong>3
</pre>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中的节点数为 <code>n</code> 。</li>
	<li><code>1 &lt;= k &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 <code>k</code> 小的值，你将如何优化算法？</p>


---
## 解题思路与复盘

1. **一句话直击本质：**  
   利用二叉搜索树的中序遍历特性，按顺序访问节点，找到第 K 小的元素。

2. **综合思路：**  
   - **迭代法：** 使用栈模拟递归的过程，通过中序遍历的方式遍历树节点，直到找到第 K 小的元素。
   - **递归法：** 通过递归实现中序遍历，使用全局变量或类成员变量记录当前访问的节点数，当访问到第 K 个节点时，记录结果并返回。

3. **全量伪代码：**

   **迭代法：**
   ```
   初始化一个空栈
   当树未遍历完时：
       当当前节点不为空时：
           将当前节点压入栈中
           移动到左子节点
       弹出栈顶节点作为当前节点
       减少 k 的值
       如果 k 为 0：
           返回当前节点的值
       移动到右子节点
   ```

   **递归法：**
   ```
   定义全局变量 k 和结果 res
   定义递归函数 dfs(node):
       如果节点为空，返回
       递归调用左子节点
       减少 k 的值
       如果 k 为 0：
           将当前节点的值赋给结果 res
           返回
       递归调用右子节点
   调用 dfs(root)
   返回结果 res
   ```

4. **复杂度：**  
   - **时间复杂度：** $O(n)$，其中 $n$ 是树中节点的数量，因为在最坏情况下需要遍历所有节点。
   - **空间复杂度：** $O(h)$，其中 $h$ 是树的高度，迭代法使用栈存储节点，递归法使用递归栈，最坏情况下为 $O(n)$。