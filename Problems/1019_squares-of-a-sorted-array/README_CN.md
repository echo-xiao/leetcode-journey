# 1019. 有序数组的平方

**难度**: Easy | **标签**: `Array` `Two Pointers` `Sorting`

## 题目描述

<p>给你一个按 <strong>非递减顺序</strong> 排序的整数数组 <code>nums</code>，返回 <strong>每个数字的平方</strong> 组成的新数组，要求也按 <strong>非递减顺序</strong> 排序。</p>

<ul>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [-4,-1,0,3,10]
<strong>输出：</strong>[0,1,9,16,100]
<strong>解释：</strong>平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [-7,-3,2,3,11]
<strong>输出：</strong>[4,9,9,49,121]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code><span>1 &lt;= nums.length &lt;= </span>10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> 已按 <strong>非递减顺序</strong> 排序</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>请你设计时间复杂度为 <code>O(n)</code> 的算法解决本问题</li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：利用双指针从数组两端向中间遍历，比较平方值大小并从后向前填充结果数组。

2. 综合思路：
   - 双指针法：通过两个指针分别指向数组的头和尾，比较两端元素的平方值，将较大的平方值放入结果数组的末尾，并移动相应指针。
   - 变种双指针法：类似于双指针法，但通过插入操作将较大的平方值插入结果数组的开头。

3. 全量伪代码：
   - 双指针法：
     ```
     初始化结果数组 res，长度与输入数组相同
     初始化指针 i 指向数组头，指针 j 指向数组尾，指针 k 指向结果数组尾
     当 i <= j 时，重复以下步骤：
         如果 nums[i] 的平方大于 nums[j] 的平方：
             将 nums[i] 的平方放入 res[k]
             移动指针 i 向右
         否则：
             将 nums[j] 的平方放入 res[k]
             移动指针 j 向左
         移动指针 k 向左
     返回结果数组 res
     ```
   - 变种双指针法（使用插入）：
     ```
     初始化空结果数组 res
     当输入数组 A 非空时，重复以下步骤：
         如果 A[0] 的平方大于 A[-1] 的平方：
             将 A[0] 的平方插入 res 的开头
             从 A 中移除 A[0]
         否则：
             将 A[-1] 的平方插入 res 的开头
             从 A 中移除 A[-1]
     返回结果数组 res
     ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是输入数组的长度，因为每个元素最多被访问两次。
   - 空间复杂度：$O(n)$，用于存储结果数组。