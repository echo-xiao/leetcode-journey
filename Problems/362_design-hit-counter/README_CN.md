# 362. 敲击计数器

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

---
## 解题思路与复盘

1. 一句话直击本质：使用队列记录每次敲击的时间戳，并在获取敲击次数时移除超过300秒的旧记录。

2. 综合思路：
   - 队列实现：使用队列（如 `deque`）来存储每次敲击的时间戳，确保队列中只保留最近300秒内的敲击记录。
   - 滑动窗口：通过不断移除队列中超过300秒的旧时间戳，动态维护一个滑动窗口，窗口内的元素数量即为有效的敲击次数。

3. 全量伪代码：
   ```plaintext
   类 HitCounter:
       初始化方法:
           创建一个空的队列

       方法 hit(时间戳):
           将时间戳添加到队列尾部

       方法 getHits(时间戳):
           当队列不为空且队列头部的时间戳与当前时间戳的差值大于等于300:
               从队列头部移除时间戳
           返回队列的长度
   ```

4. 复杂度：
   - 时间复杂度：对于 `hit` 操作是 $O(1)$，对于 `getHits` 操作是 $O(n)$，其中 $n$ 是队列中元素的数量。
   - 空间复杂度：$O(n)$，其中 $n$ 是在300秒内的敲击次数。