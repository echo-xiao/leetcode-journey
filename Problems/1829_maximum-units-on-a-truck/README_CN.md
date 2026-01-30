# 1829. 卡车上的最大单元数

**难度**: Easy | **标签**: `Array` `Greedy` `Sorting`

## 题目描述

<p>请你将一些箱子装在 <strong>一辆卡车</strong> 上。给你一个二维数组 <code>boxTypes</code> ，其中 <code>boxTypes[i] = [numberOfBoxes<sub>i</sub>, numberOfUnitsPerBox<sub>i</sub>]</code> ：</p>

<ul>
	<li><code>numberOfBoxes<sub>i</sub></code> 是类型 <code>i</code> 的箱子的数量。</li>
	<li><code>numberOfUnitsPerBox<sub>i</sub></code><sub> </sub>是类型 <code>i</code> 每个箱子可以装载的单元数量。</li>
</ul>

<p>整数 <code>truckSize</code> 表示卡车上可以装载 <strong>箱子</strong> 的 <strong>最大数量</strong> 。只要箱子数量不超过 <code>truckSize</code> ，你就可以选择任意箱子装到卡车上。</p>

<p>返回卡车可以装载 <strong>单元</strong> 的 <strong>最大</strong> 总数<em>。</em></p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
<strong>输出：</strong>8
<strong>解释：</strong>箱子的情况如下：
- 1 个第一类的箱子，里面含 3 个单元。
- 2 个第二类的箱子，每个里面含 2 个单元。
- 3 个第三类的箱子，每个里面含 1 个单元。
可以选择第一类和第二类的所有箱子，以及第三类的一个箱子。
单元总数 = (1 * 3) + (2 * 2) + (1 * 1) = 8</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
<strong>输出：</strong>91
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= boxTypes.length <= 1000</code></li>
	<li><code>1 <= numberOfBoxes<sub>i</sub>, numberOfUnitsPerBox<sub>i</sub> <= 1000</code></li>
	<li><code>1 <= truckSize <= 10<sup>6</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过贪心算法，优先选择单位数最多的箱子类型以最大化卡车上的单元数。

2. 综合思路：
   - 贪心算法：对箱子类型按单位数降序排序，然后依次选择箱子，直到卡车装满或没有更多的箱子可选。

3. 全量伪代码：
   ```
   箱子类型按单位数降序排序
   初始化已装载箱子数为0
   初始化总单元数为0
   对于每种箱子类型：
       如果当前箱子数加上已装载箱子数超过卡车容量：
           计算剩余可装载箱子数
           增加相应的单元数
           结束循环
       否则：
           增加该类型箱子的所有单元数
           更新已装载箱子数
   返回总单元数
   ```

4. 复杂度：
   - 时间复杂度：$O(n \log n)$，其中 $n$ 是箱子类型的数量，因为需要对箱子类型进行排序。
   - 空间复杂度：$O(1)$，因为除了输入数据外，只使用了常数个额外变量。