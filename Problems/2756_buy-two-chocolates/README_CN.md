# 2756. 购买两块巧克力

**难度**: Easy | **标签**: `Array` `Greedy` `Sorting`

## 题目描述

<p>给你一个整数数组&nbsp;<code>prices</code>&nbsp;，它表示一个商店里若干巧克力的价格。同时给你一个整数&nbsp;<code>money</code>&nbsp;，表示你一开始拥有的钱数。</p>

<p>你必须购买 <strong>恰好&nbsp;</strong>两块巧克力，而且剩余的钱数必须是 <strong>非负数</strong>&nbsp;。同时你想最小化购买两块巧克力的总花费。</p>

<p>请你返回在购买两块巧克力后，最多能剩下多少钱。如果购买任意两块巧克力都超过了你拥有的钱，请你返回 <code>money</code>&nbsp;。注意剩余钱数必须是非负数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>prices = [1,2,2], money = 3
<b>输出：</b>0
<b>解释：</b>分别购买价格为 1 和 2 的巧克力。你剩下 3 - 3 = 0 块钱。所以我们返回 0 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>prices = [3,2,3], money = 3
<b>输出：</b>3
<b>解释：</b>购买任意 2 块巧克力都会超过你拥有的钱数，所以我们返回 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= prices.length &lt;= 50</code></li>
	<li><code>1 &lt;= prices[i] &lt;= 100</code></li>
	<li><code>1 &lt;= money &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过排序找到价格最低的两块巧克力，判断是否可以购买并返回剩余金额。

2. 综合思路：
   - 排序法：首先对价格列表进行排序，然后选择价格最低的两块巧克力，计算其总和并与可用金额进行比较，最后返回剩余金额。
   - 该题目主要涉及排序和简单的条件判断，没有其他复杂的解法。

3. 全量伪代码：
   ```
   定义函数 buyChoco(prices, money):
       将 prices 列表进行升序排序
       计算最便宜的两块巧克力的总价格 ttl = prices[0] + prices[1]
       如果 ttl 大于 money:
           返回 money （无法购买两块巧克力）
       否则:
           返回 money - ttl （购买两块巧克力后的剩余金额）
   ```

4. 复杂度：
   - 时间复杂度：$O(n \log n)$，其中 $n$ 是价格列表的长度，因为排序操作的时间复杂度为 $O(n \log n)$。
   - 空间复杂度：$O(1)$，因为只使用了常量级别的额外空间。