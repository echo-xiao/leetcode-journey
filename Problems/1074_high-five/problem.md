# 1074. 前五科的均分 · 题目

**难度**: Easy | **标签**: `Array` `Hash Table` `Sorting` `Heap (Priority Queue)`

## 题目描述

<p>给定一个不同学生的分数列表，<code>items</code>，其中 <code>items[i] = [ID<sub>i</sub>, score<sub>i</sub>]</code> 表示一个学生的分数，ID 为 <code>ID<sub>i</sub></code>，计算每个学生的 <strong>前五名平均分</strong>。</p>

<p>返回 <em>作为一对数组的答案 </em><code>result</code><em>，其中 </em><code>result[j] = [ID<sub>j</sub>, topFiveAverage<sub>j</sub>]</code><em> 表示学生的 </em><code>ID<sub>j</sub></code><em> 及其 <strong>前五名平均分</strong>。按 </em><code>ID<sub>j</sub></code><em> 的 <strong>升序</strong> 排序 </em><code>result</code><em>。</em></p>

<p>学生的 <strong>前五名平均分</strong> 是通过将他们的前五个分数相加并使用 <strong>整数除法</strong> 除以 <code>5</code> 来计算的。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
<strong>输出:</strong> [[1,87],[2,88]]
<strong>解释: </strong>
ID = 1 的学生获得了分数 91, 92, 60, 65, 87 和 100。他们的前五名平均分是 (100 + 92 + 91 + 87 + 65) / 5 = 87。
ID = 2 的学生获得了分数 93, 97, 77, 100 和 76。他们的前五名平均分是 (100 + 97 + 93 + 77 + 76) / 5 = 88.6，但通过整数除法，他们的平均分转换为 88。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
<strong>输出:</strong> [[1,100],[7,100]]
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>1 &lt;= items.length &lt;= 1000</code></li>
	<li><code>items[i].length == 2</code></li>
	<li><code>1 &lt;= ID<sub>i</sub> &lt;= 1000</code></li>
	<li><code>0 &lt;= score<sub>i</sub> &lt;= 100</code></li>
	<li>对于每个 <code>ID<sub>i</sub></code>，将至少有五个分数。</li>
</ul>
