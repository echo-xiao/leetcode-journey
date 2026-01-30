# 2345. 转化时间需要的最少操作数

**难度**: Easy | **标签**: `String` `Greedy`

## 题目描述

<p>给你两个字符串 <code>current</code> 和 <code>correct</code> ，表示两个 <strong>24 小时制时间</strong> 。</p>

<p><strong>24 小时制时间</strong> 按 <code>"HH:MM"</code> 进行格式化，其中 <code>HH</code> 在 <code>00</code> 和 <code>23</code> 之间，而 <code>MM</code> 在 <code>00</code> 和 <code>59</code> 之间。最早的 24 小时制时间为 <code>00:00</code> ，最晚的是 <code>23:59</code> 。</p>

<p>在一步操作中，你可以将 <code>current</code> 这个时间增加 <code>1</code>、<code>5</code>、<code>15</code> 或 <code>60</code> 分钟。你可以执行这一操作 <strong>任意</strong> 次数。</p>

<p>返回将&nbsp;<code>current</code><em> </em>转化为<em> </em><code>correct</code> 需要的 <strong>最少操作数</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>current = "02:30", correct = "04:35"
<strong>输出：</strong>3
<strong>解释：
</strong>可以按下述 3 步操作将 current 转换为 correct ：
- 为 current 加 60 分钟，current 变为 "03:30" 。
- 为 current 加 60 分钟，current 变为 "04:30" 。 
- 为 current 加 5 分钟，current 变为 "04:35" 。
可以证明，无法用少于 3 步操作将 current 转化为 correct 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>current = "11:00", correct = "11:01"
<strong>输出：</strong>1
<strong>解释：</strong>只需要为 current 加一分钟，所以最小操作数是 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>current</code> 和 <code>correct</code> 都符合 <code>"HH:MM"</code> 格式</li>
	<li><code>current &lt;= correct</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法通过逐步使用最大单位的时间操作（小时、15分钟、5分钟、1分钟）来减少时间差，从而计算出转化时间所需的最少操作数。

2. 综合思路：
   - 迭代法：通过将时间转换为分钟数，计算出当前时间与目标时间的差值，然后依次使用最大单位的时间操作来减少差值，直到差值为零。

3. 全量伪代码：
   ```
   定义函数 convertTime(当前时间, 目标时间):
       将当前时间转换为分钟数 curr
       将目标时间转换为分钟数 corr
       计算时间差 diff1 = corr - curr

       计算需要的小时数 h = diff1 整除 60
       更新剩余差值 diff2 = diff1 减去 h 乘以 60

       计算需要的15分钟数 k = diff2 整除 15
       更新剩余差值 diff3 = diff2 减去 k 乘以 15

       计算需要的5分钟数 m = diff3 整除 5
       更新剩余差值 diff4 = diff3 减去 m 乘以 5

       计算需要的1分钟数 t = diff4 整除 1

       返回总操作数 h + k + m + t
   ```

4. 复杂度：
   - 时间复杂度：$O(1)$，因为算法只涉及固定次数的算术运算。
   - 空间复杂度：$O(1)$，因为只使用了常量个数的额外变量。