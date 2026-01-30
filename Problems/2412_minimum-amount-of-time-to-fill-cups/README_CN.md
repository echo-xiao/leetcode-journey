# 2412. 装满杯子需要的最短总时长

**难度**: Easy | **标签**: `Array` `Greedy` `Sorting` `Heap (Priority Queue)`

## 题目描述

<p>现有一台饮水机，可以制备冷水、温水和热水。每秒钟，可以装满 <code>2</code> 杯 <strong>不同</strong> 类型的水或者 <code>1</code> 杯任意类型的水。</p>

<p>给你一个下标从 <strong>0</strong> 开始、长度为 <code>3</code> 的整数数组 <code>amount</code> ，其中 <code>amount[0]</code>、<code>amount[1]</code> 和 <code>amount[2]</code> 分别表示需要装满冷水、温水和热水的杯子数量。返回装满所有杯子所需的 <strong>最少</strong> 秒数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>amount = [1,4,2]
<strong>输出：</strong>4
<strong>解释：</strong>下面给出一种方案：
第 1 秒：装满一杯冷水和一杯温水。
第 2 秒：装满一杯温水和一杯热水。
第 3 秒：装满一杯温水和一杯热水。
第 4 秒：装满一杯温水。
可以证明最少需要 4 秒才能装满所有杯子。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>amount = [5,4,4]
<strong>输出：</strong>7
<strong>解释：</strong>下面给出一种方案：
第 1 秒：装满一杯冷水和一杯热水。
第 2 秒：装满一杯冷水和一杯温水。
第 3 秒：装满一杯冷水和一杯温水。
第 4 秒：装满一杯温水和一杯热水。
第 5 秒：装满一杯冷水和一杯热水。
第 6 秒：装满一杯冷水和一杯温水。
第 7 秒：装满一杯热水。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>amount = [5,0,0]
<strong>输出：</strong>5
<strong>解释：</strong>每秒装满一杯冷水。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>amount.length == 3</code></li>
	<li><code>0 &lt;= amount[i] &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法的核心逻辑是通过最大堆优先处理数量最多的两种杯子，每次减少其数量，直至所有杯子都被装满。

2. 综合思路：
   - 最大堆方法：使用最大堆（优先队列）来存储杯子数量，每次从中取出数量最多的两个杯子进行处理，减少其数量，直到所有杯子都被装满。

3. 全量伪代码：
   ```plaintext
   定义函数 fillCups，输入为一个列表 amount，表示三种杯子的数量
   初始化一个空的最大堆 maxHeap
   对于 amount 中的每个数量 i：
       如果 i 大于 0，将 -i 压入 maxHeap（因为 Python 的 heapq 是最小堆）
   
   初始化计数器 cnt 为 0
   当 maxHeap 不为空时：
       如果 maxHeap 的长度大于等于 2：
           从 maxHeap 中弹出两个最大值 num1 和 num2（注意是负数，表示最大值）
           将 num1 和 num2 各加 1（表示减少其绝对值）
           如果 num1 小于 0，将 num1 压回 maxHeap
           如果 num2 小于 0，将 num2 压回 maxHeap
           计数器 cnt 增加 1
       否则：
           从 maxHeap 中弹出一个最大值 num
           将 num 加 1
           如果 num 小于 0，将 num 压回 maxHeap
           计数器 cnt 增加 1
   
   返回计数器 cnt 作为结果
   ```

4. 复杂度：
   - 时间复杂度：$O(n \log n)$，其中 $n$ 是初始非零杯子的数量，因为每次操作涉及堆的插入和删除。
   - 空间复杂度：$O(n)$，用于存储最大堆。