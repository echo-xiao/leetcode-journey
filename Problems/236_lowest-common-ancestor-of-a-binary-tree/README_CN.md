# 236. 二叉树的最近公共祖先

**难度**: Medium | **标签**: `Tree` `Depth-First Search` `Binary Tree`

## 题目描述

<p>给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。</p>

<p><a href="https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin" target="_blank">百度百科</a>中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（<strong>一个节点也可以是它自己的祖先</strong>）。”</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarytree.png" style="width: 200px; height: 190px;" />
<pre>
<strong>输入：</strong>root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
<strong>输出：</strong>3
<strong>解释：</strong>节点 <code>5 </code>和节点 <code>1 </code>的最近公共祖先是节点 <code>3 。</code>
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarytree.png" style="width: 200px; height: 190px;" />
<pre>
<strong>输入：</strong>root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
<strong>输出：</strong>5
<strong>解释：</strong>节点 <code>5 </code>和节点 <code>4 </code>的最近公共祖先是节点 <code>5 。</code>因为根据定义最近公共祖先节点可以为节点本身。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = [1,2], p = 1, q = 2
<strong>输出：</strong>1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目在范围 <code>[2, 10<sup>5</sup>]</code> 内。</li>
	<li><code>-10<sup>9</sup> <= Node.val <= 10<sup>9</sup></code></li>
	<li>所有 <code>Node.val</code> <code>互不相同</code> 。</li>
	<li><code>p != q</code></li>
	<li><code>p</code> 和 <code>q</code> 均存在于给定的二叉树中。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法通过递归遍历二叉树，寻找节点 p 和 q 的路径，找到它们的分叉点即为最近公共祖先。

2. 综合思路：
   - 递归解法：通过递归遍历二叉树，检查当前节点是否为 p 或 q，若是则返回当前节点；否则递归检查左右子树，若左右子树均返回非空节点，则当前节点为最近公共祖先。
   - 迭代解法：使用栈或队列进行深度优先搜索（DFS）或广度优先搜索（BFS），同时记录每个节点的父节点，最后通过回溯找到 p 和 q 的路径并确定最近公共祖先。
   - 使用父指针：在树节点中增加指向父节点的指针，直接通过路径比较找到最近公共祖先。

3. 全量伪代码：
   - 递归解法：
     ```
     函数 lowestCommonAncestor(根节点, 节点 p, 节点 q):
         如果 根节点为空 或 根节点是 p 或 q:
             返回 根节点
         左子树结果 = lowestCommonAncestor(根节点的左子树, p, q)
         右子树结果 = lowestCommonAncestor(根节点的右子树, p, q)
         如果 左子树结果 和 右子树结果 均不为空:
             返回 根节点
         如果 左子树结果 不为空:
             返回 左子树结果
         否则:
             返回 右子树结果
     ```

   - 迭代解法（DFS/BFS）：
     ```
     函数 lowestCommonAncestor(根节点, 节点 p, 节点 q):
         使用栈/队列初始化搜索
         初始化字典记录每个节点的父节点
         当栈/队列不为空:
             弹出当前节点
             如果当前节点有左子节点:
                 记录左子节点的父节点为当前节点
                 将左子节点加入栈/队列
             如果当前节点有右子节点:
                 记录右子节点的父节点为当前节点
                 将右子节点加入栈/队列
         初始化集合记录 p 的祖先路径
         从 p 开始向上回溯记录路径
         从 q 开始向上回溯，找到第一个在 p 祖先路径中的节点即为最近公共祖先
     ```

4. 复杂度：
   - 时间复杂度：递归和迭代解法的时间复杂度均为 $O(n)$，其中 $n$ 是二叉树的节点数，因为每个节点最多被访问一次。
   - 空间复杂度：递归解法的空间复杂度为 $O(h)$，其中 $h$ 是二叉树的高度，主要是递归调用栈的空间；迭代解法的空间复杂度为 $O(n)$，用于存储父节点信息。