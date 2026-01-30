# 108. 将有序数组转换为二叉搜索树

**难度**: Easy | **标签**: `Array` `Divide and Conquer` `Tree` `Binary Search Tree` `Binary Tree`

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，其中元素已经按 <strong>升序</strong> 排列，请你将其转换为一棵 <span data-keyword="height-balanced">平衡</span> 二叉搜索树。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg" style="width: 302px; height: 222px;" />
<pre>
<strong>输入：</strong>nums = [-10,-3,0,5,9]
<strong>输出：</strong>[0,-3,9,-10,null,5]
<strong>解释：</strong>[0,-10,5,null,-3,null,9] 也将被视为正确答案：
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg" style="width: 302px; height: 222px;" />
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree.jpg" style="width: 342px; height: 142px;" />
<pre>
<strong>输入：</strong>nums = [1,3]
<strong>输出：</strong>[3,1]
<strong>解释：</strong>[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> 按 <strong>严格递增</strong> 顺序排列</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：**  
   将有序数组的中间元素作为根节点，递归地对左右子数组重复此过程，构建平衡二叉搜索树。

2. **综合思路：**  
   - **递归方法：**  
     通过递归地选择数组的中间元素作为根节点，左半部分作为左子树，右半部分作为右子树，直到数组为空。
   - **模拟中序遍历：**  
     通过递归构建左子树后，使用一个索引来选择当前根节点，然后构建右子树，模拟中序遍历的顺序。

3. **全量伪代码：**

   - **递归方法：**
     ```
     函数 sortedArrayToBST(数组 nums):
         如果 nums 为空:
             返回 None
         设 mid 为 nums 的中间索引
         创建根节点 root，值为 nums[mid]
         root.left 赋值为 sortedArrayToBST(nums 的左半部分)
         root.right 赋值为 sortedArrayToBST(nums 的右半部分)
         返回 root
     ```

   - **模拟中序遍历：**
     ```
     函数 sortedArrayToBST(数组 nums):
         初始化索引 index 为 0
         返回 build(0, len(nums) - 1)

     函数 build(整数 left, 整数 right):
         如果 left > right:
             返回 None
         设 mid 为 (left + right) // 2
         递归构建左子树 leftTree = build(left, mid - 1)
         创建根节点 root，值为 nums[index]
         增加 index
         root.left 赋值为 leftTree
         root.right 赋值为 build(mid + 1, right)
         返回 root
     ```

4. **复杂度：**  
   - 时间复杂度：$O(n)$，其中 $n$ 是数组的长度，因为每个元素都被访问一次。
   - 空间复杂度：$O(\log n)$，用于递归调用栈的空间，最坏情况下是树的高度。