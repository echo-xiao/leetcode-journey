# 2005. 检查是否区域内所有整数都被覆盖

**难度**: Easy | **标签**: `Array` `Hash Table` `Prefix Sum`

## 题目描述

<p>给你一个二维整数数组 <code>ranges</code> 和两个整数 <code>left</code> 和 <code>right</code> 。每个 <code>ranges[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> 表示一个从 <code>start<sub>i</sub></code> 到 <code>end<sub>i</sub></code> 的 <strong>闭区间</strong> 。</p>

<p>如果闭区间 <code>[left, right]</code> 内每个整数都被 <code>ranges</code> 中 <strong>至少一个</strong> 区间覆盖，那么请你返回 <code>true</code> ，否则返回 <code>false</code> 。</p>

<p>已知区间 <code>ranges[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> ，如果整数 <code>x</code> 满足 <code>start<sub>i</sub> <= x <= end<sub>i</sub></code> ，那么我们称整数<code>x</code> 被覆盖了。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
<b>输出：</b>true
<b>解释：</b>2 到 5 的每个整数都被覆盖了：
- 2 被第一个区间覆盖。
- 3 和 4 被第二个区间覆盖。
- 5 被第三个区间覆盖。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>ranges = [[1,10],[10,20]], left = 21, right = 21
<b>输出：</b>false
<b>解释：</b>21 没有被任何一个区间覆盖。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= ranges.length <= 50</code></li>
	<li><code>1 <= start<sub>i</sub> <= end<sub>i</sub> <= 50</code></li>
	<li><code>1 <= left <= right <= 50</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：
   - 版本 1 使用差分数组记录区间覆盖变化，版本 2 直接检查每个整数是否被至少一个区间覆盖。

2. 综合思路：
   - 版本 1（差分数组法）：利用差分数组记录区间的开始和结束，通过累加差分数组来判断每个整数是否被覆盖。
   - 版本 2（直接检查法）：遍历目标区间内的每个整数，检查其是否被任何一个给定区间覆盖。

3. 全量伪代码：
   - 差分数组法：
     ```
     初始化一个长度为100的差分数组 diff，所有元素初始化为0
     对于每个区间 [start, end]：
         将 diff[start] 增加1
         将 diff[end+1] 减少1
     初始化计数器 cnt 为0
     从1遍历到 right：
         累加 cnt 和 diff[i]
         如果 i 在 [left, right] 范围内且 cnt 为0：
             返回 False
     返回 True
     ```
   - 直接检查法：
     ```
     对于从 left 到 right 的每个整数 i：
         初始化标志 is_covered 为 False
         对于每个区间 [start, end]：
             如果 start <= i <= end：
                 将 is_covered 设为 True
                 跳出内层循环
         如果 is_covered 为 False：
             返回 False
     返回 True
     ```

4. 复杂度：
   - 版本 1（差分数组法）：
     - 时间复杂度：$O(n + m)$，其中 $n$ 是 ranges 的长度，$m$ 是 right 的值。
     - 空间复杂度：$O(1)$，因为差分数组的大小是固定的常数。
   - 版本 2（直接检查法）：
     - 时间复杂度：$O(n \cdot m)$，其中 $n$ 是 ranges 的长度，$m$ 是目标区间的长度 (right - left + 1)。
     - 空间复杂度：$O(1)$，因为只使用了常数空间。