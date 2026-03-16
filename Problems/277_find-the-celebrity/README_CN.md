# 277. 搜寻名人

**难度**: Medium | **标签**: `Two Pointers` `Graph Theory` `Interactive`

## 题目描述

<p>假设你在一个有 <code>n</code> 个人的派对上，这些人被标记为 <code>0</code> 到 <code>n - 1</code>，其中可能存在一个名人。名人的定义是所有其他 <code>n - 1</code> 个人都认识这个名人，但名人不认识他们中的任何一个。</p>

<p>现在你想找出这个名人是谁，或者验证是否没有名人。你只能问类似于：“嗨，A。你认识B吗？”的问题，以获取关于A是否认识B的信息。你需要通过尽可能少的问题（在渐进意义上）来找出名人（或验证没有名人）。</p>

<p>给定一个整数 <code>n</code> 和一个辅助函数 <code>bool knows(a, b)</code>，该函数告诉你 <code>a</code> 是否认识 <code>b</code>。实现一个函数 <code>int findCelebrity(n)</code>。如果派对上有名人，则将会有且仅有一个名人。</p>

<p>如果派对上有名人，返回<em>名人的标签</em>。如果没有名人，返回 <code>-1</code>。</p>

<p><strong>注意</strong>，输入的 <code>n x n</code> 2D 数组 <code>graph</code> <strong>并不</strong>直接可用，而是 <strong>只能</strong>通过辅助函数 <code>knows</code> 访问。<code>graph[i][j] == 1</code> 表示人 <code>i</code> 认识人 <code>j</code>，而 <code>graph[i][j] == 0</code> 表示人 <code>j</code> 不认识人 <code>i</code>。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/01/19/g1.jpg" style="width: 224px; height: 145px;" />
<pre>
<strong>输入:</strong> graph = [[1,1,0],[0,1,0],[1,1,1]]
<strong>输出:</strong> 1
<strong>解释:</strong> 有三个人标记为 0、1 和 2。graph[i][j] = 1 表示人 i 认识人 j，否则 graph[i][j] = 0 表示人 i 不认识人 j。名人是标记为 1 的人，因为 0 和 2 都认识他，但 1 不认识任何人。
</pre>

<p><strong class="example">示例 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/01/19/g2.jpg" style="width: 224px; height: 145px;" />
<pre>
<strong>输入:</strong> graph = [[1,0,1],[1,1,0],[0,1,1]]
<strong>输出:</strong> -1
<strong>解释:</strong> 没有名人。
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>n == graph.length == graph[i].length</code></li>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>graph[i][j]</code> 是 <code>0</code> 或 <code>1</code>。</li>
	<li><code>graph[i][i] == 1</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>后续问题:</strong> 如果允许调用 API <code>knows</code> 的最大次数为 <code>3 * n</code>，你能找到一个不超过最大调用次数的解决方案吗？</p>

---
## 解题思路与复盘

1. 一句话直击本质：算法的核心逻辑是通过两次遍历确定唯一的候选者，并验证其是否为名人。

2. 综合思路：
   - **迭代法**：所有版本都使用了迭代法，通过两次遍历来确定名人。第一次遍历确定一个可能的候选者，第二次遍历验证该候选者是否满足名人的条件，即所有人都认识他且他不认识其他任何人。

3. 全量伪代码：
   ```plaintext
   定义函数 findCelebrity(n)
       初始化候选者 candidate 为 0
       对于 i 从 1 到 n-1:
           如果 candidate 知道 i:
               将 candidate 更新为 i
       
       对于 i 从 0 到 n-1:
           如果 i 等于 candidate:
               跳过当前循环
           
           如果 candidate 知道 i 或者 i 不知道 candidate:
               返回 -1
       
       返回 candidate
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，因为算法需要两次遍历每个人。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外变量。