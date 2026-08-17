# 170. 两数之和 III - 数据结构设计 · 题目

**难度**: Easy | **标签**: `Array` `Hash Table` `Two Pointers` `Design` `Data Stream`

## 题目描述

<p>设计一个数据结构，接受一系列整数流，并检查是否存在一对整数的和等于特定值。</p>

<p>实现 <code>TwoSum</code> 类：</p>

<ul>
	<li><code>TwoSum()</code> 初始化 <code>TwoSum</code> 对象，初始时为空数组。</li>
	<li><code>void add(int number)</code> 将 <code>number</code> 添加到数据结构中。</li>
	<li><code>boolean find(int value)</code> 如果存在任何一对数字的和等于 <code>value</code>，则返回 <code>true</code>，否则返回 <code>false</code>。</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入</strong>
[&quot;TwoSum&quot;, &quot;add&quot;, &quot;add&quot;, &quot;add&quot;, &quot;find&quot;, &quot;find&quot;]
[[], [1], [3], [5], [4], [7]]
<strong>输出</strong>
[null, null, null, null, true, false]

<strong>解释</strong>
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --&gt; [1]
twoSum.add(3);   // [1] --&gt; [1,3]
twoSum.add(5);   // [1,3] --&gt; [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, 返回 true
twoSum.find(7);  // 没有两个整数的和等于 7，返回 false
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>-10<sup>5</sup> &lt;= number &lt;= 10<sup>5</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= value &lt;= 2<sup>31</sup> - 1</code></li>
	<li>最多会对 <code>add</code> 和 <code>find</code> 调用 <code>10<sup>4</sup></code> 次。</li>
</ul>
