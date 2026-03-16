# 1980. 有缺陷的传感器

**难度**: Easy | **标签**: `Array` `Two Pointers`

## 题目描述

<p>实验正在实验室进行。为了确保准确性，有<strong>两个</strong>传感器同时收集数据。给定两个数组<code>sensor1</code>和<code>sensor2</code>，其中<code>sensor1[i]</code>和<code>sensor2[i]</code>是两个传感器收集的第<code>i<sup>th</sup></code>个数据点。</p>

<p>然而，这种类型的传感器有可能出现缺陷，这会导致<strong>恰好一个</strong>数据点被丢弃。在数据被丢弃后，丢弃数据右侧的所有数据点将<strong>向左</strong>移动一个位置，最后一个数据点将被某个<strong>随机值</strong>替换。可以保证这个随机值<strong>不会</strong>等于被丢弃的值。</p>

<ul>
	<li>例如，如果正确的数据是<code>[1,2,<u><strong>3</strong></u>,4,5]</code>，而<code>3</code>被丢弃，传感器可能返回<code>[1,2,4,5,<u><strong>7</strong></u>]</code>（最后一个位置可以是<strong>任何</strong>值，而不仅仅是<code>7</code>）。</li>
</ul>

<p>我们知道最多只有<strong>一个</strong>传感器存在缺陷。返回<em>有缺陷的传感器编号（</em><code>1</code><em>或</em><code>2</code><em>）。如果两个传感器都<strong>没有缺陷</strong>，或者<strong>无法</strong>确定哪个传感器有缺陷，则返回</em><code>-1</code><em>。</em></p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> sensor1 = [2,3,4,5], sensor2 = [2,1,3,4]
<strong>输出:</strong> 1
<strong>解释:</strong> 传感器 2 的值是正确的。
传感器 2 的第二个数据点被丢弃，传感器 1 的最后一个值被替换为 5。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> sensor1 = [2,2,2,2,2], sensor2 = [2,2,2,2,5]
<strong>输出:</strong> -1
<strong>解释:</strong> 无法确定哪个传感器有缺陷。
丢弃任一传感器的最后一个值都可能产生另一个传感器的输出。
</pre>

<p><strong class="example">示例 3:</strong></p>

<pre>
<strong>输入:</strong> sensor1 = [2,3,2,2,3,2], sensor2 = [2,3,2,3,2,7]
<strong>输出:</strong> 2
<strong>解释:</strong> 传感器 1 的值是正确的。
传感器 1 的第四个数据点被丢弃，传感器 1 的最后一个值被替换为 7。
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>sensor1.length == sensor2.length</code></li>
	<li><code>1 &lt;= sensor1.length &lt;= 100</code></li>
	<li><code>1 &lt;= sensor1[i], sensor2[i] &lt;= 100</code></li>
</ul>

---
## 解题思路与复盘

1. 一句话直击本质：通过比较两个传感器数据的偏移子数组来判断哪个传感器有缺陷。

2. 综合思路：
   - 迭代比较：逐个比较两个传感器的数据，当发现不一致时，通过比较偏移后的子数组来判断哪个传感器有缺陷，或者无法判断。
   - 由于题目提供的代码只有一种实现方式，因此没有其他解法。

3. 全量伪代码：
   ```
   定义函数 badSensor(sensor1, sensor2):
       初始化 i 为 0
       获取传感器数据长度 n
       当 i 小于 n-1 时，重复以下步骤:
           如果 sensor1[i] 不等于 sensor2[i]:
               如果 sensor1 从 i+1 到 n 的子数组等于 sensor2 从 i 到 n-1 的子数组 且 sensor1 从 i 到 n-1 的子数组等于 sensor2 从 i+1 到 n 的子数组:
                   返回 -1  // 无法判断哪个传感器有缺陷
               否则如果 sensor1 从 i+1 到 n 的子数组等于 sensor2 从 i 到 n-1 的子数组:
                   返回 2  // 第二个传感器有缺陷
               否则如果 sensor1 从 i 到 n-1 的子数组等于 sensor2 从 i+1 到 n 的子数组:
                   返回 1  // 第一个传感器有缺陷
           i 增加 1
       返回 -1  // 如果没有发现不一致，返回 -1 表示无法判断
   ```

4. 复杂度：
   - 时间复杂度：$O(n^2)$，因为在最坏情况下，比较偏移子数组的操作需要 $O(n)$ 的时间复杂度，并且可能在每个位置都进行比较。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外的变量。