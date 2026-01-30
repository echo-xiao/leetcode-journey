# 1646. 第 k 个缺失的正整数

**难度**: Easy | **标签**: `Array` `Binary Search`

## 题目描述

<p>给你一个 <strong>严格升序排列</strong>&nbsp;的正整数数组 <code>arr</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。</p>

<p>请你找到这个数组里第&nbsp;<code>k</code>&nbsp;个缺失的正整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [2,3,4,7,11], k = 5
<strong>输出：</strong>9
<strong>解释：</strong>缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2,3,4], k = 2
<strong>输出：</strong>6
<strong>解释：</strong>缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 1000</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= 1000</code></li>
	<li>对于所有&nbsp;<code>1 &lt;= i &lt; j &lt;= arr.length</code>&nbsp;的 <code>i</code>&nbsp;和 <code>j</code> 满足&nbsp;<code>arr[i] &lt; arr[j]</code>&nbsp;</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<p>你可以设计一个时间复杂度小于 O(n) 的算法解决此问题吗？</p>


---
## 解题思路与复盘

1. 一句话直击本质：所有版本的核心逻辑都是通过计算数组中缺失的正整数数量，找到第 k 个缺失的正整数。

2. 综合思路：
   - 二分查找法：版本 1、2、3 和 4 使用二分查找法，通过计算当前中间位置的缺失数来调整搜索范围，最终确定第 k 个缺失的正整数。
   - 线性扫描法：版本 5 使用线性扫描法，遍历数组并调整 k 的值，直到找到第 k 个缺失的正整数。

3. 全量伪代码：
   - 二分查找法：
     ```
     初始化 left 为 0，right 为数组长度减 1
     当 left 小于等于 right 时：
         计算 mid 为 left 和 right 的中间索引
         计算 cnt 为 arr[mid] 减去 (mid + 1)
         如果 cnt 小于 k：
             将 left 更新为 mid + 1
         否则：
             将 right 更新为 mid - 1
     返回 k 加上 left
     ```
   - 线性扫描法：
     ```
     遍历数组中的每个元素 num：
         如果 num 小于等于 k：
             增加 k 的值
         否则：
             退出循环
     返回 k
     ```

4. 复杂度：
   - 二分查找法的时间复杂度为 $O(\log n)$，空间复杂度为 $O(1)$。
   - 线性扫描法的时间复杂度为 $O(n)$，空间复杂度为 $O(1)$。