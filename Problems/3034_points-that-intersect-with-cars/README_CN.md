# 3034. 与车相交的点

**难度**: Easy | **标签**: `Array` `Hash Table` `Prefix Sum`

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的二维整数数组 <code>nums</code> 表示汽车停放在数轴上的坐标。对于任意下标 <code>i</code>，<code>nums[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> ，其中 <code>start<sub>i</sub></code> 是第 <code>i</code> 辆车的起点，<code>end<sub>i</sub></code> 是第 <code>i</code> 辆车的终点。</p>

<p>返回数轴上被车 <strong>任意部分</strong> 覆盖的整数点的数目。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [[3,6],[1,5],[4,7]]
<strong>输出：</strong>7
<strong>解释：</strong>从 1 到 7 的所有点都至少与一辆车相交，因此答案为 7 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [[1,3],[5,8]]
<strong>输出：</strong>7
<strong>解释：</strong>1、2、3、5、6、7、8 共计 7 个点满足至少与一辆车相交，因此答案为 7 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>nums[i].length == 2</code></li>
	<li><code><font face="monospace">1 &lt;= start<sub>i</sub>&nbsp;&lt;= end<sub>i</sub>&nbsp;&lt;= 100</font></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是使用差分数组技术来计算所有被车覆盖的点的数量。

2. 综合思路：
   - 差分数组方法：所有版本都采用了差分数组的方法，通过在起始点增加1，在结束点的下一个位置减少1，最后通过前缀和计算出被覆盖的点的数量。

3. 全量伪代码：
   ```plaintext
   初始化一个长度为最大可能点数的数组 curr，所有元素初始化为 0
   对于每个区间 [start, end]：
       在 curr[start] 位置增加 1
       如果 end + 1 小于 curr 的长度：
           在 curr[end + 1] 位置减少 1
   初始化 res 和 cnt 为 0
   对于 curr 中的每个元素：
       将当前元素累加到 res
       如果 res 大于 0：
           增加 cnt
   返回 cnt
   ```

4. 复杂度：
   - 时间复杂度：$O(n + m)$，其中 $n$ 是输入区间的数量，$m$ 是数组 curr 的长度。
   - 空间复杂度：$O(m)$，其中 $m$ 是数组 curr 的长度。