# 1280. 健身计划评估

**难度**: Easy | **标签**: `Array` `Sliding Window`

## 题目描述

<p>一个节食者在第 <code>i</code> 天消耗了 <code>calories[i]</code> 卡路里。</p>

<p>给定一个整数 <code>k</code>，对于<strong>每个</strong>连续的 <code>k</code> 天的序列（<code>calories[i], calories[i+1], ..., calories[i+k-1]</code>，对于所有 <code>0 &lt;= i &lt;= n-k</code>），他们关注 <em>T</em>，即在这 <code>k</code> 天的序列中消耗的总卡路里（<code>calories[i] + calories[i+1] + ... + calories[i+k-1]</code>）：</p>

<ul>
	<li>如果 <code>T &lt; lower</code>，他们在饮食上表现不佳，失去 1 分；</li>
	<li>如果 <code>T &gt; upper</code>，他们在饮食上表现良好，获得 1 分；</li>
	<li>否则，他们表现正常，积分没有变化。</li>
</ul>

<p>最初，节食者的积分为零。返回节食者在饮食 <code>calories.length</code> 天后的总积分。</p>

<p>请注意，总积分可能为负数。</p>

<p>&nbsp;</p>
<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3
<strong>输出:</strong> 0
<strong>解释</strong>: 由于 k = 1，我们分别考虑数组的每个元素，并将其与 lower 和 upper 进行比较。
calories[0] 和 calories[1] 小于 lower，因此失去 2 分。
calories[3] 和 calories[4] 大于 upper，因此获得 2 分。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> calories = [3,2], k = 2, lower = 0, upper = 1
<strong>输出:</strong> 1
<strong>解释</strong>: 由于 k = 2，我们考虑长度为 2 的子数组。
calories[0] + calories[1] &gt; upper，因此获得 1 分。
</pre>

<p><strong class="example">示例 3:</strong></p>

<pre>
<strong>输入:</strong> calories = [6,5,0,0], k = 2, lower = 1, upper = 5
<strong>输出:</strong> 0
<strong>解释</strong>:
calories[0] + calories[1] &gt; upper，因此获得 1 分。
lower &lt;= calories[1] + calories[2] &lt;= upper，因此积分没有变化。
calories[2] + calories[3] &lt; lower，因此失去 1 分。
</pre>

<p>&nbsp;</p>
<p><strong>约束条件:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= calories.length &lt;= 10^5</code></li>
	<li><code>0 &lt;= calories[i] &lt;= 20000</code></li>
	<li><code>0 &lt;= lower &lt;= upper</code></li>
</ul>

---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是使用滑动窗口技术计算每个长度为 k 的子数组的卡路里总和，并根据总和与上下限的比较调整计数器。

2. 综合思路：
   - 滑动窗口：通过维护一个长度为 k 的窗口，计算窗口内元素的总和，并在窗口移动时更新总和，判断是否需要调整计数器。
   - 这两种实现的区别在于更新计数器和移动窗口的顺序，但本质上都是滑动窗口的应用。

3. 全量伪代码：
   ```
   初始化 T 为前 k 个元素的和
   初始化计数器 cnt 为 0
   初始化左指针 left 为 0

   如果 T 小于 lower，计数器减 1
   否则如果 T 大于 upper，计数器加 1

   对于右指针从 k 到数组长度 - 1：
       更新 T 为 T 加上 calories[right] 减去 calories[left]
       如果 T 小于 lower，计数器减 1
       否则如果 T 大于 upper，计数器加 1
       左指针加 1

   返回计数器 cnt
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，因为每个元素最多被访问两次（一次加入窗口，一次移出窗口）。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外变量。