# 1141. 最多可以买到的苹果数量

**难度**: Easy | **标签**: `Array` `Greedy` `Sorting`

## 题目描述

<p>你有一些苹果和一个可以承载最多 <code>5000</code> 单位重量的篮子。</p>

<p>给定一个整数数组 <code>weight</code>，其中 <code>weight[i]</code> 是第 <code>i<sup>th</sup></code> 个苹果的重量，返回 <em>你可以放入篮子的苹果的最大数量</em>。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> weight = [100,200,150,1000]
<strong>输出:</strong> 4
<strong>解释:</strong> 所有 4 个苹果的重量之和为 1450，可以被篮子承载。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> weight = [900,950,800,1000,700,800]
<strong>输出:</strong> 5
<strong>解释:</strong> 6 个苹果的重量之和超过 5000，所以我们选择其中任意 5 个。
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>1 &lt;= weight.length &lt;= 10<sup>3</sup></code></li>
	<li><code>1 &lt;= weight[i] &lt;= 10<sup>3</sup></code></li>
</ul>

---
## 解题思路与复盘

1. 一句话直击本质：该算法通过对苹果重量排序后，逐个累加重量直至达到最大承载重量，从而计算最多能买到的苹果数量。

2. 综合思路：
   - 贪心算法：两种实现都采用贪心策略，先对苹果重量进行排序，然后从最轻的苹果开始累加，直到累加重量超过最大承载重量为止。
   - 迭代实现：通过简单的迭代方式遍历苹果重量列表，逐个累加并计数。

3. 全量伪代码：
   ```
   定义函数 maxNumberOfApples(重量列表):
       将重量列表排序
       初始化目标重量为 5000
       初始化累加重量为 0
       初始化苹果计数为 0
       对于每个苹果重量 w 在重量列表中:
           如果累加重量加上当前苹果重量小于等于目标重量:
               更新累加重量
               增加苹果计数
           否则:
               跳出循环
       返回苹果计数
   ```

4. 复杂度：
   - 时间复杂度：$O(n \log n)$，其中 $n$ 是苹果的数量，因为需要对重量列表进行排序。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外变量。