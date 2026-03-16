# 170. 两数之和 III - 数据结构设计

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

---
## 解题思路与复盘

1. 一句话直击本质：使用哈希表存储每个数字的出现次数，通过遍历检查是否存在两个数之和等于目标值。

2. 综合思路：
   - 哈希表法：利用哈希表存储每个数字的出现次数，`add` 操作将数字加入哈希表，`find` 操作通过遍历哈希表检查是否存在两个数之和等于目标值。
   - 该题目主要有一个实现思路，即使用哈希表来高效地进行查找和存储操作。

3. 全量伪代码：
   ```plaintext
   类 TwoSum:
       初始化:
           创建一个空的哈希表 counts

       方法 add(数字 number):
           如果 number 在 counts 中:
               将 counts[number] 增加 1
           否则:
               将 counts[number] 设为 1

       方法 find(值 value):
           对于 counts 中的每个数字 num:
               计算差值 diff = value - num
               如果 diff 在 counts 中:
                   如果 diff 不等于 num:
                       返回 True
                   否则如果 counts[num] >= 2:
                       返回 True
           返回 False
   ```

4. 复杂度：
   - 时间复杂度：`add` 操作的时间复杂度为 $O(1)$，`find` 操作的时间复杂度为 $O(n)$，其中 $n$ 是哈希表中的不同数字个数。
   - 空间复杂度：空间复杂度为 $O(n)$，其中 $n$ 是哈希表中存储的不同数字个数。