# 561. 数组拆分

**难度**: Easy | **标签**: `Array` `Greedy` `Sorting` `Counting Sort`

## 题目描述

<p>给定长度为&nbsp;<code>2n</code><strong>&nbsp;</strong>的整数数组 <code>nums</code> ，你的任务是将这些数分成&nbsp;<code>n</code><strong> </strong>对, 例如 <code>(a<sub>1</sub>, b<sub>1</sub>), (a<sub>2</sub>, b<sub>2</sub>), ..., (a<sub>n</sub>, b<sub>n</sub>)</code> ，使得从 <code>1</code> 到&nbsp;<code>n</code> 的 <code>min(a<sub>i</sub>, b<sub>i</sub>)</code> 总和最大。</p>

<p>返回该 <strong>最大总和</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,4,3,2]
<strong>输出：</strong>4
<strong>解释：</strong>所有可能的分法（忽略元素顺序）为：
1. (1, 4), (2, 3) -&gt; min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -&gt; min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -&gt; min(1, 2) + min(3, 4) = 1 + 3 = 4
所以最大总和为 4</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [6,2,6,5,1,2]
<strong>输出：</strong>9
<strong>解释：</strong>最优的分法为 (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>nums.length == 2 * n</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


---
## 解题思路与复盘

### 一句话直击本质
通过对数组进行排序后，选择每对中的较小值求和，以最大化这些较小值的总和。

### 综合思路
1. **排序与迭代**：首先对数组进行排序，然后遍历排序后的数组，选择每对中的第一个元素（即较小值）进行累加。这种方法利用了排序后相邻元素的特性，确保每对中的较小值被选中。

### 全量伪代码
```plaintext
函数 arrayPairSum(输入数组 nums):
    对 nums 进行排序
    初始化结果 res 为 0
    对于 i 从 0 到 nums 的长度，步长为 2:
        将 nums[i] 加到 res 上
    返回 res
```

### 复杂度
- 时间复杂度：排序操作的时间复杂度为 $O(n \log n)$，其中 $n$ 是数组的长度。
- 空间复杂度：排序操作通常需要 $O(1)$ 的额外空间（假设使用原地排序），因此空间复杂度为 $O(1)$。