# 235. 二叉搜索树的最近公共祖先

**难度**: Medium | **标签**: `Tree` `Depth-First Search` `Binary Search Tree` `Binary Tree`

## 题目描述

<p>给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。</p>

<p><a href="https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin" target="_blank">百度百科</a>中最近公共祖先的定义为：&ldquo;对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（<strong>一个节点也可以是它自己的祖先</strong>）。&rdquo;</p>

<p>例如，给定如下二叉搜索树:&nbsp; root =&nbsp;[6,2,8,0,4,7,9,null,null,3,5]</p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/14/binarysearchtree_improved.png" style="height: 190px; width: 200px;"></p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
<strong>输出:</strong> 6 
<strong>解释: </strong>节点 <code>2 </code>和节点 <code>8 </code>的最近公共祖先是 <code>6。</code>
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
<strong>输出:</strong> 2
<strong>解释: </strong>节点 <code>2</code> 和节点 <code>4</code> 的最近公共祖先是 <code>2</code>, 因为根据定义最近公共祖先节点可以为节点本身。</pre>

<p>&nbsp;</p>

<p><strong>说明:</strong></p>

<ul>
	<li>所有节点的值都是唯一的。</li>
	<li>p、q 为不同节点且均存在于给定的二叉搜索树中。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：利用二叉搜索树的性质，通过比较节点值来递归或迭代地缩小查找范围，直到找到分叉点即为最近公共祖先。

2. 综合思路：
   - 递归解法：通过递归调用函数，根据当前节点与目标节点值的大小关系，决定向左子树或右子树递归，直到找到分叉点。
   - 迭代解法：使用循环代替递归，通过相同的逻辑在树中迭代移动，直到找到分叉点。

3. 全量伪代码：
   - 递归解法：
     ```
     定义函数 lowestCommonAncestor(root, p, q):
         如果 root 为空:
             返回 None
         如果 p 和 q 的值都小于 root 的值:
             返回 lowestCommonAncestor(root 的左子节点, p, q)
         如果 p 和 q 的值都大于 root 的值:
             返回 lowestCommonAncestor(root 的右子节点, p, q)
         否则:
             返回 root
     ```
   - 迭代解法：
     ```
     定义函数 lowestCommonAncestor(root, p, q):
         当 root 不为空时:
             如果 p 和 q 的值都小于 root 的值:
                 移动 root 到 root 的左子节点
             如果 p 和 q 的值都大于 root 的值:
                 移动 root 到 root 的右子节点
             否则:
                 返回 root
         返回 None
     ```

4. 复杂度：
   - 时间复杂度：$O(h)$，其中 $h$ 是树的高度。在最坏情况下，树是一个链表，$h = n$。
   - 空间复杂度：递归解法为 $O(h)$（递归栈的深度），迭代解法为 $O(1)$。