# 362. 敲击计数器 · 题目

**难度**: Medium | **标签**: `Array` `Binary Search` `Design` `Queue` `Data Stream`

## 题目描述

<p>设计一个点击计数器，统计过去 <code>5</code> 分钟内（即过去 <code>300</code> 秒）收到的点击次数。</p>

<p>您的系统应该接受一个 <code>timestamp</code> 参数（<strong>以秒为单位</strong>），您可以假设对系统的调用是按时间顺序进行的（即 <code>timestamp</code> 是单调递增的）。多个点击可能会在大致相同的时间到达。</p>

<p>实现 <code>HitCounter</code> 类：</p>

<ul>
	<li><code>HitCounter()</code> 初始化点击计数器系统的对象。</li>
	<li><code>void hit(int timestamp)</code> 记录在 <code>timestamp</code> 时发生的点击（<strong>以秒为单位</strong>）。多个点击可能会在同一 <code>timestamp</code> 时发生。</li>
	<li><code>int getHits(int timestamp)</code> 返回在 <code>timestamp</code> 过去 5 分钟内的点击次数（即过去 <code>300</code> 秒）。</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入</strong>
[&quot;HitCounter&quot;, &quot;hit&quot;, &quot;hit&quot;, &quot;hit&quot;, &quot;getHits&quot;, &quot;hit&quot;, &quot;getHits&quot;, &quot;getHits&quot;]
[[], [1], [2], [3], [4], [300], [300], [301]]
<strong>输出</strong>
[null, null, null, null, 3, null, 4, 3]

<strong>解释</strong>
HitCounter hitCounter = new HitCounter();
hitCounter.hit(1);       // 在时间戳 1 处点击。
hitCounter.hit(2);       // 在时间戳 2 处点击。
hitCounter.hit(3);       // 在时间戳 3 处点击。
hitCounter.getHits(4);   // 在时间戳 4 处获取点击，返回 3。
hitCounter.hit(300);     // 在时间戳 300 处点击。
hitCounter.getHits(300); // 在时间戳 300 处获取点击，返回 4。
hitCounter.getHits(301); // 在时间戳 301 处获取点击，返回 3。
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>1 &lt;= timestamp &lt;= 2 * 10<sup>9</sup></code></li>
	<li>所有调用都是按时间顺序进行的（即 <code>timestamp</code> 是单调递增的）。</li>
	<li>最多会对 <code>hit</code> 和 <code>getHits</code> 进行 <code>300</code> 次调用。</li>
</ul>

<p>&nbsp;</p>
<p><strong>后续问题:</strong> 如果每秒的点击次数可能非常大呢？您的设计能扩展吗？</p>
