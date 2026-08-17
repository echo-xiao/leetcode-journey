# 1980. 有缺陷的传感器 · 题目

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
