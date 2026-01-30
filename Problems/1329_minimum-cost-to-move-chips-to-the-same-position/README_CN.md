# 1329. 玩筹码

**难度**: Easy | **标签**: `Array` `Math` `Greedy`

## 题目描述

<p>有&nbsp;<code>n</code>&nbsp;个筹码。第 <code>i</code> 个筹码的位置是<meta charset="UTF-8" />&nbsp;<code>position[i]</code>&nbsp;。</p>

<p>我们需要把所有筹码移到同一个位置。在一步中，我们可以将第 <code>i</code> 个筹码的位置从&nbsp;<code>position[i]</code>&nbsp;改变为:</p>

<p><meta charset="UTF-8" /></p>

<ul>
	<li><code>position[i] + 2</code>&nbsp;或&nbsp;<code>position[i] - 2</code>&nbsp;，此时&nbsp;<code>cost = 0</code></li>
	<li><code>position[i] + 1</code>&nbsp;或&nbsp;<code>position[i] - 1</code>&nbsp;，此时&nbsp;<code>cost = 1</code></li>
</ul>

<p>返回将所有筹码移动到同一位置上所需要的 <em>最小代价</em> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/08/15/chips_e1.jpg" style="height: 217px; width: 750px;" /></p>

<pre>
<strong>输入：</strong>position = [1,2,3]
<strong>输出：</strong>1
<strong>解释：</strong>第一步:将位置3的筹码移动到位置1，成本为0。
第二步:将位置2的筹码移动到位置1，成本= 1。
总成本是1。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/08/15/chip_e2.jpg" style="height: 306px; width: 750px;" /></p>

<pre>
<strong>输入：</strong>position = [2,2,2,3,3]
<strong>输出：</strong>2
<strong>解释：</strong>我们可以把位置3的两个筹码移到位置2。每一步的成本为1。总成本= 2。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入：</strong>position = [1,1000000000]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= position.length &lt;= 100</code></li>
	<li><code>1 &lt;= position[i] &lt;= 10^9</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：算法的核心逻辑是计算奇数位置和偶数位置的筹码数量，选择较小的数量作为移动筹码的最小成本。

2. 综合思路：
   - 计数法：遍历所有筹码位置，分别统计奇数位置和偶数位置的筹码数量，最后返回较小的数量作为结果。这是因为移动筹码到相邻位置的成本为0，而移动到相隔位置的成本为1，因此将所有筹码移动到奇数或偶数位置的成本取决于较少的筹码数量。

3. 全量伪代码：
   ```
   定义函数 minCostToMoveChips，输入为筹码位置列表 position
       初始化 oddCount 为 0
       初始化 evenCount 为 0

       对于 position 中的每个位置 i：
           如果 i 是偶数：
               将 evenCount 增加 1
           否则：
               将 oddCount 增加 1

       如果 oddCount 小于等于 evenCount：
           返回 oddCount
       否则：
           返回 evenCount
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是筹码位置的数量，因为需要遍历所有位置一次。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外的变量来存储计数。