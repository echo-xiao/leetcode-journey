# 436. 寻找右区间

**难度**: Medium | **标签**: `Array` `Binary Search` `Sorting`

## 题目描述

<p>给你一个区间数组 <code>intervals</code> ，其中&nbsp;<code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> ，且每个&nbsp;<code>start<sub>i</sub></code> 都 <strong>不同</strong> 。</p>

<p>区间 <code>i</code> 的 <strong>右侧区间</strong>&nbsp;是满足 <code>start<sub>j</sub>&nbsp;&gt;= end<sub>i</sub></code>，且 <code>start<sub>j</sub></code> <strong>最小&nbsp;</strong>的区间 <code>j</code>。注意 <code>i</code> 可能等于 <code>j</code> 。</p>

<p>返回一个由每个区间 <code>i</code>&nbsp;对应的 <strong>右侧区间</strong> 下标组成的数组。如果某个区间 <code>i</code> 不存在对应的 <strong>右侧区间</strong> ，则下标 <code>i</code> 处的值设为 <code>-1</code> 。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,2]]
<strong>输出：</strong>[-1]
<strong>解释：</strong>集合中只有一个区间，所以输出-1。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[3,4],[2,3],[1,2]]
<strong>输出：</strong>[-1,0,1]
<strong>解释：</strong>对于 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间[3,4]具有最小的“右”起点;
对于 [1,2] ，区间[2,3]具有最小的“右”起点。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,4],[2,3],[3,4]]
<strong>输出：</strong>[-1,2,-1]
<strong>解释：</strong>对于区间 [1,4] 和 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间 [3,4] 有最小的“右”起点。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;intervals.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>-10<sup>6</sup> &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
	<li>每个间隔的起点都 <strong>不相同</strong></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过对起始点进行排序并使用二分查找来快速找到每个区间的右区间。

2. 综合思路：
   - 排序与二分查找：所有版本都采用了先对区间的起始点进行排序，然后使用二分查找来寻找每个区间的右区间。
   - 二分查找的变体：不同版本在二分查找的实现上略有不同，但核心思想是相同的，即在排序后的数组中寻找第一个大于或等于目标值的起始点。

3. 全量伪代码：
   ```
   函数 findRightInterval(intervals):
       创建空数组 arr
       对于每个区间 i 从 0 到 intervals 的长度:
           将 (intervals[i][0], i) 添加到 arr
       按照第一个元素对 arr 进行排序
       创建结果数组 res
       对于每个区间 i 从 0 到 intervals 的长度:
           设 target 为 intervals[i][1]
           调用 binarySearch(arr, target) 并将结果添加到 res
       返回 res

   函数 binarySearch(arr, target):
       初始化 left 为 0, right 为 arr 的长度减 1
       初始化 ans 为 -1
       当 left 小于等于 right 时:
           计算 mid 为 left 和 right 的中间值
           设 start 为 arr[mid][0], idx 为 arr[mid][1]
           如果 start 大于等于 target:
               更新 ans 为 idx
               将 right 更新为 mid - 1
           否则:
               将 left 更新为 mid + 1
       返回 ans
   ```

4. 复杂度：
   - 时间复杂度：$O(n \log n)$，其中 $n$ 是区间的数量。排序的时间复杂度为 $O(n \log n)$，每次二分查找的时间复杂度为 $O(\log n)$，总共进行 $n$ 次二分查找。
   - 空间复杂度：$O(n)$，用于存储排序后的起始点和索引的数组。