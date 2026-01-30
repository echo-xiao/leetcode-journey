# 167. 两数之和 II - 输入有序数组

**难度**: Medium | **标签**: `Array` `Two Pointers` `Binary Search`

## 题目描述

<p>给你一个下标从 <strong>1</strong> 开始的整数数组&nbsp;<code>numbers</code> ，该数组已按<strong><em> </em>非递减顺序排列&nbsp; </strong>，请你从数组中找出满足相加之和等于目标数&nbsp;<code>target</code> 的两个数。如果设这两个数分别是 <code>numbers[index<sub>1</sub>]</code> 和 <code>numbers[index<sub>2</sub>]</code> ，则 <code>1 &lt;= index<sub>1</sub> &lt; index<sub>2</sub> &lt;= numbers.length</code> 。</p>

<p>以长度为 2 的整数数组 <code>[index<sub>1</sub>, index<sub>2</sub>]</code> 的形式返回这两个整数的下标 <code>index<sub>1</sub></code><em> </em>和<em> </em><code>index<sub>2</sub></code>。</p>

<p>你可以假设每个输入 <strong>只对应唯一的答案</strong> ，而且你 <strong>不可以</strong> 重复使用相同的元素。</p>

<p>你所设计的解决方案必须只使用常量级的额外空间。</p>
&nbsp;

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>numbers = [<strong><em>2</em></strong>,<strong><em>7</em></strong>,11,15], target = 9
<strong>输出：</strong>[1,2]
<strong>解释：</strong>2 与 7 之和等于目标数 9 。因此 index<sub>1</sub> = 1, index<sub>2</sub> = 2 。返回 [1, 2] 。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>numbers = [<strong><em>2</em></strong>,3,<strong><em>4</em></strong>], target = 6
<strong>输出：</strong>[1,3]
<strong>解释：</strong>2 与 4 之和等于目标数 6 。因此 index<sub>1</sub> = 1, index<sub>2</sub> = 3 。返回 [1, 3] 。</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>numbers = [<strong><em>-1</em></strong>,<strong><em>0</em></strong>], target = -1
<strong>输出：</strong>[1,2]
<strong>解释：</strong>-1 与 0 之和等于目标数 -1 。因此 index<sub>1</sub> = 1, index<sub>2</sub> = 2 。返回 [1, 2] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= numbers.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= numbers[i] &lt;= 1000</code></li>
	<li><code>numbers</code> 按 <strong>非递减顺序</strong> 排列</li>
	<li><code>-1000 &lt;= target &lt;= 1000</code></li>
	<li><strong>仅存在一个有效答案</strong></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：利用双指针从数组两端向中间移动，寻找两个数之和等于目标值。

2. 综合思路：
   - 双指针法：通过两个指针分别指向数组的起始和末尾，根据当前和与目标值的比较，调整指针位置以找到满足条件的两个数。
   - 二分查找法（未在提供的代码中实现，但作为一种可能的思路）：对于每个元素，使用二分查找寻找另一个满足条件的数。

3. 全量伪代码：
   - 双指针法：
     ```
     初始化左指针为0，右指针为数组长度减1
     当左指针小于等于右指针时：
         计算当前左指针和右指针指向的元素之和
         如果和等于目标值：
             返回左指针和右指针的索引（注意加1）
         如果和大于目标值：
             右指针左移
         否则：
             左指针右移
     返回[-1, -1]表示未找到
     ```
   - 二分查找法（思路，未在代码中实现）：
     ```
     对于数组中的每个元素：
         计算目标值与当前元素的差值
         在剩余部分使用二分查找寻找该差值
         如果找到，返回当前元素和找到元素的索引
     返回[-1, -1]表示未找到
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，因为每个元素最多被访问一次。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外空间。