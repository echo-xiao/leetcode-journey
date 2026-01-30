# 1755. 拆炸弹

**难度**: Easy | **标签**: `Array` `Sliding Window`

## 题目描述

<p>你有一个炸弹需要拆除，时间紧迫！你的情报员会给你一个长度为 <code>n</code> 的 <strong>循环</strong> 数组 <code>code</code> 以及一个密钥 <code>k</code> 。</p>

<p>为了获得正确的密码，你需要替换掉每一个数字。所有数字会 <strong>同时</strong> 被替换。</p>

<ul>
	<li>如果 <code>k > 0</code> ，将第 <code>i</code> 个数字用 <strong>接下来</strong> <code>k</code> 个数字之和替换。</li>
	<li>如果 <code>k < 0</code> ，将第 <code>i</code> 个数字用 <strong>之前</strong> <code>k</code> 个数字之和替换。</li>
	<li>如果 <code>k == 0</code> ，将第 <code>i</code> 个数字用 <code>0</code> 替换。</li>
</ul>

<p>由于 <code>code</code> 是循环的， <code>code[n-1]</code> 下一个元素是 <code>code[0]</code> ，且 <code>code[0]</code> 前一个元素是 <code>code[n-1]</code> 。</p>

<p>给你 <strong>循环</strong> 数组 <code>code</code> 和整数密钥 <code>k</code> ，请你返回解密后的结果来拆除炸弹！</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>code = [5,7,1,4], k = 3
<b>输出：</b>[12,10,16,13]
<b>解释：</b>每个数字都被接下来 3 个数字之和替换。解密后的密码为 [7+1+4, 1+4+5, 4+5+7, 5+7+1]。注意到数组是循环连接的。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>code = [1,2,3,4], k = 0
<b>输出：</b>[0,0,0,0]
<b>解释：</b>当 k 为 0 时，所有数字都被 0 替换。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>code = [2,4,9,3], k = -2
<b>输出：</b>[12,5,6,13]
<b>解释：</b>解密后的密码为 [3+9, 2+3, 4+2, 9+4] 。注意到数组是循环连接的。如果 k 是负数，那么和为 <strong>之前</strong> 的数字。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == code.length</code></li>
	<li><code>1 <= n <= 100</code></li>
	<li><code>1 <= code[i] <= 100</code></li>
	<li><code>-(n - 1) <= k <= n - 1</code></li>
</ul>


---
## 解题思路与复盘

1. **一句话直击本质：** 通过滑动窗口技术计算每个位置的前后 k 个元素的和。

2. **综合思路：**
   - **滑动窗口法：** 通过维护一个动态窗口，逐步更新窗口内元素的和，适用于正向和反向的 k 值。
   - **循环数组处理：** 由于数组是循环的，使用取模操作来处理数组的边界问题。

3. **全量伪代码：**

   - **初始化：**
     - 计算数组长度 `n`
     - 初始化结果数组 `arr` 长度为 `n`，所有元素为 0
     - 计算初始窗口和 `next_win` 或 `befr_win`，根据 `k` 的正负决定

   - **处理 k = 0 的情况：**
     - 对于每个元素，结果为 0

   - **处理 k > 0 的情况：**
     - 初始化 `next_win` 为从第一个元素开始的 k 个元素的和
     - 对于每个元素 `i`：
       - 更新 `next_win` 为 `next_win + code[(i + k) % n] - code[i]`
       - 将 `next_win` 赋值给 `arr[i]`

   - **处理 k < 0 的情况：**
     - 初始化 `befr_win` 为从最后一个元素开始的 k 个元素的和
     - 对于每个元素 `i`：
       - 更新 `befr_win` 为 `befr_win + code[i-1] - code[i - 1 - (abs(k) % n)]`
       - 将 `befr_win` 赋值给 `arr[i]`

   - **返回结果数组 `arr`**

4. **复杂度：**

   - 时间复杂度：$O(n)$，因为每个元素都被访问常数次。
   - 空间复杂度：$O(n)$，用于存储结果数组。