# 924. 公平的糖果交换

**难度**: Easy | **标签**: `Array` `Hash Table` `Binary Search` `Sorting`

## 题目描述

<p>爱丽丝和鲍勃拥有不同总数量的糖果。给你两个数组 <code>aliceSizes</code> 和 <code>bobSizes</code> ，<code>aliceSizes[i]</code> 是爱丽丝拥有的第 <code>i</code> 盒糖果中的糖果数量，<code>bobSizes[j]</code> 是鲍勃拥有的第 <code>j</code> 盒糖果中的糖果数量。</p>

<p>两人想要互相交换一盒糖果，这样在交换之后，他们就可以拥有相同总数量的糖果。一个人拥有的糖果总数量是他们每盒糖果数量的总和。</p>

<p>返回一个整数数组 <code>answer</code>，其中 <code>answer[0]</code> 是爱丽丝必须交换的糖果盒中的糖果的数目，<code>answer[1]</code> 是鲍勃必须交换的糖果盒中的糖果的数目。如果存在多个答案，你可以返回其中 <strong>任何一个</strong> 。题目测试用例保证存在与输入对应的答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>aliceSizes = [1,1], bobSizes = [2,2]
<strong>输出：</strong>[1,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>aliceSizes = [1,2], bobSizes = [2,3]
<strong>输出：</strong>[1,2]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>aliceSizes = [2], bobSizes = [1,3]
<strong>输出：</strong>[2,3]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>aliceSizes = [1,2,5], bobSizes = [2,4]
<strong>输出：</strong>[5,4]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= aliceSizes.length, bobSizes.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= aliceSizes[i], bobSizes[j] &lt;= 10<sup>5</sup></code></li>
	<li>爱丽丝和鲍勃的糖果总数量不同。</li>
	<li>题目数据保证对于给定的输入至少存在一个有效答案。</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过计算两个数组的和的差值，找到一对元素交换使得两者的和相等。

2. 综合思路：
   - 哈希表法：通过计算两者和的差值，利用哈希表快速查找满足条件的元素对。
   - 数学推导法：通过数学公式推导出需要交换的元素对。

3. 全量伪代码：
   - 哈希表法：
     ```
     定义函数 fairCandySwap(aliceSizes, bobSizes):
         计算 suma 为 aliceSizes 的总和
         计算 sumb 为 bobSizes 的总和
         计算 sumt 为 (suma + sumb) / 2
         创建一个集合 seen 包含 bobSizes 的所有元素
         
         对于 aliceSizes 中的每个元素 i:
             计算 res 为 sumt - suma + i
             如果 res 在 seen 中:
                 返回 [i, res]
         返回 -1
     ```

4. 复杂度：
   - 时间复杂度：$O(n + m)$，其中 $n$ 是 `aliceSizes` 的长度，$m$ 是 `bobSizes` 的长度。
   - 空间复杂度：$O(m)$，用于存储 `bobSizes` 中的元素到集合 `seen`。