# 2602. 最多可以摧毁的敌人城堡数目

**难度**: Easy | **标签**: `Array` `Two Pointers`

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;，下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>forts</code>&nbsp;，表示一些城堡。<code>forts[i]</code> 可以是&nbsp;<code>-1</code>&nbsp;，<code>0</code>&nbsp;或者&nbsp;<code>1</code>&nbsp;，其中：</p>

<ul>
	<li><code>-1</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;个位置 <strong>没有</strong>&nbsp;城堡。</li>
	<li><code>0</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;个位置有一个 <strong>敌人</strong>&nbsp;的城堡。</li>
	<li><code>1</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;个位置有一个你控制的城堡。</li>
</ul>

<p>现在，你需要决定，将你的军队从某个你控制的城堡位置&nbsp;<code>i</code>&nbsp;移动到一个空的位置&nbsp;<code>j</code>&nbsp;，满足：</p>

<ul>
	<li><code>0 &lt;= i, j &lt;= n - 1</code></li>
	<li>军队经过的位置 <strong>只有</strong>&nbsp;敌人的城堡。正式的，对于所有&nbsp;<code>min(i,j) &lt; k &lt; max(i,j)</code>&nbsp;的&nbsp;<code>k</code>&nbsp;，都满足&nbsp;<code>forts[k] == 0</code>&nbsp;。</li>
</ul>

<p>当军队移动时，所有途中经过的敌人城堡都会被 <strong>摧毁</strong> 。</p>

<p>请你返回 <strong>最多</strong>&nbsp;可以摧毁的敌人城堡数目。如果 <strong>无法</strong>&nbsp;移动你的军队，或者没有你控制的城堡，请返回 <code>0</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>forts = [1,0,0,-1,0,0,0,0,1]
<b>输出：</b>4
<strong>解释：</strong>
- 将军队从位置 0 移动到位置 3 ，摧毁 2 个敌人城堡，位置分别在 1 和 2 。
- 将军队从位置 8 移动到位置 3 ，摧毁 4 个敌人城堡。
4 是最多可以摧毁的敌人城堡数目，所以我们返回 4 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>forts = [0,0,1,-1]
<b>输出：</b>0
<b>解释：</b>由于无法摧毁敌人的城堡，所以返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= forts.length &lt;= 1000</code></li>
	<li><code>-1 &lt;= forts[i] &lt;= 1</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法通过遍历城堡列表，寻找相邻不同类型城堡之间的空地数量，并记录最大值。

2. 综合思路：
   - 迭代法：遍历整个城堡列表，记录上一个非零城堡的位置，当遇到不同类型的城堡时，计算两者之间的空地数量，并更新最大值。

3. 全量伪代码：
   ```
   初始化最大摧毁城堡数 max_cnt 为 0
   初始化上一个非零城堡的索引 idx 为 -1

   对于每个城堡位置 i 从 0 到 forts 列表的长度 - 1：
       如果 forts[i] 是 0，继续下一个位置
       如果 forts[i] 是 1 或 -1：
           如果 idx 不等于 -1 且 forts[i] 与 forts[idx] 相同：
               跳过（不做任何操作）
           如果 idx 不等于 -1 且 forts[i] 与 forts[idx] 不同：
               计算当前城堡与上一个城堡之间的空地数量 cnt 为 i - idx - 1
               更新 max_cnt 为 max(max_cnt, cnt)
       更新 idx 为当前城堡位置 i

   返回 max_cnt 作为结果
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是城堡列表的长度，因为算法需要遍历整个列表一次。
   - 空间复杂度：$O(1)$，因为算法只使用了常数个额外的变量。