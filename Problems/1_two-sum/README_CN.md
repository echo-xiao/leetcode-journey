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

### 一句话直击本质
通过遍历数组中的每一对元素，寻找和为目标值的两个数的索引。

### 综合思路
1. **暴力枚举法**：遍历数组中的每一对元素，检查它们的和是否等于目标值。该方法直接且简单，但效率较低。
2. **哈希表法（未在提供的代码中出现）**：使用哈希表存储数组元素及其索引，在遍历数组时，通过查找哈希表来快速找到满足条件的另一半元素。这种方法可以将时间复杂度降低到线性级别。

### 全量伪代码
#### 暴力枚举法
```
函数 两数之和(数组 nums, 整数 target):
    对于 i 从 0 到 数组长度-2:
        对于 j 从 i+1 到 数组长度-1:
            如果 nums[i] + nums[j] 等于 target:
                返回 [i, j]
```

#### 哈希表法（未在提供的代码中出现）
```
函数 两数之和(数组 nums, 整数 target):
    创建一个空的哈希表 hash_table
    对于 i 从 0 到 数组长度-1:
        计算 complement = target - nums[i]
        如果 complement 在 hash_table 中:
            返回 [hash_table[complement], i]
        将 nums[i] 和 i 存入 hash_table
```

### 复杂度
- **暴力枚举法**：
  - 时间复杂度：$O(n^2)$，因为需要遍历每一对元素。
  - 空间复杂度：$O(1)$，不需要额外的存储空间。
  
- **哈希表法**（未在提供的代码中出现）：
  - 时间复杂度：$O(n)$，因为每个元素最多被访问两次。
  - 空间复杂度：$O(n)$，因为需要存储每个元素的索引。