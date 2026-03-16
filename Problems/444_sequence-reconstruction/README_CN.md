# 444. 序列重建

**难度**: Medium | **标签**: `Array` `Graph Theory` `Topological Sort`

## 题目描述

<p>给定一个长度为 <code>n</code> 的整数数组 <code>nums</code>，其中 <code>nums</code> 是范围 <code>[1, n]</code> 内整数的一个排列。还给定一个二维整数数组 <code>sequences</code>，其中 <code>sequences[i]</code> 是 <code>nums</code> 的一个子序列。</p>

<p>检查 <code>nums</code> 是否是唯一的最短 <strong>超序列</strong>。最短的 <strong>超序列</strong> 是一个 <strong>长度最短</strong> 的序列，并且包含所有 <code>sequences[i]</code> 作为子序列。对于给定的数组 <code>sequences</code>，可能存在多个有效的 <strong>超序列</strong>。</p>

<ul>
	<li>例如，对于 <code>sequences = [[1,2],[1,3]]</code>，存在两个最短的 <strong>超序列</strong>，<code>[1,2,3]</code> 和 <code>[1,3,2]</code>。</li>
	<li>而对于 <code>sequences = [[1,2],[1,3],[1,2,3]]</code>，唯一的最短 <strong>超序列</strong> 是 <code>[1,2,3]</code>。<code>[1,2,3,4]</code> 是一个可能的超序列，但不是最短的。</li>
</ul>

<p>如果 <code>nums</code> 是 <code>sequences</code> 的唯一最短 <strong>超序列</strong>，则返回 <code>true</code><em>，否则返回 </em><code>false</code>.</p>

<p>一个 <strong>子序列</strong> 是一个可以通过删除某些或不删除任何元素而不改变剩余元素顺序从另一个序列中派生出的序列。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,2,3], sequences = [[1,2],[1,3]]
<strong>输出:</strong> false
<strong>解释:</strong> 存在两个可能的超序列: [1,2,3] 和 [1,3,2]。
序列 [1,2] 是两个序列的子序列: [<strong><u>1</u></strong>,<strong><u>2</u></strong>,3] 和 [<strong><u>1</u></strong>,3,<strong><u>2</u></strong>]。
序列 [1,3] 是两个序列的子序列: [<strong><u>1</u></strong>,2,<strong><u>3</u></strong>] 和 [<strong><u>1</u></strong>,<strong><u>3</u></strong>,2]。
由于 nums 不是唯一的最短超序列，因此返回 false。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,2,3], sequences = [[1,2]]
<strong>输出:</strong> false
<strong>解释:</strong> 最短的超序列是 [1,2]。
序列 [1,2] 是它的子序列: [<strong><u>1</u></strong>,<strong><u>2</u></strong>]。
由于 nums 不是最短超序列，因此返回 false。
</pre>

<p><strong class="example">示例 3:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]
<strong>输出:</strong> true
<strong>解释:</strong> 最短的超序列是 [1,2,3]。
序列 [1,2] 是它的子序列: [<strong><u>1</u></strong>,<strong><u>2</u></strong>,3]。
序列 [1,3] 是它的子序列: [<strong><u>1</u></strong>,2,<strong><u>3</u></strong>]。
序列 [2,3] 是它的子序列: [1,<strong><u>2</u></strong>,<strong><u>3</u></strong>]。
由于 nums 是唯一的最短超序列，因此返回 true。
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> 是范围 <code>[1, n]</code> 内所有整数的一个排列。</li>
	<li><code>1 &lt;= sequences.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= sequences[i].length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= sum(sequences[i].length) &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= sequences[i][j] &lt;= n</code></li>
	<li>所有的 <code>sequences</code> 数组都是 <strong>唯一</strong> 的。</li>
	<li><code>sequences[i]</code> 是 <code>nums</code> 的一个子序列。</li>
</ul>

---
## 解题思路与复盘

1. 一句话直击本质：
   - 使用拓扑排序验证唯一序列重建，通过检查是否存在唯一的拓扑排序路径来判断给定序列是否可以被唯一重建。

2. 综合思路：
   - 拓扑排序（BFS）：利用入度数组和邻接表构建图，使用队列进行拓扑排序，确保每次只有一个节点可以被选择以保证唯一性。

3. 全量伪代码：
   ```plaintext
   初始化节点数量 n 为 nums 的长度
   创建一个大小为 n+1 的入度数组 indegree，初始值为 0
   创建一个大小为 n+1 的邻接表 adj，初始为空列表

   对于每个序列 seq 在 sequences 中：
       对于 seq 中的每对相邻元素 (u, v)：
           在 adj[u] 中添加 v
           增加 indegree[v] 的值

   初始化队列 queue，包含所有入度为 0 的节点

   初始化结果列表 res 为空

   当队列不为空时：
       如果队列中元素数量大于 1，返回 False
       弹出队列中的第一个元素 curr
       将 curr 添加到结果列表 res 中
       对于 curr 的每个邻居 neighbor：
           减少 indegree[neighbor] 的值
           如果 indegree[neighbor] 为 0，将 neighbor 添加到队列中

   返回 res 是否等于 nums
   ```

4. 复杂度：
   - 时间复杂度：$O(n + m)$，其中 $n$ 是 nums 的长度，$m$ 是 sequences 中所有序列的总长度。
   - 空间复杂度：$O(n + m)$，用于存储入度数组和邻接表。