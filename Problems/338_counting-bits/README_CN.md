# 338. 比特位计数

**难度**: Easy | **标签**: `Dynamic Programming` `Bit Manipulation`

## 题目描述

<p>给你一个整数 <code>n</code> ，对于&nbsp;<code>0 &lt;= i &lt;= n</code> 中的每个 <code>i</code> ，计算其二进制表示中 <strong><code>1</code> 的个数</strong> ，返回一个长度为 <code>n + 1</code> 的数组 <code>ans</code> 作为答案。</p>

<p>&nbsp;</p>

<div class="original__bRMd">
<div>
<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>[0,1,1]
<strong>解释：</strong>
0 --&gt; 0
1 --&gt; 1
2 --&gt; 10
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 5
<strong>输出：</strong>[0,1,1,2,1,2]
<strong>解释：</strong>
0 --&gt; 0
1 --&gt; 1
2 --&gt; 10
3 --&gt; 11
4 --&gt; 100
5 --&gt; 101
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>很容易就能实现时间复杂度为 <code>O(n log n)</code> 的解决方案，你可以在线性时间复杂度 <code>O(n)</code> 内用一趟扫描解决此问题吗？</li>
	<li>你能不使用任何内置函数解决此问题吗？（如，C++ 中的&nbsp;<code>__builtin_popcount</code> ）</li>
</ul>
</div>
</div>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过递归或直接计算每个数的二进制表示中 '1' 的个数来构建结果数组。

2. **综合思路：**
   - **递归与记忆化搜索：** 版本 1、2 和 3 使用递归来计算每个数的二进制 '1' 的个数，其中版本 1 采用了记忆化搜索来优化重复计算。
   - **直接计算：** 版本 4 直接通过将数字转换为二进制字符串并统计 '1' 的个数来实现。

3. **全量伪代码：**

   - **递归与记忆化搜索（版本 1）：**
     ```
     初始化结果数组 res 为长度 n+1，初始值为 -1
     对于每个 i 从 0 到 n：
         调用 count(i) 并将结果存入 res[i]
     返回 res

     函数 count(n):
         如果 n 为 0，返回 0
         如果 n 为 1，返回 1
         如果 res[n] 不为 -1，返回 res[n]
         否则，计算 res[n] 为 count(n // 2) + (n % 2)
         返回 res[n]
     ```

   - **递归（版本 2 和 3）：**
     ```
     初始化结果数组 res 为长度 n+1
     对于每个 i 从 0 到 n：
         调用 count(i) 并将结果添加到 res
     返回 res

     函数 count(n):
         如果 n 为 0，返回 0
         如果 n 为 1，返回 1
         计算 val 为 count(n // 2) + (n % 2) 或 count(n >> 1) + (n & 1)
         返回 val
     ```

   - **直接计算（版本 4）：**
     ```
     初始化结果数组 res 为长度 n+1
     对于每个 i 从 0 到 n：
         将 i 转换为二进制字符串
         统计二进制字符串中 '1' 的个数
         将统计结果添加到 res
     返回 res
     ```

4. **复杂度：**
   - **递归与记忆化搜索（版本 1）：** 时间复杂度 $O(n \log n)$，空间复杂度 $O(n)$。
   - **递归（版本 2 和 3）：** 时间复杂度 $O(n \log n)$，空间复杂度 $O(\log n)$。
   - **直接计算（版本 4）：** 时间复杂度 $O(n \log n)$，空间复杂度 $O(n)$。