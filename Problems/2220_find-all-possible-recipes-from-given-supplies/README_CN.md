# 2220. 从给定原材料中找到所有可以做出的菜

**难度**: Medium | **标签**: `Array` `Hash Table` `String` `Graph Theory` `Topological Sort`

## 题目描述

<p>你有 <code>n</code>&nbsp;道不同菜的信息。给你一个字符串数组&nbsp;<code>recipes</code>&nbsp;和一个二维字符串数组&nbsp;<code>ingredients</code>&nbsp;。第&nbsp;<code>i</code>&nbsp;道菜的名字为&nbsp;<code>recipes[i]</code>&nbsp;，如果你有它&nbsp;<strong>所有</strong>&nbsp;的原材料&nbsp;<code>ingredients[i]</code>&nbsp;，那么你可以&nbsp;<strong>做出</strong>&nbsp;这道菜。一份食谱也可以是 <strong>其它</strong>&nbsp;食谱的原料，也就是说&nbsp;<code>ingredients[i]</code>&nbsp;可能包含&nbsp;<code>recipes</code>&nbsp;中另一个字符串。</p>

<p>同时给你一个字符串数组&nbsp;<code>supplies</code>&nbsp;，它包含你初始时拥有的所有原材料，每一种原材料你都有无限多。</p>

<p>请你返回你可以做出的所有菜。你可以以 <strong>任意顺序</strong>&nbsp;返回它们。</p>

<p>注意两道菜在它们的原材料中可能互相包含。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
<b>输出：</b>["bread"]
<strong>解释：</strong>
我们可以做出 "bread" ，因为我们有原材料 "yeast" 和 "flour" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
<b>输出：</b>["bread","sandwich"]
<strong>解释：</strong>
我们可以做出 "bread" ，因为我们有原材料 "yeast" 和 "flour" 。
我们可以做出 "sandwich" ，因为我们有原材料 "meat" 且可以做出原材料 "bread" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
<b>输出：</b>["bread","sandwich","burger"]
<strong>解释：</strong>
我们可以做出 "bread" ，因为我们有原材料 "yeast" 和 "flour" 。
我们可以做出 "sandwich" ，因为我们有原材料 "meat" 且可以做出原材料 "bread" 。
我们可以做出 "burger" ，因为我们有原材料 "meat" 且可以做出原材料 "bread" 和 "sandwich" 。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<b>输入：</b>recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast"]
<b>输出：</b>[]
<strong>解释：</strong>
我们没法做出任何菜，因为我们只有原材料 "yeast" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == recipes.length == ingredients.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= ingredients[i].length, supplies.length &lt;= 100</code></li>
	<li><code>1 &lt;= recipes[i].length, ingredients[i][j].length, supplies[k].length &lt;= 10</code></li>
	<li><code>recipes[i], ingredients[i][j]</code>&nbsp;和&nbsp;<code>supplies[k]</code>&nbsp;只包含小写英文字母。</li>
	<li>所有&nbsp;<code>recipes</code> 和&nbsp;<code>supplies</code>&nbsp;中的值互不相同。</li>
	<li><code>ingredients[i]</code>&nbsp;中的字符串互不相同。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过构建依赖图并使用拓扑排序或深度优先搜索来确定哪些菜肴可以根据现有的原材料和供应品制作。

2. 综合思路：
   - **深度优先搜索 (DFS) 解法**：通过递归遍历每个菜肴的依赖关系，使用状态标记来避免重复计算和检测循环依赖。
   - **拓扑排序 (BFS) 解法**：使用队列和入度计数来进行拓扑排序，逐步减少依赖关系，确定可以制作的菜肴。

3. 全量伪代码：
   - **DFS 版本伪代码**：
     ```
     初始化图 graph 和供应品集合 suppSet
     对于每个菜肴，构建其所需原料的依赖关系
     初始化状态字典 status
     对于每个菜肴，调用 DFS 函数
     如果 DFS 返回 True，添加菜肴到结果列表
     返回结果列表

     DFS 函数(name, graph, suppSet, status):
         如果 name 在 suppSet 中，返回 True
         如果 name 不在 graph 中，返回 False
         如果 name 在 status 中，根据状态返回相应的结果
         将 name 标记为正在处理
         对于 name 所需的每个原料，递归调用 DFS
         如果任何一个原料不可用，标记 name 为不可制作并返回 False
         将 name 标记为可制作并返回 True
     ```

   - **BFS 版本伪代码**：
     ```
     初始化图 graph 和入度字典 indegree
     对于每个菜肴，构建其所需原料的依赖关系，并更新入度
     初始化队列 queue 并将所有供应品加入队列
     初始化结果列表 ans
     当队列不为空时，进行以下操作：
         从队列中取出当前元素 curr
         如果 curr 是菜肴，添加到结果列表
         对于 curr 的每个后继菜肴，减少其入度
         如果后继菜肴的入度为 0，将其加入队列
     返回结果列表
     ```

4. 复杂度：
   - **时间复杂度**：对于 DFS 解法，时间复杂度为 $O(V + E)$，其中 $V$ 是菜肴数量，$E$ 是原料依赖关系的数量。对于 BFS 解法，时间复杂度同样为 $O(V + E)$。
   - **空间复杂度**：两种解法的空间复杂度均为 $O(V + E)$，用于存储图结构和辅助数据结构（如状态字典或入度字典）。