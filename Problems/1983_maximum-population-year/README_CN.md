# 1983. 人口最多的年份

**难度**: Easy | **标签**: `Array` `Counting` `Prefix Sum`

## 题目描述

<p>给你一个二维整数数组 <code>logs</code> ，其中每个 <code>logs[i] = [birth<sub>i</sub>, death<sub>i</sub>]</code> 表示第 <code>i</code> 个人的出生和死亡年份。</p>

<p>年份 <code>x</code> 的 <strong>人口</strong> 定义为这一年期间活着的人的数目。第 <code>i</code> 个人被计入年份 <code>x</code> 的人口需要满足：<code>x</code> 在闭区间 <code>[birth<sub>i</sub>, death<sub>i</sub> - 1]</code> 内。注意，人不应当计入他们死亡当年的人口中。</p>

<p>返回 <strong>人口最多</strong> 且 <strong>最早</strong> 的年份。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>logs = [[1993,1999],[2000,2010]]
<strong>输出：</strong>1993
<strong>解释：</strong>人口最多为 1 ，而 1993 是人口为 1 的最早年份。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>logs = [[1950,1961],[1960,1971],[1970,1981]]
<strong>输出：</strong>1960
<strong>解释：</strong> 
人口最多为 2 ，分别出现在 1960 和 1970 。
其中最早年份是 1960 。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= logs.length &lt;= 100</code></li>
	<li><code>1950 &lt;= birth<sub>i</sub> &lt; death<sub>i</sub> &lt;= 2050</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过差分数组记录每年人口变化，累加求出最大人口年份。

2. 综合思路：
   - 差分数组法：使用一个差分数组记录每年的人口变化，遍历该数组累加得到每年的实际人口数，找出人口最多的年份。
   - 该题目主要采用差分数组法实现，没有其他显著不同的数据结构或算法变体。

3. 全量伪代码：
   - 初始化一个长度为151（1950到2100年）的差分数组`delta`，初始值为0。
   - 遍历每个出生和死亡年份对：
     - 在出生年份对应的索引位置增加1。
     - 在死亡年份对应的索引位置减少1。
   - 初始化变量`curr`为0，用于记录当前年份的人口数。
   - 初始化变量`res`为0，用于记录人口最多的年份。
   - 初始化变量`max_res`为0，用于记录最大人口数。
   - 遍历差分数组`delta`：
     - 累加当前索引位置的值到`curr`。
     - 如果`curr`大于`max_res`，更新`max_res`为`curr`，并更新`res`为当前年份。
   - 返回`res`作为人口最多的年份。

4. 复杂度：
   - 时间复杂度：$O(n + m)$，其中$n$是日志条目的数量，$m$是年份范围（151年）。
   - 空间复杂度：$O(m)$，用于存储差分数组。