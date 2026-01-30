# 2571. 找出中枢整数

**难度**: Easy | **标签**: `Math` `Prefix Sum`

## 题目描述

<p>给你一个正整数 <code>n</code> ，找出满足下述条件的<strong> 中枢整数</strong> <code>x</code> ：</p>

<ul>
	<li><code>1</code> 和 <code>x</code> 之间的所有元素之和等于 <code>x</code> 和 <code>n</code> 之间所有元素之和。</li>
</ul>

<p>返回中枢整数<em> </em><code>x</code> 。如果不存在中枢整数，则返回 <code>-1</code> 。题目保证对于给定的输入，至多存在一个中枢整数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 8
<strong>输出：</strong>6
<strong>解释：</strong>6 是中枢整数，因为 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>1
<strong>解释：</strong>1 是中枢整数，因为 1 = 1 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 4
<strong>输出：</strong>-1
<strong>解释：</strong>可以证明不存在满足题目要求的整数。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：该算法通过前缀和数组来判断某个整数是否为中枢整数。

2. 综合思路：
   - 前缀和法：通过构建前缀和数组，计算每个位置的左侧和与右侧和，判断是否存在一个位置使得左右和相等。

3. 全量伪代码：
   ```plaintext
   定义函数 pivotInteger(n):
       初始化 nums 为从 1 到 n 的整数列表
       初始化 arr 为长度为 n+1 的数组，初始值为 0

       对于 i 从 0 到 n-1:
           arr[i+1] = arr[i] + nums[i]  # 计算前缀和

       对于 j 从 1 到 n:
           如果 arr[j] 等于 arr[n] - arr[j-1]:  # 判断左右和是否相等
               返回 j  # 找到中枢整数

       返回 -1  # 如果没有找到中枢整数

   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，因为需要遍历数组两次，分别计算前缀和和查找中枢整数。
   - 空间复杂度：$O(n)$，因为使用了一个额外的数组来存储前缀和。