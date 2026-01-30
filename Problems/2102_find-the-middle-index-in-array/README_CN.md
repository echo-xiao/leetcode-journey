# 2102. 找到数组的中间位置

**难度**: Easy | **标签**: `Array` `Prefix Sum`

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;，请你找到 <strong>最左边</strong>&nbsp;的中间位置&nbsp;<code>middleIndex</code>&nbsp;（也就是所有可能中间位置下标最小的一个）。</p>

<p>中间位置&nbsp;<code>middleIndex</code>&nbsp;是满足&nbsp;<code>nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1]</code>&nbsp;的数组下标。</p>

<p>如果&nbsp;<code>middleIndex == 0</code>&nbsp;，左边部分的和定义为 <code>0</code>&nbsp;。类似的，如果&nbsp;<code>middleIndex == nums.length - 1</code>&nbsp;，右边部分的和定义为&nbsp;<code>0</code>&nbsp;。</p>

<p>请你返回满足上述条件 <strong>最左边</strong>&nbsp;的<em>&nbsp;</em><code>middleIndex</code>&nbsp;，如果不存在这样的中间位置，请你返回&nbsp;<code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [2,3,-1,<em><strong>8</strong></em>,4]
<b>输出：</b>3
<strong>解释：</strong>
下标 3 之前的数字和为：2 + 3 + -1 = 4
下标 3 之后的数字和为：4 = 4
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,-1,<em><strong>4</strong></em>]
<b>输出：</b>2
<strong>解释：</strong>
下标 2 之前的数字和为：1 + -1 = 0
下标 2 之后的数字和为：0
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [2,5]
<b>输出：</b>-1
<b>解释：</b>
不存在符合要求的 middleIndex 。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<b>输入：</b>nums = [<em><strong>1</strong></em>]
<b>输出：</b>0
<strong>解释：</strong>
下标 0 之前的数字和为：0
下标 0 之后的数字和为：0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与主站 724 题相同：<a href="https://leetcode.cn/problems/find-pivot-index/" target="_blank">https://leetcode.cn/problems/find-pivot-index/</a></p>


---
## 解题思路与复盘

1. 一句话直击本质：通过前缀和数组计算每个位置的左侧和与右侧和，找到满足条件的位置。

2. 综合思路：
   - 前缀和方法：使用一个辅助数组来存储前缀和，通过两次遍历数组，第一次计算前缀和，第二次检查每个位置的左侧和与右侧和是否相等。

3. 全量伪代码：
   ```plaintext
   定义函数 findMiddleIndex(nums):
       令 n 为 nums 的长度
       创建一个数组 arr，长度为 n+1，初始值为 0

       // 计算前缀和
       对于 i 从 0 到 n-1:
           arr[i+1] = arr[i] + nums[i]

       // 查找中间位置
       对于 j 从 0 到 n-1:
           如果 arr[j] == arr[n] - arr[j+1]:
               返回 j
       返回 -1
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，因为我们遍历数组两次。
   - 空间复杂度：$O(n)$，因为我们使用了一个额外的数组来存储前缀和。