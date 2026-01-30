# 1. 两数之和

**难度**: Easy | **标签**: `Array` `Hash Table`

## 题目描述

<p>给定一个整数数组 <code>nums</code>&nbsp;和一个整数目标值 <code>target</code>，请你在该数组中找出 <strong>和为目标值 </strong><em><code>target</code></em>&nbsp; 的那&nbsp;<strong>两个</strong>&nbsp;整数，并返回它们的数组下标。</p>

<p>你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。</p>

<p>你可以按任意顺序返回答案。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,7,11,15], target = 9
<strong>输出：</strong>[0,1]
<strong>解释：</strong>因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,4], target = 6
<strong>输出：</strong>[1,2]
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,3], target = 6
<strong>输出：</strong>[0,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>只会存在一个有效答案</strong></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你可以想出一个时间复杂度小于 <code>O(n<sup>2</sup>)</code> 的算法吗？</p>


---
## 解题思路与复盘

### 1. 一句话直击本质

使用暴力枚举法，检查每一对数的和是否等于目标值。

### 2. 简洁的中文实现思路描述

遍历数组中的每一个元素，并对每个元素之后的所有元素进行检查，寻找两个数的和等于目标值的组合。

### 3. 总结AC版本所有的通用解决方式/逻辑的中文伪代码

1. **暴力枚举法**：
   - 双重循环遍历数组中的每一对元素。
   - 如果找到一对元素的和等于目标值，返回它们的索引。

2. **哈希表法**（更高效的解决方案）：
   - 创建一个哈希表来存储每个数及其对应的索引。
   - 遍历数组，对于每个数，计算其与目标值的差值。
   - 检查差值是否在哈希表中存在，如果存在，返回当前数和差值的索引。
   - 如果不存在，将当前数和索引存入哈希表。

伪代码如下：

```plaintext
function twoSum(nums, target):
    create an empty hash_map
    for i from 0 to length of nums - 1:
        complement = target - nums[i]
        if complement is in hash_map:
            return [hash_map[complement], i]
        hash_map[nums[i]] = i
```

### 4. 时间复杂度和空间复杂度

- **暴力枚举法**：
  - 时间复杂度：$O(n^2)$
  - 空间复杂度：$O(1)$

- **哈希表法**：
  - 时间复杂度：$O(n)$
  - 空间复杂度：$O(n)$

通过使用哈希表法，可以显著提高算法的效率，特别是在处理较大规模数据时。