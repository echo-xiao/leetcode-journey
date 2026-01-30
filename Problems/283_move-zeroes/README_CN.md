# 283. 移动零

**难度**: Easy | **标签**: `Array` `Two Pointers`

## 题目描述

<p>给定一个数组 <code>nums</code>，编写一个函数将所有 <code>0</code> 移动到数组的末尾，同时保持非零元素的相对顺序。</p>

<p><strong>请注意</strong>&nbsp;，必须在不复制数组的情况下原地对数组进行操作。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = <code>[0,1,0,3,12]</code>
<strong>输出:</strong> <code>[1,3,12,0,0]</code>
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = <code>[0]</code>
<strong>输出:</strong> <code>[0]</code></pre>

<p>&nbsp;</p>

<p><strong>提示</strong>:</p>
<meta charset="UTF-8" />

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup>&nbsp;&lt;= nums[i] &lt;= 2<sup>31</sup>&nbsp;- 1</code></li>
</ul>

<p>&nbsp;</p>

<p><b>进阶：</b>你能尽量减少完成的操作次数吗？</p>


---
## 解题思路与复盘

### 一句话直击本质

使用双指针遍历数组，将非零元素前移并在末尾填充零。

### 综合思路

1. **双指针法**：使用两个指针，一个用于遍历数组（`fast`），另一个用于记录非零元素的插入位置（`slow`）。遍历过程中，将非零元素移动到`slow`指针位置，并在遍历结束后，将`slow`指针后的所有位置填充为零。

### 全量伪代码

```plaintext
函数 moveZeroes(数组 nums):
    初始化 slow 指针为 0
    
    对于 fast 从 0 到 数组长度 - 1:
        如果 nums[fast] 不等于 0:
            将 nums[slow] 设为 nums[fast]
            slow 指针加 1
    
    对于 i 从 slow 到 数组长度 - 1:
        将 nums[i] 设为 0
    
    返回 nums
```

### 复杂度

- 时间复杂度：$O(n)$，其中 $n$ 是数组的长度，因为我们只需遍历数组两次。
- 空间复杂度：$O(1)$，因为我们只使用了常数级别的额外空间。