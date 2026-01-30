# 2463. 得到 K 个黑块的最少涂色次数

**难度**: Easy | **标签**: `String` `Sliding Window`

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;下标从 <strong>0</strong>&nbsp;开始的字符串&nbsp;<code>blocks</code>&nbsp;，<code>blocks[i]</code>&nbsp;要么是&nbsp;<code>'W'</code>&nbsp;要么是&nbsp;<code>'B'</code>&nbsp;，表示第&nbsp;<code>i</code>&nbsp;块的颜色。字符&nbsp;<code>'W'</code> 和&nbsp;<code>'B'</code>&nbsp;分别表示白色和黑色。</p>

<p>给你一个整数&nbsp;<code>k</code>&nbsp;，表示想要&nbsp;<strong>连续</strong>&nbsp;黑色块的数目。</p>

<p>每一次操作中，你可以选择一个白色块将它 <strong>涂成</strong>&nbsp;黑色块。</p>

<p>请你返回至少出现 <strong>一次</strong>&nbsp;连续 <code>k</code>&nbsp;个黑色块的 <strong>最少</strong>&nbsp;操作次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>blocks = "WBBWWBBWBW", k = 7
<b>输出：</b>3
<strong>解释：</strong>
一种得到 7 个连续黑色块的方法是把第 0 ，3 和 4 个块涂成黑色。
得到 blocks = "BBBBBBBWBW" 。
可以证明无法用少于 3 次操作得到 7 个连续的黑块。
所以我们返回 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>blocks = "WBWBBBW", k = 2
<b>输出：</b>0
<strong>解释：</strong>
不需要任何操作，因为已经有 2 个连续的黑块。
所以我们返回 0 。
</pre>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>n == blocks.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>blocks[i]</code>&nbsp;要么是&nbsp;<code>'W'</code>&nbsp;，要么是&nbsp;<code>'B'</code> 。</li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：使用滑动窗口技术计算每个长度为 K 的子串中白块的最小数量。

2. 综合思路：
   - 滑动窗口：通过维护一个长度为 K 的滑动窗口，计算窗口内白块的数量，并在窗口滑动时更新计数，寻找最小值。

3. 全量伪代码：
   ```plaintext
   定义函数 minimumRecolors(blocks, k):
       初始化 n 为 blocks 的长度
       初始化 i 为 0
       初始化 cnt 为 0
       初始化 min_cnt 为一个很大的数
       初始化 win 为 blocks 的前 k 个字符
       
       对于 win 中的每个字符 e:
           如果 e 是 'W':
               cnt 增加 1
       将 min_cnt 更新为 cnt 和 min_cnt 的较小值

       对于 j 从 k 到 n-1:
           将 win 更新为 blocks 从 i+1 到 i+k+1 的子串
           如果 blocks[j] 是 'W':
               cnt 增加 1
           如果 blocks[i] 是 'W':
               cnt 减少 1
           将 min_cnt 更新为 cnt 和 min_cnt 的较小值
           i 增加 1
       
       返回 min_cnt
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，因为每个字符最多被访问两次。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外变量。