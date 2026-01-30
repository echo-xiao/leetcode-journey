# 3704. 统计元素和差值为偶数的分区方案

**难度**: Easy | **标签**: `Array` `Math` `Prefix Sum`

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p><strong>分区</strong>&nbsp;是指将数组按照下标&nbsp;<code>i</code>&nbsp;（<code>0 &lt;= i &lt; n - 1</code>）划分成两个 <strong>非空</strong> 子数组，其中：</p>

<ul>
	<li>左子数组包含区间&nbsp;<code>[0, i]</code>&nbsp;内的所有下标。</li>
	<li>右子数组包含区间&nbsp;<code>[i + 1, n - 1]</code>&nbsp;内的所有下标。</li>
</ul>

<p>对左子数组和右子数组先求元素 <strong>和</strong> 再做 <strong>差</strong> ，统计并返回差值为 <strong>偶数</strong> 的 <strong>分区</strong> 方案数。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<div class="example-block">
<p><b>输入：</b><span class="example-io">nums = [10,10,3,7,6]</span></p>

<p><span class="example-io"><b>输出：</b>4</span></p>

<p><b>解释：</b></p>

<p>共有 4 个满足题意的分区方案：</p>

<ul>
	<li><code>[10]</code>、<code>[10, 3, 7, 6]</code>&nbsp;元素和的差值为&nbsp;<code>10 - 26 = -16</code>&nbsp;，是偶数。</li>
	<li><code>[10, 10]</code>、<code>[3, 7, 6]</code> 元素和的差值为&nbsp;<code>20 - 16 = 4</code>，是偶数。</li>
	<li><code>[10, 10, 3]</code>、<code>[7, 6]</code> 元素和的差值为&nbsp;<code>23 - 13 = 10</code>，是偶数。</li>
	<li><code>[10, 10, 3, 7]</code>、<code>[6]</code> 元素和的差值为&nbsp;<code>30 - 6 = 24</code>，是偶数。</li>
</ul>
</div>

<p><b>示例 2：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,2]</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><b>解释：</b></p>

<p>不存在元素和的差值为偶数的分区方案。</p>
</div>

<p><b>示例 3：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [2,4,6,8]</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><b>解释：</b></p>

<p>所有分区方案都满足元素和的差值为偶数。</p>
</div>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>2 &lt;= n == nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过前缀和计算每个可能的分区点的左右子数组和，判断其差值是否为偶数。

2. 综合思路：
   - 前缀和法：使用前缀和数组快速计算每个分区点的左右子数组和，然后判断差值是否为偶数。
   - 其他可能解法（未在提供的代码中出现）：可以使用动态规划或递归来探索所有可能的分区方案，判断每种方案的左右子数组和差值是否为偶数。

3. 全量伪代码：
   ```
   初始化前缀和数组 curr，长度为 n+1，初始值为 0
   对于每个元素 i 从 1 到 n：
       计算前缀和 curr[i] = curr[i-1] + nums[i-1]
   初始化计数器 cnt 为 0
   对于每个可能的分区点 i 从 1 到 n-1：
       计算左子数组和 left = curr[i]
       计算右子数组和 right = curr[-1] - curr[i]
       如果 (left - right) 是偶数：
           增加计数器 cnt
   返回计数器 cnt
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，因为需要遍历数组两次，一次计算前缀和，一次检查每个分区点。
   - 空间复杂度：$O(n)$，因为需要额外的前缀和数组来存储中间结果。