# 190. 颠倒二进制位

**难度**: Easy | **标签**: `Divide and Conquer` `Bit Manipulation`

## 题目描述

<p>颠倒给定的 32 位有符号整数的二进制位。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 43261596</span></p>

<p><span class="example-io"><b>输出：</b>964176192</span></p>

<p><strong>解释：</strong></p>

<table>
	<tbody>
		<tr>
			<th>整数</th>
			<th>二进制</th>
		</tr>
		<tr>
			<td>43261596</td>
			<td>00000010100101000001111010011100</td>
		</tr>
		<tr>
			<td>964176192</td>
			<td>00111001011110000010100101000000</td>
		</tr>
	</tbody>
</table>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 2147483644</span></p>

<p><span class="example-io"><b>输出：</b>1073741822</span></p>

<p><strong>解释：</strong></p>

<table>
	<tbody>
		<tr>
			<th>整数</th>
			<th>二进制</th>
		</tr>
		<tr>
			<td>2147483644</td>
			<td>01111111111111111111111111111100</td>
		</tr>
		<tr>
			<td>1073741822</td>
			<td>00111111111111111111111111111110</td>
		</tr>
	</tbody>
</table>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 2<sup>31</sup>&nbsp;- 2</code></li>
	<li><code>n</code>&nbsp;为偶数</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶</strong>: 如果多次调用这个函数，你将如何优化你的算法？</p>


---
## 解题思路与复盘

1. 一句话直击本质：通过逐位提取和重组，将给定的32位整数的二进制表示进行反转。

2. 综合思路：
   - **迭代法**：直接通过位操作，逐位提取给定整数的最低位，并将其插入到结果整数的相应位置，最终实现二进制位的反转。
   - **数组存储法**：先将整数的二进制位逐位提取并存储到数组中，然后通过遍历数组重构反转后的整数。

3. 全量伪代码：
   - **迭代法伪代码**：
     ```
     初始化结果 res 为 0
     循环 32 次：
         将 res 左移 1 位
         提取 n 的最低有效位 last
         将 last 插入 res 的最低位
         将 n 右移 1 位
     返回 res
     ```
   - **数组存储法伪代码**：
     ```
     初始化空数组 arr
     初始化结果 res 为 0
     循环 32 次：
         计算 n 的最低有效位 k
         将 k 添加到数组 arr
         将 n 整除 2
     遍历数组 arr：
         将 res 乘以 2 并加上当前位 i
     返回 res
     ```

4. 复杂度：
   - 时间复杂度：两种方法的时间复杂度均为 $O(32)$，即 $O(1)$，因为循环次数固定为32次。
   - 空间复杂度：
     - 迭代法的空间复杂度为 $O(1)$，因为只使用了常数个额外变量。
     - 数组存储法的空间复杂度为 $O(32)$，即 $O(1)$，因为数组大小固定为32。