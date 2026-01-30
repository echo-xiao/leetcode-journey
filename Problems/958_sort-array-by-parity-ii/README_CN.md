# 958. 按奇偶排序数组 II

**难度**: Easy | **标签**: `Array` `Two Pointers` `Sorting`

## 题目描述

<p>给定一个非负整数数组&nbsp;<code>nums</code>，&nbsp;&nbsp;<code>nums</code> 中一半整数是 <strong>奇数</strong> ，一半整数是 <strong>偶数</strong> 。</p>

<p>对数组进行排序，以便当&nbsp;<code>nums[i]</code> 为奇数时，<code>i</code>&nbsp;也是 <strong>奇数</strong> ；当&nbsp;<code>nums[i]</code>&nbsp;为偶数时， <code>i</code> 也是 <strong>偶数</strong> 。</p>

<p>你可以返回 <em>任何满足上述条件的数组作为答案</em> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,2,5,7]
<strong>输出：</strong>[4,5,2,7]
<strong>解释：</strong>[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [2,3]
<b>输出：</b>[2,3]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>nums.length</code>&nbsp;是偶数</li>
	<li><code>nums</code>&nbsp;中一半是偶数</li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>可以不使用额外空间解决问题吗？</p>


---
## 解题思路与复盘

1. 一句话直击本质：使用双指针分别在偶数位和奇数位寻找错位的元素并交换，以实现按奇偶排序。

2. 综合思路：
   - 双指针法：使用两个指针分别指向偶数位和奇数位，寻找需要交换的错位元素并进行交换，直到所有元素都在正确的位置上。

3. 全量伪代码：
   ```plaintext
   定义函数 sortArrayByParityII(nums):
       初始化 n 为 nums 的长度
       初始化 even_ptr 为 0  # 指向偶数位
       初始化 odd_ptr 为 1   # 指向奇数位

       当 even_ptr 和 odd_ptr 都在数组范围内时:
           # 找到偶数位上的错位奇数
           当 even_ptr 在范围内且 nums[even_ptr] 是偶数:
               将 even_ptr 移动到下一个偶数位

           # 找到奇数位上的错位偶数
           当 odd_ptr 在范围内且 nums[odd_ptr] 是奇数:
               将 odd_ptr 移动到下一个奇数位

           # 如果两个指针都找到错位元素，进行交换
           如果 even_ptr 和 odd_ptr 都在范围内:
               交换 nums[even_ptr] 和 nums[odd_ptr]

       返回 nums
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，因为每个元素最多被访问一次。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外空间。