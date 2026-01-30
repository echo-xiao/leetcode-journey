# 1833. 找到最高海拔

**难度**: Easy | **标签**: `Array` `Prefix Sum`

## 题目描述

<p>有一个自行车手打算进行一场公路骑行，这条路线总共由 <code>n + 1</code> 个不同海拔的点组成。自行车手从海拔为 <code>0</code> 的点 <code>0</code> 开始骑行。</p>

<p>给你一个长度为 <code>n</code> 的整数数组 <code>gain</code> ，其中 <code>gain[i]</code> 是点 <code>i</code> 和点 <code>i + 1</code> 的 <strong>净海拔高度差</strong>（<code>0 <= i < n</code>）。请你返回 <strong>最高点的海拔</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>gain = [-5,1,5,0,-7]
<b>输出：</b>1
<b>解释：</b>海拔高度依次为 [0,-5,-4,1,1,-6] 。最高海拔为 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>gain = [-4,-3,-2,-1,4,3,2]
<b>输出：</b>0
<b>解释：</b>海拔高度依次为 [0,-4,-7,-9,-10,-6,-3,-1] 。最高海拔为 0 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == gain.length</code></li>
	<li><code>1 <= n <= 100</code></li>
	<li><code>-100 <= gain[i] <= 100</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过累加海拔增量数组来计算每个点的海拔高度，并找出其中的最大值。

2. 综合思路：
   - 迭代法：遍历增量数组，逐步累加计算每个位置的海拔高度，并在过程中记录最大海拔。
   - 直接计算法：在遍历增量数组时，直接更新当前海拔高度，并同时更新最大海拔值。

3. 全量伪代码：
   ```plaintext
   方法1：迭代法
   输入：增量数组 gain
   初始化：当前海拔 curr_altitude = 0，最大海拔 max_altitude = 0
   对于每个增量值 g 在增量数组 gain 中：
       更新当前海拔 curr_altitude = curr_altitude + g
       如果 curr_altitude > max_altitude，则更新 max_altitude = curr_altitude
   返回 max_altitude

   方法2：直接计算法
   输入：增量数组 gain
   初始化：当前海拔 curr_altitude = 0，最大海拔 max_altitude = 0
   对于每个增量值 g 在增量数组 gain 中：
       更新当前海拔 curr_altitude = curr_altitude + g
       更新最大海拔 max_altitude = max(max_altitude, curr_altitude)
   返回 max_altitude
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是增量数组的长度，因为需要遍历整个数组一次。
   - 空间复杂度：$O(1)$，如果不存储每个位置的海拔高度，仅使用常数额外空间来存储当前和最大海拔。