# 1916. 找出星型图的中心节点

**难度**: Easy | **标签**: `Graph Theory`

## 题目描述

<p>有一个无向的 <strong>星型</strong> 图，由 <code>n</code> 个编号从 <code>1</code> 到 <code>n</code> 的节点组成。星型图有一个 <strong>中心</strong> 节点，并且恰有 <code>n - 1</code> 条边将中心节点与其他每个节点连接起来。</p>

<p>给你一个二维整数数组 <code>edges</code> ，其中 <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> 表示在节点 <code>u<sub>i</sub></code> 和 <code>v<sub>i</sub></code> 之间存在一条边。请你找出并返回 <code>edges</code> 所表示星型图的中心节点。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/03/14/star_graph.png" style="width: 331px; height: 321px;" />
<pre>
<strong>输入：</strong>edges = [[1,2],[2,3],[4,2]]
<strong>输出：</strong>2
<strong>解释：</strong>如上图所示，节点 2 与其他每个节点都相连，所以节点 2 是中心节点。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>edges = [[1,2],[5,1],[1,3],[1,4]]
<strong>输出：</strong>1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 <= n <= 10<sup>5</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>1 <= u<sub>i,</sub> v<sub>i</sub> <= n</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li>题目数据给出的 <code>edges</code> 表示一个有效的星型图</li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过构建邻接表，找到连接所有其他节点的节点即为星型图的中心节点。

2. **综合思路：**
   - **邻接表法：** 使用一个哈希表（字典）记录每个节点的邻接节点列表，遍历每个节点的邻接列表，找到连接数为 $n-1$ 的节点。
   - **直接比较法：** 由于星型图的中心节点会在所有边中出现，因此可以直接比较前两条边的节点，找到公共节点即为中心节点。

3. **全量伪代码：**

   - **邻接表法：**
     ```
     初始化一个空的邻接表 mapp
     对于每条边 (u, v)：
         将 v 添加到 mapp[u] 的邻接列表中
         将 u 添加到 mapp[v] 的邻接列表中
     计算节点总数 n = 边数 + 1
     对于邻接表中的每个节点 k：
         如果 k 的邻接节点数为 n - 1：
             返回 k 作为中心节点
     返回 -1 （如果没有找到中心节点）
     ```

   - **直接比较法：**
     ```
     取第一条边的两个节点 a 和 b
     如果第二条边的任一节点等于 a：
         返回 a 作为中心节点
     否则：
         返回 b 作为中心节点
     ```

4. **复杂度：**

   - **邻接表法：** 
     - 时间复杂度：$O(n)$，其中 $n$ 是边的数量，因为需要遍历所有边来构建邻接表。
     - 空间复杂度：$O(n)$，因为邻接表需要存储每个节点的邻接列表。

   - **直接比较法：**
     - 时间复杂度：$O(1)$，因为只需检查前两条边。
     - 空间复杂度：$O(1)$，因为不需要额外的数据结构。