# 3334. 重新分装苹果

**难度**: Easy | **标签**: `Array` `Greedy` `Sorting`

## 题目描述

<p>给你一个长度为 <code>n</code> 的数组 <code>apple</code> 和另一个长度为 <code>m</code> 的数组 <code>capacity</code> 。</p>

<p>一共有 <code>n</code> 个包裹，其中第 <code>i</code> 个包裹中装着 <code>apple[i]</code> 个苹果。同时，还有 <code>m</code> 个箱子，第 <code>i</code> 个箱子的容量为 <code>capacity[i]</code> 个苹果。</p>

<p>请你选择一些箱子来将这 <code>n</code> 个包裹中的苹果重新分装到箱子中，返回你需要选择的箱子的<strong> 最小</strong> 数量。</p>

<p><strong>注意</strong>，同一个包裹中的苹果可以分装到不同的箱子中。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>apple = [1,3,2], capacity = [4,3,1,5,2]
<strong>输出：</strong>2
<strong>解释：</strong>使用容量为 4 和 5 的箱子。
总容量大于或等于苹果的总数，所以可以完成重新分装。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>apple = [5,5,5], capacity = [2,4,2,7]
<strong>输出：</strong>4
<strong>解释：</strong>需要使用所有箱子。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == apple.length &lt;= 50</code></li>
	<li><code>1 &lt;= m == capacity.length &lt;= 50</code></li>
	<li><code>1 &lt;= apple[i], capacity[i] &lt;= 50</code></li>
	<li>输入数据保证可以将包裹中的苹果重新分装到箱子中。</li>
</ul>


---
## 解题思路与复盘

1. **一句话总结核心逻辑**：通过对箱子容量从大到小排序，逐个累加容量直到满足苹果总数，从而找到最少的箱子数量。

2. **综合思路**：
   - **贪心算法**：此题采用贪心算法，通过优先使用容量最大的箱子，逐步累加容量，直到满足苹果的总需求量。这样可以确保使用最少数量的箱子。
   - **排序与累加**：首先对箱子容量进行排序，然后通过累加容量来判断是否满足条件。

3. **全量伪代码**：
   ```plaintext
   定义函数 minimumBoxes(苹果数量列表, 箱子容量列表):
       计算苹果总数 = 苹果数量列表的总和
       将箱子容量列表按降序排序
       初始化箱子计数 = 0
       初始化当前容量 = 0

       对于每个箱子容量 in 排序后的箱子容量列表:
           将当前容量增加当前箱子容量
           增加箱子计数
           如果当前容量 >= 苹果总数:
               跳出循环

       返回箱子计数
   ```

4. **复杂度**：
   - 时间复杂度：$O(n \log n)$，其中 $n$ 是箱子数量，因为需要对箱子容量进行排序。
   - 空间复杂度：$O(1)$，因为只使用了常数级别的额外空间。