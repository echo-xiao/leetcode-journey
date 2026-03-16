# 270. 最接近的二叉搜索树值

**难度**: Easy | **标签**: `Binary Search` `Tree` `Depth-First Search` `Binary Search Tree` `Binary Tree`

## 题目描述

<p>给定一个二叉搜索树的 <code>root</code> 和一个 <code>target</code> 值，返回 <em>在 BST 中最接近</em> <code>target</code> 的值。如果有多个答案，返回最小的。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/12/closest1-1-tree.jpg" style="width: 292px; height: 302px;" />
<pre>
<strong>输入:</strong> root = [4,2,5,1,3], target = 3.714286
<strong>输出:</strong> 4
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> root = [1], target = 4.428571
<strong>输出:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li>树中的节点数量在 <code>[1, 10<sup>4</sup>]</code> 范围内。</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>

---
## 解题思路与复盘

1. **一句话直击本质：** 利用二叉搜索树的性质，通过递归或迭代遍历树节点，逐步逼近目标值，找到与目标值差距最小的节点值。

2. **综合思路：**
   - **递归解法：** 通过递归遍历树的左右子节点，根据当前节点值与目标值的大小关系选择合适的子树继续递归，并在回溯时比较当前节点值与递归结果，选择更接近目标值的节点。
   - **迭代解法：** 使用一个循环遍历树节点，维护一个变量记录当前最接近目标值的节点值，根据当前节点值与目标值的大小关系选择合适的子树继续遍历。

3. **全量伪代码：**

   - **递归解法伪代码：**
     ```
     定义函数 closestValue(root, target):
         如果 root 为空:
             返回正无穷
         
         如果 root.val 等于 target:
             返回 root.val
         
         如果 target 大于 root.val:
             递归调用 closestValue(root.right, target) 并赋值给 closest
         否则:
             递归调用 closestValue(root.left, target) 并赋值给 closest
         
         如果 abs(target - root.val) 小于 abs(target - closest):
             返回 root.val
         否则如果 abs(target - root.val) 大于 abs(target - closest):
             返回 closest
         否则:
             返回 min(root.val, closest)
     ```

   - **迭代解法伪代码：**
     ```
     定义函数 closestValue(root, target):
         初始化 closest 为 root.val
         
         当 root 不为空时:
             如果 abs(root.val - target) 小于 abs(closest - target) 或者 (abs(root.val - target) 等于 abs(closest - target) 且 root.val 小于 closest):
                 更新 closest 为 root.val
             
             如果 target 小于 root.val:
                 移动 root 到 root.left
             否则如果 target 大于 root.val:
                 移动 root 到 root.right
             否则:
                 返回 root.val
         
         返回 closest
     ```

4. **复杂度：**
   - 时间复杂度：对于递归和迭代解法，时间复杂度均为 $O(h)$，其中 $h$ 是二叉搜索树的高度。在最坏情况下（例如，树退化为链表），时间复杂度为 $O(n)$，其中 $n$ 是节点总数。
   - 空间复杂度：递归解法的空间复杂度为 $O(h)$，因为递归调用栈的深度为树的高度。迭代解法的空间复杂度为 $O(1)$，因为只使用了常数空间。