# 2715. K 件物品的最大和

**难度**: Easy | **标签**: `Math` `Greedy`

## 题目描述

<p>袋子中装有一些物品，每个物品上都标记着数字 <code>1</code> 、<code>0</code> 或 <code>-1</code> 。</p>

<p>给你四个非负整数 <code>numOnes</code> 、<code>numZeros</code> 、<code>numNegOnes</code> 和 <code>k</code> 。</p>

<p>袋子最初包含：</p>

<ul>
	<li><code>numOnes</code> 件标记为 <code>1</code> 的物品。</li>
	<li><code>numZeros</code> 件标记为 <code>0</code> 的物品。</li>
	<li><code>numNegOnes</code> 件标记为 <code>-1</code> 的物品。</li>
</ul>

<p>现计划从这些物品中恰好选出 <code>k</code> 件物品。返回所有可行方案中，物品上所标记数字之和的最大值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2
<strong>输出：</strong>2
<strong>解释：</strong>袋子中的物品分别标记为 {1, 1, 1, 0, 0} 。取 2 件标记为 1 的物品，得到的数字之和为 2 。
可以证明 2 是所有可行方案中的最大值。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4
<strong>输出：</strong>3
<strong>解释：</strong>袋子中的物品分别标记为 {1, 1, 1, 0, 0} 。取 3 件标记为 1 的物品，1 件标记为 0 的物品，得到的数字之和为 3 。
可以证明 3 是所有可行方案中的最大值。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= numOnes, numZeros, numNegOnes &lt;= 50</code></li>
	<li><code>0 &lt;= k &lt;= numOnes + numZeros + numNegOnes</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是优先选择尽可能多的正数1，其次选择0，最后选择负数-1，以最大化总和。

2. 综合思路：
   - 迭代解法：通过条件判断依次选择1、0和-1，确保在选择的k个物品中总和最大化。
   - 递归解法：虽然在提供的代码中没有递归实现，但可以通过递归方式逐步减少k并选择最优的物品类型。

3. 全量伪代码：
   ```
   定义函数 kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k):
       如果 k 小于等于 numOnes:
           返回 k
       否则:
           如果 k - numOnes 小于等于 numZeros:
               返回 numOnes
           否则:
               计算被迫选择的 -1 的数量 forced_neg_ones_count = k - numOnes - numZeros
               返回 numOnes - forced_neg_ones_count
   ```

4. 复杂度：
   - 时间复杂度：$O(1)$，因为算法只涉及常数次的条件判断和简单的算术运算。
   - 空间复杂度：$O(1)$，因为算法只使用了固定数量的额外变量。