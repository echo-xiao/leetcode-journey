# 3193. 找出强数对的最大异或值 I

**难度**: Easy | **标签**: `Array` `Hash Table` `Bit Manipulation` `Trie` `Sliding Window`

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 。如果一对整数 <code>x</code> 和 <code>y</code> 满足以下条件，则称其为 <strong>强数对</strong> ：</p>

<ul>
	<li><code>|x - y| &lt;= min(x, y)</code></li>
</ul>

<p>你需要从 <code>nums</code> 中选出两个整数，且满足：这两个整数可以形成一个强数对，并且它们的按位异或（<code>XOR</code>）值是在该数组所有强数对中的<strong> 最大值 </strong>。</p>

<p>返回数组 <code>nums</code> 所有可能的强数对中的<strong> 最大 </strong>异或值。</p>

<p><strong>注意</strong>，你可以选择同一个整数两次来形成一个强数对。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4,5]
<strong>输出：</strong>7
<strong>解释：</strong>数组<code> nums </code>中有 11 个强数对：(1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5) 和 (5, 5) 。
这些强数对中的最大异或值是 3 XOR 4 = 7 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [10,100]
<strong>输出：</strong>0
<strong>解释：</strong>数组<code> nums </code>中有 2 个强数对：(10, 10) 和 (100, 100) 。
这些强数对中的最大异或值是 10 XOR 10 = 0 ，数对 (100, 100) 的异或值也是 100 XOR 100 = 0 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,6,25,30]
<strong>输出：</strong>7
<strong>解释：</strong>数组<code> nums </code>中有 6 个强数对：(5, 5), (5, 6), (6, 6), (25, 25), (25, 30) 和 (30, 30) 。
这些强数对中的最大异或值是 25 XOR 30 = 7 ；另一个异或值非零的数对是 (5, 6) ，其异或值是 5 XOR 6 = 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过排序和双重循环，找出满足条件的数对并计算其异或值，更新最大异或值。

2. 综合思路：
   - 排序 + 双重循环：首先对数组进行排序，然后使用双重循环遍历所有可能的数对，检查是否满足条件（即右侧数小于等于左侧数的两倍），计算其异或值并更新最大值。

3. 全量伪代码：
   ```
   定义函数 maximumStrongPairXor(nums):
       将 nums 数组排序
       初始化 max_res 为 0

       对于 r 从 0 到 nums 的长度:
           对于 l 从 0 到 r:
               如果 nums[r] 小于等于 nums[l] 的两倍:
                   计算 res 为 nums[l] 异或 nums[r]
                   更新 max_res 为 res 和 max_res 中的较大值

       返回 max_res
   ```

4. 复杂度：
   - 时间复杂度：$O(n^2)$，因为双重循环遍历所有可能的数对。
   - 空间复杂度：$O(1)$，因为只使用了常数额外空间。