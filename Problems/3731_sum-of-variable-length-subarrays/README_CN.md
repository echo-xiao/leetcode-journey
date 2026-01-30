# 3731. 变长子数组求和

**难度**: Easy | **标签**: `Array` `Prefix Sum`

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;。对于 <strong>每个</strong> 下标&nbsp;<code>i</code>（<code>0 &lt;= i &lt; n</code>），定义对应的子数组&nbsp;<code>nums[start ... i]</code>（<code>start = max(0, i - nums[i])</code>）。</p>

<p>返回为数组中每个下标定义的子数组中所有元素的总和。</p>
<strong>子数组</strong>&nbsp;是数组中的一个连续、<strong>非空</strong> 的元素序列。

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<div class="example-block">
<p><b>输入：</b><span class="example-io">nums = [2,3,1]</span></p>

<p><span class="example-io"><b>输出：</b>11</span></p>

<p><b>解释：</b></p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">下标 i</th>
			<th style="border: 1px solid black;">子数组</th>
			<th style="border: 1px solid black;">和</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;"><code>nums[0] = [2]</code></td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>nums[0 ... 1] = [2, 3]</code></td>
			<td style="border: 1px solid black;">5</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;"><code>nums[1 ... 2] = [3, 1]</code></td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><b>总和</b></td>
			<td style="border: 1px solid black;">&nbsp;</td>
			<td style="border: 1px solid black;">11</td>
		</tr>
	</tbody>
</table>

<p>总和为 11 。因此，输出 11 。</p>
</div>

<p><b>示例 2：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [3,1,1,2]</span></p>

<p><span class="example-io"><b>输出：</b>13</span></p>

<p><b>解释：</b></p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">下标 i</th>
			<th style="border: 1px solid black;">子数组</th>
			<th style="border: 1px solid black;">和</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;"><code>nums[0] = [3]</code></td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>nums[0 ... 1] = [3, 1]</code></td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;"><code>nums[1 ... 2] = [1, 1]</code></td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;"><code>nums[1 ... 3] = [1, 1, 2]</code></td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><b>总和</b></td>
			<td style="border: 1px solid black;">&nbsp;</td>
			<td style="border: 1px solid black;">13</td>
		</tr>
	</tbody>
</table>

<p>总和为 13 。因此，输出为 13 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


---
## 解题思路与复盘

### 一句话直击本质

利用前缀和数组快速计算变长子数组的和。

### 综合思路

1. **前缀和数组**：这两种实现都使用了前缀和数组来快速计算子数组的和。通过构建一个前缀和数组 `curr`，可以在常数时间内计算任意子数组的和。
2. **迭代法**：两种实现都采用了迭代的方法，遍历数组中的每一个元素，计算以该元素为结尾的子数组的和。

### 全量伪代码

```plaintext
函数 subarraySum(数组 nums):
    令 n 为 nums 的长度
    初始化 curr 为长度为 n+1 的数组，所有元素为 0

    # 构建前缀和数组
    对于 i 从 1 到 n:
        curr[i] = curr[i-1] + nums[i-1]

    初始化 res 为 0
    初始化 ttl 为 0

    # 计算变长子数组的和
    对于 end 从 0 到 n-1:
        令 start 为 max(0, end - nums[end])
        ttl += curr[end+1] - curr[start]
        res += ttl

    返回 ttl
```

### 复杂度

- 时间复杂度：构建前缀和数组需要 $O(n)$，计算子数组和的过程也需要 $O(n)$，因此总时间复杂度为 $O(n)$。
- 空间复杂度：使用了一个长度为 $n+1$ 的前缀和数组，因此空间复杂度为 $O(n)$。