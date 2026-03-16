# 2843. 从 Rope 树中提取第 K 个字符

**难度**: Easy | **标签**: `Tree` `Depth-First Search` `Binary Tree`

## 题目描述

<p>给定一个二叉树的 <code>root</code> 和一个整数 <code>k</code>。除了左子节点和右子节点之外，这棵树的每个节点还有两个其他属性，一个包含仅小写英文字母（可能为空）的 <strong>字符串</strong> <code>node.val</code> 和一个非负整数 <code>node.len</code>。这棵树中有两种类型的节点：</p>

<ul>
	<li><strong>叶子节点</strong>：这些节点没有子节点，<code>node.len = 0</code>，并且 <code>node.val</code> 是某个<strong>非空</strong>字符串。</li>
	<li><strong>内部节点</strong>：这些节点至少有一个子节点（最多两个子节点），<code>node.len &gt; 0</code>，并且 <code>node.val</code> 是一个<strong>空</strong>字符串。</li>
</ul>

<p>上述描述的树被称为 <em>绳子</em> 二叉树。现在我们递归地定义 <code>S[node]</code> 如下：</p>

<ul>
	<li>如果 <code>node</code> 是某个叶子节点，<code>S[node] = node.val</code>，</li>
	<li>否则如果 <code>node</code> 是某个内部节点，<code>S[node] = concat(S[node.left], S[node.right])</code> 并且 <code>S[node].length = node.len</code>。</li>
</ul>

<p>返回 <em>字符串</em> <code>S[root]</code> 的第 <code>k</code> 个字符。</p>

<p><strong>注意：</strong>如果 <code>s</code> 和 <code>p</code> 是两个字符串，<code>concat(s, p)</code> 是通过将 <code>p</code> 连接到 <code>s</code> 上得到的字符串。例如，<code>concat(&quot;ab&quot;, &quot;zz&quot;) = &quot;abzz&quot;</code>。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> root = [10,4,&quot;abcpoe&quot;,&quot;g&quot;,&quot;rta&quot;], k = 6
<strong>输出:</strong> &quot;b&quot;
<strong>解释:</strong> 在下图中，我们在内部节点上放置一个整数，表示 node.len，在叶子节点上放置一个字符串，表示 node.val。
可以看到 S[root] = concat(concat(&quot;g&quot;, &quot;rta&quot;), &quot;abcpoe&quot;) = &quot;grtaabcpoe&quot;。所以 S[root][5]，表示它的第 6 个字符，等于 &quot;b&quot;。
</pre>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/05/14/example1.png" style="width: 300px; height: 213px; margin-left: 280px; margin-right: 280px;" /></p>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> root = [12,6,6,&quot;abc&quot;,&quot;efg&quot;,&quot;hij&quot;,&quot;klm&quot;], k = 3
<strong>输出:</strong> &quot;c&quot;
<strong>解释:</strong> 在下图中，我们在内部节点上放置一个整数，表示 node.len，在叶子节点上放置一个字符串，表示 node.val。
可以看到 S[root] = concat(concat(&quot;abc&quot;, &quot;efg&quot;), concat(&quot;hij&quot;, &quot;klm&quot;)) = &quot;abcefghijklm&quot;。所以 S[root][2]，表示它的第 3 个字符，等于 &quot;c&quot;。
</pre>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/05/14/example2.png" style="width: 400px; height: 232px; margin-left: 255px; margin-right: 255px;" /></p>

<p><strong class="example">示例 3:</strong></p>

<pre>
<strong>输入:</strong> root = [&quot;ropetree&quot;], k = 8
<strong>输出:</strong> &quot;e&quot;
<strong>解释:</strong> 在下图中，我们在内部节点上放置一个整数，表示 node.len，在叶子节点上放置一个字符串，表示 node.val。
可以看到 S[root] = &quot;ropetree&quot;。所以 S[root][7]，表示它的第 8 个字符，等于 &quot;e&quot;。
</pre>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/05/14/example3.png" style="width: 80px; height: 78px; margin-left: 400px; margin-right: 400px;" /></p>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li>树中的节点数量在 <code>[1, 10<sup>3</sup>]</code> 范围内</li>
	<li><code>node.val</code> 仅包含小写英文字母</li>
	<li><code>0 &lt;= node.val.length &lt;= 50</code></li>
	<li><code>0 &lt;= node.len &lt;= 10<sup>4</sup></code></li>
	<li>对于叶子节点，<code>node.len = 0</code> 并且 <code>node.val</code> 是非空的</li>
	<li>对于内部节点，<code>node.len &gt; 0</code> 并且 <code>node.val</code> 是空的</li>
	<li><code>1 &lt;= k &lt;= S[root].length</code></li>
</ul>

---
## 解题思路与复盘

1. 一句话直击本质：通过深度优先搜索（DFS）遍历 Rope 树，将所有叶子节点的字符串连接起来，然后直接访问第 K 个字符。

2. 综合思路：
   - 递归 DFS：通过递归的方式遍历 Rope 树，将每个叶子节点的字符串拼接成一个完整的字符串，然后直接访问第 K 个字符。
   - 迭代 DFS：可以使用栈来模拟递归的过程，达到同样的效果。
   - Rope 树特性：利用 Rope 树的特性，通过节点的长度信息直接定位到第 K 个字符，而不需要完整遍历所有字符。

3. 全量伪代码：
   - 递归 DFS 版本：
     ```
     定义函数 getKthCharacter(root, k):
         如果 root 为空，返回空
         初始化 res 为空字符串
         调用 dfs(root)
         返回 res 的第 k-1 个字符

     定义函数 dfs(node):
         如果 node 为空，返回
         递归调用 dfs(node.left)
         如果 node 是叶子节点，将 node.val 拼接到 res
         递归调用 dfs(node.right)
     ```
   - 迭代 DFS 版本（伪代码未提供，但可以推导）：
     ```
     定义函数 getKthCharacter(root, k):
         如果 root 为空，返回空
         初始化栈 stack
         初始化 res 为空字符串
         将 root 压入栈中
         当栈不为空时：
             弹出栈顶元素 node
             如果 node 是叶子节点，将 node.val 拼接到 res
             如果 node.right 不为空，将 node.right 压入栈
             如果 node.left 不为空，将 node.left 压入栈
         返回 res 的第 k-1 个字符
     ```
   - 利用 Rope 树特性（伪代码未提供，但可以推导）：
     ```
     定义函数 getKthCharacter(root, k):
         初始化当前节点 current 为 root
         当 current 不为空时：
             如果 k 小于等于 current.left.len：
                 current 移动到 current.left
             否则：
                 k 减去 current.left.len
                 如果 current 是叶子节点，返回 current.val 的第 k-1 个字符
                 否则，current 移动到 current.right
     ```

4. 复杂度：
   - 递归 DFS 版本：时间复杂度为 $O(n)$，空间复杂度为 $O(n)$，其中 $n$ 是树中节点的数量。
   - 迭代 DFS 版本：时间复杂度为 $O(n)$，空间复杂度为 $O(n)$。
   - 利用 Rope 树特性版本：时间复杂度为 $O(\log n)$，空间复杂度为 $O(1)$，假设树是平衡的。