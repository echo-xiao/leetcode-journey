# 3790. 水果成篮 II

**难度**: Easy | **标签**: `Array` `Binary Search` `Segment Tree` `Simulation` `Ordered Set`

## 题目描述

<p>给你两个长度为 <code>n</code>&nbsp;的整数数组，<code>fruits</code> 和 <code>baskets</code>，其中 <code>fruits[i]</code> 表示第 <code>i</code>&nbsp;种水果的 <strong>数量</strong>，<code>baskets[j]</code> 表示第 <code>j</code>&nbsp;个篮子的 <strong>容量</strong>。</p>

<p>你需要对 <code>fruits</code> 数组从左到右按照以下规则放置水果：</p>

<ul>
	<li>每种水果必须放入第一个 <strong>容量大于等于</strong> 该水果数量的 <strong>最左侧可用篮子</strong> 中。</li>
	<li>每个篮子只能装 <b>一种</b> 水果。</li>
	<li>如果一种水果 <b>无法放入</b> 任何篮子，它将保持 <b>未放置</b>。</li>
</ul>

<p>返回所有可能分配完成后，剩余未放置的水果种类的数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">fruits = [4,2,5], baskets = [3,5,4]</span></p>

<p><strong>输出：</strong> <span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><code>fruits[0] = 4</code> 放入 <code>baskets[1] = 5</code>。</li>
	<li><code>fruits[1] = 2</code> 放入 <code>baskets[0] = 3</code>。</li>
	<li><code>fruits[2] = 5</code> 无法放入 <code>baskets[2] = 4</code>。</li>
</ul>

<p>由于有一种水果未放置，我们返回 1。</p>
</div>

<p><strong class="example">示例 2</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">fruits = [3,6,1], baskets = [6,4,7]</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><code>fruits[0] = 3</code> 放入 <code>baskets[0] = 6</code>。</li>
	<li><code>fruits[1] = 6</code> 无法放入 <code>baskets[1] = 4</code>（容量不足），但可以放入下一个可用的篮子 <code>baskets[2] = 7</code>。</li>
	<li><code>fruits[2] = 1</code> 放入 <code>baskets[1] = 4</code>。</li>
</ul>

<p>由于所有水果都已成功放置，我们返回 0。</p>
</div>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>n == fruits.length == baskets.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= fruits[i], baskets[i] &lt;= 1000</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是使用贪心策略，通过遍历水果和篮子，尽可能将每个水果放入一个未使用且容量足够的篮子中。

2. 综合思路：
   - 贪心策略：两种实现都采用了贪心策略，通过从左到右遍历水果和篮子，尝试将每个水果放入第一个容量足够且未使用的篮子中。
   - 数据结构：使用布尔数组来标记篮子是否已被使用。

3. 全量伪代码：
   ```plaintext
   定义函数 numOfUnplacedFruits(fruits, baskets):
       初始化布尔数组 is_basket_used，长度为篮子数量，初始值为 False
       初始化未放置水果计数器 unplaced_count 为 0

       对于每个水果 fruit_quantity 在 fruits 中:
           初始化 fruit_placed 为 False，表示当前水果是否已放置

           对于每个篮子索引 i 从 0 到 len(baskets) - 1:
               如果篮子未使用且容量大于等于当前水果:
                   标记篮子为已使用
                   标记水果为已放置
                   跳出当前循环

           如果水果未放置:
               增加未放置水果计数器 unplaced_count

       返回未放置水果计数器 unplaced_count
   ```

4. 复杂度：
   - 时间复杂度：$O(n \times m)$，其中 $n$ 是水果的数量，$m$ 是篮子的数量，因为每个水果都可能需要检查所有篮子。
   - 空间复杂度：$O(m)$，用于存储篮子的使用状态。