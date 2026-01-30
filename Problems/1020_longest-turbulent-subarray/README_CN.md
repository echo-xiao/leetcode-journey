# 1020. 最长湍流子数组

**难度**: Medium | **标签**: `Array` `Dynamic Programming` `Sliding Window`

## 题目描述

<p>给定一个整数数组 <code>arr</code>&nbsp;，返回 <code>arr</code>&nbsp;的&nbsp;<em>最大湍流子数组的<strong>长度</strong></em><strong>&nbsp;</strong>。</p>

<p>如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是&nbsp;<strong>湍流子数组</strong>&nbsp;。</p>

<p>更正式地来说，当 <code>arr</code>&nbsp;的子数组&nbsp;<code>A[i], A[i+1], ..., A[j]</code>&nbsp;满足仅满足下列条件时，我们称其为<em>湍流子数组</em>：</p>

<ul>
	<li>若&nbsp;<code>i &lt;= k &lt; j</code>&nbsp;：

	<ul>
		<li>当 <code>k</code>&nbsp;为奇数时，&nbsp;<code>A[k] &gt; A[k+1]</code>，且</li>
		<li>当 <code>k</code> 为偶数时，<code>A[k] &lt; A[k+1]</code>；</li>
	</ul>
	</li>
	<li><strong>或 </strong>若&nbsp;<code>i &lt;= k &lt; j</code>&nbsp;：
	<ul>
		<li>当 <code>k</code> 为偶数时，<code>A[k] &gt; A[k+1]</code>&nbsp;，且</li>
		<li>当 <code>k</code>&nbsp;为奇数时，&nbsp;<code>A[k] &lt; A[k+1]</code>。</li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [9,4,2,10,7,8,8,1,9]
<strong>输出：</strong>5
<strong>解释：</strong>arr[1] &gt; arr[2] &lt; arr[3] &gt; arr[4] &lt; arr[5]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [4,8,12,16]
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [100]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
</ul>


---
## 解题思路与复盘

1. 一句话直击本质：通过双指针滑动窗口法，动态调整窗口边界以寻找最长的湍流子数组。

2. 综合思路：
   - 滑动窗口法：使用双指针 `left` 和 `right` 来定义当前的窗口范围，通过比较相邻元素的大小关系来判断当前窗口是否为湍流子数组，并根据条件调整窗口的左边界。
   - 由于提供的代码实现逻辑相同，均采用了滑动窗口法，没有其他解法如递归或不同数据结构的实现。

3. 全量伪代码：
   ```
   定义函数 maxTurbulenceSize(arr):
       如果 arr 长度小于 2:
           返回 arr 的长度

       初始化 left 和 right 为 0
       初始化 maxLen 为 1
       初始化 isBroken 为 False

       当 right 小于 arr 长度减 1 时:
           right 增加 1
           计算 curr 为 arr[right] 和 arr[right-1] 的比较结果

           如果 curr 等于 0:
               设置 isBroken 为 True
           否则如果 right 大于 1:
               计算 prev 为 arr[right-1] 和 arr[right-2] 的比较结果
               如果 curr 等于 prev:
                   设置 isBroken 为 True

           当 isBroken 为 True 时:
               如果 curr 等于 0:
                   设置 left 为 right
               否则:
                   设置 left 为 right - 1
               设置 isBroken 为 False

           更新 maxLen 为 max(maxLen, right-left+1)

       返回 maxLen

   定义函数 compare(arr, i):
       如果 arr[i] 大于 arr[i-1]:
           返回 1
       否则如果 arr[i] 小于 arr[i-1]:
           返回 -1
       否则:
           返回 0
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，因为每个元素最多被访问两次（一次作为 `right`，一次作为 `left`）。
   - 空间复杂度：$O(1)$，因为只使用了常数个额外变量。