# 572. 另一棵树的子树

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `String Matching` `Binary Tree` `Hash Function`

## 题目描述

<div class="original__bRMd">
<div>
<p>给你两棵二叉树 <code>root</code> 和 <code>subRoot</code> 。检验 <code>root</code> 中是否包含和 <code>subRoot</code> 具有相同结构和节点值的子树。如果存在，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>二叉树 <code>tree</code> 的一棵子树包括 <code>tree</code> 的某个节点和这个节点的所有后代节点。<code>tree</code> 也可以看做它自身的一棵子树。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://pic.leetcode.cn/1724998676-cATjhe-image.png" style="width: 532px; height: 400px;" />
<pre>
<strong>输入：</strong>root = [3,4,5,1,2], subRoot = [4,1,2]
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://pic.leetcode.cn/1724998698-sEJWnq-image.png" style="width: 502px; height: 458px;" />
<pre>
<strong>输入：</strong>root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>root</code> 树上的节点数量范围是 <code>[1, 2000]</code></li>
	<li><code>subRoot</code> 树上的节点数量范围是 <code>[1, 1000]</code></li>
	<li><code>-10<sup>4</sup> &lt;= root.val &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= subRoot.val &lt;= 10<sup>4</sup></code></li>
</ul>
</div>
</div>


---
## 解题思路与复盘

1. 一句话直击本质：通过递归遍历主树的每个节点，检查从该节点开始的子树是否与目标子树相同。

2. 综合思路：
   - **递归方法**：对于每个节点，递归地检查该节点的子树是否与目标子树相同，或者继续在左子树和右子树中查找。
   - **DFS（深度优先搜索）**：在递归过程中，使用深度优先搜索遍历树的每个节点。
   - **树比较**：通过递归比较两个树的每个节点的值和结构来判断它们是否相同。

3. 全量伪代码：
   ```plaintext
   函数 isSubtree(主树节点, 目标子树节点):
       如果主树节点为空:
           返回 False
       
       如果 isSame(主树节点, 目标子树节点):
           返回 True
       
       返回 isSubtree(主树节点的左子节点, 目标子树节点) 或 isSubtree(主树节点的右子节点, 目标子树节点)

   函数 isSame(树节点 p, 树节点 q):
       如果 p 和 q 都为空:
           返回 True
       
       如果 p 为空 或 q 为空 或 p 的值不等于 q 的值:
           返回 False
       
       返回 isSame(p 的左子节点, q 的左子节点) 且 isSame(p 的右子节点, q 的右子节点)
   ```

4. 复杂度：
   - 时间复杂度：$O(m \times n)$，其中 $m$ 是主树的节点数，$n$ 是目标子树的节点数。对于主树的每个节点，都可能需要调用一次 isSame 函数来比较两个树。
   - 空间复杂度：$O(n)$，主要是递归调用栈的深度，最坏情况下是目标子树的高度。