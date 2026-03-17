# 433. 最小基因变化

**难度**: Medium | **标签**: `Hash Table` `String` `Breadth-First Search`

**归类**: 8. 常用数据结构 > Hash Table

## 题目描述

<p>基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 <code>'A'</code>、<code>'C'</code>、<code>'G'</code> 和 <code>'T'</code> 之一。</p>

<p>假设我们需要调查从基因序列&nbsp;<code>start</code> 变为 <code>end</code> 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。</p>

<ul>
	<li>例如，<code>"AACCGGTT" --&gt; "AACCGGTA"</code> 就是一次基因变化。</li>
</ul>

<p>另有一个基因库 <code>bank</code> 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。（变化后的基因必须位于基因库 <code>bank</code> 中）</p>

<p>给你两个基因序列 <code>start</code> 和 <code>end</code> ，以及一个基因库 <code>bank</code> ，请你找出并返回能够使&nbsp;<code>start</code> 变化为 <code>end</code> 所需的最少变化次数。如果无法完成此基因变化，返回 <code>-1</code> 。</p>

<p>注意：起始基因序列&nbsp;<code>start</code> 默认是有效的，但是它并不一定会出现在基因库中。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
<strong>输出：</strong>3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>start.length == 8</code></li>
	<li><code>end.length == 8</code></li>
	<li><code>0 &lt;= bank.length &lt;= 10</code></li>
	<li><code>bank[i].length == 8</code></li>
	<li><code>start</code>、<code>end</code> 和 <code>bank[i]</code> 仅由字符 <code>['A', 'C', 'G', 'T']</code> 组成</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法使用广度优先搜索（BFS）在基因序列的变化路径中寻找从起始基因到目标基因的最短变化序列。

2. 综合思路：
   - 广度优先搜索（BFS）：使用队列来逐层遍历可能的基因变化，从起始基因开始，每次改变一个字符，检查是否能到达目标基因，确保找到最短路径。
   - 数据结构：使用集合来存储基因库以便快速查找，使用队列来实现广度优先搜索，使用集合来跟踪已访问的基因以避免重复访问。

3. 全量伪代码：
   ```
   定义函数 minMutation(startGene, endGene, bank)
       将 bank 转换为集合 bank_set
       如果 endGene 不在 bank_set 中
           返回 -1

       初始化队列 queue，包含元组 (startGene, 0)
       初始化集合 visited，包含 startGene

       当队列 queue 不为空时
           弹出队列的第一个元素，赋值给 curr 和 step

           如果 curr 等于 endGene
               返回 step

           对于 curr 中的每个字符位置 i
               对于字符集合 'ACGT' 中的每个字符 char
                   生成新的基因序列 nxt_gene
                   如果 nxt_gene 在 bank_set 中且不在 visited 中
                       将 nxt_gene 添加到 visited
                       将 (nxt_gene, step+1) 添加到队列 queue

       返回 -1
   ```

4. 复杂度：
   - 时间复杂度：$O(N \times M \times 4)$，其中 $N$ 是基因序列的长度，$M$ 是基因库的大小，4 是每个位置可能的字符变化数。
   - 空间复杂度：$O(M)$，用于存储基因库集合和访问集合。